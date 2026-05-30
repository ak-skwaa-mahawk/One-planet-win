def muni_tick_from_targets(substrate: SubstrateEngine, muni_targets: MuniTargets):
    # 1) Apply unified muni targets
    substrate.set_setpoints(
        spin=muni_targets.spin_setpoint,
        pressure=muni_targets.pressure_setpoint,
        temp=muni_targets.temp_setpoint,
    )

    # 2) Run one closed-loop physics tick
    snapshot = substrate.closed_loop_tick()

    # 3) This snapshot is the physically realized state:
    #    - gs_state: geometry + six-face boundary
    #    - manifold_state: 6D particle field
    #    - safety_flags: stability, caps, violations
    #    - lifecycle_state: health, ticks, uptime
    return snapshot