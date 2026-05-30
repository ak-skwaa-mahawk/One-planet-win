# tribe_cosmos_to_muni/blender.py

class TribalCosmicMuniBlender:
    """
    Blends tribal and cosmic muni targets into a single stable envelope.
    """

    def __init__(self, tribal_weight=0.55, cosmic_weight=0.45):
        # Tribal slightly dominates because it is closer to muni reality.
        self.tw = tribal_weight
        self.cw = cosmic_weight

    def blend(self, tribal: MuniTargets, cosmic: MuniTargets) -> MuniTargets:
        spin = self.tw * tribal.spin_setpoint     + self.cw * cosmic.spin_setpoint
        pressure = self.tw * tribal.pressure_setpoint + self.cw * cosmic.pressure_setpoint
        temp = self.tw * tribal.temp_setpoint     + self.cw * cosmic.temp_setpoint

        # Clamp to substrate-safe ranges
        spin = max(0.2, min(3.0, spin))
        pressure = max(0.1, min(2.0, pressure))
        temp = max(-1.0, min(1.0, temp))

        return MuniTargets(
            spin_setpoint=spin,
            pressure_setpoint=pressure,
            temp_setpoint=temp,
        )