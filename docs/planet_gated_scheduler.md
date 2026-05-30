Below is a repo‑native document, written exactly in the One‑planet‑win voice: terse, geometric, sovereign, and system‑first. It reads like it belongs in your cathedral—no fluff, no apologies, just the machinery.

You can drop this in as:

docs/planetgatedscheduler.md

---

Planet‑Gated Scheduler

A Collimated Compute Regulator for Sovereign Systems

0. Intent

The Planet‑Gated Scheduler (PGS) is the execution throat of One‑Planet‑Win.  
It enforces the tri‑layer boolean hierarchy:

\[
P \le T \le I
\]

where:

- I = Individual validity  
- T = Tribe quota integrity  
- P = Planetary stability  

PGS ensures that no compute action can violate this ordering.  
It is the collimator that prevents runaway extraction and forces all computation to remain inside the planetary tube.

---

1. State Machine

The scheduler is a discrete‑time dynamical system:

\[
S{t+1} = F(St)
\]

with global state:

\[
St = \big(x^Pt,\ (u{k,t}){k\in\mathcal{K}},\ \mathcal{J}_t\big)
\]

Where:

1.1 Planet State
\[
x^Pt = (Et,\ Ct,\ Gt)
\]

- \(E_t\): power draw  
- \(C_t\): carbon / externality proxy  
- \(G_t\): grid / thermal stress  

Planetary error:

\[
e^Pt = x^Pt - x^{P,\max}
\]

Planet boolean:

\[
Pt = \mathbf{1}\big(\|e^Pt\|2 \le \varepsilonP\big)
\]

---

1.2 Tribe State

For each tribe \(k\):

- Quota: \(Q_k\)  
- Used quota: \(u_{k,t}\)

Tribe boolean:

\[
T{k,t} = \mathbf{1}(u{k,t} \le Q_k)
\]

---

1.3 Individual Jobs

Each job \(j\) has:

- Tribe: \(k(j)\)  
- Estimated cost: \(e_j\)  
- Base priority: \(p_j\)  
- Planet weight: \(w_j \in [0,1]\)  
- Individual boolean: \(I_{j,t} \in \{0,1\}\)

Eligible jobs:

\[
\mathcal{E}t = \{ j \in \mathcal{J}t \mid I_{j,t} = 1 \}
\]

---

2. Planet Gate

The planet gate is the scalar that compresses or expands compute throughput:

\[
gt = \exp\big(-K \cdot \max(0,\|e^Pt\|_2)\big)
\]

Properties:

- \(g_t = 1\) when planet is stable  
- \(g_t \to 0\) as planetary stress increases  
- Monotone, smooth, sovereign‑aligned  

This is the collimation gain.

---

3. Emergency Mode

When \(P_t = 0\):

- Only high‑planet‑weight jobs survive:
  \[
  w_j \ge \bar{w}
  \]
- Tribe allocations shrink by \(g_t\)  
- Forbidden patterns become repulsive  

This is the planetary recoil mechanism.

---

4. Allocation Law

For each tribe \(k\):

Remaining quota:

\[
r{k,t} = \max(0, Qk - u_{k,t})
\]

Planet‑gated allocation:

\[
a_{k,t} =
\begin{cases}
gt \cdot r{k,t} & T_{k,t} = 1 \\
0 & T_{k,t} = 0
\end{cases}
\]

Within tribe \(k\), jobs are sorted by collimated priority:

\[
\pij = pj \cdot w_j
\]

Dispatch rule:

\[
j \in Dt \iff ej \le a_{k(j),t}
\]

Deferred jobs remain in \(\mathcal{J}_{t+1}\).

---

5. State Transitions

5.1 Tribe Usage
\[
u{k,t+1} = u{k,t} + \sum{j \in Dt,\ k(j)=k} e_j
\]

5.2 Job Set
\[
\mathcal{J}{t+1} = \mathcal{J}t \setminus D_t
\]

5.3 Planet Dynamics
\[
x^P{t+1} = fP(x^Pt, Dt)
\]

\(f_P\) is external: the world’s response to compute.

---

6. Invariants

These are the sovereign guarantees PGS must uphold.

6.1 Boolean Hierarchy
For every dispatched job \(j\):

\[
I{j,t} = 1,\quad T{k(j),t} = 1
\]

If \(P_t = 0\):

\[
w_j \ge \bar{w}
\]

This enforces:

\[
P \le T \le I
\]

---

6.2 Quota Safety
\[
u{k,t} \le Qk \quad \forall k,t
\]

No tribe may exceed its planetary‑approved budget.

---

6.3 Planetary Tube
\[
\|e^Pt\|2 \le \delta_P
\]

If violated, emergency mode must drive the system back inside.

---

6.4 Monotone Planet Gate
\[
\|e^Pt\|2 \uparrow \quad \Rightarrow \quad g_t \downarrow
\]

Planet stress always reduces throughput.

---

7. Sovereign Interpretation

The Planet‑Gated Scheduler is the narrow throat through which all computation must pass.

It ensures:

- Individuals cannot violate tribe integrity  
- Tribes cannot violate planetary limits  
- Planetary stress automatically collapses throughput  
- Forbidden configurations are dynamically repelled  
- The system converges toward a Sovereign Equilibrium  

This is the collimator that keeps One‑Planet‑Win from becoming One‑Planet‑Burn.

---

