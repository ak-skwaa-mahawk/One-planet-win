resolver = PriorityResolver()
tw, cw = resolver.resolve(tribe_state, cosmic_state)

blender = TribalCosmicMuniBlender(tribal_weight=tw, cosmic_weight=cw)
muni_targets = blender.blend(tribal_muni, cosmic_muni)