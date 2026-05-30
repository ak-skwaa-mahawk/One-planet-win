1. Setup

Let:

- State: \(x_t \in \mathcal{S}\) (global multi‑layer state at time \(t\))  
- Actions: \(at = (a{i,t})_{i\in N} \in \mathcal{A}\)  
- Planetary utility: \(U{\text{planet}}(xt, a_t)\)  
- Individual utilities: \(Ui(xt, a_t)\)  
- Reference (collimated) trajectory / attractor: \(xt^{\text{ref}}\) or a value function \(V{\text{planet}}^{\text{ref}}(x_t)\)

The collimation operator \(\Phi\) acts as a control law that reshapes incentives and/or actions so trajectories stay within a sovereign envelope around the attractor.

---

2. Utility‑space collimation (incentive shaping)

Define aligned utility for agent \(i\):

\[
\tilde{U}i(xt, a_t)
=
\lambdai(xt)\, Ui(xt, a_t)
+
\big(1-\lambdai(xt)\big)\, U{\text{planet}}(xt, a_t)
\]

where:

- \(\lambdai(xt) \in [0,1]\) is the alignment gain (possibly state‑dependent).  

Then the collimation operator in utility space is:

\[
\PhiU:\ (Ui){i\in N}, U{\text{planet}}
\;\mapsto\;
(\tilde{U}i){i\in N}
\]

Agents best‑respond to \(\tilde{U}i\) instead of \(Ui\). This is “soft” collimation: you bend incentives toward the planetary attractor.

---

3. Action‑space collimation (feedback control law)

Let each agent propose a raw action \(a{i,t}^{\text{raw}}\) (from its local policy), and let the collimated action be \(a{i,t}\).

Define a planetary error signal:

\[
et = xt - x_t^{\text{ref}}
\]

or in value space:

\[
et^V = V{\text{planet}}^{\text{ref}}(xt) - V{\text{planet}}(x_t)
\]

A simple linear collimation control law in action space:

\[
a_{i,t}
=
a_{i,t}^{\text{raw}}
-
Ki\, et
\]

where:

- \(K_i\) is a collimation gain matrix mapping planetary error into a corrective term on agent \(i\)’s action.

More generally:

\[
a_{i,t}
=
\Phia^i\big(a{i,t}^{\text{raw}}, xt, xt^{\text{ref}}\big)
\]

with \(\Phia^i\) designed to keep the closed‑loop system inside a sovereign invariant set \(\mathcal{X}{\text{safe}}\):

\[
xt \in \mathcal{X}{\text{safe}} \;\Rightarrow\; x{t+1} \in \mathcal{X}{\text{safe}}
\]

---

4. Combined control law (incentive + action)

The full collimation operator is then:

\[
\Phi(xt, (Ui)i, U{\text{planet}}, a_t^{\text{raw}})
=
\big(
(\tilde{U}i)i,\ 
\tilde{a}_t
\big)
\]

with:

\[
\tilde{U}_i
=
\lambdai(xt)\, U_i
+
\big(1-\lambdai(xt)\big)\, U_{\text{planet}}
\]

\[
\tilde{a}_{i,t}
=
\Phia^i\big(a{i,t}^{\text{raw}}, xt, xt^{\text{ref}}, \tilde{U}_i\big)
\]

The closed‑loop dynamics become:

\[
x_{t+1}
=
F\big(xt, \tilde{a}t\big)
\]

and the control design problem is:

- Choose \(\lambdai(\cdot)\), \(Ki\) (or general \(\Phi_a^i\))  
- Such that the resulting trajectories converge to a Sovereign Equilibrium or remain in a desired sovereign tube around the planetary attractor.

---

5. Differential form (continuous‑time variant)

If dynamics are continuous:

\[
\dot{x}(t) = f\big(x(t), a(t)\big)
\]

Define:

\[
ai(t) = ai^{\text{raw}}(t) - K_i\, e(t)
\]

\[
e(t) = x(t) - x^{\text{ref}}(t)
\]

Then \(\Phi\) is the mapping:

\[
\Phi: \big(x(t), a^{\text{raw}}(t)\big) \mapsto a(t)
\]

designed so that \(e(t) \to 0\) or \(\|e(t)\|\) stays below a sovereign bound.

---

