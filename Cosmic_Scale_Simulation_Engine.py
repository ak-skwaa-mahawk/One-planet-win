import random

class CosmicSector:
    def __init__(self, name, scale_multiplier):
        self.name = name
        self.scale = scale_multiplier  # Multiplier for resource volume
        
        # Sector-specific infrastructure metrics
        self.logical_alignment = 100    # Out of 100. Measures resistance to irrational hype.
        self.tether_integration = 10   # Percent integration into the main network.
        self.structural_drag = 40       # Systemic friction. Lower is more efficient.

class GalacticTetherNetwork:
    def __init__(self):
        # Initializing the distinct cosmic tiers of the project
        self.sectors = {
            "EARTH": CosmicSector("Immediate Earth Grid", 1),
            "SOL": CosmicSector("Sol Interplanetary Tier", 10),
            "MILKYWAY": CosmicSector("Milky Way Core Sectors", 100),
            "DEEPCOSMOS": CosmicSector("Extragalactic Quadrants", 1000)
        }
        # Central equilibrium variables for network defense
        self.global_irrationality_hype = 65
        self.tether_integrity_score = 25

    def display_network_matrix(self):
        print("\n======================= COSMIC TETHER MATRIX =======================")
        print(f"Network Integrity: {self.tether_integrity_score}% | External Disruption Hype: {self.global_irrationality_hype}%")
        print("--------------------------------------------------------------------")
        for code, sector in self.sectors.items():
            print(f"[{code:10}] Integration: {sector.tether_integration:3}% | Logic Alignment: {sector.logical_alignment:3}% | Drag: {sector.structural_drag}")
        print("====================================================================")

    def deploy_logical_protocol(self, target_code, directive_type):
        if target_code not in self.sectors:
            return "Invalid coordinate sector."
        
        sector = self.sectors[target_code]
        print(f"\n[Executing Directive: '{directive_type}' on {sector.name}]")

        if directive_type == "SYNCHRONIZE":
            # Forces the sector to match the universal equal split
            sector.tether_integration = min(100, sector.tether_integration + 25)
            sector.structural_drag = max(5, sector.structural_drag - 15)
            self.tether_integrity_score = min(100, self.tether_integrity_score + 10)
            
        elif directive_type == "DEFEND_BY_LOGIC":
            # Purges emotional bias and unverified hype from the local sector network
            sector.logical_alignment = min(100, sector.logical_alignment + 15)
            self.global_irrationality_hype = max(0, self.global_irrationality_hype - 20)
            # A systematic audit may cause temporary structural drag due to alignment checks
            sector.structural_drag = min(100, sector.structural_drag + 5)
            
        elif directive_type == "FLATTEN_CEILING":
            # Implements the 'hate everyone equal' optimization baseline
            # Deepest cost reduction cuts friction exponentially across the connected network
            sector.structural_drag = max(1, int(sector.structural_drag * 0.4))
            for s_code, s_obj in self.sectors.items():
                if s_code != target_code:
                    s_obj.structural_drag = max(1, s_obj.structural_drag - 5)
            print("-> Equilibrium shift: Optimization ripple felt across adjacent tiers.")

        self.evaluate_existential_lock()

    def evaluate_existential_lock(self):
        # High external hype degrades alignment across unintegrated tiers
        if self.global_irrationality_hype >= 90:
            print("\n⚠️ LOGIC CRITICAL: External irrationality spikes detected. Tiers degrading.")
            for sector in self.sectors.values():
                if sector.tether_integration < 50:
                    sector.logical_alignment = max(0, sector.logical_alignment - 20)

        # Winning Equilibrium Condition
        fully_integrated = all(s.tether_integration >= 80 for s in self.sectors.values())
        minimized_drag = all(s.structural_drag <= 10 for s in self.sectors.values())
        
        if fully_integrated and minimized_drag and self.global_irrationality_hype <= 15:
            print("\n🏆 COSMIC equilibrium SECURED: System locked across the Milky Way and beyond.")

# --- SIMULATION ORCHESTRATION ---
network = GalacticTetherNetwork()
network.display_network_matrix()

# Step 1: Establish foundational baseline on Immediate Earth
network.deploy_logical_protocol("EARTH", "SYNCHRONIZE")

# Step 2: Purge systemic anomalies and enforce mathematical logic at the Galactic Core level
network.deploy_logical_protocol("MILKYWAY", "DEFEND_BY_LOGIC")

# Step 3: Flatten the operational ceilings to pull the Deep Cosmos into alignment
network.deploy_logical_protocol("DEEPCOSMOS", "FLATTEN_CEILING")

network.display_network_matrix()
