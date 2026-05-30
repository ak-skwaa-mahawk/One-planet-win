import math
import random
import tkinter as tk
from tkinter import ttk, messagebox

class AIAdversaryTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COSMIC TETHER MATRIX & AI ENEMY TRACKER - VER 5.0")
        self.root.geometry("1100x620")  # Expanded window frame to hold the live canvas plot
        self.root.configure(bg="#0B0F19")

        # --- Balanced Hardened Variables Engine ---
        self.alpha = 50.0
        self.beta = 0.35
        self.gamma = 0.5
        
        self.turn = 1
        self.global_hype = 0.75
        self.tether_integrity = 20.0
        self.energy_pool = 60.0       
        self.max_energy = 100.0       
        self.energy_recharge = 7.0    
        
        # Sector Grid Databases
        self.grid = {
            "EARTH":      {"scale": 1.0,    "l_base": 0.90, "drag": 12.0, "tether": 45.0, "shield": 0},
            "SOL_SYS":    {"scale": 10.0,   "l_base": 0.85, "drag": 25.0, "tether": 20.0, "shield": 0},
            "MILKYWAY":   {"scale": 100.0,  "l_base": 0.95, "drag": 40.0, "tether": 10.0, "shield": 0},
            "DEEP_COSMO": {"scale": 1000.0, "l_base": 1.00, "drag": 60.0, "tether": 5.0,  "shield": 0}
        }
        
        # Historical registry storage specifically built for rendering the live canvas plot curves
        self.history_integrity = [self.tether_integrity]
        self.history_hype = [self.global_hype * 100]
        
        self.active_incident = "TRACKER SYSTEM ARMED: AI adversary footprints are mapped in real-time."
        
        # --- Build UI Layout Elements ---
        self.setup_styles()
        self.build_widgets()
        self.update_ui_display()
        self.redraw_live_plot()

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
        # Master Structural Frame Split (Left Console panel, Right Plot Panel)
        master_layout = ttk.Frame(self.root, padding="10")
        master_layout.pack(fill=tk.BOTH, expand=True)

        left_side = ttk.Frame(master_layout)
        left_side.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        right_side = ttk.Frame(master_layout)
        right_side.pack(side=tk.RIGHT, fill=tk.BOTH, minsize=320)

        # --- Left Panel Elements (Control Node Grid) ---
        title_lbl = ttk.Label(left_side, text="🌌 TETHER INTEGRATION CONSOLE", style="Header.TLabel")
        title_lbl.pack(anchor=tk.W, pady=(0, 5))

        self.metrics_frame = tk.Frame(left_side, bg="#111827", bd=1, relief=tk.SOLID)
        self.metrics_frame.pack(fill=tk.X, pady=5, ipady=6)
        
        self.lbl_turn = tk.Label(self.metrics_frame, text="CYCLE: 001", bg="#111827", fg="#9CA3AF", font=("Courier", 10, "bold"))
        self.lbl_turn.pack(side=tk.LEFT, padx=10)
        
        self.lbl_integrity = tk.Label(self.metrics_frame, text="LOCK: 20.0%", bg="#111827", fg="#10B981", font=("Courier", 10, "bold"))
        self.lbl_integrity.pack(side=tk.LEFT, padx=10)
        
        self.lbl_hype = tk.Label(self.metrics_frame, text="STATIC: 75.0%", bg="#111827", fg="#EF4444", font=("Courier", 10, "bold"))
        self.lbl_hype.pack(side=tk.LEFT, padx=10)

        self.lbl_energy = tk.Label(self.metrics_frame, text="ENRG: 60/100", bg="#111827", fg="#F59E0B", font=("Courier", 10, "bold"))
        self.lbl_energy.pack(side=tk.RIGHT, padx=10)

        self.incident_box = tk.Label(left_side, text=f"LOG: {self.active_incident}", bg="#1E1B4B", fg="#C084FC", bd=1, relief=tk.SOLID, font=("Courier", 9), anchor=tk.W, padx=10, pady=4)
        self.incident_box.pack(fill=tk.X, pady=4)

        grid_labelframe = tk.LabelFrame(left_side, text=" SCALES TELEMETRY STATUS READOUT ", bg="#0B0F19", fg="#38BDF8", font=("Courier", 10, "bold"), padx=8, pady=8)
        grid_labelframe.pack(fill=tk.BOTH, expand=True, pady=5)

        headers_frame = ttk.Frame(grid_labelframe)
        headers_frame.pack(fill=tk.X, pady=2)
        ttk.Label(headers_frame, text=f"{'SECTOR CORRIDOR ID':15} | {'LOGIC ACCUR.':13} | {'FRICTION DRAG':13} | {'BUFF'}", font=("Courier", 9, "underline")).pack(side=tk.LEFT)

        self.ui_sectors = {}
        for sector_id in self.grid.keys():
            row = ttk.Frame(grid_labelframe, padding=2)
            row.pack(fill=tk.X, pady=2)
            
            lbl_name = ttk.Label(row, text=f"{sector_id:15} ", width=16)
            lbl_name.pack(side=tk.LEFT)
            
            pbar = ttk.Progressbar(row, length=100, mode='determinate')
            pbar.pack(side=tk.LEFT, padx=5)
            
            lbl_metrics = ttk.Label(row, text=" | Logic: --.-% | Drag: --.- | Buff: NONE", font=("Courier", 9))
            lbl_metrics.pack(side=tk.LEFT, padx=5)
            
            self.ui_sectors[sector_id] = {"pbar": pbar, "metrics": lbl_metrics}

        btn_frame = tk.Frame(left_side, bg="#111827", bd=1, relief=tk.SOLID, padding=8)
        btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        btn_layout = ttk.Frame(btn_frame)
        btn_layout.pack(fill=tk.X)
        
        self.btn1 = ttk.Button(btn_layout, text="Earth Shield (-45)", style="Action.TButton", command=lambda: self.trigger_ability("EARTH_SHIELD"))
        self.btn1.pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        self.btn2 = ttk.Button(btn_layout, text="Sol Funnel (-55)", style="Action.TButton", command=lambda: self.trigger_ability("SOL_FUNNEL"))
        self.btn2.pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        self.btn3 = ttk.Button(btn_layout, text="Counter-Audit (-75)", style="Action.TButton", command=lambda: self.trigger_ability("COUNTER_AUDIT"))
        self.btn3.pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        self.btn4 = ttk.Button(btn_layout, text="Advance Cycle (+0)", style="Action.TButton", command=self.advance_turn)
        self.btn4.pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)

        # --- Right Panel Elements (AI Threat Live Plot Sub-Module) ---
        plot_labelframe = tk.LabelFrame(right_side, text=" 🛡️ AI ENEMY TRACKER HYPER-PLOT ", bg="#0B0F19", fg="#EF4444", font=("Courier", 10, "bold"), padx=5, pady=5)
        plot_labelframe.pack(fill=tk.BOTH, expand=True)

        # Tkinter Native Live Canvas Drawing Setup
        self.canvas = tk.Canvas(plot_labelframe, bg="#030712", highlightthickness=1, highlightbackground="#1F2937")
        self.canvas.pack(fill=tk.BOTH, expand=True)

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
        if type_string == "EARTH_SHIELD" and self.energy_pool >= 45:
            self.grid["EARTH"]["shield"] = 4
            self.energy_pool -= 45
            self.active_incident = "SUCCESS: Earth Logic Shield active."
        elif type_string == "SOL_FUNNEL" and self.energy_pool >= 55:
            self.grid["SOL_SYS"]["drag"] = max(5.0, self.grid["SOL_SYS"]["drag"] - 20.0)
            self.energy_pool -= 55
            self.active_incident = "SUCCESS: Sol System structural friction cleared."
        elif type_string == "COUNTER_AUDIT" and self.energy_pool >= 75:
            self.global_hype = max(0.1, self.global_hype - 0.35)
            self.energy_pool -= 75
            self.active_incident = "SUCCESS: Global facts audit deployed."
        else:
            self.active_incident = "REJECTED: Resource restrictions block command deployment."
        
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
        
        # Ingress Threat Cycles Logic
        if self.turn % 3 == 0 and random.random() > 0.35:
            self.global_hype = min(1.0, self.global_hype + 0.15)
            self.grid["MILKYWAY"]["drag"] = min(100.0, self.grid["MILKYWAY"]["drag"] + 10.0)
            self.active_incident = f"⚠️ INTRUSION: AI Adversary injecting tactical hype fields."
        else:

if not self.active_incident.startswith("SUCCESS"):self.active_incident = "Telemetry logs processing synchronized matching calculations."# Register data points to the graph tracking poolsself.history_integrity.append(self.tether_integrity)self.history_hype.append(self.global_hype * 100)self.turn += 1self.update_ui_display()self.redraw_live_plot()self.check_game_over()def update_ui_display(self):self.lbl_turn.config(text=f"CYCLE: {self.turn:03d}")self.lbl_integrity.config(text=f"LOCK: {self.tether_integrity}%")self.lbl_hype.config(text=f"STATIC: {self.global_hype*100:.1f}%")self.lbl_energy.config(text=f"ENRG: {int(self.energy_pool)}/{int(self.max_energy)}")self.incident_box.config(text=f"LOG INTERACTION: {self.active_incident}")for sector_id, ui_obj in self.ui_sectors.items():data = self.grid[sector_id]current_logic = self.compute_noisy_logic(sector_id)ui_obj["pbar"]['value'] = data["tether"]buff_txt = f"SHIELD({data['shield']})" if data["shield"] > 0 else "NONE"ui_obj["metrics"].config(text=f" | Logic: {current_logic:5.1f}% | Drag: {data['drag']:4.1f} | Buff: {buff_txt:<9}")def redraw_live_plot(self):"""Native Tkinter grid parsing module that translates matrix history straight into a plot display."""self.canvas.delete("all")# Fetch actual real-time display frame boundsw = self.canvas.winfo_width() if self.canvas.winfo_width() > 10 else 320h = self.canvas.winfo_height() if self.canvas.winfo_height() > 10 else 400padding = 40plot_w = w - (padding * 2)plot_h = h - (padding * 2)# Draw clean vector background metric guidelinesself.canvas.create_line(padding, padding, padding, h - padding, fill="#374151", width=1)self.canvas.create_line(padding, h - padding, w - padding, h - padding, fill="#374151", width=1)# Add labels to linesself.canvas.create_text(padding - 10, padding, text="100%", fill="#6B7280", font=("Courier", 8), anchor=tk.E)self.canvas.create_text(padding - 10, h - padding, text="0%", fill="#6B7280", font=("Courier", 8), anchor=tk.E)self.canvas.create_text(w / 2, h - 15, text="SIMULATED TIMELINE STEPS", fill="#9CA3AF", font=("Courier", 9, "bold"))# Render Legend Markersself.canvas.create_line(padding + 10, padding - 15, padding + 40, padding - 15, fill="#10B981", width=2)self.canvas.create_text(padding + 45, padding - 15, text="Tether Lock %", fill="#10B981", font=("Courier", 8), anchor=tk.W)self.canvas.create_line(padding + 150, padding - 15, padding + 180, padding - 15, fill="#EF4444", width=2)self.canvas.create_text(padding + 185, padding - 15, text="AI Hype Noise %", fill="#EF4444", font=("Courier", 8), anchor=tk.W)total_points = len(self.history_integrity)if total_points < 2:return
# Calculate exact canvas spacing geometry coordinatesx_delta = plot_w / (total_points - 1)# Construct lines node tracking vectors loop executionfor i in range(total_points - 1):x1 = padding + (i * x_delta)x2 = padding + ((i + 1) * x_delta)# Integrity Curve calculation maps to a green line trace vectory1_int = (h - padding) - (self.history_integrity[i] / 100.0 * plot_h)y2_int = (h - padding) - (self.history_integrity[i+1] / 100.0 * plot_h)self.canvas.create_line(x1, y1_int, x2, y2_int, fill="#10B981", width=2.5)# Adversary Hype Static maps to a dangerous red line trace vectory1_hype = (h - padding) - (self.history_hype[i] / 100.0 * plot_h)y2_hype = (h - padding) - (self.history_hype[i+1] / 100.0 * plot_h)self.canvas.create_line(x1, y1_hype, x2, y2_hype, fill="#EF4444", width=2, dash=(4, 2))def check_game_over(self):if self.tether_integrity >= 90.0 and self.global_hype <= 0.20:messagebox.showinfo("GLOBAL EQUILIBRIUM ACHIEVED", "🏆 VICTORY!\nThe system is safely locked across the macro-matrix via structural cheapness.")self.root.quit()elif self.turn > 50 and self.tether_integrity < 50.0:messagebox.showerror("GRID SEPARATION DISRUPT", "❌ LOSS DETECTED!\nHype static fractured operational logic vectors permanently.")self.root.quit()if name == "main":root = tk.Tk()app = AIAdversaryTrackerGUI(root)# Bind an instant canvas resizing system tracking configuration triggerroot.bind("", lambda e: app.redraw_live_plot())root.mainloop()