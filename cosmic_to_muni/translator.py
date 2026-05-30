# cosmic_to_muni/translator.py
import math
from .types import CosmicState, MuniTargets


class CosmicToMuniTranslator:
    def __init__(
        self,
        base_spin: float = 1.5,
        base_pressure: float = 1.0,
        base_temp: float = 0.0,
    ):
        self.base_spin = base_spin
        self.base_pressure = base_pressure
        self.base_temp = base_temp

    def aggregate_cosmic_state(self, state: CosmicState):
        """Collapse quadrant signals into global aggregates."""
        if not state.quadrants:
            return 0.0, 0.0, 0.0

        drifts = [q.drift for q in state.quadrants.values()]
        hypes = [q.hype for q in state.quadrants.values()]
        threats = [q.threat for q in state.quadrants.values()]

        avg_drift = sum(drifts) / len(drifts)
        max_hype = max(hypes)
        max_threat = max(threats)

        return avg_drift, max_hype, max_threat

    def translate(self, state: CosmicState) -> MuniTargets:
        """
        Map cosmic signals to six-cylinder setpoints.

        - High hype → reduce pressure, reduce temp.
        - High threat → reduce spin, reduce pressure.
        - High drift → adjust spin/pressure to pull back toward equilibrium.
        """

        avg_drift, max_hype, max_threat = self.aggregate_cosmic_state(state)

        # Start from base
        spin = self.base_spin
        pressure = self.base_pressure
        temp = self.base_temp

        # 1) Hype dampening: hype ∈ [0,1] → pressure/temp scaling
        hype_factor = 1.0 - 0.6 * max_hype      # up to -60% pressure/temp
        pressure *= hype_factor
        temp *= hype_factor

        # 2) Threat response: threat ∈ [0,1] → spin/pressure reduction
        threat_factor = 1.0 - 0.7 * max_threat  # up to -70% spin/pressure
        spin *= threat_factor
        pressure *= threat_factor

        # 3) Drift correction: avg_drift pulls spin/pressure up or down
        # Positive drift = overextended → reduce spin/pressure slightly
        drift_correction = -0.3 * avg_drift
        spin += drift_correction
        pressure += drift_correction

        # 4) Equilibrium lock: if lock is strong, allow slightly higher spin
        spin *= 1.0 + 0.2 * (state.equilibrium_lock - 0.5)

        # Clamp to sane ranges
        spin = max(0.2, min(3.0, spin))
        pressure = max(0.1, min(2.0, pressure))
        temp = max(-1.0, min(1.0, temp))

        return MuniTargets(
            spin_setpoint=spin,
            pressure_setpoint=pressure,
            temp_setpoint=temp,
        )