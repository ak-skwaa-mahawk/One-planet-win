import math
import random
import tkinter as tk
from tkinter import ttk, messagebox

class HardenedCosmicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COSMIC TETHER INTEGRATION CORE - VER 4.0")
        self.root.geometry("850x600")
        self.root.configure(bg="#0B0F19")

        # --- Balanced Hardened Variables Engine ---
        self.alpha = 50.0
        self.beta = 0.35
        self.gamma = 0.5
        
        self.turn = 1
        self.global_hype = 0.75
        self.tether_integrity = 20.0
        self.energy_pool = 60.0       # Starts lower for immediate tension
        self.max_energy = 100.0       # Capped lower to prevent item hoarding
        self.energy_recharge = 7.0    # Tight, restrictive energy flow
        
        # Sector Grid Databases
        self.grid = {
            "EARTH":      {"scale": 1.0,    "l_base": 0.90, "drag": 12.0, "tether": 45.0, "shield": 0},
            "SOL_SYS":    {"scale": 10.0,   "l_base": 0.85, "drag": 25.0, "tether": 20.0, "shield": 0},
            "MILKYWAY":   {"scale": 100.0,  "l_base": 0.95, "drag": 40.0, "tether": 10.0, "shield": 0},
            "DEEP_COSMO": {"scale": 1000.0, "l_base": 1.00, "drag": 60.0, "tether": 5.0,  "shield": 0}
        }
        
        self.active_incident = "SYSTEM COLD BOOT: Enforce baseline math equations."
        
        # --- Build UI Layout Elements ---
        self.setup_styles()
        self.build_widgets()
        self.update_ui_display()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(".", background="#0B0F19", foreground="#E2E8F0")
        style.configure("TFrame", background="#0B0F19")
        style.configure("TLabel", background="#0B0F19", font=("Courier", 10))
        style.configure("Header.TLabel", font=("Courier", 14, "bold"), foreground="#38BDF8")
        style.configure("Action.TButton", font=("Courier", 10, "bold"), background="#1E293B", foreground="#F8FAFC")
        style.map("Action.TButton", background=[('active', '#334155')])

    def build_widgets(self):
        # Master Frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header Sector Banner
        title_lbl = ttk.Label(main_frame, text="🌌 MILKY WAY TETHER INTEGRATION ENGINE", style="Header.TLabel")
        title_lbl.pack(anchor=tk.W, pady=(0, 10))

        # Core Metrics Overview Bar Panel
        self.metrics_frame = tk.Frame(main_frame, bg="#111827", bd=1, relief=tk.SOLID, padding=10)
        self.metrics_frame.pack(fill=tk.X, pady=5)
        
        self.lbl_turn = tk.Label(self.metrics_frame, text="CYCLE: 001", bg="#111827", fg="#9CA3AF", font=("Courier", 11, "bold"))
        self.lbl_turn.pack(side=tk.LEFT, padx=15)
        
        self.lbl_integrity = tk.Label(self.metrics_frame, text="GLOBAL MATRIX LOCK: 20.0%", bg="#111827", fg="#10B981", font=("Courier", 11, "bold"))
        self.lbl_integrity.pack(side=tk.LEFT, padx=15)
        
        self.lbl_hype = tk.Label(self.metrics_frame, text="ADVERSARIAL HYPER-STATIC: 75.0%", bg="#111827", fg="#EF4444", font=("Courier", 11, "bold"))
        self.lbl_hype.pack(side=tk.LEFT, padx=15)

        self.lbl_energy = tk.Label(self.metrics_frame, text="ENERGY: 60/100 MJ", bg="#111827", fg="#F59E0B", font=("Courier", 11, "bold"))
        self.lbl_energy.pack(side=tk.RIGHT, padx=15)

        # Incident / Intrusion Alert Banner Window Box
        self.incident_box = tk.Label(main_frame, text=f"LOG STATUS: {self.active_incident}", bg="#1E1B4B", fg="#C084FC", bd=1, relief=tk.SOLID, font=("Courier", 10), anchor=tk.W, padx=10, pady=6)
        self.incident_box.pack(fill=tk.X, pady=5)

        # Telemetry Display Grid Data List Section Frame
        grid_labelframe = tk.LabelFrame(main_frame, text=" DYNAMIC SCALES STATUS READOUT ", bg="#0B0F19", fg="#38BDF8", font=("Courier", 10, "bold"), padx=10, pady=10)
        grid_labelframe.pack(fill=tk.BOTH, expand=True, pady=10)

        # Table Column Descriptions row lines
        headers_frame = ttk.Frame(grid_labelframe)
        headers_frame.pack(fill=tk.X, pady=2)
        ttk.Label(headers_frame, text=f"{'SECTOR CORRIDOR ID':20} | {'LOGIC ACC. (Ls)':18} | {'FRICTION DRAG':16} | {'ACTIVE BUFF'}", font=("Courier", 10, "underline")).pack(side=tk.LEFT)

        # Generate UI dynamic visual lines per sector object rows
        self.ui_sectors = {}
        for sector_id in self.grid.keys():
            row = ttk.Frame(grid_labelframe, padding=4)
            row.pack(fill=tk.X, pady=3)
            
            lbl_name = ttk.Label(row, text=f"{sector_id:20} ", width=22)
            lbl_name.pack(side=tk.LEFT)
            
            pbar = ttk.Progressbar(row, length=140, mode='determinate')
            pbar.pack(side=tk.LEFT, padx=5)
            
            lbl_metrics = ttk.Label(row, text=" | Logic: --.-% | Drag: --.- | Buff: NONE", font=("Courier", 10))
            lbl_metrics.pack(side=tk.LEFT, padx=5)
            
            self.ui_sectors[sector_id] = {"pbar": pbar, "metrics": lbl_metrics}

        # Command Control panel interact operational array row buttons frame
        btn_frame = tk.Frame(main_frame, bg="#111827", bd=1, relief=tk.SOLID, padding=10)
        btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Label(btn_frame, text="OPERATIVE COMMAND CONSOLE INTERACTION METRICS:", bg="#111827", fg="#9CA3AF", font=("Courier", 9, "bold")).pack(anchor=tk.W, pady=(0,5))
        
        btn_layout = ttk.Frame(btn_frame)
        btn_layout.pack(fill=tk.X)
        
        self.btn1 = ttk.Button(btn_layout, text="Earth Shield (-45 ENRG)", style="Action.TButton", command=lambda: self.trigger_ability("EARTH_SHIELD"))
        self.btn1.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.btn2 = ttk.Button(btn_layout, text="Sol Funnel (-55 ENRG)", style="Action.TButton", command=lambda: self.trigger_ability("SOL_FUNNEL"))
        self.btn2.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.btn3 = ttk.Button(btn_layout, text="Counter-Audit (-75 ENRG)", style="Action.TButton", command=lambda: self.trigger_ability("COUNTER_AUDIT"))
        self.btn3.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.btn4 = ttk.Button(btn_layout, text="Advance Passive Cycle (+0)", style="Action.TButton", command=self.advance_turn)
        self.btn4.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

    def compute_noisy_logic(self, sector_id):
        sec = self.grid[sector_id]
        if sec["shield"] > 0:
            return round(sec["l_base"] * 100, 1)
        S = sec["scale"]
        t_integrated = sec["tether"] / 100.0
        scale_damping = math.log(S + math.e)
        noise_impact = (self.global_hype * (1.0 - t_integrated) / scale_damping) * random.uniform(0.95, 1.05)
        return round(max(0.0, sec["l_base"] - noise_impact) * 100, 1)

    def compute_lock_velocity(self, sector_id, current_logic):
        sec = self.grid[sector_id]
        L_s = current_logic / 100.0
        D_s = max(1.0, float(sec["drag"]))
        S = sec["scale"]
        other_tethers = [s["tether"] for k, s in self.grid.items() if k != sector_id]
        e_adj = sum(other_tethers) / len(other_tethers)
        
        scale_friction = math.pow(S, self.gamma)
        internal_vel = (self.alpha * L_s) / (scale_friction * D_s)
        external_pull = self.beta * e_adj
        return round(max(0.1, min(30.0, internal_vel + external_pull)), 2)

    def trigger_ability(self, type_string):
        if type_string == "EARTH_SHIELD":
            if self.energy_pool >= 45:
                self.grid["EARTH"]["shield"] = 4
                self.energy_pool -= 45
                self.active_incident = "SUCCESS: Earth Local Matrix logic field deployed securely."
            else:
                self.active_incident = "REJECTED: Energy requirements unmet for Earth Shield projection."
        elif type_string == "SOL_FUNNEL":
            if self.energy_pool >= 55:
                self.grid["SOL_SYS"]["drag"] = max(5.0, self.grid["SOL_SYS"]["drag"] - 20.0)
                self.energy_pool -= 55
                self.active_incident = "SUCCESS: Resource pipeline optimized; mechanical drag crushed."
            else:
                self.active_incident = "REJECTED: Energy requirements unmet for Sol Funnel configuration."
        elif type_string == "COUNTER_AUDIT":
            if self.energy_pool >= 75:
                self.global_hype = max(0.1, self.global_hype - 0.35)
                self.energy_pool -= 75
                self.active_incident = "SUCCESS: Factual audited metrics published globally. Adversary hype dropped."
            else:
                self.active_incident = "REJECTED: Energy requirements unmet for wide Global Counter-Audit."
        
        self.update_ui_display()

    def advance_turn(self):
        total_tether = 0
        for sector_id, data in self.grid.items():
            if data["shield"] > 0:
                data["shield"] -= 1
            logic_score = self.compute_noisy_logic(sector_id)
            velocity = self.compute_lock_velocity(sector_id, logic_score)
            self.grid[sector_id]["tether"] = min(100.0, round(self.grid[sector_id]["tether"] + velocity, 1))
            total_tether += self.grid[sector_id]["tether"]
            
        self.tether_integrity = round(total_tether / len(self.grid), 1)
        self.energy_pool = min(self.max_energy, self.energy_pool + self.energy_recharge)
        
        # Tight dynamic random adversarial strikes loop setup
        if self.turn % 3 == 0 and random.random() > 0.35:
            self.global_hype = min(1.0, self.global_hype + 0.15)
            self.grid["MILKYWAY"]["drag"] = min(100.0, self.grid["MILKYWAY"]["drag"] + 10.0)
            self.active_incident = f"⚡ INTRUSION CYCLE DETECTED! Global Hype surged across sectors."
        else:
