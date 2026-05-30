use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};

/// ---------- Planet Signals ----------

#[derive(Clone, Debug)]
pub struct PlanetState {
    pub power: f64,       // E_t
    pub carbon: f64,      // C_t
    pub grid_stress: f64, // G_t
}

#[derive(Clone, Debug)]
pub struct PlanetLimits {
    pub power_max: f64,
    pub carbon_max: f64,
    pub grid_max: f64,
    pub eps: f64, // tolerance for P = 1
}

/// Compute planetary error vector
pub fn planet_error(state: &PlanetState, limits: &PlanetLimits) -> (f64, f64, f64) {
    (
        state.power - limits.power_max,
        state.carbon - limits.carbon_max,
        state.grid_stress - limits.grid_max,
    )
}

/// Planet gate scalar g_t ∈ (0,1]
pub fn planet_gate(state: &PlanetState, limits: &PlanetLimits, gain: f64) -> f64 {
    let (e1, e2, e3) = planet_error(state, limits);
    let norm = (e1 * e1 + e2 * e2 + e3 * e3).sqrt();
    (-gain * norm.max(0.0)).exp()
}

/// Boolean P ∈ {0,1}
pub fn planet_boolean(state: &PlanetState, limits: &PlanetLimits) -> u8 {
    let (e1, e2, e3) = planet_error(state, limits);
    let norm = (e1 * e1 + e2 * e2 + e3 * e3).sqrt();
    if norm <= limits.eps { 1 } else { 0 }
}


/// ---------- Tribe State ----------

#[derive(Clone, Debug)]
pub struct TribeState {
    pub id: String,
    pub used_quota: f64,
    pub quota: f64,
}

/// Boolean T_k ∈ {0,1}
pub fn tribe_boolean(tribe: &TribeState) -> u8 {
    if tribe.used_quota <= tribe.quota { 1 } else { 0 }
}


/// ---------- Job State ----------

#[derive(Clone, Debug)]
pub struct Job {
    pub id: String,
    pub tribe_id: String,
    pub est_cost: f64,
    pub base_priority: f64,
    pub planet_weight: f64, // w_planet(j)
    pub valid_individual: bool,
    pub submit_ts: u128,
}

impl Job {
    pub fn new(id: &str, tribe_id: &str, est_cost: f64, base_priority: f64, planet_weight: f64, valid_individual: bool) -> Self {
        let ts = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_millis();
        Self {
            id: id.to_string(),
            tribe_id: tribe_id.to_string(),
            est_cost,
            base_priority,
            planet_weight,
            valid_individual,
            submit_ts: ts,
        }
    }
}

/// Boolean I_j ∈ {0,1}
pub fn individual_boolean(job: &Job) -> u8 {
    if job.valid_individual { 1 } else { 0 }
}


/// ---------- Scheduler Config ----------

#[derive(Clone, Debug)]
pub struct SchedulerConfig {
    pub planet_gain: f64,
}


/// ---------- Scheduler Core ----------

pub struct PlanetGatedScheduler {
    limits: PlanetLimits,
    config: SchedulerConfig,
    tribes: HashMap<String, TribeState>,
    pending: Vec<Job>,
}

impl PlanetGatedScheduler {
    pub fn new(limits: PlanetLimits, config: SchedulerConfig) -> Self {
        Self {
            limits,
            config,
            tribes: HashMap::new(),
            pending: Vec::new(),
        }
    }

    pub fn register_tribe(&mut self, tribe: TribeState) {
        self.tribes.insert(tribe.id.clone(), tribe);
    }

    pub fn submit_job(&mut self, job: Job) {
        self.pending.push(job);
    }

    /// Hook: replace with real sensors
    pub fn read_planet_state(&self) -> PlanetState {
        PlanetState { power: 0.0, carbon: 0.0, grid_stress: 0.0 }
    }

    /// Hook: replace with real GPU executor
    pub fn dispatch_job(&self, job: &Job, cost: f64) {
        println!("Dispatching job {} for {} units", job.id, cost);
    }

    pub fn tick(&mut self) {
        let planet_state = self.read_planet_state();
        let g_t = planet_gate(&planet_state, &self.limits, self.config.planet_gain);
        let P = planet_boolean(&planet_state, &self.limits);

        // Group jobs by tribe
        let mut jobs_by_tribe: HashMap<String, Vec<Job>> = HashMap::new();
        for job in self.pending.drain(..) {
            jobs_by_tribe.entry(job.tribe_id.clone()).or_default().push(job);
        }

        let mut new_pending = Vec::new();

        for (tribe_id, mut jobs) in jobs_by_tribe {
            let tribe = self.tribes.get_mut(&tribe_id).unwrap();
            let T = tribe_boolean(tribe);

            // Emergency mode: P = 0 → only high-planet-weight jobs
            if P == 0 {
                let min_w = 0.7;
                jobs.retain(|j| j.planet_weight >= min_w);
            }

            // Tribe over quota → no allocation
            if T == 0 {
                new_pending.extend(jobs);
                continue;
            }

            let remaining_quota = (tribe.quota - tribe.used_quota).max(0.0);
            let mut tribe_alloc = g_t * remaining_quota;

            // Filter invalid individuals
            jobs.retain(|j| individual_boolean(j) == 1);

            // Priority = base_priority * planet_weight
            jobs.sort_by(|a, b| {
                let pa = a.base_priority * a.planet_weight;
                let pb = b.base_priority * b.planet_weight;
                pb.partial_cmp(&pa).unwrap()
            });

            for job in jobs {
                if tribe_alloc <= 0.0 {
                    new_pending.push(job);
                    continue;
                }

                if job.est_cost <= tribe_alloc {
                    self.dispatch_job(&job, job.est_cost);
                    tribe_alloc -= job.est_cost;
                    tribe.used_quota += job.est_cost;
                } else {
                    new_pending.push(job);
                }
            }
        }

        self.pending = new_pending;
    }
}