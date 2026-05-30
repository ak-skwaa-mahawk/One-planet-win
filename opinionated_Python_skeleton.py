from dataclasses import dataclass, field
from typing import List, Dict, Callable
import math
import time


# ---------- Signals ----------

@dataclass
class PlanetState:
    power: float        # E_t
    carbon: float       # C_t
    grid_stress: float  # G_t


@dataclass
class PlanetLimits:
    power_max: float
    carbon_max: float
    grid_max: float
    eps: float = 0.0    # tolerance for "P = 1"


@dataclass
class TribeState:
    id: str
    used_quota: float   # u_{k,t}
    quota: float        # Q_k


@dataclass
class Job:
    id: str
    tribe_id: str
    est_cost: float          # e_j (GPU-seconds, etc.)
    base_priority: float     # p_j
    planet_weight: float     # w_planet(j) in [0,1]
    valid_individual: bool   # I_j (local constraints)
    submit_ts: float = field(default_factory=time.time)


# ---------- Scheduler config ----------

@dataclass
class SchedulerConfig:
    planet_gain: float = 1.0   # K in g_t = exp(-K * ||e_t||)
    tick_duration: float = 1.0 # seconds per scheduling tick
def planet_error(state: PlanetState, limits: PlanetLimits):
    e_power = state.power - limits.power_max
    e_carbon = state.carbon - limits.carbon_max
    e_grid = state.grid_stress - limits.grid_max
    return (e_power, e_carbon, e_grid)


def planet_gate(state: PlanetState, limits: PlanetLimits, gain: float) -> float:
    e = planet_error(state, limits)
    norm = math.sqrt(sum(x * x for x in e))
    # g_t in (0,1], decays as error grows
    return math.exp(-gain * max(0.0, norm))


def planet_boolean(state: PlanetState, limits: PlanetLimits) -> int:
    e = planet_error(state, limits)
    norm = math.sqrt(sum(x * x for x in e))
    return 1 if norm <= limits.eps else 0  # P in {0,1}


def tribe_boolean(tribe: TribeState) -> int:
    return 1 if tribe.used_quota <= tribe.quota else 0  # T_k in {0,1}


def individual_boolean(job: Job) -> int:
    return 1 if job.valid_individual else 0  # I_j in {0,1}
class PlanetGatedScheduler:
    def __init__(self,
                 limits: PlanetLimits,
                 config: SchedulerConfig):
        self.limits = limits
        self.config = config
        self.tribes: Dict[str, TribeState] = {}
        self.pending_jobs: List[Job] = []

    def register_tribe(self, tribe: TribeState):
        self.tribes[tribe.id] = tribe

    def submit_job(self, job: Job):
        self.pending_jobs.append(job)

    # Hook: you wire this to real sensors
    def read_planet_state(self) -> PlanetState:
        # placeholder
        return PlanetState(power=0.0, carbon=0.0, grid_stress=0.0)

    # Hook: you wire this to actual execution
    def dispatch_job(self, job: Job, allocated_cost: float):
        print(f"Dispatching job {job.id} for {allocated_cost} units")

    def tick(self):
        planet_state = self.read_planet_state()
        g_t = planet_gate(planet_state, self.limits, self.config.planet_gain)
        P = planet_boolean(planet_state, self.limits)

        # Group jobs by tribe
        jobs_by_tribe: Dict[str, List[Job]] = {}
        for job in self.pending_jobs:
            jobs_by_tribe.setdefault(job.tribe_id, []).append(job)

        new_pending: List[Job] = []

        for tribe_id, jobs in jobs_by_tribe.items():
            tribe = self.tribes[tribe_id]
            T = tribe_boolean(tribe)

            # Planet-gated tribe allocation
            if P == 0:
                # emergency: only allow high-planet-weight jobs
                min_w = 0.7
                jobs = [j for j in jobs if j.planet_weight >= min_w]

            if T == 0:
                # tribe over quota: no allocation
                continue

            remaining_quota = max(0.0, tribe.quota - tribe.used_quota)
            tribe_alloc = g_t * remaining_quota

            # Filter invalid individuals
            valid_jobs = [j for j in jobs if individual_boolean(j) == 1]

            # Priority: base_priority * planet_weight
            valid_jobs.sort(
                key=lambda j: (j.base_priority * j.planet_weight, -j.submit_ts),
                reverse=True
            )

            for job in valid_jobs:
                if tribe_alloc <= 0:
                    new_pending.append(job)
                    continue

                cost = job.est_cost
                if cost <= tribe_alloc:
                    # full dispatch
                    self.dispatch_job(job, cost)
                    tribe_alloc -= cost
                    tribe.used_quota += cost
                else:
                    # partial or defer; here we just defer
                    new_pending.append(job)

        self.pending_jobs = new_pending
