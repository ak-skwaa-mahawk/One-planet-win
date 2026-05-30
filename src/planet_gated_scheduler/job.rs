#[derive(Clone, Debug)]
pub struct Job {
    pub id: String,
    pub tribe_id: String,
    pub est_cost: f64,
    pub base_priority: f64,
    pub planet_weight: f64,
    pub valid: bool,
}

impl Job {
    pub fn score(&self) -> f64 {
        self.base_priority * self.planet_weight
    }
}