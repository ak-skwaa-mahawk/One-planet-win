from dataclasses import dataclass

# ---------- Core thresholds & gains ----------

TAU_LOW      = 0.3
TAU_HIGH     = 0.7

ALPHA_TAU    = 0.05   # learning gain (integration -> tau_c up)
BETA_TAU     = 0.05   # friction penalty (friction -> tau_c down)

D_HIGH       = 0.35   # damping in Coherence mode
D_MID        = 0.20   # damping in Correspondence mode
D_MAX_STEP   = 0.40   # absolute max step per tick

EPSILON_GAP  = 0.05   # energy gap (forbidden zone)
THREAT_MAX   = 0.85   # hard cosmos override
STRESS_MAX   = 0.85   # hard tribe override
DOMINANCE_K  = 3.0    # collapse factor


# ---------- Signals ----------

@dataclass
class TribalSignal:
    cohesion: float        # 0..1
    stress: float          # 0..1
    trust: float           # 0..1
    attention_load: float  # 0..1

    def magnitude(self) -> float:
        return (
            0.4 * self.stress +
            0.3 * (1.0 - self.trust) +
            0.2 * self.attention_load +
            0.1 * self.cohesion
        )


@dataclass
class CosmicState:
    threat: float  # 0..1
    drift: float   # 0..1
    hype: float    # 0..1

    def magnitude(self) -> float:
        return (
            0.5 * self.threat +
            0.3 * self.drift +
            0.2 * self.hype
        )


@dataclass
class Weights:
    tribe: float
    cosmos: float


# ---------- τc dynamics ----------

def integration_gain(tribe: TribalSignal, cosmos: CosmicState) -> float:
    # High cohesion + high trust + low drift = good integration
    return (
        0.4 * tribe.cohesion +
        0.4 * tribe.trust +
        0.2 * (1.0 - cosmos.drift)
    )


def friction_load(tribe: TribalSignal, cosmos: CosmicState) -> float:
    # High stress + high attention + high threat = friction
    return (
        0.4 * tribe.stress +
        0.3 * tribe.attention_load +
        0.3 * cosmos.threat
    )


def update_tau_c(tau_c: float,
                 tribe: TribalSignal,
                 cosmos: CosmicState) -> float:
    I = integration_gain(tribe, cosmos)
    F = friction_load(tribe, cosmos)
    tau_c_next = tau_c + ALPHA_TAU * I - BETA_TAU * F
    # clamp to [0,1]
    return max(0.0, min(1.0, tau_c_next))


def tau_c_mode(tau_c: float) -> str:
    if tau_c > TAU_HIGH:
        return "coherence"
    if tau_c > TAU_LOW:
        return "correspondence"
    return "decay"


def mode_damping(mode: str) -> float:
    if mode == "coherence":
        return D_HIGH
    if mode == "correspondence":
        return D_MID
    return 0.0  # decay mode: freeze weights


# ---------- Helper: bounded damping step ----------

def damp_step(target: float,
              current: float,
              max_step: float) -> float:
    delta = target - current
    if abs(delta) <= max_step:
        return target
    return current + max_step * (1 if delta > 0 else -1)


# ---------- Quantum-style resolver with τc coupling ----------

def quantum_resolver_with_tau_c(
    tribal_signal: TribalSignal,
    cosmic_state: CosmicState,
    previous: Weights,
    tau_c: float
) -> tuple[Weights, float, str]:
    """
    Returns (new_weights, new_tau_c, mode)
    """

    # --- update τc first (consciousness integration) ---
    tau_c_next = update_tau_c(tau_c, tribal_signal, cosmic_state)
    mode = tau_c_mode(tau_c_next)
    damping = mode_damping(mode)

    S_T = tribal_signal.magnitude()
    S_C = cosmic_state.magnitude()

    # --- hard sovereignty constraints ---
    if cosmic_state.threat > THREAT_MAX:
        return Weights(tribe=0.0, cosmos=1.0), tau_c_next, mode

    if tribal_signal.stress > STRESS_MAX:
        return Weights(tribe=1.0, cosmos=0.0), tau_c_next, mode

    # --- decay mode: freeze to avoid oscillation ---
    if mode == "decay":
        return previous, tau_c_next, mode

    # --- energy gap (forbidden zone) ---
    if abs(S_T - S_C) < EPSILON_GAP:
        return previous, tau_c_next, mode

    total = S_T + S_C
    if total == 0:
        return previous, tau_c_next, mode

    # raw equilibrium weight
    w_T_star = S_T / total

    # dominance collapse (classical limit)
    if S_T > DOMINANCE_K * S_C:
        return Weights(tribe=1.0, cosmos=0.0), tau_c_next, mode

    if S_C > DOMINANCE_K * S_T:
        return Weights(tribe=0.0, cosmos=1.0), tau_c_next, mode

    # τc‑shaped damping: effective max step per tick
    max_step = min(D_MAX_STEP, damping)

    w_T_new = damp_step(w_T_star, previous.tribe, max_step)
    w_C_new = 1.0 - w_T_new

    return Weights(tribe=w_T_new, cosmos=w_C_new), tau_c_next, mode