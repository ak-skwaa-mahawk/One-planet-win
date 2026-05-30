@dataclass
class MuniTargets:
    spin_setpoint: float
    pressure_setpoint: float
    temp_setpoint: float

@dataclass
class TribeState:
    cohesion: float        # 0..1
    stress: float          # 0..1
    trust: float           # 0..1
    attention_load: float  # 0..1

@dataclass
class CosmicState:
    equilibrium_lock: float   # 0..1
    max_threat: float         # 0..1
    max_hype: float           # 0..1