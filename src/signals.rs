#[derive(Clone, Debug)]
pub struct PlanetState {
    pub power: f64,
    pub carbon: f64,
    pub grid: f64,
}

#[derive(Clone, Debug)]
pub struct PlanetLimits {
    pub power_max: f64,
    pub carbon_max: f64,
    pub grid_max: f64,
    pub eps: f64,
}

impl PlanetState {
    pub fn error(&self, lim: &PlanetLimits) -> [f64; 3] {
        [
            self.power - lim.power_max,
            self.carbon - lim.carbon_max,
            self.grid - lim.grid_max,
        ]
    }
}