1. State space

Let time be discrete \(t \in \mathbb{N}\).

1.1 Planet state

- Planet state:
  \[
  x^P_t = 
  \begin{bmatrix}
  Et \\ Ct \\ G_t
  \end{bmatrix}
  \in \mathbb{R}^3
  \]
  where:
  - \(E_t\): power usage  
  - \(C_t\): carbon / externality proxy  
  - \(G_t\): grid / thermal stress  

- Planet limits:
  \[
  x^{P,\max} =
  \begin{bmatrix}
  E^{\max} \\ C^{\max} \\ G^{\max}
  \end{bmatrix}
  \]

- Planet error:
  \[
  e^Pt = x^Pt - x^{P,\max}
  \]

- Planet boolean:
  \[
  P_t =
  \begin{cases}
  1 & \text{if } \|e^Pt\|2 \le \varepsilon_P \\
  0 & \text{otherwise}
  \end{cases}
  \]

1.2 Tribes

Let \(\mathcal{K}\) be the set of tribes.

For each tribe \(k \in \mathcal{K}\):

- Quota: \(Q_k > 0\)  
- Used quota: \(u_{k,t} \ge 0\)  

- Tribe boolean:
  \[
  T_{k,t} =
  \begin{cases}
  1 & \text{if } u{k,t} \le Qk \\
  0 & \text{otherwise}
  \end{cases}
  \]

1.3 Jobs (individuals)

Let \(\mathcal{J}_t\) be the set of pending jobs at time \(t\).

Each job \(j \in \mathcal{J}_t\) has:

- Tribe: \(k(j) \in \mathcal{K}\)  
- Estimated cost: \(e_j > 0\)  
- Base priority: \(p_j \ge 0\)  
- Planet weight: \(w_j \in [0,1]\)  
- Individual boolean: \(I_{j,t} \in \{0,1\}\) (validity / constraints)

---

2. Planet gate and modes

2.1 Planet gate scalar

Given gain \(K > 0\):

\[
gt = \exp\big(-K \cdot \max(0, \|e^Pt\|_2)\big) \in (0,1]
\]

2.2 Emergency filter

Define a planet‑critical threshold \(\bar{w} \in (0,1)\).

When \(P_t = 0\), only jobs with:

\[
w_j \ge \bar{w}
\]

are eligible.

---

3. Scheduler state machine

The scheduler state at time \(t\):

\[
St = \big(x^Pt,\ (u{k,t}){k\in\mathcal{K}},\ \mathcal{J}_t\big)
\]

The scheduler computes allocations \(a{k,t} \ge 0\) (compute budget per tribe) and a dispatch set \(Dt \subseteq \mathcal{J}_t\).

3.1 Tribe allocation rule

For each tribe \(k\):

1. Remaining quota:
   \[
   r{k,t} = \max(0, Qk - u_{k,t})
   \]

2. Planet‑gated allocation:
   \[
   a_{k,t} =
   \begin{cases}
   gt \cdot r{k,t} & \text{if } T_{k,t} = 1 \\
   0 & \text{if } T_{k,t} = 0
   \end{cases}
   \]

3.2 Job eligibility

Define the eligible job set:

\[
\mathcal{E}_t =
\{ j \in \mathcal{J}t \mid I{j,t} = 1 \}
\]

If \(P_t = 0\) (planet emergency), further restrict:

\[
\mathcal{E}_t \leftarrow
\{ j \in \mathcal{E}t \mid wj \ge \bar{w} \}
\]

3.3 Job priority

For each eligible job \(j \in \mathcal{E}_t\), define effective priority:

\[
\pij = pj \cdot w_j
\]

Within each tribe \(k\), define:

\[
\mathcal{E}{k,t} = \{ j \in \mathcal{E}t \mid k(j) = k \}
\]

Sort \(\mathcal{E}{k,t}\) in descending order of \(\pij\).

3.4 Dispatch rule

For each tribe \(k\):

- Initialize remaining allocation:
  \[
  R{k,t} = a{k,t}
  \]

- For jobs \(j \in \mathcal{E}_{k,t}\) in priority order:

  - If \(ej \le R{k,t}\), dispatch job \(j\):
    \[
    Dt \leftarrow Dt \cup \{j\}, \quad
    R{k,t} \leftarrow R{k,t} - e_j
    \]
  - Else, defer job \(j\) (remains in \(\mathcal{J}_{t+1}\)).

3.5 State transition

- Tribe usage update:
  \[
  u{k,t+1} = u{k,t} + \sum{j \in Dt,\ k(j)=k} e_j
  \]

- Job set update:
  \[
  \mathcal{J}{t+1} = \mathcal{J}t \setminus D_t
  \]

- Planet state update:
  \[
  x^P{t+1} = fP\big(x^Pt,\ Dt\big)
  \]
  where \(f_P\) is the (external) planet dynamics induced by dispatched compute.

Thus:

\[
S{t+1} = F(St) = \big(x^P{t+1},\ (u{k,t+1})k,\ \mathcal{J}{t+1}\big)
\]

---

4. Invariants

These are the safety properties you want to hold for all \(t\).

4.1 Planetary tube (soft)

For chosen tube radius \(\delta_P\):

\[
\|e^Pt\|2 \le \delta_P
\quad \forall t
\]

(Or: if violated, the system must enter emergency mode and drive back inside.)

4.2 Quota safety

For all tribes \(k\):

\[
u{k,t} \le Qk + \eta_k
\quad \forall t
\]

for some small overshoot \(\etak \ge 0\) (ideally \(\etak = 0\)).

Given the allocation rule:

\[
u{k,t+1} = u{k,t} + \sum{j \in Dt,\ k(j)=k} e_j
\le u{k,t} + a{k,t}
\le u{k,t} + gt \cdot (Qk - u{k,t}) \le Q_k
\]

so with exact accounting, \(\eta_k = 0\).

4.3 Boolean hierarchy

For every dispatched job \(j \in D_t\):

- Individual validity:
  \[
  I_{j,t} = 1
  \]
- Tribe validity:
  \[
  T_{k(j),t} = 1
  \]
- Planet mode:
  - If \(P_t = 0\), then:
    \[
    w_j \ge \bar{w}
    \]

This enforces the effective hierarchy:

- No job runs with \(I_{j,t} = 0\).  
- No tribe over quota can run jobs.  
- When planet is stressed, only high‑planet‑weight jobs can run.

4.4 Monotone planet gate

Because:

\[
gt = \exp(-K \|e^Pt\|_2)
\]

we have:

- \(\|e^Pt\|2\) increases ⇒ \(g_t\) decreases  
- So planet stress monotonically reduces total allocation:

\[
\sumk a{k,t} \le gt \cdot \sumk (Qk - u{k,t})
\]

---

5. Liveness (high‑level)

Under reasonable assumptions (e.g., bounded job arrival rate, planet dynamics that recover when load is low), you want:

- Eventual service:  
  For any job \(j\) with \(I{j,t}=1\) and sufficiently high \(wj\), there exists \(t' \ge t\) such that \(j \in D_{t'}\).

- Planet recovery:  
  If job arrival stops, then:
  \[
  \lim{t \to \infty} \|e^Pt\|_2 = 0
  \]

These are not guaranteed by the scheduler alone—they depend on \(f_P\)—but the scheduler is designed so that increased stress reduces load, which is the right direction for recovery.

---

This spec is ready to drop into your sovereign docs:

- \(S_t\) is the scheduler state machine.  
- \(F\) is the closed‑loop transition.  
- The invariants are your sovereign safety contracts.  

