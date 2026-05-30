import math

class ScaleVectorEngine:
    def __init__(self):
        # Operational constants for the simulation grid
        self.alpha = 50.0  # Base integration scaling factor
        self.beta = 0.35   # Neighbor pull strength multiplier
        self.gamma = 0.5   # Dimensional scale friction constant

    def calculate_convergence(self, sector_scale, logic, drag, neighbor_efficiency_avg):
        """
        Executes the continuous mathematical vector formula to find the 
        exact conversion speed of a specific cosmic tier.
        """
        # Step 1: Normalize inputs to floats
        L_s = float(logic) / 100.0  # Normalize logic percentage to 0.0-1.0
        D_s = max(1.0, float(drag)) # Prevent division by zero
        S = float(sector_scale)
        E_adj = float(neighbor_efficiency_avg)

        # Step 2: Compute the Physical Scale Friction Core
        scale_friction = math.pow(S, self.gamma)
        
        # Step 3: Compute Internal Vector (Logic divided by Scale-Friction and Structural Drag)
        internal_velocity = (self.alpha * L_s) / (scale_friction * D_s)
        
        # Step 4: Compute External Neighbor Vector (Adjacent Equilibrium Pull)
        external_pull = self.beta * E_adj

        # Step 5: Combine Vectors to get the final Convergence Velocity
        total_convergence = internal_velocity + external_pull
        
        # Return rounded vector speed bounded safely between 0.1% and 50.0% per turn
        return max(0.1, min(50.0, round(total_convergence, 2)))

# --- VECTOR VERIFICATION TEST RUN ---
engine = ScaleVectorEngine()

print("=== MATHEMATICAL VECTOR SIMULATION ===")

# Test 1: Immediate Earth Grid (Scale = 1, High Logic, Low Drag, Neighbors average 10% efficiency)
earth_speed = engine.calculate_convergence(sector_scale=1, logic=95, drag=15, neighbor_efficiency_avg=10)
print(f"Earth Grid Conversion Velocity:      +{earth_speed}% per step")

# Test 2: Milky Way Core (Scale = 100, High Logic, High Structural Drag due to raw size)
milkyway_speed = engine.calculate_convergence(sector_scale=100, logic=85, drag=55, neighbor_efficiency_avg=25)
print(f"Milky Way Sector Conversion Velocity: +{milkyway_speed}% per step")

# Test 3: Deep Cosmos (Scale = 1000, Peak Logic, Minimal Drag due to 'Hate Everyone Equal' locking)
cosmos_speed = engine.calculate_convergence(sector_scale=1000, logic=100, drag=1, neighbor_efficiency_avg=50)
print(f"Deep Cosmos Conversion Velocity:     +{cosmos_speed}% per step")
print("======================================")
