use crate::{PlanetState, PlanetLimits};

pub fn planet_gate(p: &PlanetState, lim: &PlanetLimits, gain: f64) -> f64 {
    let e = p.error(lim);
    let norm = (e[0]*e[0] + e[1]*e[1] + e[2]*e[2]).sqrt();
    (-gain * norm.max(0.0)).exp()
}