import random

class Quadrant:
    def __init__(self, name):
        self.name = name
        self.bureaucracy_points = 100
        self.capital_points = 100
        self.approval_rating = 80
        self.market_cost_baseline = 50  # Lower is more efficient

class GlobalMatrix:
    def __init__(self):
        # Initializing three distinct player quadrants
        self.quadrants = {
            "NA": Quadrant("North America"),
            "EU": Quadrant("European Union"),
            "IP": Quadrant("Indo-Pacific")
        }
        # Centralized superpower metrics affecting the whole globe
        self.superpower_hype = 70
        self.tether_strength = 50

    def display_global_status(self):
        print("\n==================== GLOBAL MATRIX STATUS ====================")
        print(f"Superpower Global Hype: {self.superpower_hype}% | Lite Tether Stability: {self.tether_strength}%")
        print("--------------------------------------------------------------")
        for code, q in self.quadrants.items():
            print(f"[{q.name}] Bur: {q.bureaucracy_points} | Cap: {q.capital_points} | App: {q.approval_rating}% | Cost: {q.market_cost_baseline}")
        print("==============================================================")

    def execute_quadrant_choice(self, quadrant_code, choice):
        if quadrant_code not in self.quadrants:
            return "Invalid quadrant."
        
        q = self.quadrants[quadrant_code]
        print(f"\n[Directive executed by {q.name} on Choice {choice}]")

        if choice == 1:
            q.bureaucracy_points -= 5
            q.capital_points -= 5
            self.superpower_hype = min(100, self.superpower_hype + 20)
            self.tether_strength = min(100, self.tether_strength + 5)
            q.approval_rating -= random.randint(1, 10)
            
        elif choice == 2:
            q.capital_points -= 20
            self.superpower_hype = max(0, self.superpower_hype - 25)
            q.market_cost_baseline -= 10
            if random.random() < 0.4:
                q.capital_points -= 15
                print(f"-> Alert: Retaliatory economic leak detected in {q.name}!")
                
        elif choice == 3:
            q.bureaucracy_points -= 30
            self.tether_strength = min(100, self.tether_strength + 30)
            # Tighter regulations slightly raise localized market friction cost
            q.market_cost_baseline += 5 
            
        elif choice == 4:
            q.approval_rating -= 20
            q.market_cost_baseline -= 25
            self.superpower_hype = max(0, self.superpower_hype - 10)
            # Interdependence: Lowering cost here puts downward pressure on everyone else
            for target_code, target_q in self.quadrants.items():
                if target_code != quadrant_code:
                    target_q.market_cost_baseline = max(5, target_q.market_cost_baseline - 5)
            print("-> Economy spun up! Market efficiency forced neighboring regions to cut costs.")

        self.check_system_equilibrium()

    def check_system_equilibrium(self):
        # If global hype peaks, it damages approval ratings across the board
        if self.superpower_hype >= 100:
            print("\n⚠️ SYSTEM ALERT: Superpower Hype has peaked globally! Public unrest spreading.")
            for q in self.quadrants.values():
                q.approval_rating -= 15
        
        # Check for global win state
        all_costs_low = all(q.market_cost_baseline <= 25 for q in self.quadrants.values())
        if all_costs_low and self.tether_strength >= 80:
            print("\n🏆 GLOBAL EQUILIBRIUM ACHIEVED: All quadrants locked at universal cheapness!")

# --- MULTI-PLAYER RUN DEMO ---
matrix = GlobalMatrix()
matrix.display_global_status()

# Step 1: North America plays a localized economic audit (Choice 2)
matrix.execute_quadrant_choice("NA", 2)

# Step 2: European Union uses an Institutional Lock (Choice 3) to freeze the tether
matrix.execute_quadrant_choice("EU", 3)

# Step 3: Indo-Pacific undergoes an internal pivot (Choice 4), dragging global costs down
matrix.execute_quadrant_choice("IP", 4)

matrix.display_global_status()
