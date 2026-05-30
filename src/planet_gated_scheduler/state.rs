use crate::{PlanetState, TribeState, Job};

pub struct SchedulerState {
    pub planet: PlanetState,
    pub tribes: Vec<TribeState>,
    pub jobs: Vec<Job>,
}