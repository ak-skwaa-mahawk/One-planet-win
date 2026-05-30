Definition

Let \(\mathcal{G} = \langle N, (Ai){i\in N}, U{\text{planet}}, (Ui)_{i\in N} \rangle\) be a game with:

- Agents: \(N = \{1,\dots,n\}\)  
- Action sets: \(Ai\) for each agent, \(A = \prod{i} A_i\)  
- Planetary utility: \(U_{\text{planet}} : A \to \mathbb{R}\)  
- Individual utilities: \(U_i : A \to \mathbb{R}\)

A Sovereign Equilibrium (SE) is a joint action \(a^* \in A\) such that for every agent \(i\in N\) and every unilateral deviation \(ai' \in Ai\):

\[
\begin{aligned}
&\text{(1) Individual non‑profitable deviation:} \\
&\quad Ui(a^) \;\ge\; Ui(ai', a{-i}^) \\
[4pt]
&\text{(2) Planetary non‑profitable deviation:} \\
&\quad U{\text{planet}}(a^) \;\ge\; U{\text{planet}}(ai', a{-i}^)
\end{aligned}
\]

So no agent can deviate in a way that improves their own payoff and simultaneously does not harm (or improves) the planet—because any such deviation would violate at least one inequality.

---

Strong and weak versions

- Strong Sovereign Equilibrium (SSE):  
  For all \(i\) and all \(a_i'\):

  \[
  \big(Ui(ai', a{-i}^) > Ui(a^)\big) \;\Rightarrow\; \big(U{\text{planet}}(ai', a{-i}^) < U{\text{planet}}(a^)\big)
  \]

  Any strictly better move for an agent strictly harms the planet.

- Weak Sovereign Equilibrium (WSE):  
  The two inequalities hold as written above; beneficial deviations for the agent are allowed only if they strictly improve the planet too:

  \[
  \big(Ui(ai', a{-i}^) > Ui(a^)\big) \;\Rightarrow\; \big(U{\text{planet}}(ai', a{-i}^) > U{\text{planet}}(a^)\big)
  \]

---

Dynamic version (trajectory form)

Let \(xt\) be the system state and \(\pii\) the policy of agent \(i\). A policy profile \(\pi^ = (\pii^){i\in N}\) is a Sovereign Equilibrium policy profile if for all \(i\) and all alternative policies \(\pi_i'\):

\[
\begin{aligned}
&Ui(\pi^) \;\ge\; Ui(\pii', \pi{-i}^) \\
&U{\text{planet}}(\pi^) \;\ge\; U{\text{planet}}(\pii', \pi{-i}^)
\end{aligned}
\]

where utilities are evaluated over the induced trajectory \((xt){t\ge 0}\) (e.g., discounted sum or long‑run average).

---

