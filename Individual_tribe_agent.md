1. Layer setup: individual and tribe

We’ll carve out just two layers from the full stack:

- Individual layer: agents \(i \in \mathcal{I}\)  
- Tribe layer: tribes \(k \in \mathcal{K}\), each tribe is a coalition of individuals

State factorization:

\[
xt = \big(x^{\text{tribe}}t,\ x^{\text{ind}}_t\big)
\]

- Tribe state:  
  \[
  x^{\text{tribe}}t = (x{k,t})_{k\in\mathcal{K}}
  \]
- Individual state:  
  \[
  x^{\text{ind}}t = (x{i,t})_{i\in\mathcal{I}}
  \]

Actions:

\[
at = \big(a^{\text{tribe}}t,\ a^{\text{ind}}_t\big)
\]

- Tribe actions: \(a^{\text{tribe}}t = (a{k,t})_{k\in\mathcal{K}}\)  
- Individual actions: \(a^{\text{ind}}t = (a{i,t})_{i\in\mathcal{I}}\)

---

2. Utilities at individual and tribe level

Let:

- Planetary utility: \(U{\text{planet}}(xt, a_t)\)  
- Tribe utility: \(Uk(xt, a_t)\) for tribe \(k\)  
- Individual utility: \(Ui(xt, a_t)\) for individual \(i\)

You can also define tribe‑aggregated individual utility:

\[
Uk^{\text{ind}}(xt, a_t)
=
\sum{i \in \mathcal{I}k} wi\, Ui(xt, at)
\]

where \(\mathcal{I}k\) is the set of individuals in tribe \(k\), and \(wi\) are weights.

---

3. Collimation in utility space

3.1 Individual‑level aligned utility

For individual \(i\) in tribe \(k\):

\[
\tilde{U}_i
=
\lambdai(xt)\, U_i
+
\mui(xt)\, U_k
+
\big(1-\lambdai(xt)-\mui(xt)\big)\, U_{\text{planet}}
\]

with:

\[
\lambdai(xt), \mui(xt) \ge 0,\quad
\lambdai(xt) + \mui(xt) \le 1
\]

Interpretation:

- \(\lambda_i\): self‑alignment weight  
- \(\mu_i\): tribal alignment weight  
- Residual: planetary alignment weight

3.2 Tribe‑level aligned utility

For tribe \(k\):

\[
\tilde{U}_k
=
\alphak(xt)\, U_k
+
\big(1-\alphak(xt)\big)\, U_{\text{planet}}
\]

with \(\alphak(xt) \in [0,1]\).

---

4. Collimation in action space

Let:

- Raw individual action: \(a_{i,t}^{\text{raw}}\) (from local policy)  
- Raw tribe action: \(a_{k,t}^{\text{raw}}\) (from tribal policy)

Define reference states:

- Tribe reference: \(x_{k,t}^{\text{ref}}\)  
- Planet reference: \(x_t^{\text{ref}}\)

4.1 Error signals

- Tribe error for tribe \(k\):
  \[
  e{k,t} = x{k,t} - x_{k,t}^{\text{ref}}
  \]
- Planetary error:
  \[
  et = xt - x_t^{\text{ref}}
  \]

You can also define value‑space errors:

\[
e{k,t}^U = Uk^{\text{ref}}(xt) - Uk(xt, at)
\]
\[
et^U = U{\text{planet}}^{\text{ref}}(xt) - U{\text{planet}}(xt, at)
\]

---

5. Individual collimation control law

Define the collimated individual action:

\[
a_{i,t}
=
a_{i,t}^{\text{raw}}
-
Ki^{\text{tribe}}\, e{k(i),t}
-
Ki^{\text{planet}}\, et
\]

where:

- \(k(i)\) is the tribe of individual \(i\)  
- \(K_i^{\text{tribe}}\) maps tribe‑level error into individual action correction  
- \(K_i^{\text{planet}}\) maps planetary error into individual action correction

Compactly:

\[
a_{i,t}
=
\Phia^{\text{ind},i}\big(a{i,t}^{\text{raw}}, xt, x^{\text{ref}}t\big)
\]

with:

\[
\Phi_a^{\text{ind},i}(\cdot)
=
a_{i,t}^{\text{raw}}
-
Ki^{\text{tribe}}\, (x{k(i),t} - x_{k(i),t}^{\text{ref}})
-
Ki^{\text{planet}}\, (xt - x_t^{\text{ref}})
\]

---

6. Tribe collimation control law

Define the collimated tribe action:

\[
a_{k,t}
=
a_{k,t}^{\text{raw}}
-
Lk^{\text{planet}}\, et
\]

where \(L_k^{\text{planet}}\) is the tribe‑level gain.

Compactly:

\[
a_{k,t}
=
\Phia^{\text{tribe},k}\big(a{k,t}^{\text{raw}}, xt, xt^{\text{ref}}\big)
\]

---

7. Closed‑loop dynamics and sovereign tube

Let the environment dynamics be:

\[
x{t+1} = F\big(xt,\ a^{\text{tribe}}t,\ a^{\text{ind}}t\big)
\]

with:

\[
a^{\text{tribe}}t = (a{k,t})_{k\in\mathcal{K}},\quad
a^{\text{ind}}t = (a{i,t})_{i\in\mathcal{I}}
\]

After collimation:

\[
x_{t+1}
=
F\Big(
x_t,\ 
\Phia^{\text{tribe}}(a^{\text{tribe,raw}}t, xt, xt^{\text{ref}}),\ 
\Phia^{\text{ind}}(a^{\text{ind,raw}}t, xt, xt^{\text{ref}})
\Big)
\]

You then design \(Ki^{\text{tribe}}, Ki^{\text{planet}}, Lk^{\text{planet}}\) and the alignment weights \(\lambdai, \mui, \alphak\) so that:

- The error \(e_t\) stays inside a sovereign tube:
  \[
  \|et\| \le \epsilon{\text{planet}}
  \]
- Tribe errors \(e_{k,t}\) stay inside tribe‑level tubes:
  \[
  \|e{k,t}\| \le \epsilonk
  \]
- The resulting steady state satisfies the Sovereign Equilibrium conditions for individuals and tribes.

---

If you want to go one notch deeper, we can:

- pick a concrete state representation (e.g., \(x{k,t} =\) resource, cohesion, risk; \(x{i,t} =\) health, agency, load)  
- choose linear dynamics \(x{t+1} = A xt + B a_t\)  
- and actually solve for gains \(Ki^{\text{tribe}}, Ki^{\text{planet}}, L_k^{\text{planet}}\) via an LQR‑style design that encodes “planet‑first, tribe‑second, individual‑third” in the cost.