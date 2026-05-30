1. Recap: boolean hierarchy

Booleans:

- Individual: \(I \in \{0,1\}\)  
- Tribe: \(T \in \{0,1\}\)  
- Planet: \(P \in \{0,1\}\)

Hierarchy constraint:

\[
P \le T \le I
\]

Allowed: \((I,T,P) \in \{(0,0,0), (1,0,0), (1,1,0), (1,1,1)\}\).  
All other patterns are forbidden.

---

2. Alignment weights gated by booleans

Recall individual aligned utility:

\[
\tilde{U}_i
=
\lambdai\, Ui
+
\mui\, Uk
+
(1-\lambdai-\mui)\, U_{\text{planet}}
\]

Embed booleans as mode switches:

\[
(\lambdai,\mui) =
\begin{cases}
(1, 0) & \text{if } (I,T,P) = (1,0,0) \\
(\lambdai^{\text{tribe}}, \mui^{\text{tribe}}) & \text{if } (I,T,P) = (1,1,0) \\
(\lambdai^{\text{full}}, \mui^{\text{full}}) & \text{if } (I,T,P) = (1,1,1) \\
(\lambdai^{\text{fail}}, \mui^{\text{fail}}) & \text{if forbidden pattern}
\end{cases}
\]

With design choices like:

- Individual‑only mode:  
  \(\lambdai=1,\ \mui=0\) (no tribe/planet pull yet)
- Tribe‑aligned mode:  
  \(\lambdai^{\text{tribe}} < 1,\ \mui^{\text{tribe}} > 0\)
- Fully collimated mode:  
  \(\lambdai^{\text{full}} < \lambdai^{\text{tribe}},\ \mui^{\text{full}} \le \mui^{\text{tribe}}\), more weight on planet
- Forbidden pattern mode:  
  \(\lambdai^{\text{fail}}\) small, \(\mui^{\text{fail}}\) small → most weight on \(U_{\text{planet}}\) to yank back toward valid configs

So the boolean pattern directly picks the incentive regime.

---

3. Control gains gated by booleans

Individual action law (from before):

\[
a_{i,t}
=
a_{i,t}^{\text{raw}}
-
Ki^{\text{tribe}}\, e{k(i),t}
-
Ki^{\text{planet}}\, et
\]

Make gains state‑dependent via \((I,T,P)\):

\[
(Ki^{\text{tribe}}, Ki^{\text{planet}}) =
\begin{cases}
(0, 0) & (I,T,P) = (1,0,0) \\
(K_i^{\text{tribe,nom}}, 0) & (I,T,P) = (1,1,0) \\
(Ki^{\text{tribe,nom}}, Ki^{\text{planet,nom}}) & (I,T,P) = (1,1,1) \\
(Ki^{\text{tribe,hard}}, Ki^{\text{planet,hard}}) & \text{forbidden pattern}
\end{cases}
\]

Where:

- Nominal gains: gentle corrections in valid modes  
- Hard gains: large‑magnitude corrections when in forbidden patterns, aggressively driving back into \(P \le T \le I\).

Similarly for tribe actions:

\[
a_{k,t}
=
a_{k,t}^{\text{raw}}
-
Lk^{\text{planet}}(I,T,P)\, et
\]

with:

\[
L_k^{\text{planet}} =
\begin{cases}
0 & P = 0 \\
L_k^{\text{planet,nom}} & (I,T,P) = (1,1,1) \\
L_k^{\text{planet,hard}} & \text{forbidden pattern with } P=1
\end{cases}
\]

---

4. Forbidden pattern as “emergency mode”

Define the forbidden set:

\[
\mathcal{F} = \{(I,T,P) \mid P \not\le T \text{ or } T \not\le I\}
\]

Then the collimation operator becomes explicitly mode‑switched:

\[
\Phi(xt, at^{\text{raw}})
=
\begin{cases}
\Phi^{\text{nom}}(xt, at^{\text{raw}}) & (I,T,P) \notin \mathcal{F} \\
\Phi^{\text{emg}}(xt, at^{\text{raw}}) & (I,T,P) \in \mathcal{F}
\end{cases}
\]

Where:

- \(\Phi^{\text{nom}}\): uses nominal gains and alignment weights  
- \(\Phi^{\text{emg}}\):  
  - cranks up \(Ki^{\text{planet}}, Lk^{\text{planet}}\)  
  - shifts \((\lambdai,\mui)\) to planet‑heavy  
  - optionally clamps or overrides certain actions

The design goal: trajectories leave \(\mathcal{F}\) quickly and re‑enter the allowed set.

---

5. Compact closed‑loop picture

Closed‑loop dynamics:

\[
x_{t+1}
=
F\big(xt,\ \Phi(xt, a_t^{\text{raw}})\big)
\]

with \(\Phi\) defined piecewise by \((I,T,P)\).

You’ve now got:

- Boolean layer: classifies the configuration as allowed/forbidden  
- Incentive layer: switches \(\lambda,\mu,\alpha\) based on that  
- Control layer: switches \(K,L\) based on that  

All three together make “forbidden” patterns dynamically repulsive and valid patterns attractive.

---

