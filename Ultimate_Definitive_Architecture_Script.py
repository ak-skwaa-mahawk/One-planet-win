import math
import random
import tkinter as tk
from tkinter import ttk, messagebox

class FinalCosmicLedgerCore:
    def __init__(self, root):
        self.root = root
        self.root.title("PREDICTIVE CONTAINER GRID & ASYMMETRIC LEDGER - VER 7.0")
        self.root.geometry("1200x660")
        self.root.configure(bg="#0B0F19")

        # --- Re-Balanced Hardened Core Engine ---
        self.alpha, self.beta, self.gamma = 50.0, 0.35, 0.5
        self.turn = 1
        self.global_hype = 0.70
        self.tether_integrity = 20.0
        self.energy_pool = 70.0       
        self.max_energy = 100.0       
        self.energy_recharge = 7.0    
        
        # Sector Grid Databases
        self.grid = {
            "EARTH":      {"scale": 1.0,    "l_base": 0.90, "drag": 12.0, "tether": 45.0, "shield": 0},
            "SOL_SYS":    {"scale": 10.0,   "l_base": 0.85, "drag": 25.0, "tether": 20.0, "shield": 0},
            "MILKYWAY":   {"scale": 100.0,  "l_base": 0.95, "drag": 40.0, "tether": 10.0, "shield": 0},
            "DEEP_COSMO": {"scale": 1000.0, "l_base": 1.00, "drag": 60.0, "tether": 5.0,  "shield": 0}
        }
        
        # RL Training & Ledger Registry Metrics
        self.total_simulated_episodes = 0
        self.current_policy_edge = 15.0  
        self.history_integrity = [self.tether_integrity]
        self.history_hype = [self.global_hype * 100]
        
        # --- Asymmetric Ledger Accounting Variables ---
        self.total_energy_spent = 0.0
        self.structural_waste_index = 137.0  # Lower is cleaner
        self.net_capital_efficiency = 78.5   # Target > 90%
        
        self.active_incident = "CORE BOOT: Asymmetric Ledger accounting active. Tracking neural volatility."
        
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
        style.configure("Header.TLabel", font=("Courier", 13, "bold"), foreground="#38BDF8")
        style.configure("Action.TButton", font=("Courier", 9, "bold"), background="#1E293B", foreground="#F8FAFC")
        style.map("Action.TButton", background=[('active', '#334155')])

    def build_widgets(self):
        master_layout = ttk.Frame(self.root, padding="8")
        master_layout.pack(fill=tk.BOTH, expand=True)

        # 3-Column Split Interface Layout Grid
        left_side = ttk.Frame(master_layout)
        left_side.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 6))

        center_side = ttk.Frame(master_layout)
        center_side.pack(side=tk.LEFT, fill=tk.BOTH, minsize=340, padx=(0, 6))

        right_side = ttk.Frame(master_layout)
        right_side.pack(side=tk.RIGHT, fill=tk.BOTH, minsize=320)

        # --- LEFT PANEL: Operational Console Grid ---
        title_lbl = ttk.Label(left_side, text="🌌 CONTROL MATRIX OPERATIVE", style="Header.TLabel")
        title_lbl.pack(anchor=tk.W, pady=(0, 4))

        self.metrics_frame = tk.Frame(left_side, bg="#111827", bd=1, relief=tk.SOLID)
        self.metrics_frame.pack(fill=tk.X, pady=4, ipady=4)
        
        self.lbl_turn = tk.Label(self.metrics_frame, text="CYC: 001", bg="#111827", fg="#9CA3AF", font=("Courier", 9, "bold"))
        self.lbl_turn.pack(side=tk.LEFT, padx=6)
        self.lbl_integrity = tk.Label(self.metrics_frame, text="LOCK: 20%", bg="#111827", fg="#10B981", font=("Courier", 9, "bold"))
        self.lbl_integrity.pack(side=tk.LEFT, padx=6)
        self.lbl_hype = tk.Label(self.metrics_frame, text="STATIC: 70%", bg="#111827", fg="#EF4444", font=("Courier", 9, "bold"))
        self.lbl_hype.pack(side=tk.LEFT, padx=6)
        self.lbl_energy = tk.Label(self.metrics_frame, text="ENRG: 70/100", bg="#111827", fg="#F59E0B", font=("Courier", 9, "bold"))
        self.lbl_energy.pack(side=tk.RIGHT, padx=6)

        self.incident_box = tk.Label(left_side, text=f"LOG: {self.active_incident}", bg="#1E1B4B", fg="#C084FC", bd=1, relief=tk.SOLID, font=("Courier", 9), anchor=tk.W, padx=8, pady=4)
        self.incident_box.pack(fill=tk.X, pady=4)

        grid_frame = tk.LabelFrame(left_side, text=" SCALES TELEMETRY CONSOLE ", bg="#0B0F19", fg="#38BDF8", font=("Courier", 9, "bold"), padx=6, pady=6)
        grid_frame.pack(fill=tk.BOTH, expand=True, pady=4)

        self.ui_sectors = {}
        for sector_id in self.grid.keys():
            row = ttk.Frame(grid_frame, padding=1)
            row.pack(fill=tk.X, pady=2)
            ttk.Label(row, text=f"{sector_id:12}", width=13).pack(side=tk.LEFT)
            pbar = ttk.Progressbar(row, length=80, mode='determinate')
            pbar.pack(side=tk.LEFT, padx=4)
            lbl_m = ttk.Label(row, text=" | Logic: --% | Drag: --", font=("Courier", 9))
            lbl_m.pack(side=tk.LEFT, padx=4)
            self.ui_sectors[sector_id] = {"pbar": pbar, "metrics": lbl_m}

        btn_frame = tk.Frame(left_side, bg="#111827", bd=1, relief=tk.SOLID, padding=6)
        btn_frame.pack(fill=tk.X, pady=(4, 0))
        btn_layout = ttk.Frame(btn_frame)
        btn_layout.pack(fill=tk.X)
        
        ttk.Button(btn_layout, text="Shield (-45)", style="Action.TButton", command=lambda: self.trigger_ability("EARTH_SHIELD")).pack(side=tk.LEFT, padx=1, expand=True, fill=tk.X)
        ttk.Button(btn_layout, text="Funnel (-55)", style="Action.TButton", command=lambda: self.trigger_ability("SOL_FUNNEL")).pack(side=tk.LEFT, padx=1, expand=True, fill=tk.X)
        ttk.Button(btn_layout, text="Audit (-75)", style="Action.TButton", command=lambda: self.trigger_ability("COUNTER_AUDIT")).pack(side=tk.LEFT, padx=1, expand=True, fill=tk.X)
        ttk.Button(btn_layout, text="Advance (+0)", style="Action.TButton", command=self.advance_turn).pack(side=tk.LEFT, padx=1, expand=True, fill=tk.X)

        # --- CENTER PANEL: AI Threat Live Canvas Plot ---
        plot_frame = tk.LabelFrame(center_side, text=" 🛡️ AI ADVERSARIAL MUTATION TRACKER ", bg="#0B0F19", fg="#EF4444", font=("Courier", 9, "bold"), padx=4, pady=4)
        plot_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(plot_frame, bg="#030712", highlightthickness=1, highlightbackground="#1F2937")
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=(0, 4))
        
        ttk.Button(plot_frame, text="⚡ EXECUTE OPTIMIZATION GRADIENT (+250 EPISODES)", style="Action.TButton", command=self.run_training_pool).pack(fill=tk.X)

        # --- RIGHT PANEL: Asymmetric Economy Ledger Sheet ---
        ledger_frame = tk.LabelFrame(right_side, text=" 📊 ASYMMETRIC ECONOMY LEDGER ", bg="#0B0F19", fg="#F59E0B", font=("Courier", 9, "bold"), padx=6, pady=6)
        ledger_frame.pack(fill=tk.BOTH, expand=True)

        # Ledger Summary Readout Widgets
        self.ledger_summary_box = tk.Frame(ledger_frame, bg="#1C1917", padding=6, bd=1, relief=tk.SOLID)
        self.ledger_summary_box.pack(fill=tk.X, pady=(0, 6))
        
        self.lbl_ledger_spent = tk.Label(self.ledger_summary_box, text="TOTAL ENERGY SPENT: 0.0 MJ", bg="#1C1917", fg="#FDBA74", font=("Courier", 9, "bold"))
        self.lbl_ledger_spent.pack(anchor=tk.W)
        self.lbl_ledger_waste = tk.Label(self.ledger_summary_box, text="STRUCTURAL WASTE: 137.0", bg="#1C1917", fg="#FCA5A5", font=("Courier", 9, "bold"))
        self.lbl_ledger_waste.pack(anchor=tk.W)
        self.lbl_ledger_eff = tk.Label(self.ledger_summary_box, text="NET NET COEFF EFF: 78.5%", bg="#1C1917", fg="#86EFAC", font=("Courier", 9, "bold"))
        self.lbl_ledger_eff.pack(anchor=tk.W)

        # Scrolling Real-Time Transaction Ledger History Logs
        tk.Label(ledger_frame, text="REAL-TIME LEDGER AUDIT STREAM:", bg="#0B0F19", fg="#78716C", font=("Courier", 8, "bold")).pack(anchor=tk.W)
        self.ledger_text_log = tk.Text(ledger_frame, bg="#0C0A09", fg="#F59E0B", font=("Courier", 8), state=tk.DISABLED, highlightthickness=0)
        self.ledger_text_log.pack(fill=tk.BOTH, expand=True)

    def compute_noisy_logic(self, sector_id):
        sec = self.grid[sector_id]
        if sec["shield"] > 0: return round(sec["l_base"] * 100, 1)
        S = sec["scale"]
        t_integrated = sec["tether"] / 100.0
        scale_damping = math.log(S + math.e)
        mitigation = max(0.1, 1.0 - (self.current_policy_edge / 100.0))
        noise = (self.global_hype * (1.0 - t_integrated) / scale_damping) * random.uniform(0.95, 1.05) * mitigation
        return round(max(0.0, sec["l_base"] - noise) * 100, 1)

    def compute_lock_velocity(self, sector_id, current_logic):
        sec = self.grid[sector_id]
        L_s, D_s, S = current_logic / 100.0, max(1.0, float(sec["drag"])), sec["scale"]
        other_tethers = [s["tether"] for k, s in self.grid.items() if k != sector_id]
        e_adj = sum(other_tethers) / len(other_tethers)
        scale_friction = math.pow(S, self.gamma)
        return round(max(0.1, min(30.0, ((self.alpha * L_s) / (scale_friction * D_s)) + (self.beta * e_adj))), 2)

    def log_transaction(self, message):
        """Appends a cryptographically format audited record straight to the scrolling Ledger window pane."""
        self.ledger_text_log.config(state=tk.NORMAL)
        self.ledger_text_log.insert(tk.END, f"[{self.turn:03d}] AUDIT >> {message}\n")
        self.ledger_text_log.see(tk.END)
        self.ledger_text_log.config(state=tk.DISABLED)

    def run_training_pool(self):
        self.total_simulated_episodes += 250
        gain = random.uniform(2.5, 5.0)
        self.current_policy_edge = min(85.0, round(self.current_policy_edge + gain, 1))
        self.global_hype = max(0.05, round(self.global_hype - 0.06, 2))
        
        # Accounting metrics alteration
        self.structural_waste_index = max(40.0, round(self.structural_waste_index - 8.5, 1))

self.net_capital_efficiency = min(99.5, round(self.net_capital_efficiency + 1.8, 1))self.log_transaction(f"Gradient optimization loop completed. Mitigated +250 profiles. Gap: +{gain}%")self.active_incident = "TRAINING LOGGED: Optimization parameters integrated securely."self.update_ui_display()self.redraw_live_plot()def trigger_ability(self, type_string):if type_string == "EARTH_SHIELD" and self.energy_pool >= 45:self.grid["EARTH"]["shield"] = 4self.energy_pool -= 45self.total_energy_spent += 45self.log_transaction("DEPL: Earth Local Logic Shield activated. Capital escrow frozen.")elif type_string == "SOL_FUNNEL" and self.energy_pool >= 55:self.grid["SOL_SYS"]["drag"] = max(5.0, self.grid["SOL_SYS"]["drag"] - 20.0)self.energy_pool -= 55self.total_energy_spent += 55self.log_transaction("OPTIM: Sol friction array parameters compressed by manual balance funnel.")elif type_string == "COUNTER_AUDIT" and self.energy_pool >= 75:self.global_hype = max(0.05, self.global_hype - 0.35)self.energy_pool -= 75self.total_energy_spent += 75self.log_transaction("PURGE: Disinformation data audit executed globally. Hype lines smashed.")else:self.active_incident = "REJECTED: Ledger verification failure. Resource allocation blocked."self.update_ui_display()returnself.active_incident = "COMMAND LOGGED: Asymmetric parameter vectors altered successfully."self.update_ui_display()def advance_turn(self):total_tether = 0for sector_id, data in self.grid.items():if data["shield"] > 0: data["shield"] -= 1logic_score = self.compute_noisy_logic(sector_id)velocity = self.compute_lock_velocity(sector_id, logic_score)self.grid[sector_id]["tether"] = min(100.0, round(self.grid[sector_id]["tether"] + velocity, 1))total_tether += self.grid[sector_id]["tether"]self.tether_integrity = round(total_tether / len(self.grid), 1)self.energy_pool = min(self.max_energy, self.energy_pool + self.energy_recharge)# --- Neural Mutation Factor & Threat Generator ---if self.turn % 5 == 0:  # Neural Mutation check windowif random.random() > 0.40:# Rogue data algorithm encounters bypass standard network filters completelymutation_spike = random.uniform(0.18, 0.32)self.global_hype = min(1.0, round(self.global_hype + mutation_spike, 2))self.structural_waste_index = min(300.0, round(self.structural_waste_index + 35.0, 1))self.net_capital_efficiency = max(40.0, round(self.net_capital_efficiency - 5.5, 1))self.active_incident = f"⚡ MUTATION ANOMALY: Rogue algorithm injected +{int(mutation_spike*100)}% unpredictable static!"self.log_transaction(f"CRITICAL: Neural Mutation detected. Structural waste index spiked.")else:self.active_incident = "Mutation profile scanning sequence passed cleanly."elif self.turn % 3 == 0:strike_power = max(0.02, 0.20 - (self.current_policy_edge / 400.0))self.global_hype = min(1.0, round(self.global_hype + strike_power, 2))self.active_incident = "⚠️ THREAT ATTEMPT: Standard hype footprint checked by control gap."else:if not self.active_incident.startswith("⚡") and not self.active_incident.startswith("COMMAND"):self.active_incident = "Ledger accounting streams matching standard baseline synchronization."self.history_integrity.append(self.tether_integrity)self.history_hype.append(self.global_hype * 100)self.turn += 1self.update_ui_display()self.redraw_live_plot()self.check_game_over()def update_ui_display(self):self.lbl_turn.config(text=f"CYC: {self.turn:03d}")self.lbl_integrity.config(text=f"LOCK: {self.tether_integrity}%")self.lbl_hype.config(text=f"STATIC: {self.global_hype*100:.1f}%")self.lbl_energy.config(text=f"ENRG: {int(self.energy_pool)}/{int(self.max_energy)}")self.incident_box.config(text=f"LOG INTERACTION: {self.active_incident}")# Ledger summary pane labels configuration updateself.lbl_ledger_spent.config(text=f"TOTAL ENERGY SPENT: {self.total_energy_spent:.1f} MJ")self.lbl_ledger_waste.config(text=f"STRUCTURAL WASTE: {self.structural_waste_index}")self.lbl_ledger_eff.config(text=f"NET CAPITAL EFFICIENCY: {self.net_capital_efficiency}%")
for sector_id, ui_obj in self.ui_sectors.items():data = self.grid[sector_id]current_logic = self.compute_noisy_logic(sector_id)ui_obj["pbar"]['value'] = data["tether"]buff_txt = f"SHLD({data['shield']})" if data["shield"] > 0 else "NONE"ui_obj["metrics"].config(text=f" | Log: {current_logic:4.0f}% | Drg: {data['drag']:2.0f} | Bff: {buff_txt:<8}")def redraw_live_plot(self):self.canvas.delete("all")w = self.canvas.winfo_width() if self.canvas.winfo_width() > 10 else 340h = self.canvas.winfo_height() if self.canvas.winfo_height() > 10 else 400padding = 35plot_w, plot_h = w - (padding * 2), h - (padding * 2)self.canvas.create_line(padding, padding, padding, h - padding, fill="#1E293B")self.canvas.create_line(padding, h - padding, w - padding, h - padding, fill="#1E293B")total_points = len(self.history_integrity)if total_points < 2: returnx_delta = plot_w / (total_points - 1)for i in range(total_points - 1):x1, x2 = padding + (i * x_delta), padding + ((i + 1) * x_delta)y1_int = (h - padding) - (self.history_integrity[i] / 100.0 * plot_h)y2_int = (h - padding) - (self.history_integrity[i+1] / 100.0 * plot_h)self.canvas.create_line(x1, y1_int, x2, y2_int, fill="#10B981", width=2)y1_hype = (h - padding) - (self.history_hype[i] / 100.0 * plot_h)y2_hype = (h - padding) - (self.history_hype[i+1] / 100.0 * plot_h)self.canvas.create_line(x1, y1_hype, x2, y2_hype, fill="#EF4444", width=1.5, dash=(3, 3))def check_game_over(self):if self.tether_integrity >= 90.0 and self.global_hype <= 0.20:messagebox.showinfo("MATRIX EQUILIBRIUM ACHIEVED", f"🏆 ABSOLUTE LOCK!\nNetwork secured across all training layers with a Net Capital Efficiency of {self.net_capital_efficiency}%!")self.root.quit()elif self.turn > 50 and self.tether_integrity < 50.0:messagebox.showerror("LEDGER CONTAINMENT BREAK", "❌ FAILURE!\nRogue mutations corrupted core logical alignment maps permanently.")self.root.quit()if name == "main":root = tk.Tk()app = FinalCosmicLedgerCore(root)root.bind("", lambda e: app.redraw_live_plot())root.mainloop()