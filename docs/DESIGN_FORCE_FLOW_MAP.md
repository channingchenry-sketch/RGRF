# Design → Force → Flow map
*License CC0. Prepared with Channing, 2026-10-12. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Equations come only from the linked docs or standard textbook physics. No new numbers: a "—" means the value is not in the repo yet.*

## Principle
Channing's words: *"A lot of informed speculation depends on design parameters, which we map to force parameters as much as possible so we have flow vs force."*

What that means for this table: every design choice (a material, a size, a frequency, a field strength) gets traced to the **force or equation** that it sets. That force then drives a **flow**, meaning whatever actually moves: charge, heat, fluid, field, or phonons. Once a speculative idea has a row here, it can be tested. Measure the flow, then check whether the force law predicts it. A parameter with no force behind it yet goes in [Unmapped parameters](#unmapped-parameters) and is not counted as part of the design.

Columns: **Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source**

## 1. Tungsten–Bismuth core (heartbeat)
Source: [tungsten_bismuth_core.md](tungsten_bismuth_core.md). Section numbers (§) refer to that file.

### 1a. Tungsten shell: heat and induced current
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| W thermal conductivity k(T) (~174 W/m·K at room temperature, falling to ~100–120 W/m·K near 1000 °C) | Fourier: q = −k∇T | Heat (conduction through the shell) | Grounded | Not measured here. Bench 3: heat a W rod, log T, fit k(T) | §1, §9 |
| W shell thickness / temperature gradient ∇T | q = −k∇T (heat flux is set by the gradient and the thickness) | Heat | Grounded | — | §1 |
| W operating temperature | ρ(T) rises with temperature, so δ grows; k(T) falls | Heat, charge | Grounded | — | §1, §7a-math |
| W resistivity ρ ≈ 5.6×10⁻⁸ Ω·m × drive frequency f | Skin depth δ = √(ρ/(πfμ₀)) = √(2/(ωμσ)): ~3.8 mm at 1 kHz, ~0.12 mm at 1 MHz | Charge (induced eddy current confined to depth δ), field | Grounded (calculated) | Calculated only. Coil-impedance sweep (§7a-inv) | §7a-math |
| He/neutron exposure of the plasma-facing surface | Materials damage (fuzz, embrittlement, transmutation): no single force law | Material degradation | Grounded (phenomenon) | — | §1 |

### 1b. Bismuth layer: diamagnetism and carriers
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Bi volume susceptibility χ ≈ −1.6×10⁻⁴, volume V | Diamagnetic force F = (χV/μ₀) B ∇B (textbook; equivalent to −∇(−χVB²/2μ₀)) | Force on the Bi piece (repulsion from high field); magnetization | Grounded | Bench 2: levitate Bi over NdFeB, measure gap vs field | §2, §9 |
| Field product B∇B of the magnet array | Same F = (χV/μ₀)B∇B; must at least balance ρ_Bi·V·g to lift (textbook) | Force | Grounded | Bench 2 | §2, §7c |
| Bi melting point (~271 °C) vs core temperature | Thermal limit (Fourier heat reaching the Bi layer through the W) | Heat | Grounded | — | §2, §6 |
| Bi resistivity ~1.3×10⁻⁶ Ω·m × f | δ = √(ρ/(πfμ₀)): ~18 mm at 1 kHz, ~0.57 mm at 1 MHz | Charge, field (Bi is far more transparent than W) | Grounded (calculated) | Calculated only | §7a-math |
| Bi carrier density n, effective mass m* | Drude ω_p = √(n e²/(ε₀ m*)) | Charge (free-carrier plasma oscillation, infrared edge) | Grounded | — | §2 |
| Bi nanoparticle size | LSPR resonance condition | Field (optical absorption) | Grounded | Bench 4 (optional): absorption vs size | §2, §9 |
| W–Bi composite fill fraction / layering | Effective-medium mixing for k and permittivity | Heat, field | Plausible-untested | — | §6 |

### 1c. Quartz / piezo partner
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Piezo phase choice (α-quartz, BNT, BiFeO₃; *not* elemental Bi) | Symmetry rule: a centrosymmetric crystal has d = 0. Quartz is point group 32, so d ≠ 0 | Charge ↔ strain | Grounded | — | §0, §7d |
| Quartz d-coefficients (d₁₁, d₁₄ nonzero for class 32; values not in repo) | Direct effect D = d·T + ε^T E; converse S = s^E·T + dᵀE (textbook) | Charge (surface charge from stress); phonons (strain from field) | Grounded (law); values — | Not measured | §7d |
| Shunt L, C | f = 1/(2π√(LC)); piezo shunt damping | Charge (through the shunt) → heat; phonon energy removed | Grounded (mechanical structures); Plausible-untested for a core | Bench 1: Q / ring-down with and without the shunt | §4, §9 |
| Heartbeat frequency and geometry | Mode frequencies of the lattice: no drive law given | Phonons | Speculative (missing) | — | §0, §10 |
| Coherent-phonon excitation | Electron–phonon coupling (pump–probe) | Phonons ↔ charge | Grounded (phenomenon); plasma coupling Plausible-untested / Speculative (only through surface, sheath, wall) | — | §7d |

### 1d. Z-pinch / plasma
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Axial current I_z | J×B pinch; radial balance dp/dr = −(B_θ/μ₀r)·d(rB_θ)/dr | Charge (axial), plasma inward (compression) | Grounded | — | §3 |
| Current I vs line density N, T_e+T_i | Bennett I² = (8π/μ₀) N k_B (T_e + T_i) | Charge; plasma pressure balance | Grounded | — | §3 |
| Sheared axial flow dv_z/dr | Stability: dv_z/dr ≳ 0.1 k V_A (Shumlak & Hartman 1995) | Fluid (plasma axial flow) suppressing m=0, m=1 modes | Grounded (ZaP/FuZE) | — | §3 |
| Length scale L vs ion inertial length d_i = c/ω_pi | Hall-MHD ∂B/∂t = ∇×(v×B) − ∇×[(J×B)/(ne)] + η∇²B; ε_H = d_i/L | Field (advection, Hall decoupling, diffusion) | Grounded | — | §7b-math |
| Wavenumber k (small scales) | Whistler ω ≈ k² v_A d_i; ion-cyclotron branch at Ω_i | Field (dispersive waves) | Grounded | — | §7b-math |
| Resistivity η | η∇²B term | Field diffusion, heat | Grounded | — | §7b-math |
| "Optimal drive ~0.65", vortex 0.388, ion density 0.844 | Unrecovered toy model, normalized units | — | Speculative (no script) | Not physical | §7b |
| Wireless (CNT-sensor) feedback latency | Loop delay limits bandwidth (ms radio latency) | Information/charge | Plausible-untested | — | §7b, §7c |
| Attosecond pulses | HHG cutoff E = I_p + 3.17U_p | Charge (photoelectrons), field | Grounded as a diagnostic; Speculative as control (timescale mismatch) | — | §5 |

### 1e. Diagnostics: MT / CSAMT on the core
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Probe frequency sweep (e.g. 1 kHz–1 MHz) | Faraday ∇×E = −∂B/∂t, J = σE, ∇×B = μ₀J; δ sets the probing depth | Charge (induced currents), field | Grounded | — | §7a-math, §7a-csamt |
| Measured E/H at the surface | ρ_a = (1/ωμ₀)\|E/H\|², φ = arg(E/H); E = ZH | Field (impedance data) | Grounded | Not built. Coil sweep + inversion | §7a-math, §7a-inv |
| Inversion trade-off λ, model mesh | Occam Φ = Φ_d + λΦ_m; Gauss–Newton Δm update | Information (layer conductivity) | Grounded (method); Plausible-untested on the core | — | §7a-inv |
| Source–sample distance | Far field only beyond several δ; at bench scale it is near field | Field | Grounded | Use a full coil forward model | §7a-csamt |
| Telluric / geomagnetic tuning | mV/km natural fields | Charge | Speculative (for tuning) | — | §7a |
| Toroidal "photon chase", phi standing waves | No force law given | — | Speculative / Symbolic | — | §7, §8 |

## 2. POL lift: eddy currents, EDS, Halbach
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Coil frequency ω, plate skin depth δ | Plate loss P/F ≥ ωδ (Dodd & Deeds eddy model) | Charge (eddy current) → heat | Grounded | Sim: 10–17 kW for 88 kg (~52 N/kW). Bench: Al plate, N per W vs f | [ANALYSIS](ANALYSIS_2026-10-12.md), [lift §9](lift_and_equilibrium_systems.md) |
| Relative speed v (EDS / Inductrack) | Lenz repulsion; drag ∝ ~1/v above the transition speed; L/D ≥ 200:1 | Charge (induced), heat (drag) | Grounded | — | [lift §9](lift_and_equilibrium_systems.md) |
| Halbach magnet sequence | One-sided field concentration | Field | Grounded | Proposed sim upgrade | [lift §9](lift_and_equilibrium_systems.md) |
| Gap (EMS) | Attractive force, unstable by Earnshaw → active feedback | Force, charge (control current) | Grounded | — | [lift §9](lift_and_equilibrium_systems.md) |
| Coil current and gap stiffness | m z'' = F(I, z) − mg; eddy stiffness ~37 kN/m (sim) | Force | Grounded (sim) | Sim only | [piezo_helium](piezo_helium_feedback_loop.md) |
| Helium cell p, A, V | Gas spring k ≈ γpA²/V (≈8 kN/m for the stated case) | Fluid (gas compression) | Grounded / Plausible-untested as an add-on | — | [piezo_helium](piezo_helium_feedback_loop.md) |
| Driver lag τ | Loop tolerates τ = 20 ms, not 40 ms | Charge | Grounded (sim) | Sim | [piezo_helium](piezo_helium_feedback_loop.md) |
| Chirp probe on the drive coil | Resonance shift vs gap (system identification) | Charge, field | Plausible-untested | Bench: series-resonant coil + Al plate, ±0.5 mm prediction | [lift §8](lift_and_equilibrium_systems.md) |
| Conductive floor conductivity | Needs ~10⁷ S/m for eddy floors | Charge | Speculative for mycelium | — | [mycelium_uses](mycelium_uses.md) |

## 3. Buoyancy, Lorentz, ionic wind
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Envelope gas volume V, gas density | Archimedes F = (ρ_air − ρ_gas)gV (≈10.4 N/m³ for He) | Fluid (displaced air) | Grounded | Bench 1 (balloon trim) | [lift §1](lift_and_equilibrium_systems.md) |
| Conductor current I, length L, local B | F = q(E + v×B); F = IL×B; net external force needs an external field or medium | Charge; force | Grounded | — | [lift §2](lift_and_equilibrium_systems.md) |
| Corona voltage / electrode geometry | Electroaerodynamic thrust: 6.25 N/kW (aircraft) to ~50 N/kW (lab) | Charge (ions) → fluid (air) | Grounded; integration Plausible-untested | Bench 1: trim N vs W | [lift §4](lift_and_equilibrium_systems.md) |
| Coulomb egg charge (5 cm, 10 kV → ~5.6×10⁻⁸ C) | Coulomb; gyroscopic torque | Charge; torque, not lift | Grounded / Speculative for lift | Bench 5 (resonance transfer) | [lift §7](lift_and_equilibrium_systems.md) |

## 4. Multi-Egg / Elliptical Eye, ponderomotive, Maxwell stress
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Field gradient ∇⟨E²⟩, frequency ω | Ponderomotive F_p = −(e²/4mω²)∇⟨E²⟩ | Charge (electrons expelled from strong-field regions) | Grounded; free-air Newton lift Speculative | Prediction: depletion ∝ 1/ω² | [em_topo Dive A](em_topological_gravity_review.md) |
| Focus field strength (E, B at the foci) | Maxwell stress T_ij = ε₀(E_iE_j − ½δ_ijE²) + (1/μ₀)(B_iB_j − ½δ_ijB²); magnetic pressure B²/2μ₀ | Field momentum → force on boundaries | Grounded | — | [em_topo](em_topological_gravity_review.md) |
| Lens index profile | Luneburg n(r) = √(2 − (r/R)²) | Field (rays focused) | Grounded | — | [em_topo](em_topological_gravity_review.md) |
| Egg spin / eddy springs (C8) | Gyroscopic torque vs Lenz damping | Torque; charge → heat | Grounded (each); which dominates is open | — | [C1-C12](C1-C12_seed_map.md), [butterfly_node](butterfly_node.md) |
| Magnet/ferrofluid near copper (Butterfly-Node) | Lenz: velocity-proportional damping | Charge → heat | Grounded | Planned: copper control "to measure" | [butterfly_node](butterfly_node.md) |
| Multi-Egg rotors as gravity source | None ("gyro = torque not F_z") | — | Speculative | — | [em_topo](em_topological_gravity_review.md) |

## 5. Acoustic streaming and centrifugal buoyancy
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Drive ω, fluid viscosity ν | Boundary layer δ = √(2ν/ω) | Fluid (boundary-layer oscillation) | Grounded | — | [acoustic §1](acoustic_streaming_and_centrifugal.md) |
| Standing-wave amplitude U₁(x) | Rayleigh slip U_s = −(3/4ω)U₁ dU₁/dx | Fluid (steady streaming) | Grounded | — | [acoustic §1](acoustic_streaming_and_centrifugal.md) |
| Beam intensity I, attenuation α, scale L | Eckart u ~ αIL²/(ρcν) | Fluid (quartz-wind jet) | Grounded | — | [acoustic §1](acoustic_streaming_and_centrifugal.md) |
| Spin rate ω, radius r | dp/dr = ρω²r; a_c = ω²r | Fluid (dense outward, vapor inward) | Grounded; spin throttling Plausible-untested | — | [acoustic §2](acoustic_streaming_and_centrifugal.md) |
| Particle contrast factor | Acoustic radiation force to nodes/antinodes vs ρω²r | Fluid/particles | Grounded; combined control Plausible-untested (bridged text) | — | [acoustic §2](acoustic_streaming_and_centrifugal.md) |
| 60° torus twist | g_eff = ω²r along the helix | Fluid | Grounded kinematics; benefit Plausible-untested | — | [acoustic §2](acoustic_streaming_and_centrifugal.md) |
| Radial E in magnetized plasma | E×B drift; polarization drift | Charge (cross-B transport) | Grounded | — | [acoustic §3](acoustic_streaming_and_centrifugal.md) |
| Muon "buoyant lanes", spin-sum | None (GeV muons ignore buoyancy) | — | Speculative | — | [acoustic §3](acoustic_streaming_and_centrifugal.md) |

## 6. Fluid loops: Tesla valves, fluidic RLC, ferrofluid, dual-oil
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Tesla-valve geometry, Reynolds number, pulsation | Diodicity (reverse/forward ΔP), onset near Re ≈ 200 | Fluid (rectified net flow) | Grounded | Bench 2: net flow vs f | [lift §3, §8](lift_and_equilibrium_systems.md) |
| Wall compliance, fluid inertia, channel resistance | Fluidic R–L–C; series resonance → forward DC, parallel → backward | Fluid | Grounded | — | [lift §8](lift_and_equilibrium_systems.md) |
| Ferrofluid magnetization M, field gradient ∇H | Kelvin body force μ₀M·∇H | Fluid | Grounded | Bench 3: flow vs coil W; scale shows no net weight change | [lift §6](lift_and_equilibrium_systems.md) |
| Conducting-fluid current density | J×B (MHD pump) | Fluid, charge | Grounded | — | [lift loop 1](lift_and_equilibrium_systems.md) |
| Current path / induction zone | Joule heating J²/σ | Heat (steerable hot zone) | Grounded | Loop bench: ΔT vs W | [lift loop 2](lift_and_equilibrium_systems.md) |
| Expansion/compression pulses | Adiabatic cooling; condensation | Heat, fluid | Grounded | — | [lift loop 3](lift_and_equilibrium_systems.md) |
| Precessing elements, B | Larmor ω = γB; coupling efficiency unmeasured | Field/magnetization | Grounded in principle | — | [lift loop 5](lift_and_equilibrium_systems.md) |
| Castor E-field, particle polarizability | Electrorheological chaining (Winslow) | Particles; fluid stress | Grounded | Dual-oil runs 1–4 | [lift §6b](lift_and_equilibrium_systems.md) |
| Conductivity/permittivity/viscosity ratios at the interface | Taylor–Melcher leaky dielectric | Fluid (interface circulation) | Grounded; terpene knob Plausible-untested | Run 2 vs Taylor prediction | [lift §6b](lift_and_equilibrium_systems.md) |

## 7. Mycelium skins and materials
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Mycelium composite k (0.04–0.08 W/m·K; Bath 0.0415) | Fourier q = −k∇T | Heat | Grounded (measured in literature) | Literature values | [mycelium_uses](mycelium_uses.md) |
| Porosity / hyphal structure | Acoustic absorption | Phonons (sound) → heat | Grounded | — | [mycelium_uses](mycelium_uses.md), [core §7c](tungsten_bismuth_core.md) |
| Helmholtz cavity in the skin | Acoustic pressure → stress → piezo charge | Fluid (pressure) → charge | Grounded components; Plausible-untested hybrid | — | [core §7c](tungsten_bismuth_core.md) |
| Ultrasound alignment during growth | Claimed to raise the chitin/cellulose d-coefficient | Phonons → charge | Plausible-untested | — | [core §7c](tungsten_bismuth_core.md) |
| Coil-former dielectric loss at 13.56 MHz / kHz | Dielectric heating | Heat | Plausible-untested | Check loss and moisture | [mycelium_uses](mycelium_uses.md) |

## 8. Wireless power, Casimir, plasma bench, reefs, Schumann
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Coil Q, coupling, alignment | Coupled-mode resonant transfer (up to ~98.5 % at 11–20 kW) | Charge/field (near field) | Grounded | Bench: two-coil efficiency vs distance | [em_topo L6](em_topological_gravity_review.md), [ANALYSIS](ANALYSIS_2026-10-12.md) |
| Plate gap d | Casimir P = −π²ħc/(240d⁴) | Field (zero-point) → force | Grounded | — | [em_topo Casimir](em_topological_gravity_review.md) |
| Atom–wall distance z, polarizability α | U = −3ħcα/(8πz⁴) (retarded); F = −dU/dz | Force | Grounded | — | [em_topo Casimir](em_topological_gravity_review.md) |
| Anode bias, gas pressure | Double-layer threshold ∝ 1/P + C (Baalrud 2009) | Charge (plasma bubble) | Grounded (prediction) | Dusty-plasma bench | [dusty_plasma_bench](dusty_plasma_bench.md) |
| Reef crest geometry | Wave breaking/friction: 86 % energy at the crest, 97 % whole reef | Fluid (wave energy) → heat | Grounded | Meta-analysis | [coral_wave_barriers](coral_wave_barriers.md) |
| Earth–ionosphere cavity radius | f_n = (c/2πR)√(n(n+1)) | Field | Grounded | — | [bioelectric_coupling](bioelectric_coupling.md) |
| EZ water / H₃O₂ | None measured | — | Speculative / debated | Bench 4: EZ vs ion concentration | [lift §5](lift_and_equilibrium_systems.md) |

## Unmapped parameters
These are design parameters that have no force mapping yet.
- Heartbeat frequency, geometry and drive mechanism ([core §0, §10](tungsten_bismuth_core.md)).
- Phi / fractal / golden-spiral geometry factors (core §7, §8; [em_geometry_map](em_geometry_map.md): Symbolic).
- Helium "octave" positions ([helium_octave_table](helium_octave_table.md): Symbolic/curiosity).
- "Impedance zone" and "equilibrium" as quantities ([lift, Missing pieces](lift_and_equilibrium_systems.md)).
- Terpene / spice concentration as an interface-tension knob (size of effect unknown).
- CBD oil (no EM role).
- 60° twist as an "information-rich signal".
- Sheath/envelope EM manipulation against external air (the reaction body is unspecified).
- Toy HMHD "drive 0.65" (units unknown).
- Copper half-tube control and impedance-cascade values ([butterfly_node](butterfly_node.md): "to measure").
- Casimir 9×7 matrix (Missing).

## Top gaps
These are the parameters that change the force most, but whose values are unknown.
1. **Heartbeat drive frequency f.** It sets δ (∝ f^-½), the piezo shunt tuning and the eddy loss P/F ≥ ωδ. Every core force depends on it, and no value exists.
2. **Core geometry (W, Bi and quartz thicknesses, radius).** These set ∇T and so q, the B∇B the Bi sees, and the layering seen by inversion.
3. **Field product B∇B at the Bi.** The diamagnetic force is linear in it, and no magnet design has been specified.
4. **Pinch current I and line density N / temperatures.** The Bennett balance goes as I², and stability depends on dv_z/dr vs kV_A. None of these are given.
5. **Quartz/piezo d-coefficients and the coupling path into the plasma.** These set the charge per stress, but the sheath/wall coupling mechanism has no quantity.
6. **W k(T) and ρ(T) at operating temperature.** Using room-temperature values overstates the heat flow and understates δ.
7. **Length scale L vs d_i.** This sets whether the Hall term matters (ε_H). The plasma density is not given.
8. **Halbach EDS force-per-watt vs speed.** This is the open re-run that decides whether POL improves on ~52 N/kW.
9. **Larmor coupling efficiency and terpene interface effect.** Both are named as design parameters but have never been measured.
