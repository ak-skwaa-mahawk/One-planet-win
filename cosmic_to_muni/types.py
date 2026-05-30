# cosmic_to_muni/types.py
from dataclasses import dataclass
from typing import Dict


@dataclass
class CosmicQuadrantState:
    drift: float          # + = overextended, - = under-engaged
    hype: float           # 0..1
    threat: float         # 0..1


@dataclass
class CosmicState:
    quadrants: Dict[str, CosmicQuadrantState]
    equilibrium_lock: float   # 0..1, higher = more stable


@dataclass
class MuniTargets:
    spin_setpoint: float
    pressure_setpoint: float
    temp_setpoint: float