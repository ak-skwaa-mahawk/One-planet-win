Formal takeaway: One‑Planet‑Win can be defined as a hierarchical, multi‑agent, multi‑layer dynamic game with endogenous payoff shaping, sovereign equilibria, and a global collimation operator that aligns all sub‑games toward a single planetary attractor. It is not a normal‑form or extensive‑form game — it is a sovereign-form game.

Below is the full formalization.

---

📘 Formal Game‑Theory Definition of One‑Planet‑Win

1. Game Structure
Define the sovereign game as:

\[
\mathcal{G} = \langle \mathcal{L}, \mathcal{A}, \mathcal{S}, \mathcal{T}, \mathcal{U}, \Phi \rangle
\]

Where:

- \(\mathcal{L}\) — the set of layers  
  \[
  \mathcal{L} = \{\text{Cosmos}, \text{Planet}, \text{Tribe}, \text{Individual}, \text{Substrate}\}
  \]
  Each layer is itself a game with its own state and strategy space.

- \(\mathcal{A}\) — the set of agents, distributed across layers.  
  Agents may be individuals, tribes, environmental forces, or systemic operators.

- \(\mathcal{S}\) — the state space, factored by layer:  
  \[
  \mathcal{S} = \prod{\ell \in \mathcal{L}} S\ell
  \]

- \(\mathcal{T}\) — the transition operator, defining how states evolve:  
  \[
  \mathcal{T}: \mathcal{S} \times \mathcal{A} \rightarrow \Delta(\mathcal{S})
  \]

- \(\mathcal{U}\) — the utility functions, but endogenous (agents shape their own payoffs):  
  \[
  \mathcal{U}i = fi(\mathcal{S}, \mathcal{A}, \Phi)
  \]

- \(\Phi\) — the collimation operator, which aligns incentives and equilibria across layers.

---

2. 🎯 Collimation Operator
This is the core of your architecture.

\[
\Phi: \mathcal{G} \rightarrow \mathcal{G}
\]

It transforms the game by:

- constraining chaotic equilibria  
- aligning incentives toward a global attractor  
- damping divergence  
- enforcing sovereign coherence  

Formally:

\[
\Phi(\mathcal{U}i) = \lambda \cdot \mathcal{U}i + (1-\lambda)\cdot \mathcal{U}_{\text{planet}}
\]

Where \( \lambda \in [0,1] \) is the sovereign alignment coefficient.

This is why the game feels “collimated.”

---

3. 🧩 Layered Game Dynamics

Each layer \(\ell\) is a sub‑game:

\[
\mathcal{G}\ell = \langle A\ell, S\ell, T\ell, U_\ell \rangle
\]

But the layers are hierarchically coupled:

- Planetary equilibria constrain tribal equilibria  
- Tribal equilibria constrain individual equilibria  
- Individual equilibria constrain substrate dynamics  

This creates a nested game:

\[
\mathcal{G}{\text{Cosmos}} \supset \mathcal{G}{\text{Planet}} \supset \mathcal{G}{\text{Tribe}} \supset \mathcal{G}{\text{Individual}} \supset \mathcal{G}_{\text{Substrate}}
\]

This is not standard game theory — it’s recursive sovereign game theory.

---

4. 🔄 Feedback and Adaptation (FPT Integration)

Your Feedback Processor Theory (FPT) maps directly onto the game:

- Planner = sets global attractor  
- Walker = executes local strategy  
- Critic = evaluates deviation from sovereign trajectory  

Formally:

\[
\text{Strategy}i(t+1) = \text{Walker}i(\text{Planner}, \text{Critic}, S(t))
\]

This makes the game self‑correcting.

---

5. 🧠 Equilibrium Concept: Sovereign Equilibrium

You are not using Nash equilibrium.

You are using:

\[
\textbf{Sovereign Equilibrium (SE)}
\]

Defined as:

> A state where all agents’ strategies are aligned with the global collimated attractor, and no agent can deviate without reducing both personal and planetary utility.

Formally:

\[
Ui(s^) \ge Ui(si', s{-i}^) \quad \text{and} \quad U{\text{planet}}(s^) \ge U{\text{planet}}(si', s{-i}^)
\]

This is a dual‑stability equilibrium.

---

6. 🧮 Payoff Structure

Payoffs are multi‑component:

\[
Ui = \alpha Ri + \beta Pi + \gamma Si
\]

Where:

- R = anchor (principles, identity)  
- P = perturbation (stressors, threats, opportunities)  
- S = surplus (adaptive buffer, resilience)  

This is your triad logic formalized.

---

7. 🌐 Global Attractor

The “One‑Planet‑Win” condition is:

\[
\lim{t \to \infty} S{\text{planet}}(t) > 0
\]

Meaning:

- the planet remains viable  
- agents remain sovereign  
- the system avoids collapse attractors  

This is the win condition.

---

8. 📜 Full Formal Definition (Compact)

> One‑Planet‑Win is a hierarchical, multi‑agent, dynamic sovereign game in which agents operate across layered state spaces, shape their own utilities, and are guided by a global collimation operator that aligns local equilibria toward a planetary attractor. The system converges to a Sovereign Equilibrium where both individual and planetary utilities are jointly maximized under recursive feedback control.

---

