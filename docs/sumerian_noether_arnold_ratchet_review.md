# Review: Sumerian history, Noether's theorem, Navier–Stokes, Arnold geodesics and ratchet handoffs (share #97)

- **Archive:** [grok_archive/2026-10-22_sumerian_history_and_noethers_theorem.md](grok_archive/2026-10-22_sumerian_history_and_noethers_theorem.md) (share `900583cc`, 18 messages: 9 Channing, 9 Grok).
- **Checks:** [sims/noether_sumer_s97_checks.py](../sims/noether_sumer_s97_checks.py) ([output](../sims/noether_sumer_s97_checks_output.txt)).
- **Related:** [shifting_phase_order_review.md](shifting_phase_order_review.md), [magnus_floquet_inertial_copv_review.md](magnus_floquet_inertial_copv_review.md), [inertia_sheath_stress_review.md](inertia_sheath_stress_review.md), [acoustic_streaming_and_centrifugal.md](acoustic_streaming_and_centrifugal.md), [stellarator_argon_heliosphere_review.md](stellarator_argon_heliosphere_review.md) (§0, friction and counter-rotation), [recent_fluid_dynamics_2024_2026.md](recent_fluid_dynamics_2024_2026.md), [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md), [chern_simons_manta_butterfly_review.md](chern_simons_manta_butterfly_review.md), [em_topological_gravity_review.md](em_topological_gravity_review.md), [letter_number_systems_528_review.md](letter_number_systems_528_review.md), [grok_archive/2026-10-17_ancient_alphabetic_number_systems.md](grok_archive/2026-10-17_ancient_alphabetic_number_systems.md), [grok_archive/2026-10-17_hopf_flow_topology_vortex_systems.md](grok_archive/2026-10-17_hopf_flow_topology_vortex_systems.md), [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md).
- **Labels:** Grounded = established in peer-reviewed literature / standard references, or rerun here; Plausible-untested; Speculative; Symbolic (φ and similar, unless tested). "Grok-reported" = figure not rerun here.

## 0. Context and the RGRF link

RGRF core themes: leaky boundaries, inertial vectors, shifting phase order, spin/vortex tensors, MHD equilibrium. Channing has also raised **friction from inertial momentum setting up opposite angular momentum**.

- **Grounded (Noether link):** rotation symmetry of the laws ⇒ total angular momentum conserved. Friction or viscous coupling between two rotating parts moves angular momentum from one to the other; it cannot create net L. The check script (§5) reruns two viscously coupled rotors: total L stays 10.000 to 6 digits while one rotor loses 7.5 units and the other gains 7.5; kinetic energy falls 50 → 12.5 (dissipated as heat). When one part is anchored to a frame, the frame takes the opposite L. That is the standard reaction torque, not a new effect.
- **Grounded:** Grok's msg 6 to 12 "sum vs difference" split (S = Γ_i + Γ_o kept, Δ = Γ_i − Γ_o spent) is the circulation version of the same bookkeeping. Joint relabeling symmetry protects the sum. Interface friction or drive only moves circulation between the inner and outer phases.
- **Plausible-untested:** that a timed difference channel (Δϕ locked near 180°) reproduces the shifting-phase-order settling sequence (magnetic → thermal → precession → kinematic → recovery). No model or bench data here tests it.

## 1. Sumer (msg 2)

| Claim | Label | Note |
|---|---|---|
| Timeline Ubaid ~6500–4000, Uruk ~4000–3100, Early Dynastic ~2900–2334, Akkadian ~2334–2154, Ur III ~2112–2004 BCE | **Grounded** | Middle-chronology dates as in standard surveys (Postgate, *Early Mesopotamia*, 1992; Van De Mieroop, *A History of the Ancient Near East*, 3rd ed. 2016). Ubaid end is often given as ~3800 BCE. |
| Sumerian is a language isolate; persisted as a written prestige language after ~2000 BCE | **Grounded** | Standard (e.g. ETCSL, Oxford). |
| Writing begins as accounting: tokens → proto-cuneiform (Uruk IV, ~3300–3200 BCE) | **Grounded** | Nissen, Damerow & Englund, *Archaic Bookkeeping* (1993); Schmandt-Besserat on tokens (the token-to-writing path is debated in detail). |
| Enheduanna, daughter of Sargon, en-priestess of Nanna at Ur, earliest named author | **Grounded** | Widely accepted; some scholars question her authorship of all attributed hymns. |
| Ur-Nammu's code is one of the earliest surviving law codes; standardized measures | **Grounded** | Earlier reform texts exist (Urukagina of Lagash), but no earlier surviving code. |
| Wheel, sail, bronze tools "first recorded at scale" | **Plausible-untested** as stated | Wheeled vehicles appear ~3500–3300 BCE across Mesopotamia, the Caucasus and Europe; "first" is contested. |
| Sexagesimal (base-60) place value; 60 has many divisors | **Grounded** (rerun) | 60 has 12 divisors; the 10 proper ones match Grok's list. Full positional notation is Old Babylonian. 360° and the 12 × 30° zodiac are later Babylonian (first millennium BCE), as Grok says. |
| Systematic mathematical astronomy mostly Babylonian; Sumerians tracked visible planets and star groups | **Grounded** | Neugebauer, *A History of Ancient Mathematical Astronomy* (1975); Hunger & Pingree, *Astral Sciences in Mesopotamia* (1999). |
| Pantheon (An, Enlil, Enki, Inanna, Nanna/Utu); the *me*; layered cosmology; ziggurats as temple platforms | **Grounded** | Black & Green, *Gods, Demons and Symbols of Ancient Mesopotamia* (1992); Woolley's excavation of the Ziggurat of Ur. |
| Kramer's list of "firsts" | **Grounded** | S. N. Kramer, *History Begins at Sumer* (1956). Grok's caveat that it is "a little promotional" is fair. |

**Alternative claims, stated plainly.** Zecharia Sitchin's readings (*The 12th Planet*, 1976), including the Anunnaki as visitors from a planet "Nibiru", Sumerian knowledge of Pluto or of a full heliocentric system, and ziggurats as launch pads or docking stations, are **Speculative**. Mainstream Assyriology rejects them. The cuneiform texts do not support them, and Sitchin's translations do not hold up against the lexical sources (Sumerologist critiques, e.g. M. Heiser [to verify]; NASA on Nibiru as a non-object). Grok kept these out, and so does this review. People who find the Anunnaki stories meaningful are welcome to read them as modern myth-making. They are not history.

**Small correction:** Grok says Sumer and Noether "sit centuries apart". The gap is about four millennia.

## 2. Noether's theorem (msg 2)

| Claim | Label | Note |
|---|---|---|
| *Invariante Variationsprobleme*, 1918, prompted by Hilbert/Klein and energy in GR | **Grounded** | Nachr. Ges. Wiss. Göttingen 1918, 235–257; Kosmann-Schwarzbach, *The Noether Theorems* (2011). |
| First theorem: continuous symmetry of the action ⇒ conserved quantity; converse under technical conditions | **Grounded** | Grok states it correctly (variational, continuous, on-shell). |
| Dictionary: time → energy; space → linear momentum; rotation → angular momentum; boost → uniform centre-of-mass motion; global U(1) phase → electric charge | **Grounded** | All correct. Rerun (§4): the central potential keeps L to 7e-15; an anisotropic potential that breaks rotation symmetry lets L drift by 5e-2. Energy is conserved in both cases. |
| Q = Σ a_i ∂L/∂q̇_i − F, cyclic coordinates | **Grounded** | Standard (Goldstein; Arnold, *Mathematical Methods*). |
| Second theorem: local (gauge/diffeomorphism) symmetries give identities, not proper charges; subtlety of energy in GR | **Grounded** | Correct. |
| Limits: thermodynamic second law is not a Noether law; discrete symmetries outside the original statement | **Grounded** | Correct. |
| Einstein quote "penetrating mathematical thinking" | Grok-reported [to verify] | Einstein praised the 1918 paper in a letter to Hilbert; the exact phrase needs a source. Biography (dismissed 1933, Bryn Mawr, died 1935 aged 53) **Grounded** (age rerun). |
| "Where they touch": accounting as conservation practice; ziggurat orientation as a local symmetry choice | **Symbolic** | Grok itself frames it as analogy and calls "Sumerians anticipated Noether" a category error. Agreed. |

## 3. Navier–Stokes, Euler, Buckmaster, Fuller (msg 4)

- **Grounded:** Euler = NS with ν = 0. Clay asks about global smoothness vs finite-time blowup of 3D incompressible NS. Arnold (1966) describes ideal Euler as geodesic flow on SDiff(M). Fuller's domes use the Euler characteristic V − E + F = 2, and C60 has exactly 12 pentagons (rerun: 60 − 90 + 32 = 2).
- **Grounded (sources found):** On 8 September 2026 OpenAI posted a Lean-formalized finite-time blowup for *forced* NS (Clay alternatives C/D). Buckmaster (NYU) and Alpöge separately released smooth-forcing blowups for Euler, Boussinesq and porous media, building on Córdoba and Martínez-Zoroa (NYU news, Sept 2026; Buckmaster statement). An independent Lean rebuild passed the kernel check but does not show that the formal statement matches the Clay prose.
- **Plausible-untested:** that the Clay problem is "settled". Grok quotes a Clay note dated 11 Sept 2026 [to verify]. No prize has been awarded. Grok's own "claimed, not certified" framing is the right one.
- Grok correctly reads "Buckminister" as most likely Buckmaster, and treats Fuller separately.

## 4. Inner/outer phase and Arnold geodesics (msgs 6, 8)

| Claim | Label | Note |
|---|---|---|
| Boundary-layer (Prandtl) scale ∼ √ν, i.e. δ/L ∼ Re^-1/2; matched asymptotics fix constants, not a lag | **Grounded** (rerun) | Standard. |
| Two-phase NS: density/viscosity jumps, Young–Laplace stress, shared time | **Grounded** | Standard free-boundary formulation. |
| Arnold 1966: Euler = geodesics of the right-invariant L² metric; Euler–Arnold equation; Kelvin and vorticity freezing from relabeling symmetry (Noether) | **Grounded** | Arnold, Ann. Inst. Fourier 16 (1966); Salmon, Annu. Rev. Fluid Mech. 20 (1988) for relabeling → Kelvin; Arnold & Khesin, *Topological Methods in Hydrodynamics* (1998/2021). |
| Helicity as Casimir; negative sectional curvature; Arnold energy-Casimir stability; Ebin–Marsden Sobolev manifold | **Grounded** | Moffatt 1969; Ebin & Marsden, Ann. Math. 92 (1970). Caveat that curvature sign is not a stability criterion is correct. |
| Group/metric dictionary (rigid body, Kirchhoff, MHD, Burgers, KdV via Virasoro, Camassa–Holm) | **Grounded** | Standard in Arnold–Khesin and Khesin–Misiołek–Modin (2019+). |
| Multiphase Euler on a Lie groupoid (Izosimov–Khesin); Brenier generalized flows | **Grounded** / Izosimov–Khesin [to verify exact reference] | Brenier, JAMS 2 (1989). |
| "Settling order" (magnetic → thermal → precession → kinematic → recovery); ~0.09 s recovery with valves at L = 8 cm | **Plausible-untested** / Grok-reported | Comes from earlier RGRF threads. See [shifting_phase_order_review.md](shifting_phase_order_review.md). Recovery time [Channing to supply] the source run. |
| S = Γ_i + Γ_o as the joint relabeling charge, Δ = Γ_i − Γ_o as the phase channel | **Plausible-untested** | Sound bookkeeping. Whether Δ is the variable that matters for a real cell is untested. |

## 5. Two-component Lagrangian and the sin Δϕ coupler (msgs 10, 12)

- **Grounded pieces:** kinetic metrics, ideal-MHD magnetic energy, surface tension, the pressure multiplier, and the Euler / MHD-Euler bulk equations from varying S.
- **Correction (sign), rerun §6:** with U(Δϕ) = A cos Δϕ (minimum at the π lock), the generalized force is τ = −∂U/∂Δϕ = **+A sin Δϕ**, and that is restoring toward π. Grok wrote τ = −A sin Δϕ "restoring toward π". That sign pushes away from π. Likewise the second variation is ½U'' (δΔϕ)² = **−½A cos Δϕ (δΔϕ)²**, which is positive at π (a well). Grok wrote A cos Δϕ (δΔϕ)², called it negative at π, and still called it a well. That is internally inconsistent. The qualitative conclusion holds: a well for recovery, plus a ratchet for pumping.
- The factor 2 in Δ̇ = −2A sin Δϕ is Grok-reported (it depends on loop normalization).
- **Plausible-untested:** that the sum-channel Hessian can be made positive (Arnold-stable) while the difference channel stays neutral. That is a criterion to test, as Grok says.
- **Grounded:** a ratchet needs broken symmetry plus a non-equilibrium drive (Feynman's ratchet and pawl; Reimann, Phys. Rep. 361 (2002)).
- **Grounded:** ferrofluid thermal ratchet with static + oscillating fields: Engel, Müller, Reimann & Jung, PRL 91, 060602 (2003). The quoted torque formula N_z ∝ α_y³ α_x ω²(ω cos β + 2 sin β)/[(1+ω²)(4+ω²)²] is Grok-reported [to verify against the paper].
- Traveling-wave ferrofluid pumps, magnetic bead ratchets: **Grounded** (general literature). Tesla valve as a passive fluid diode: **Grounded** (Tesla valve patent 1920; Nguyen et al., PNAS 2021).
- Two-ODE sweep: proposed, not run. [Channing to supply] parameter ranges if wanted.

## 6. Skyrmion / domain-wall ratchets (msg 14)

- **Grounded:** topological charge Q = (1/4π)∫ m·(∂_x m × ∂_y m); Thiele equation; skyrmion Hall effect (Jiang et al., Nat. Phys. 2017; Litzius et al., Nat. Phys. 2017). Domain-wall ratchets and shift registers (Parkin racetrack, Science 2008; Franken et al., Nat. Nanotech. 2012).
- **Plausible-untested / Grok-reported:** Göbel & Mertig skyrmion ratchet [to verify: Sci. Rep. 2021], the ~50% rectification ceiling and ~20 m/s simulated speeds. These are micromagnetic, nanoscale results.
- **Symbolic:** the mapping to the cell (pocket = valve flare, counted seats = acoustic nodes, two lanes = inner/outer). It is useful design language, as Grok labels it.

## 7. EM / plasma skyrmions (msg 16)

- **Plausible-untested / Grok-reported [to verify]:** Wits (Forbes group) optical skyrmions over a ~270 m free-space link with topological fidelity >98% (worst ~86%), Physics World 9–10 Sept 2026; the Nature Communications turbulence result; stochastic optical skyrmions; the plasma SHG skyrmion preprint (Barriopedro, Oliva, Porras, May 2026, N_sk = ℓ₂ − ℓ₁); photonic Shankar skyrmions (Wang–Fan); vortex-electron → 15–25 GHz skyrmion (Opto-Electronic Advances, Aug 2026). The underlying ideas (Stokes skyrmions, OAM, topological robustness) are **Grounded**. The specific 2026 papers were not checked here.
- **Speculative:** cosmic plasma filaments carrying such wrappings, and "ley-line" readings. Grok labels them that way too.

## 8. φ and symbols

φ does not appear in this share. The "priestess and mathematician" Entanglements scene is fiction (**Symbolic**). Grok says so.

## 9. Withheld

- One clause in msg 6 (a drive-actuator aside) replaced with `[omitted: out of scope]`.
- The three embedded web images (tablet, ziggurat, portrait) are described in text, not committed.
- No personal material found.

## 10. Open items

- [to verify] Clay 11 Sept 2026 note; Izosimov–Khesin, Göbel–Mertig, Engel torque formula, 2026 optical/plasma skyrmion papers; Einstein quote; Heiser critique reference.
- [Channing to supply] source run for the ~0.09 s valve recovery time and the L = 8 cm geometry; whether to run the two-ODE ratchet sweep.
