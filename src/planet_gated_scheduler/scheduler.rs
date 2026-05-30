use crate::*;

pub struct PlanetGatedScheduler {
    pub limits: PlanetLimits,
    pub gain: f64,
}

impl PlanetGatedScheduler {
    pub fn tick(&self, state: &mut SchedulerState) {
        let g = planet_gate(&state.planet, &self.limits, self.gain);
        let p_ok = planet_ok(&state.planet, &self.limits);

        let mut new_jobs = Vec::new();

        for tribe in &mut state.tribes {
            if !tribe_ok(tribe) {
                continue;
            }

            let mut alloc = g * tribe.remaining();

            let mut tribe_jobs: Vec<Job> = state.jobs
                .iter()
                .filter(|j| j.tribe_id == tribe.id && individual_ok(j))
                .cloned()
                .collect();

            if !p_ok {
                tribe_jobs.retain(|j| j.planet_weight >= 0.7);
            }

            tribe_jobs.sort_by(|a, b| b.score().partial_cmp(&a.score()).unwrap());

            for job in tribe_jobs {
                if job.est_cost <= alloc {
                    alloc -= job.est_cost;
                    tribe.used_quota += job.est_cost;
                } else {
                    new_jobs.push(job);
                }
            }
        }

        state.jobs = new_jobs;
    }
}