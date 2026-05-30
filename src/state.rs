use crate::{PlanetState, TribeState, Job};

#[derive(Clone, Debug)]
pub struct SchedulerState {
    pub planet: PlanetState,
    pub tribes: Vec<TribeState>,
    pub jobs: Vec<Job>,
}