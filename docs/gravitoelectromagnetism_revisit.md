# Gravitoelectromagnetism revisited: gravitoelectric and gravitomagnetic fields (2026-10-25)

*License CC0. Request (Channing, 2026-10-25): "Can we explore gravitomagnetic fields and gravitoelectric fields again?" Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations were checked by web search on 2026-10-25, or carried from repo docs where they were already checked; anything else is marked [to verify]. Sim: [../sims/gem_field_scale_sim.py](../sims/gem_field_scale_sim.py) (illustration). This builds on the earlier docs below and does not redo them.*

## 0. What the archive already has

| Doc (section, line) | Channing (verbatim) | Concluded then |
|---|---|---|
| [em_topological_gravity_review.md §4](em_topological_gravity_review.md) (lines 54–61, 84) | EU/GEM chain (no direct quote in that section) | GEM is a valid weak-field GR approximation, **Grounded** (GP-B ~37 mas/yr, LAGEOS). Lab rotor fields are "Grounded but negligible", ~GJ/(c²r³). Tajmar-type anomalies are **Speculative**, not reproduced. GEM is "real physics, but at strengths far too small for craft." |
| [shifting_phase_order_review.md §H3](shifting_phase_order_review.md) (lines 435, 453–466, 493–496) | line 435: "We went down a rabbit hole and bounced around from Pais effect in gravitoelectromagnetism in fractal spacetime to cathodoluminescence and imprinting techniques to Sonoluminescence." | GP-B −37.2 ± 7.2 vs −39.2 mas/yr, geodetic −6601.8 ± 18.3 (Everitt 2011); LAGEOS ~10 % (Ciufolini & Pavlis 2004). Tajmar gr-qc/0603033: unconfirmed; ring-laser null (Graham et al., Physica C 2008); the fractal-spacetime preprint was withdrawn. "Pais × GEM × fractal spacetime" is **Speculative / Symbolic**. |
| [tau_scaling_photon_drive_generator_review.md](tau_scaling_photon_drive_generator_review.md) (lines 26–28, 77–78; archive [grok_archive/2026-10-17_tau_scaling_law_electronics.md](grok_archive/2026-10-17_tau_scaling_law_electronics.md) ~841–951) | line 27: "Can we explore gravitomagnetic field locking, save our discoveries, and create a generator from this concept?" line 28: "So I’m picturing this generator almost looking like a hamster wheel this way we may be able to use ley lines in the future." | The frame-dragging physics is **Grounded**. A lab torus giving "locking" or power is **Speculative**, and **not supported** as a generator (lab rotor ~10⁻²⁰ of Earth's effect). Ley lines are **Symbolic**. |
| [holt_hau_searl_fput_jitterbug_review.md](holt_hau_searl_fput_jitterbug_review.md) line 17 | — | Spinning-superconductor weight reduction (Podkletnov-type) is unreplicated, **Speculative**. |
| [supercooled_electrons_rotation_review.md](supercooled_electrons_rotation_review.md) line 62 | — | Lense–Thirring is real but negligible for lab columns, **Grounded**. |
| [alcubierre_plasmoid_turbine_vortex_review.md](alcubierre_plasmoid_turbine_vortex_review.md) line 58 | — | Rotating EM fields frame-drag, but negligibly. |
| em_topological_gravity_review.md line 986; shifting_phase_order §G | — | The ordinary EM London moment B = (2m_e/e)ω is real and was used for GP-B gyro readout. |
| Local share `grok_share_6e822eca.txt` (same tau-scaling thread) | — | Already archived above. |

**New in this doc:**
- the field equations and convention caveats;
- LARES 2016, Tajmar's own 2011 null, Bardeen–Petterson and pulsar tests;
- the coupling-ratio number;
- a quantitative sim covering Earth, a bench rotor, an oloid, a neutron star and a black hole, with an energy check;
- the leaky-boundary and flux-attachment parallels.

## 1. The analogy (weak field, slow motion)

| Claim | Label | Note |
|---|---|---|
| With g_μν = η_μν + h_μν, the metric splits into a scalar potential Φ (Newtonian) and a vector potential A_g sourced by mass current. The gravitoelectric field E_g = −∇Φ − ∂A_g/∂t is ordinary gravity | **Grounded** | Standard treatments, e.g. B. Mashhoon, "Gravitoelectromagnetism: a brief review", arXiv:gr-qc/0311030 [to verify] |
| The gravitomagnetic field B_g = ∇×A_g comes from rotating or moving mass. The equations look like Maxwell's with ρ_e → ρ_m, 1/(4πε₀) → −G (like charges attract), and a factor that is 2 or 4 depending on convention | **Grounded** | Different authors put the factor in B_g, in the force law (a = E_g + 2v×B_g or v×B_g) or in A_g. Only the final precession is physical |
| The analogy is partial: gravity is spin-2, so the GEM "Lorentz force" is gauge/frame dependent, there are no negative masses to make dipoles, and it holds only at linear order | **Grounded** caveat | |
| Historical root: Heaviside (1893) proposed a gravitational analogue of Maxwell's equations; Holzmüller (1870) and Tisserand (1872) had velocity-dependent gravity forces | **Grounded** that Heaviside proposed it (O. Heaviside, "A gravitational and electromagnetic analogy", *The Electrician* 31, 281 (1893)) [page to verify] |
| Lense & Thirring (1918) derived frame dragging around a rotating body | **Grounded** [ref details to verify] |

Frame-dragging (gyroscope) precession: Ω = (G/c²r³)[3(J·r̂)r̂ − J]. On the spin axis this is 2GJ/(c²r³); averaged over a polar orbit it is GJ/(2c²a³).

## 2. Measurements

| Result | Label | Source |
|---|---|---|
| Gravity Probe B frame dragging −37.2 ± 7.2 mas/yr (GR −39.2); geodetic −6601.8 ± 18.3 (GR −6606.1) | **Grounded** | C. W. F. Everitt et al., *PRL* 106, 221101 (2011) |
| LAGEOS/LAGEOS II node drag at ~10 % | **Grounded** | I. Ciufolini, E. C. Pavlis, *Nature* 431, 958 (2004) |
| LARES + LAGEOS: μ = 0.994 ± 0.002 ± 0.05 (5 % systematic). L. Iorio's 2017 comment argued the error was larger; Ciufolini et al. replied in 2018 | **Grounded** (with a live error-budget debate) | Ciufolini et al., *EPJC* 76, 120 (2016); reply *EPJC* 78, 880 (2018) |
| Spin precession of binary pulsars (geodetic plus spin–orbit) | **Grounded** | e.g. Breton et al., *Science* 321, 104 (2008), double pulsar [to verify] |
| Accretion-disk Lense–Thirring precession and warping (Bardeen–Petterson); a proposed source of QPOs in X-ray binaries | **Grounded** (theory) / **Plausible-untested** (QPO identification) | J. M. Bardeen, J. A. Petterson, *ApJ* 195, L65 (1975) [to verify] |

## 3. Lab claims

| Claim | Label | Note |
|---|---|---|
| Tajmar, de Matos et al. (2006–07, ARC Seibersdorf) reported gravitomagnetic/acceleration signals near spinning niobium rings at cryogenic temperatures, ~10¹⁸ above GR | **Speculative → not reproduced** | gr-qc/0603033; gr-qc/0610015. Their own 2007–08 laser-gyro work found an onset temperature that did not match T_c and saw signals with aluminium too (*AIP Conf. Proc.* 969, doi:10.1063/1.2844946). Tajmar's improved 2011 facility found **no anomaly within 3× noise** (*Supercond. Sci. Technol.* 24, 125011 (2011)). Graham et al. 2008 ring laser: null. Respect to the group for publishing their own null. |
| Podkletnov & Nieminen (1992): a few-tenths-of-a-percent weight reduction above a spinning YBCO disk | **Speculative**, unreplicated | *Physica C* 203, 441 (1992) [to verify]. Attempted replications (e.g. NASA MSFC, late 1990s) reported no effect [to verify] |

## 4. Scale

- **Coupling.** G m_p² / (e²/4πε₀) = 8.1×10⁻³⁷ for two protons (sim). Gravity's "magnetic" part is a further v/c-squared smaller than its "electric" part.
- **Why lab rotors fail.** Ω ∝ GJ/(c²r³), with G/c² = 7.4×10⁻²⁸ m/kg. A 10 kg disk at 10,000 rpm gives Ω ≈ 2×10⁻²³ rad/s at 0.2 m, about 3×10⁻⁹ of Earth's GP-B value. **Grounded.**

## 5. Sim (illustration)

`sims/gem_field_scale_sim.py`, weak-field formulas. a_GM ≈ 2vΩ (the order-one prefactor depends on convention).

| Case | Ω (rad/s) | a_GE (m/s²) | a_GM (m/s²) | ratio a_GM/a_GE |
|---|---|---|---|---|
| Earth, GP-B orbit (642 km) | 6.3×10⁻¹⁵ = **41.1 mas/yr** | 8.1 | 9.5×10⁻¹¹ | 1.2×10⁻¹¹ |
| 10 kg steel disk, r = 0.15 m, 10,000 rpm, 0.2 m on axis | 2.2×10⁻²³ | 1.7×10⁻⁸ (its own pull) | 4.4×10⁻²³ (v = 1 m/s) | 2.6×10⁻¹⁵ |
| Oloid ~2 kg, r = 0.1 m, 3000 rpm (mass and I assumed) [Channing to supply] | 1.1×10⁻²⁴ | 5.9×10⁻⁹ | 2.2×10⁻²⁴ | 3.7×10⁻¹⁶ |
| Neutron star 1.4 M☉, P = 1.5 ms, r = 2R | 58 | 3.2×10¹¹ | 1.1×10¹⁰ (v = 0.3c) | 3×10⁻² |
| Kerr BH 10 M☉, a* = 0.9, r = 6GM/c² (weak-field formula used beyond its range, indicative only) | 170 | 1.7×10¹¹ | 4×10¹⁰ | 0.24 |

- The 41.1 mas/yr analytic polar-orbit average is within 5 % of GR's 39.2. The gap comes from the simple uniform-J model and the orbit radius [to verify the exact GP-B semimajor axis and model].
- **Energy check.** The disk stores 6.2×10⁴ J of kinetic energy. The gravitomagnetic coupling of a 1 kg·m²/s test spin, S·Ω, is 2.2×10⁻²³ J, a ratio of 3.5×10⁻²⁸. No usable energy flows; frame dragging is a precession, not a power source.

Plot: `/workspace/gem_field_scale_plot.png` (box only).

## 6. RGRF links (honest)

| Link | Label |
|---|---|
| Halbach arrays and spinning oloid/vortex/flux-tube rotors produce EM fields that matter. Their gravitomagnetic fields are ~10⁻²³ rad/s and irrelevant | **Grounded** (negligible) |
| Leaky boundary: frame dragging is strongest near the body and falls as 1/r³, so it has no "boundary". The magnetosphere is the leaky boundary; the gravitomagnetic field is not ([leaky_bound_state_family.md](leaky_bound_state_family.md)) | **Symbolic** |
| Flux-attachment parallel: a gravitational Aharonov–Bohm-like phase (the Sagnac effect for rotation; a gravitomagnetic AB phase proposed in theory) vs the AB phase of electrons around h/e flux ([flux_attachment_review.md](flux_attachment_review.md)) | Sagnac **Grounded**; GEM AB phase in the lab **Speculative** (far below detection); the analogy is **Symbolic** |
| Black-hole spin threads (Blandford–Znajek in [black_hole_magnetic_nucleus_review.md](black_hole_magnetic_nucleus_review.md)) | **Grounded**: this is where gravitomagnetism is strong |
| Levitation, propulsion or a generator from GEM | **Not supported** by evidence |

## 7. Gaps
- What is new that Channing wants from the "again": a specific device, the hamster-wheel generator, or the Pais/fractal chain? [Channing to supply]
- [to verify]: Mashhoon review ref; Heaviside 1893 page; Lense–Thirring 1918 ref; Breton 2008; Bardeen–Petterson 1975; Podkletnov 1992 page and the NASA replication; the exact GP-B orbit for the 39.2 figure.

- **See also:** [oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md): coherent rotor arrays and ratchets; no number of lab rotors reaches detectable frame dragging (packing limit ~6×10⁻²² rad/s).
