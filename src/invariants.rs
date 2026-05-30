use crate::{Job, PlanetLimits, PlanetState, TribeState};
use crate::boolean::planet_ok;

pub fn inv_individual(jobs: &[Job]) -> bool {
    jobs.iter().all(|j| j.valid)
}

pub fn inv_tribe(tribes: &[TribeState]) -> bool {
    tribes.iter().all(|t| t.used_quota <= t.quota)
}

pub fn inv_emergency(jobs: &[Job], planet: &PlanetState, limits: &PlanetLimits) -> bool {
    if planet_ok(planet, limits) {
        return true;
    }
    jobs.iter().all(|j| j.planet_weight >= 0.7)
}