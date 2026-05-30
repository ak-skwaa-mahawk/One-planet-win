#[derive(Clone, Debug)]
pub struct TribeState {
    pub id: String,
    pub quota: f64,
    pub used_quota: f64,
}

impl TribeState {
    pub fn remaining(&self) -> f64 {
        (self.quota - self.used_quota).max(0.0)
    }
}