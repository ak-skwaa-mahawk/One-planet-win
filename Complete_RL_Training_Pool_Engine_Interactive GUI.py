import math
import random
import tkinter as tk
from tkinter import ttk, messagebox

class RLLogicTrainingCore:
    def __init__(self, root):
        self.root = root
        self.root.title("COSMIC TETHER REINFORCEMENT LEARNING POOL - VER 6.0")
        self.root.geometry("1150x640")
        self.root.configure(bg="#0B0F19")

        # --- Balanced Hardened System Engine ---
        self.alpha, self.beta, self.gamma = 50.0, 0.35, 0.5
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
        
        # RL Training Pool Metrics
        self.total_simulated_episodes = 0
        self.current_policy_edge = 15.2  # The control gap margin percentage
        self.history_integrity = [self.tether_integrity]
        self.history_hype = [self.global_hype * 100]
        
        self.active_incident = "PREDICTIVE ENGAGEMENT ARMED: System is tracking and training against all profiles."
        
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
        master_layout = ttk.Frame(self.root, padding="10")
        master_layout.pack(fill=tk.BOTH, expand=True)

        left_side = ttk.Frame(master_layout)
        left_side.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        right_side = ttk.Frame(master_layout)
        right_side.pack(side=tk.RIGHT, fill=tk.BOTH, minsize=360)

        # --- Left Panel Elements (Control Core) ---
        title_lbl = ttk.Label(left_side, text="🌌 PREDICTIVE CONTAINMENT NODE", style="Header.TLabel")
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

        grid_labelframe = tk.LabelFrame(left_side, text=" SCALES TELEMETRY Baselines ", bg="#0B0F19", fg="#38BDF8", font=("Courier", 10, "bold"), padx=8, pady=8)
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

        # --- Right Panel Elements (RL Simulation Training Dashboard) ---
        plot_labelframe = tk.LabelFrame(right_side, text=" 🛡️ ASYMMETRIC TRAINING POOL & EDGE GRAPH ", bg="#0B0F19", fg="#10B981", font=("Courier", 10, "bold"), padx=5, pady=5)
        plot_labelframe.pack(fill=tk.BOTH, expand=True)

        # RL Stats Bar Panel
        rl_metrics = tk.Frame(plot_labelframe, bg="#062017", padding=5)
        rl_metrics.pack(fill=tk.X, pady=(0, 5))
        
        self.lbl_pool_size = tk.Label(rl_metrics, text="TRAINED EPISODES: 00000", bg="#062017", fg="#A7F3D0", font=("Courier", 9, "bold"))
        self.lbl_pool_size.pack(side=tk.LEFT, padx=5)
        
        self.lbl_control_gap = tk.Label(rl_metrics, text="CONTROL GAP: +15.2%", bg="#062017", fg="#34D399", font=("Courier", 9, "bold"))
        self.lbl_control_gap.pack(side=tk.RIGHT, padx=5)

        # Tkinter Canvas Drawing Engine
        self.canvas = tk.Canvas(plot_labelframe, bg="#030712", highlightthickness=1, highlightbackground="#064E3B")
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

        # Core Training Execution Button
        self.btn_train_pool = ttk.Button(plot_labelframe, text="⚡ RUN BACKGROUND POOL TRAINING GRADIENT (+250 EPISODES)", style="Action.TButton", command=self.execute_pool_training_cycle)
        self.btn_train_pool.pack(fill=tk.X, ipady=3)

    def compute_noisy_logic(self, sector_id):
        sec = self.grid[sector_id]
        if sec["shield"] > 0:
            return round(sec["l_base"] * 100, 1)
        S = sec["scale"]
        t_integrated = sec["tether"] / 100.0
        scale_damping = math.log(S + math.e)
        
        # Policy edge mitigation factor: Higher simulated policy edge reduces adversary noise intensity directly
        mitigation = max(0.1, 1.0 - (self.current_policy_edge / 100.0))
        noise_impact = (self.global_hype * (1.0 - t_integrated) / scale_damping) * random.uniform(0.95, 1.05) * mitigation
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

    def execute_pool_training_cycle(self):
        """Simulates parallel training episodes to optimize predictive algorithms and widen the control gap."""
        self.total_simulated_episodes += 250
        
        # Policy gradient calculations: The system increases efficiency parameters based on pool scale volume
        policy_gain = random.uniform(2.5, 6.0)
        self.current_policy_edge = min(85.0, round(self.current_policy_edge + policy_gain, 1))
        
        # Reward function output modifier: Training actively compresses adversary hype potential
        self.global_hype = max(0.05, round(self.global_hype - 0.08, 2))
        self.energy_pool = min(self.max_energy, self.energy_pool + 15.0) # Reward bonus energy injection
        
        self.active_incident = f"TRAINING SUCCESS: Optimized 250 models. Control gap widened by +{policy_gain}%!"
        self.update_ui_display()
        self.redraw_live_plot()

    def trigger_ability(self, type_string):
        if type_string == "EARTH_SHIELD" and self.energy_pool >= 45:
            self.grid["EARTH"]["shield"] = 4

self.energy_pool -= 45self.active_incident = "PRE-EMPTIVE COUNTERMEASURE: Earth Core Shield verified active."elif type_string == "SOL_FUNNEL" and self.energy_pool >= 55:self.grid["SOL_SYS"]["drag"] = max(5.0, self.grid["SOL_SYS"]["drag"] - 20.0)self.energy_pool -= 55self.active_incident = "OPTIMIZATION DEPLOYED: Sol drag metrics compressed."elif type_string == "COUNTER_AUDIT" and self.energy_pool >= 75:self.global_hype = max(0.05, self.global_hype - 0.35)self.energy_pool -= 75self.active_incident = "AUDIT INJECTED: Adversarial hype static dismantled."else:self.active_incident = "REJECTED: Energy constraint threshold limitation."self.update_ui_display()def advance_turn(self):total_tether = 0for sector_id, data in self.grid.items():if data["shield"] > 0:data["shield"] -= 1logic_score = self.compute_noisy_logic(sector_id)velocity = self.compute_lock_velocity(sector_id, logic_score)self.grid[sector_id]["tether"] = min(100.0, round(self.grid[sector_id]["tether"] + velocity, 1))total_tether += self.grid[sector_id]["tether"]self.tether_integrity = round(total_tether / len(self.grid), 1)self.energy_pool = min(self.max_energy, self.energy_pool + self.energy_recharge)# Asymmetric Attack Engine (Attempts to pierce the system gap)if self.turn % 3 == 0:# If the player has a wide control gap, the enemy's scaling strike parameter is largely nullifiedstrike_power = max(0.02, 0.22 - (self.current_policy_edge / 400.0))self.global_hype = min(1.0, round(self.global_hype + strike_power, 2))self.active_incident = f"⚠️ THREAT ATTEMPT: Hype vector checked and blunted by control gap padding."else:if not self.active_incident.startswith("TRAINING") and not self.active_incident.startswith("PRE-EMPTIVE"):self.active_incident = "Systems operating on stable equilibrium vector loops."self.history_integrity.append(self.tether_integrity)self.history_hype.append(self.global_hype * 100)self.turn += 1self.update_ui_display()self.redraw_live_plot()self.check_game_over()def update_ui_display(self):self.lbl_turn.config(text=f"CYCLE: {self.turn:03d}")self.lbl_integrity.config(text=f"LOCK: {self.tether_integrity}%")self.lbl_hype.config(text=f"STATIC: {self.global_hype*100:.1f}%")self.lbl_energy.config(text=f"ENRG: {int(self.energy_pool)}/{int(self.max_energy)}")self.incident_box.config(text=f"LOG INTERACTION: {self.active_incident}")self.lbl_pool_size.config(text=f"TRAINED EPISODES: {self.total_simulated_episodes:05d}")self.lbl_control_gap.config(text=f"CONTROL GAP: +{self.current_policy_edge}%")for sector_id, ui_obj in self.ui_sectors.items():data = self.grid[sector_id]current_logic = self.compute_noisy_logic(sector_id)ui_obj["pbar"]['value'] = data["tether"]buff_txt = f"SHIELD({data['shield']})" if data["shield"] > 0 else "NONE"ui_obj["metrics"].config(text=f" | Logic: {current_logic:5.1f}% | Drag: {data['drag']:4.1f} | Buff: {buff_txt:<9}")
def redraw_live_plot(self):self.canvas.delete("all")w = self.canvas.winfo_width() if self.canvas.winfo_width() > 10 else 360h = self.canvas.winfo_height() if self.canvas.winfo_height() > 10 else 380padding = 40plot_w = w - (padding * 2)plot_h = h - (padding * 2)# Draw structural framing rulesself.canvas.create_line(padding, padding, padding, h - padding, fill="#047857", width=1)self.canvas.create_line(padding, h - padding, w - padding, h - padding, fill="#047857", width=1)total_points = len(self.history_integrity)if total_points < 2:returnx_delta = plot_w / (total_points - 1)for i in range(total_points - 1):x1 = padding + (i * x_delta)x2 = padding + ((i + 1) * x_delta)# System Integrity Curve Progressy1_int = (h - padding) - (self.history_integrity[i] / 100.0 * plot_h)y2_int = (h - padding) - (self.history_integrity[i+1] / 100.0 * plot_h)self.canvas.create_line(x1, y1_int, x2, y2_int, fill="#10B981", width=2.5)# Adversary Hype Static Line (Suppressed over time via training runs)y1_hype = (h - padding) - (self.history_hype[i] / 100.0 * plot_h)y2_hype = (h - padding) - (self.history_hype[i+1] / 100.0 * plot_h)self.canvas.create_line(x1, y1_hype, x2, y2_hype, fill="#EF4444", width=2, dash=(4, 2))def check_game_over(self):if self.tether_integrity >= 90.0 and self.global_hype <= 0.20:messagebox.showinfo("CONTAINMENT COMPLETE", "🏆 PERFECT STABILIZATION LOCK ON!\nYour predictive training pool permanently closed the control gap. Adversary neutralized.")self.root.quit()elif self.turn > 50 and self.tether_integrity < 50.0:messagebox.showerror("GRID SEPARATION", "❌ REJECTED!\nYou failed to maintain a sufficient predictive training edge.")self.root.quit()if name == "main":root = tk.Tk()app = RLLogicTrainingCore(root)root.bind("", lambda e: app.redraw_live_plot())root.mainloop()