class PriorityResolver:
    """
    Computes dynamic weights for tribal vs cosmic control over muni.
    Returns (tribal_weight, cosmic_weight) that always sum to 1.0.
    """

    def resolve(self, tribe: TribeState, cosmos: CosmicState) -> tuple[float, float]:
        # Base: tribe slightly closer to muni reality
        tribal_base = 0.55
        cosmic_base = 0.45

        # If stress or attention are high → give tribe more say (protect muni)
        stress_factor = max(tribe.stress, tribe.attention_load)  # 0..1
        tribal_from_stress = 0.15 * stress_factor

        # If cosmic threat is high → give cosmos more say (macro defense)
        threat_factor = cosmos.max_threat  # 0..1
        cosmic_from_threat = 0.2 * threat_factor

        # If equilibrium_lock is strong → allow cosmos a bit more steering
        lock_factor = max(0.0, cosmos.equilibrium_lock - 0.5) * 2.0  # 0..1
        cosmic_from_lock = 0.1 * lock_factor

        tribal_weight = tribal_base + tribal_from_stress
        cosmic_weight = cosmic_base + cosmic_from_threat + cosmic_from_lock

        # Normalize
        total = max(tribal_weight + cosmic_weight, 1e-6)
        tribal_weight /= total
        cosmic_weight /= total

        return tribal_weight, cosmic_weight