# Review: Tennis racket theorem, Poinsot/SO(3) geometry and the "polarized shift" reframing (share #102)

- **Archive:** [grok_archive/2026-10-22_tennis_racket_theorem_rigid_body_stability.md](grok_archive/2026-10-22_tennis_racket_theorem_rigid_body_stability.md) (share `fbb18e8e`, 8 messages: 4 Channing, 4 Grok).
- **Checks:** [sims/tennis_racket_euler_check.py](../sims/tennis_racket_euler_check.py) ([output](../sims/tennis_racket_euler_check_output.txt)).
- **Related:** [electrostatic_nodal_spin_dynamics_review.md](electrostatic_nodal_spin_dynamics_review.md) (share #99, nodal spin; friction-coupled L conserved), [sumerian_noether_arnold_ratchet_review.md](sumerian_noether_arnold_ratchet_review.md) (Noether / angular momentum, Arnold geodesic view), [magnus_floquet_inertial_copv_review.md](magnus_floquet_inertial_copv_review.md) (share #89, inertial vectors), [shifting_phase_order_review.md](shifting_phase_order_review.md) (cascade sequence).
- **Labels:** Grounded = established in peer-reviewed/textbook literature or rerun here; Plausible-untested; Speculative; Symbolic (φ and similar, unless tested). "Grok-reported" = a number Grok gave that was not rerun here.

## 1. The theorem (msg 2)

| Claim | Label | Note |
|---|---|---|
| I1 < I2 < I3: spin about I1 and I3 stable, about I2 unstable | **Grounded** (rerun) | Landau & Lifshitz, *Mechanics* §37; Goldstein ch. 5. Sim: spins on I1 / I3 with 2 % perturbations stay within 0.04 / 0.03 of the axis. |
| Euler equations I1ω̇1 = (I2−I3)ω2ω3 and cyclic | **Grounded** | Signs as written are correct. |
| Intermediate-axis linearization: real eigenvalues ±λ; others imaginary | **Grounded** | λ = Ω·sqrt((I2−I1)(I3−I2)/(I1I3)), Ω = spin rate about axis 2. |
| Flips repeat periodically under ideal conditions | **Grounded** | Period is set by elliptic functions and diverges logarithmically as the perturbation → 0. |
| Dzhanibekov effect (wing nut, Salyut 7, 1985) | **Grounded** | Also Ashbaugh, Chicone & Cushman, J. Dyn. Diff. Eq. 3, 67 (1991); Van Damme et al. (2017) on the racket. |
| "Flip 180° and continue spinning the other way" | **Clarified** | In the body frame ω2 reverses; in space L is fixed, so it is the *body* that turns over (handle-face rotates by ~180° about another axis) while the spin about L keeps its sense. |

## 2. Mapping onto suit and Multi-Egg (msg 4, step 3)

| Claim | Label | Note |
|---|---|---|
| Lamina: perpendicular-axis theorem I3 = I1 + I2, so face-normal is largest, long axis smallest | **Grounded** | Exact for an ideal lamina; "≈" for a thick body. Note the theorem then gives I3 − I2 = I1. |
| Growth rate formula λ = ω2·sqrt((I2−I1)(I3−I2)/(I1I3)) | **Grounded** (rerun) | Closed form for I = (1,2,3): 0.5774·Ω; fitted early growth 0.564·Ω (fit window slightly nonlinear). Grok's ω2 must be read as the nominal spin rate, not a small component. |
| Moving mass along the long (focus-to-focus) axis changes I2 more than I1 | **Grounded** | A point mass on axis 1 adds m·d² to I2 and I3, ~nothing to I1. |
| Seed ω on I2, wait half a period → passive 180° inversion | **Plausible-untested** | Physics is right; no suit inertia tensor exists yet [Channing to supply mass budget]. Human body tumbling is a real analog (Dzhanibekov-type flips in diving / astronaut demos). |
| Near-spherical Multi-Egg: no violent flip, no preferred stable axis | **Grounded** | With two equal moments the body is symmetric (no unstable axis); fully spherical is neutral. |
| φ-ratio inertia (I2/I1 = φ) | **Symbolic** | Grok itself says bookkeeping only; agrees. |
| Mycelium/hemp/ferrofluid/quartz-helium suit materials | **Speculative** design context | Outside the theorem. |

## 3. Poinsot and SO(3) (msg 4, step 4)

| Claim | Label | Note |
|---|---|---|
| E and L² conserved; polhode = intersection of energy ellipsoid and L-sphere | **Grounded** | Correct formulas. |
| Inertia ellipsoid rolls without slipping on invariable plane; polhode/herpolhode | **Grounded** | Poinsot (1834). Precisely, the Poinsot ellipsoid is scaled to Σ Iᵢxᵢ² = 2E [minor]. |
| Figure-eight separatrix through the intermediate axis | **Grounded** | |
| Free rigid body = geodesic flow of left-invariant metric on SO(3) | **Grounded** | Arnold (1966), *Mathematical Methods*, App. 2. |
| Flip as heteroclinic transit between ±ω2 equilibria | **Grounded** | Heteroclinic in ω-space (connects two distinct equilibria). |
| "I = (1,2,3), 2 % perturbation, E and L² to ~1e-8, first ω2 = 0 at t ≈ 12.3" | **Corrected / Grok-reported** | No code shown. Rerun (rtol 1e-11) gives first crossing at **t ≈ 8.2–9.7** (Ω = 1) depending on where the 2 % goes, drift ~1e-14. 12.3 is not reproduced [to verify Grok's setup]. |

## 4. Polarized shift, cascade and fork (msg 6)

| Claim | Label | Note |
|---|---|---|
| ω2 sign change as a "polarity inversion" | **Symbolic** | Valid relabeling of a real event. |
| Flip retriggers magnetic shell → ferrofluid → thermal/acoustic → Tesla-valve impedance | **Speculative** | No coupling coefficients or model. Any coupling adds torque/dissipation (Grok notes this). |
| "Separatrix guarantees the geometric stage completes once past the saddle" | **Corrected** | Only in the torque-free ideal. With dissipation, a quasi-rigid body migrates to the max-axis spin (Explorer 1, 1958), so the flip can stop entirely; the cascade loses its "guarantee". |
| Opposite-cell fork keeps net L constant while raising internal shear | **Grounded** in principle | Internal exchanges conserve total L (cf. share #99 friction-coupled L). Magnitude [Channing to supply geometry]. |
| Parallel fork "reinforces net angular-momentum change" | **Corrected** | Internal rearrangement cannot change total L of an isolated system; it can only redistribute it between attitude and internal rotors. |

## 5. Other notes
- Grok dated the save "26 August 2026"; the archive date here is 2026-10-22 [to verify which is right].
- The flip time with 2 % seeds is ≈ (1/λ)·ln(1/ε) scale; for Ω = 1 rad/s and I = (1,2,3), ~8–10 s.

## Open questions for Channing
1. Suit/Multi-Egg mass budget to dimension a real inertia tensor and flip period.
2. Which coupling (magnetic shell or ferrofluid) should be tried first as a torque term in the integrator?
