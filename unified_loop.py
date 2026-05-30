# unified_loop.py

from cosmic_to_muni.translator import CosmicToMuniTranslator
from tribe_to_muni.translator import TribeToMuniTranslator
from tribe_cosmos_to_muni.blender import TribalCosmicMuniBlender
from pwc.loop import PWCController
from six_cylinder_boundary import SubstrateEngine

# Your engines
cosmic_engine = CosmicEngine(...)      # One-Planet-Win wrapper
tribal_engine = TribalEngine(...)      # however you model tribe
substrate = SubstrateEngine(...)
pwc = PWCController(engine=substrate)

cosmic_to_muni = CosmicToMuniTranslator()
tribe_to_muni = TribeToMuniTranslator()
blender = TribalCosmicMuniBlender()


def unified_tick(dt: float = 1.0):
    # 1) Advance cosmos
    cosmic_engine.step(dt)
    cosmic_state = cosmic_engine.get_state()      # -> CosmicState

    # 2) Update tribe
    tribal_engine.step(dt, cosmic_state)
    tribe_state = tribal_engine.get_state()       # -> TribeState

    # 3) Translate to muni targets
    cosmic_muni = cosmic_to_muni.translate(cosmic_state)
    tribal_muni = tribe_to_muni.translate(tribe_state)

    # 4) Blend into unified muni envelope
    muni_targets = blender.blend(tribal_muni, cosmic_muni)

    # 5) Drive substrate via PWC
    substrate.set_setpoints(
        spin=muni_targets.spin_setpoint,
        pressure=muni_targets.pressure_setpoint,
        temp=muni_targets.temp_setpoint,
    )
    snapshot = substrate.closed_loop_tick()

    # 6) Optionally let PWC run episodes on top of this baseline
    # trajectory, score = pwc.run_episode(horizon=H)

    # 7) Feed stability back up if you want adaptive behavior
    stability = snapshot.safety_flags.stability_warning
    cosmic_engine.ingest_muni_feedback(snapshot)
    tribal_engine.ingest_muni_feedback(snapshot)

    return snapshot