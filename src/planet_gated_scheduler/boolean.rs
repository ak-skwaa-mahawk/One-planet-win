use crate::{PlanetState, PlanetLimits, TribeState, Job};

pub fn planet_ok(p: &PlanetState, lim: &PlanetLimits) -> bool {
    let e = p.error(lim);
    let norm = (e[0]*e[0] + e[1]*e[1] + e[2]*e[2]).sqrt();
    norm <= lim.eps
}

pub fn tribe_ok(t: &TribeState) -> bool {
    t.used_quota <= t.quota
}

pub fn individual_ok(j: &Job) -> bool {
    j.valid
}