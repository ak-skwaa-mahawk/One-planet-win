

I’ll keep this tight but real: a discrete‑time Lyapunov argument for the correspondence / resolver layer.

---

1. What we’re proving stable

We care about stability of the priority weights:

- \( w_T(k) \) — tribal weight at tick \(k\)  
- \( wC(k) = 1 - wT(k) \)

So the system is effectively 1‑D in terms of authority: just \( w_T \in [0,1] \).

We want:

- no oscillation  
- convergence (or at least non‑explosive behavior)  
- robustness to small changes in signals  

---

2. Define the equilibrium

Pick a target equilibrium \( wT^\* \) for a given “frozen” signal pair \((ST, S_C)\):

\[
wT^\* = \frac{ST}{ST + SC}
\]

This is exactly what the raw resolver computes before damping.

Define the error state:

\[
e(k) = wT(k) - wT^\*
\]

We want \( e(k) \to 0 \) or at least \( |e(k+1)| \le |e(k)| \).

---

3. Lyapunov candidate

Use the standard quadratic Lyapunov function:

\[
V(e) = \frac{1}{2} e^2
\]

- \( V(e) \ge 0 \) for all \(e\)  
- \( V(e) = 0 \) iff \( e = 0 \)

Now we check how \(V\) evolves under the damped update.

---

4. Damped update as a contraction

Your damped update is:

\[
wT(k+1) = wT(k) + \delta(k)
\]

with

\[
\delta(k) = \text{clip}\big(wT^\* - wT(k),\, -d,\, d\big)
\]

where \( d = \text{DAMPING} \in (0,1) \).

So:

- if \( |wT^\ - wT(k)| \le d \) → you jump exactly to \( w_T^\ \)  
- if \( |wT^\* - wT(k)| > d \) → you move by at most \(d\) toward it  

In terms of error:

\[
e(k+1) = e(k) - \delta(k)
\]

Case 1: small error \( |e(k)| \le d \)

Then \( \delta(k) = e(k) \Rightarrow e(k+1) = 0 \).

So:

\[
V(k+1) = 0 \le V(k)
\]

Case 2: large error \( |e(k)| > d \)

Then \( \delta(k) = d \cdot \text{sign}(e(k)) \), so:

\[
e(k+1) = e(k) - d \cdot \text{sign}(e(k))
\]

Thus:

\[
|e(k+1)| = |e(k)| - d
\]

So:

\[
V(k+1) = \frac{1}{2} (|e(k)| - d)^2 < \frac{1}{2} |e(k)|^2 = V(k)
\]

Therefore, in all cases:

\[
V(k+1) \le V(k)
\]

with strict decrease whenever \( e(k) \neq 0 \) and \( |e(k)| > d \).

That’s discrete‑time Lyapunov stability:  
the error energy \(V\) is monotonically non‑increasing.

---

5. Role of energy gap + forbidden transitions

- Energy gap (|ST − SC| < ε → hold previous weights)  
  - This freezes \(w_T\) when signals are nearly equal → prevents chattering.  
  - In that region, \(e(k+1) = e(k)\), so \(V\) is constant → still stable.

- Forbidden transitions (hard overrides at extreme threat/stress)  
  - These are saturated equilibria: \( w_T^\* = 0 \) or \(1\).  
  - Once in those regimes, the system is again 1‑D with the same damping logic → stable.

So globally:

- \(w_T(k)\) is bounded in [0,1]  
- \(V(k)\) is non‑increasing  
- No mechanism exists to increase error magnitude step‑to‑step  

That’s exactly what you want: Lyapunov‑stable correspondence layer.

---

