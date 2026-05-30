from dataclasses import dataclass

EPSILON      = 0.05   # energy gap threshold (no transition zone)
THREAT_MAX   = 0.85   # hard cap: cosmos dominates above this
STRESS_MAX   = 0.85   # hard cap: tribe dominates above this
DAMPING      = 0.25   # how fast weights can move per tick
DOMINANCE_K  = 3.0    # how strong one signal must be to "collapse" regime


@dataclass
class TribalSignal:
    cohesion: float        # 0..1
    stress: float          # 0..1
    trust: float           # 0..1
    attention_load: float  # 0..1

    def magnitude(self) -> float:
        # You can tune this; this is one reasonable starting point.
        # High stress + low trust + high attention_load = strong tribal signal.
        return (
            0.4 * self.stress +
            0.3 * (1.0 - self.trust) +
            0.2 * self.attention_load +
            0.1 * self.cohesion
        )


@dataclass
class CosmicState:
    threat: float   # 0..1
    drift: float    # 0..1
    hype: float     # 0..1

    def magnitude(self) -> float:
        # High threat + high drift = strong cosmic signal.
        return (
            0.5 * self.threat +
            0.3 * self.drift +
            0.2 * self.hype
        )


@dataclass
class Weights:
    tribe: float
    cosmos: float


def damp(new_w: float, old_w: float, damping: float = DAMPING) -> float:
    """Limit how fast the weight can change per tick."""
    delta = new_w - old_w
    if abs(delta) <= damping:
        return new_w
    return old_w + damping * (1 if delta > 0 else -1)


def quantum_resolver(
    tribal_signal: TribalSignal,
    cosmic_state: CosmicState,
    previous: Weights
) -> Weights:
    S_T = tribal_signal.magnitude()
    S_C = cosmic_state.magnitude()

    # 1. Energy gap check (forbidden zone)
    if abs(S_T - S_C) < EPSILON:
        return previous  # hold state, no transition

    # 2. Forbidden transitions (hard sovereignty constraints)
    if cosmic_state.threat > THREAT_MAX:
        return Weights(tribe=0.0, cosmos=1.0)

    if tribal_signal.stress > STRESS_MAX:
        return Weights(tribe=1.0, cosmos=0.0)

    # 3. Raw weights from relative signal strength
    total = S_T + S_C
    if total == 0:
        # No signal anywhere → fall back to previous or neutral
        return previous

    w_T_raw = S_T / total
    w_C_raw = 1.0 - w_T_raw

    # 4. Apply damping (no jitter)
    w_T = damp(w_T_raw, previous.tribe)
    w_C = 1.0 - w_T

    # 5. Correspondence collapse (classical limit)
    if S_T > DOMINANCE_K * S_C:
        return Weights(tribe=1.0, cosmos=0.0)

    if S_C > DOMINANCE_K * S_T:
        return Weights(tribe=0.0, cosmos=1.0)

    return Weights(tribe=w_T, cosmos=w_C)