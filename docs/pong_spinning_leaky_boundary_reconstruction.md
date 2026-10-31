# Reconstruction: the H722 "pong" thread (spinning, exchanging, leaky boundary) + quantum tunnelling, superposition and exchange

- **Type:** reconstruction (2026-10-31). This is not a Grok share and has no share number. The original pong chat share was **blank / unrecoverable**.
- **Sim:** [../sims/pong_mirror_barrier_spin_sim.py](../sims/pong_mirror_barrier_spin_sim.py) → [output](../sims/pong_mirror_barrier_spin_sim_output.txt) (numpy only, deterministic, ~20 s).
- **Further continuation:** share #165 `4b786de0` extends this chat to 28 messages (spin, leaky boundary, neutrinos, monopoles, LISA): [transcript](grok_archive/2026-10-31_springer_spin_leaky_boundary_neutrino_monopole_lisa.md), [review](spin_leaky_boundary_neutrino_monopole_lisa_review.md).
- **Labels:** **Grounded** · **Plausible-untested** · **Speculative** · **Symbolic** · **Unsupported**; [to verify]; [Channing to supply/confirm]. φ is Symbolic throughout.
- **Cross-thread rows:** H778–H786.

## 1. Origin (rebuilt from memory, [Channing to confirm])

Channing, 2026-10-31, verbatim:

> That is where the pong idea was generated from although we were not this far along because I hadn’t termed electrostatic tensor as electron-positron pairs. But same principle a spinning boundary that exchanges. Where it turned into the pong concept was a boundary layer introduced that I described as leaky. Then, we moved to the transition to stress tensors which we should still have, right?

> It was blank but that’s ok we can re construct. The centrifugal force, escape velocity, and radiation were next, let’s explore.

**Reconstructed sequence:**
1. The electrostatic isotropic tensor idea.
2. A spinning boundary that exchanges.
3. A **leaky boundary layer**, which became the "pong" concept (chat lost).
4. The stress-tensor conversion. Yes, we still have it: share #90 `18a292a6`, #91 `753ca89b` (the fuller re-share) and #92 `2b696995`, all in [electrostatic_isotropic_stress_review.md](electrostatic_isotropic_stress_review.md).
5. Share #99 `c0b832a5`: [electrostatic_nodal_spin_dynamics_review.md](electrostatic_nodal_spin_dynamics_review.md).
6. Later, the electron-positron pair sea: #163 [springer_holographic_phase_transitions_pair_plasma_review.md](springer_holographic_phase_transitions_pair_plasma_review.md) (H772), and the ZPE / Euler–Heisenberg material in #164 [zpe_backreaction_euler_heisenberg_review.md](zpe_backreaction_euler_heisenberg_review.md) (H775, H776).

**Related records:**
- The pong chat is referenced in #149 msg 23 ([pais_gem_fractal_follicle_silk_review.md](pais_gem_fractal_follicle_silk_review.md) §4, H722).
- The bounce-spectrum neighbour is #154 (H737).
- Classical leakage vs tunnelling: [leaky_boundary_tunneling_review.md](leaky_boundary_tunneling_review.md), with [leaky_bound_state_family.md](leaky_bound_state_family.md) and [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md).

**Reading:** "pong" is most plausibly the *bounce* of particles between two reflecting ends of a leaky trap, with a small leak at each bounce. That reading is **Plausible-untested** as an interpretation of the lost chat [Channing to confirm].

## 2. Spin, escape and radiation

### 2.1 Centrifugal (corotation)
- Corotation radius r_c = (GM/Ω²)^(1/3). Beyond r_c, centrifugal force exceeds gravity for matter forced to corotate. **Grounded.**
- A magnetized body enforces corotation out to where the field can no longer hold the plasma. Past that, centrifugal mass loss and interchange occur (Io plasma torus at Jupiter; pulsar magnetospheres closing at the light cylinder R_L = c/Ω). **Grounded.**
- Note on t623u: "centrifugal force" is a rotating-frame (fictitious) force. The conserved quantity in that frame is the Jacobi constant, not the energy, and the sim uses it.

### 2.2 Escape
- For gravity, v_esc = √(2GM/r). **Grounded.**
- For charged particles, the barrier is the electric potential plus the magnetic mirror (μ = mv⊥²/2B conserved, mirror force −μ∇B). Particles bounce between mirror points. **Grounded.**
- The loss cone is sin²α_lc = B_min/B_max. Escape happens by pitch-angle scattering into the cone, or by energization over the potential. **Grounded** (radiation belts, Earth's magnetosphere, mirror machines).
- "Bounce = pong" is **Plausible-untested** (see §1).
- Note on t623u: for a charged particle, the relevant "escape velocity" is set by the mirror ratio and the electric potential, not by √(2GM/r).

### 2.3 Radiation
- Larmor power P = q²a²/(6πε₀c³), with synchrotron and curvature radiation as its relativistic forms. **Grounded.**
- Spin-down ledger: rotational energy flows into particles plus radiation (Crab: Ė ≈ 4–5×10³¹ W [to verify]). **Grounded.**
- Pulsar pair cascades: curvature photon γ + B → e⁺e⁻, then more photons, and so on, at B ≳ 10⁸ T near the Schwinger scale B_c ≈ 4.4×10⁹ T. This is where the #163 "pair sea" is real and where Euler–Heisenberg (photon splitting, birefringence) matters. **Grounded.**
- Applying any of this to a POL craft perimeter loop is **Speculative**: lab-scale fields are ~10⁻⁹–10⁻⁸ B_c.

### 2.4 Euler–Heisenberg E vs B (the #164 sign difference, rebuilt)
In natural Heaviside–Lorentz units, with a = 2α²/45m⁴ and L = (E²−B²)/2 + a[(E²−B²)² + 7(E·B)²]:
- **Pure B:** u_B = −L = B²/2 − aB⁴.
- **Pure E:** u_E = E·D − L, with D = ∂L/∂E = E(1+4aE²), giving u_E = E²/2 + 3aE⁴.
- **Relative shift:** 2aB² = (α/45π)(B/B_c)², with B_c = m²/e.

**Status:**
- The Lagrangian coefficients match the standard weak-field expansion: G. V. Dunne, "Heisenberg–Euler effective Lagrangians: basics and extensions", hep-th/0406216 (2004) [equation number to verify].
- I derived u_B, u_E and the pressures (δp∥ = +aB⁴, δp⊥ = −3aB⁴) by Legendre transform here and in [#164](zpe_backreaction_euler_heisenberg_review.md). I did not check them against a printed table. **Status: derived, consistent with Dunne's L_EH; printed-source check [to verify].** H773 stays open.
- The physical point is that a strong B *lowers* the vacuum energy slightly and a strong E *raises* it, because E²−B² flips sign. The cause is not F → −F.

## 3. Quantum tunnelling, superposition and exchange

### 3.1 Tunnelling (**Grounded**)
- WKB transmission T ≈ exp(−2∫κ dx), with κ = √(2m(V−E))/ħ.
- Examples:
  - Gamow alpha decay (Gamow; Gurney & Condon, 1928).
  - Field emission (Fowler–Nordheim, 1928).
  - Scanning tunnelling microscopes.
  - Schwinger pair production as vacuum tunnelling, rate ∝ exp(−πE_c/E), E_c ≈ 1.3×10¹⁸ V/m.
- Ledger: R + T = 1. The particle's energy is unchanged; tunnelling moves probability and creates no energy.
- **Heliopause / boundary leakage is not tunnelling.** Solar-wind proton de Broglie wavelengths are ~10⁻¹² m, against barrier scales of ~10⁹ m or more, so the exponent is astronomically large. The leakage that does happen is classical: charge exchange, reconnection, pitch-angle scattering. See [leaky_boundary_tunneling_review.md](leaky_boundary_tunneling_review.md).

### 3.2 Superposition
- Linear superposition of classical fields: **Grounded.**
- Quantum superposition and double-well tunnelling splitting: a state started in one well oscillates to the other at f = ΔE/h. Examples: the ammonia inversion line (~23.9 GHz) behind the first maser (Townes, Gordon and Zeiger, 1954); Josephson junctions and superconducting qubits; Rabi oscillation. This is a **genuine quantum "pong"**. **Grounded** (sim Part B).
- Decoherence (Zurek; Joos and Zeh) destroys such coherence fast for warm, large objects. Interference has been shown for molecules of ~2×10⁴ u (Arndt group, 2019 [to verify]).
- A macroscopic craft in superposition or tunnelling: **Unsupported.**

### 3.3 Exchange
| Sense | Label |
|---|---|
| (a) Exchange interaction: Pauli exclusion plus Coulomb gives Heisenberg exchange J S·S, behind ferromagnetism and covalent bonding (Heisenberg, Dirac, 1926) | **Grounded** |
| (b) Virtual-particle exchange as the QFT description of forces (photon exchange behind the Coulomb force) | **Grounded** as perturbative language; don't over-literalize "virtual particles" as objects |
| (c) Charge exchange at the heliopause (solar-wind ions + interstellar neutrals → energetic neutral atoms, seen by IBEX) | **Grounded** |
| (d) Exchange across a leaky boundary as a design principle for a spinning craft boundary | **Plausible-untested** as engineering; the link to (a)/(b) is **Symbolic** |

**No free energy.** Tunnelling, superposition and the ZPE/EH vacuum terms all conserve energy. Every ledger here balances, and nothing supports over-unity.

## 4. Sim results (rerun 2026-10-31)

Units m = q = v = 1, B0 = L = 1, mirror ratio R_m = 5.

| Case | Result | Ledger residual |
|---|---|---|
| Bounce period, α = 60°, mirror only | 7.2552 (analytic 7.2552) | \|ΔJ\| ≤ 9×10⁻⁸ |
| Bounce period, rotation Ω = 0.3 | 7.7340 (analytic 7.7341; the centrifugal term softens the mirror) | ≤ 8×10⁻⁸ |
| Isotropic escape fraction, mirror only | 0.106 (analytic 1 − cos α_lc = 0.106; α_lc = 26.6°) | ≤ 1.2×10⁻⁷ |
| + electrostatic barrier Φ0 = 0.3 | 0.047 | ≤ 3.5×10⁻⁶ |
| + rotation Ω = 0.3 | 0.149 (centrifugal widens the loss cone) | ≤ 1.0×10⁻⁷ |
| Barrier + rotation | 0.084 | ≤ 6.1×10⁻⁶ |
| Double well, λ = 1, a = 1.5 (ħ = m = 1) | ΔE = 4.18×10⁻²; tunnelling period 150.2; P(left) 0.998 → 0.002 → 0.998 | \|norm−1\| ≤ 1.2×10⁻¹⁵; \|Δ⟨H⟩\| ≤ 1.9×10⁻¹² |

The rotation energy belongs to the imposed frame. The Jacobi constant is conserved and there are no source terms. **No over-unity.**

## 5. Open items
- Confirm the sequence and the "bounce" reading of pong [Channing to confirm]. If any fragment of the lost chat (screenshots, notes) turns up, add it [Channing to supply].
- Check u_B / u_E against a printed source (H773) [to verify].
- Decide whether to extend the sim to a full 3D Boris pusher in a rotating dipole (Io-torus-like). This would be Plausible-untested modelling.

## Researchers credited
George Gamow, Ronald Gurney and Edward Condon; Ralph Fowler and Lothar Nordheim; Julian Schwinger; Werner Heisenberg and Hans Euler; Gerald Dunne; Charles Townes, James Gordon and Herbert Zeiger; Brian Josephson; Isidor Rabi; Wojciech Zurek, Erich Joos and Dieter Zeh; Markus Arndt's group; Paul Dirac; Hannes Alfvén; Peter Goldreich and William Julian (pulsar magnetospheres); Peter Sturrock (pair cascades); the IBEX team.
