# Review: Supercooled free electrons, fast rotation, the Brillouin limit and helium vortex traps (share #98)

- **Archive:** [grok_archive/2026-10-22_exploring_supercooled_free_electrons.md](grok_archive/2026-10-22_exploring_supercooled_free_electrons.md) (share `a8338f5c`, 10 messages: 5 Channing, 5 Grok).
- **Checks:** [sims/supercooled_electrons_s98_checks.py](../sims/supercooled_electrons_s98_checks.py) ([output](../sims/supercooled_electrons_s98_checks_output.txt)).
- **Related:** [dusty_plasma_bench.md](dusty_plasma_bench.md) (strongly coupled / crystallized plasmas), [stellarator_argon_heliosphere_review.md](stellarator_argon_heliosphere_review.md) (filaments, leaky boundary), [sumerian_noether_arnold_ratchet_review.md](sumerian_noether_arnold_ratchet_review.md) (Noether, angular momentum, 2D Euler / Arnold), [shifting_phase_order_review.md](shifting_phase_order_review.md), [em_topological_gravity_review.md](em_topological_gravity_review.md) (gravity vs EM), [zeeman_muon_cavity_review.md](zeeman_muon_cavity_review.md) (Larmor / cyclotron), [heliosphere_fibonacci_review.md](heliosphere_fibonacci_review.md), [fuller_tensegrity_vortex_node_review.md](fuller_tensegrity_vortex_node_review.md), [black_hole_magnetic_nucleus_review.md](black_hole_magnetic_nucleus_review.md) (frame dragging, "surfing" analogy).
- **Labels:** Grounded = established in peer-reviewed literature or rerun here; Plausible-untested; Speculative; Symbolic (φ and similar, unless tested). "Grok-reported" = a number Grok gave that was not rerun here.

## 0. Framing in RGRF terms

- **MHD equilibrium / spin-vortex tensors.** A non-neutral electron column in a uniform axial B is a clean rigid-rotor equilibrium: radial force balance between space-charge E, the Lorentz force from E×B rotation, and centrifugal force. Its 2D (r, θ) dynamics are isomorphic to 2D inviscid Euler flow (density ↔ vorticity, electrostatic potential ↔ stream function). **Grounded** (Driscoll & Fine, Phys. Fluids B 2, 1359 (1990); Fine et al., PRL 75, 3277 (1995), vortex crystals). Grok never names this analogy; it is the most direct lab bridge to RGRF's vortex-tensor theme and to the Arnold / 2D Euler material in the share #97 review.
- **Leaky boundaries.** Real columns leak: residual-gas collisions and field asymmetries exert torque and cause radial transport; a rotating-wall drive puts angular momentum back. **Grounded** (Huang et al., PRL 78, 875 (1997) for ions; Anderegg, Hollmann & Driscoll, PRL 81, 4875 (1998) for electrons).
- **Inertial vectors / shifting phase order.** Channing's msgs 7 and 9 (rock in a stream, path widening and narrowing) map onto reduced-dimension motion on a defect and onto observer effects. Labelled **Symbolic** as a picture; the component physics Grok cites is checked below.

## 1. What "supercooled free electrons" and "fast rotation" mean (msg 2)

| Claim | Label | Note |
|---|---|---|
| Ultracold neutral plasmas, Te ~1–10 K, n ~10¹⁴–10¹⁸ m⁻³ | **Grounded** | Killian et al., PRL 83, 4776 (1999); Killian et al., Phys. Rep. 449, 77 (2007). Rapid electron heating (disorder-induced, three-body) means "<10 K in hundreds of ns" is Grok-reported [to verify]. |
| Penning–Malmberg electron columns; cyclotron cooling; long confinement with a rotating wall | **Grounded** | O'Neil, Driscoll, Malmberg lineage; Anderegg et al. 1998. "Weeks" is Grok-reported; hours-to-days-scale confinement is documented [to verify the "weeks" figure]. |
| Single-electron quantum cyclotron at ≲100 mK, ground state, g/2 measurement | **Grounded** | Peil & Gabrielse, PRL 83, 1287 (1999); Fan et al., PRL 130, 071801 (2023). |
| ωc = eB/me ≈ 28 GHz/T | **Grounded** (rerun) | 27.99 GHz/T. |
| Electron vortex (OAM) beams rotating at Larmor / cyclotron / zero by m | **Grounded** | Schattschneider et al., Nat. Commun. 5, 4586 (2014). "~100 GHz" is Grok-reported. |
| Rigid E×B rotation, rotating-wall phase lock; ion crystals lock with no slip | **Grounded** | Laser-cooled ion crystals (Be⁺) phase-locked to the wall: Huang et al. 1998 (Science 279, 686) and Bollinger group. |
| Rotation-induced E in metals, E ≈ −K(M/e)ω²r | **Plausible / Grok-reported** | Basic Stewart–Tolman-type inertial field is E ≈ (m_e/e)ω²r for free electrons; the lattice-ion "K M" correction form is Grok-reported [to verify]. |
| London moment B = (2m/e)ω (sign convention aside) | **Grounded** | Tate et al. 1989 (Nb). |
| Russian patent on Cooper pairs under centripetal load | **Speculative** [to verify] | No identifier given. |
| No net gravity / inertia cancellation from an electron column | **Grounded** | Agrees with em_topological_gravity review. |
| φ-cut rotating-wall electrode segments | **Symbolic** | Untested; an engineering choice at most, as Grok says. |
| Supercooled electron liquid in organic θ-phase compounds | **Grounded** (different object) | Kagawa et al., Nat. Phys. 9, 419 (2013); Sato et al., Science 357, 1378 (2017) [to verify exact citation]. |

## 2. Brillouin limit (msg 4): rerun

| Claim | Label | Note |
|---|---|---|
| ωp² = 2ω(ωc − ω), max at ω = ωc/2, n_B = ε0B²/(2m) | **Grounded** (rerun) | Davidson, *Physics of Nonneutral Plasmas* (1990). Coefficient 4.860×10¹⁸ m⁻³ T⁻². |
| Whole B table (0.01–10 T), protons ×1/1836 | **Grounded** (rerun, all rows match to 3 s.f.) | |
| 1 T cap ~5×10¹² cm⁻³; 5 T ~1.2×10¹⁴ cm⁻³ | **Grounded** (rerun) | Real columns usually sit well below n_B (typically ≲ a few %); Grok says this qualitatively. |
| "Strain can support n/n_B > 1" | **Speculative / Grok-reported** [to verify] | |
| **Rim field "tens of kV/cm"** | **Corrected** | Uniform column n = 0.2 n_B at 1 T, R = 1 cm: E_rim = neR/(2ε0) ≈ 8.8×10⁷ V/m ≈ **880 kV/cm**, ~30× larger. The qualitative point ("density fights you through voltage") is stronger than Grok said. |
| Cyclotron cooling ∝ B² | **Grounded** (rerun) | τ = 3πε0me³c³/(e⁴B²) ≈ 2.6 s at 1 T, 0.10 s at 5 T, 258 s at 0.1 T (Grok gave no value). |

## 3. Helium vortex and surface traps (msg 6)

| Claim | Label | Note |
|---|---|---|
| Electron bubble ~2 nm (Grok); bound to vortex cores, escape frozen below ~1.5 K | **Grounded** | Bubble radius is ~1.7–1.9 nm (diameter ~3.5 nm) — "~2 nm across" is **slightly low**; binding tens of K (Donnelly, *Quantized Vortices in He II*, 1991). |
| Packard imaging of vortex lattices with electrons | **Grounded** | Yarmchuk, Gordon & Packard, PRL 43, 214 (1979). |
| Manchester bead spacing 0.1–0.4 μm; 6e/8e nanobubbles lasting ≥15 ms | **Grok-reported** [to verify] | |
| κ = h/m₄ ≈ 9.97×10⁻⁸ m²/s; n_v = 2Ω/κ | **Grounded** (rerun) | 9.969×10⁻⁸. Ω = 1 rad/s gives 2.0×10⁷ m⁻² (spacing ~220 μm); 3.5 rad/s gives 7.0×10⁷. Grok's "~2×10⁷" fits only the low end. |
| RIKEN rotating dilution fridge, ~5 mK, Ω up to 3.5 rad/s | **Grok-reported** [to verify] | |
| Surface electrons ~11 nm above He, binding ~7.6 K, 1→2 at ~125 GHz | **Grounded** (rerun) | Hydrogenic model: 0.657 meV = 7.6 K, ⟨z⟩ = 11.4 nm, 1→2 = 119 GHz; measured 125.9 GHz (Grimes et al., PRL 37, 1976). |
| Surface density ≲2×10⁹ cm⁻² (bulk), up to ~6×10¹¹ (films); Wigner crystal | **Grounded** | Grimes & Adams, PRL 42, 795 (1979) for the Wigner crystal; film density figure Grok-reported. |
| Single electrons in 5 μm pools read with an SET | **Grounded** [to verify citation] | Papageorgiou et al., APL 86 (2005) / Lyon group. |
| Cosmic filaments spin; 15 Mpc H I structure; dark-vortex bundles | **Grounded / Grok-reported** | Wang et al., Nat. Astron. 5, 839 (2021) for filament spin; the H I structure and ultralight-DM vortex model Grok-reported [to verify]. |
| He vortex ↔ cosmic filament "same sentence" | **Symbolic** | Grok itself says scales don't transfer. |

## 4. Dragging vs suction and the tunnel thought experiment (msgs 8, 10)

| Claim | Label | Note |
|---|---|---|
| Bernoulli pressure dip binds bubbles to vortex cores; motion reduced to 1D | **Grounded** | |
| Lense–Thirring measured around Earth; negligible for lab columns | **Grounded** | Gravity Probe B (Everitt 2011), LAGEOS. |
| Feynman rule fixes vortex count; lattice is an equilibrium | **Grounded** | |
| Aberration narrows the forward view with speed | **Grounded** | Relativistic aberration; noticeable only at v ≳ 0.1c. |
| Biology climbs gradients "with metabolism paying" ; vessels/mycelium widen with flux | **Grounded** in general (Murray's law, adaptive transport networks) | Mapping to R(s) is **Symbolic**. |
| Dark energy as "slow widening of every groove" | **Symbolic** | |
| "Order stored in the defect" | **Plausible-untested** as an RGRF heuristic | Testable in Penning columns via Driscoll–Fine vortex experiments. |

## 5. Corrections summary

1. Rim E-field at n = 0.2 n_B, 1 T, 1 cm: ~880 kV/cm, not "tens of kV/cm".
2. Feynman vortex density ~2×10⁷ m⁻² holds at Ω ≈ 1 rad/s; at 3.5 rad/s it is 7×10⁷.
3. Electron bubble in He-II is ~3.5–3.8 nm across, not ~2 nm.
4. Rotation-induced metal field: textbook form is (m_e/e)ω²r; Grok's K·M form [to verify].
5. Missing link added: electron-plasma ↔ 2D Euler (Driscoll & Fine 1990), the natural vortex-dynamics test bed for RGRF.

## 6. Open items

- Target B, radius and fill fraction for a bench column [Channing to supply].
- Whether the helium route (cryostat) or the Penning route (magnet + kV) is the preferred analog platform [Channing to supply].
