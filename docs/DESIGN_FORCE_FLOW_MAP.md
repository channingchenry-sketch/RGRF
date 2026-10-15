# Design → Force → Flow map
*License CC0. Prepared with Channing, 2026-10-12. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Equations come only from the linked docs or standard textbook physics. No new numbers: a "—" means the value is not in the repo yet.*

## Principle
Channing's words: *"A lot of informed speculation depends on design parameters, which we map to force parameters as much as possible so we have flow vs force."*

What that means for this table: every design choice (a material, a size, a frequency, a field strength) gets traced to the **force or equation** that it sets. That force then drives a **flow**, meaning whatever actually moves: charge, heat, fluid, field, or phonons. Once a speculative idea has a row here, it can be tested. Measure the flow, then check whether the force law predicts it. A parameter with no force behind it yet goes in [Unmapped parameters](#unmapped-parameters) and is not counted as part of the design.

Columns: **Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source**

## 1. Laminar precession in the egg (Multi-Egg)
Sources: [shifting_phase_order_review.md §A3, §B3](shifting_phase_order_review.md), [lift §7](lift_and_equilibrium_systems.md), [C1-C12 C8](C1-C12_seed_map.md), [butterfly_node](butterfly_node.md). Dimensionless groups are standard textbook definitions.

**Key point:** precession is a torque response. Inside a closed egg it **redistributes angular momentum and flow; it gives no net lift** (momentum conservation, §A3). The honest null test is to put the cell on a scale.

| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Rotor moment of inertia I, spin ω, applied torque τ | Precession rate Ω_p = τ/(Iω) | Angular momentum (axis cones) | Grounded | Not measured. Spinning rotor + known τ, time Ω_p | [§A3](shifting_phase_order_review.md) |
| Spin angular momentum L = Iω | Gyroscopic torque τ = Ω_p × L; resists the rate of tilt but has no restoring stiffness on its own | Torque (attitude), not force | Grounded (control-moment gyros) | — | [§A3](shifting_phase_order_review.md), [lift §7](lift_and_equilibrium_systems.md) |
| Egg size L, internal flow speed U, fluid ρ, μ | Reynolds Re = ρUL/μ (laminar vs turbulent) | Fluid | Grounded | — | textbook; [§A3](shifting_phase_order_review.md) |
| Spin Ω, kinematic viscosity ν = μ/ρ, size L | Ekman E = ν/(ΩL²) (boundary-layer thickness ~ E^½ L); Taylor Ta = 4Ω²L⁴/ν² (= E⁻²) | Fluid (Ekman layers, spin-up) | Grounded | — | textbook |
| Precession/spin ratio | Poincaré Po = Ω_p/Ω; a laminar spin-over mode holds below a threshold | Fluid (precession-driven flow in a spheroid) | Grounded (Kerswell; Lagrange, Meunier et al.; geodynamo experiments) | Bench 3: ferrofluid egg on a turntable, find the Po threshold | [§A3, §B3, bench 3](shifting_phase_order_review.md) |
| Egg ellipticity / aspect ratio | Sets the container's pressure torque on the fluid (sphere: viscous coupling only); shifts mode frequencies and triadic resonances | Fluid (spin-over mode amplitude, instability) | Grounded (fluids); optimum unknown | — | [§A3 item 4, §B3](shifting_phase_order_review.md) |
| Drive frequency ratio | Triadic resonance instability; detune to stay laminar | Fluid (secondary modes) | Grounded (precessing cylinders) | — | [§A3 item 4](shifting_phase_order_review.md) |
| Ferrofluid field (0–50 mT) | Magnetoviscous effect may shift the transition | Fluid, magnetization | Plausible-untested | Bench 3 | [bench 3](shifting_phase_order_review.md) |
| Egg spin near copper (eddy springs, C8) | Lenz damping ∝ velocity | Charge → heat | Grounded; which dominates (gyro or eddy) is open | — | [butterfly_node](butterfly_node.md) |
| Larmor vs flow precession | ω_L = γB; ω_c = qB/m (microscopic, not flow) | Spin/charge gyration | Grounded; equating them is a category slip | — | [§B3](shifting_phase_order_review.md) |
| "3-6-9" / φ phasing of rotors | No force law | — | Symbolic | — | [§A3](shifting_phase_order_review.md) |
| Precession for "lift assist" | None (closed system) | — | Speculative | Load-cell null test (bench 3) | [§A3](shifting_phase_order_review.md) |

**Unknown parameters (egg):** egg dimensions (L, aspect ratio), spin rate Ω and precession rate Ω_p, fluid (ρ, μ or ν), applied torque τ and rotor I. Without these, Re, E, Ta and Po cannot be computed, so the laminar regime is undetermined.

### 1b. Recovered egg design details (Channing, 2026-10-12)
> "We used a combination of fluids... the ferrofluid, cbd, water, and air was our more regenerative 1/3 fluid to air ratio, also, utilized phase shifts in the eggs design. The design parameters were built off of what it would take to be buoyant and gaps that allowed sympathetic responses."

| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| 1/3 fluid : 2/3 air fill (by volume, as stated) | Buoyancy F_b = ρ_fluid V_disp g on the egg in its surrounding medium; effective egg density ρ_eff = (m_shell + ⅓V ρ_liquid + ⅔V ρ_air)/V (textbook). The egg floats if ρ_eff < ρ_surrounding | Fluid (displaced medium); liquid slosh/settling inside | Grounded (law); fill-ratio choice Plausible-untested | Not measured. Weigh the egg and its displaced volume, compute ρ_eff | Channing 2026-10-12; [lift §1](lift_and_equilibrium_systems.md) |
| Fluid mix: ferrofluid + CBD oil + water + air | Immiscibility: water and oils separate into layers (interfacial tension). Ferrofluid is either water- or oil-based, and its carrier must match the phase it is meant to join. Kelvin force μ₀M·∇H acts only on the ferrofluid phase | Fluid (stratified layers; ferrofluid steered by field) | Grounded (immiscibility); CBD has no EM role ([lift §6](lift_and_equilibrium_systems.md)) | Vial test: count phases, check that ferrofluid follows its carrier | [lift §6, §6b](lift_and_equilibrium_systems.md) |
| Liquid-layer distribution under spin | dp/dr = ρω²r (dense phase goes outward; air goes inward) | Fluid | Grounded | — | [acoustic §2](acoustic_streaming_and_centrifugal.md) |
| Phase shift Δφ between eggs | Coupled oscillators: x₁, x₂ with coupling κ give normal modes split by ~κ. Energy exchange and interference depend on Δφ (in phase adds, antiphase cancels) | Field/mechanical energy exchanged between eggs (not created) | Grounded (law); egg implementation Plausible-untested | Bench 5 (two tuned rotors/coils, transfer vs detuning and Δφ) | [lift §7, bench 5](lift_and_equilibrium_systems.md) |
| Gap between eggs (for "sympathetic responses") | Coupling coefficient falls with gap. For magnetic/inductive coupling k = M/√(L₁L₂); the transfer rate scales with k, and critical coupling needs k·Q ≳ 1 (textbook coupled-mode) | Field (near-field coupling), energy | Grounded (law); k(gap) for eggs unknown | Measure k vs gap (two coils/eggs, splitting of resonance) | [em_topo L6](em_topological_gravity_review.md), [lift §7](lift_and_equilibrium_systems.md) |

**Unknowns (recovered egg):** egg volume and shell mass; the volume fractions of ferrofluid, CBD oil and water within the 1/3; the ferrofluid carrier (water or oil); the medium the egg floats in; the Δφ values used; egg resonant frequency and Q; gap distances and the resulting k.

## 2. Pulse / heartbeat in the W–Bi–quartz lattice
Source: [tungsten_bismuth_core.md §0, §4, §7a-math, §7d, §9](tungsten_bismuth_core.md). Piezo constitutive and thickness-mode formulas are standard textbook ones.

Chain: **drive amplitude → stress (quartz) → charge → current in the shunt / W shell → field confined to the skin depth δ.**

| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Quartz plate thickness t, stiffness c, density ρ | Thickness-mode resonance f = (1/2t)√(c/ρ) | Phonons (standing acoustic wave) | Grounded (law); values — | Not measured. Impedance sweep of a plate | textbook; [§7d](tungsten_bismuth_core.md) |
| Mechanical/electrical losses | Q = f₀/Δf; ring-down time ~ Q/(πf₀) | Phonon energy → heat | Grounded | Bench 1: Q / ring-down with vs without the shunt | [§9](tungsten_bismuth_core.md) |
| Shunt L, C (electrical analog) | f = 1/(2π√(LC)); piezo shunt damping | Charge (through the shunt) → heat | Grounded (structures); Plausible-untested for a core | Bench 1 | [§4](tungsten_bismuth_core.md) |
| Drive amplitude (voltage V or stress T) | Converse S = s^E·T + dᵀE gives strain; direct D = d·T + ε^T E gives charge Q = d·F (along the axis) | Phonons ↔ charge | Grounded | — | textbook; [§7d](tungsten_bismuth_core.md) |
| Pulse rate (charge per cycle × f) | Current I = dQ/dt ≈ 2πf·Q_amp | Charge (current flow) | Grounded | — | textbook |
| Pulse frequency vs W/Bi resistivity | Skin depth δ = √(ρ/(πfμ₀)): W 3.8 mm→0.12 mm, Bi 18 mm→0.57 mm (1 kHz→1 MHz) | Charge/field confined near the surface (W shields; Bi transparent; quartz unshielded) | Grounded (calculated) | Coil-impedance sweep + inversion (§7a-inv) | [§7a-math](tungsten_bismuth_core.md) |
| Piezo phase (quartz/BNT/BiFeO₃, not elemental Bi) | Only non-centrosymmetric crystals have d ≠ 0 | Charge ↔ strain | Grounded | — | [§0, §7d](tungsten_bismuth_core.md) |
| Lattice → plasma coupling path | Only via surface, sheath, wall or boundary conditions | Phonons → plasma (unknown) | Plausible-untested / Speculative | — | [§7d](tungsten_bismuth_core.md) |
| "Synchronizes the entire system" | No drive law or geometry | — | Speculative | — | [§0](tungsten_bismuth_core.md) |

**Unknown parameters (lattice):** quartz/lattice thickness t (and cut), heartbeat frequency f, drive amplitude (V or stress), Q of the mounted lattice, shunt L/C values, and the W/Bi layer thicknesses relative to δ at f.

### 2b. Recovered TBQ layout (Channing, 2026-10-12)
> "The TBQ core was partially embedded in a resonant cavity (bottom) and an ionized wind cavity top."

| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Bottom resonant cavity: neck area A, volume V, effective neck length L_eff | Helmholtz f = (c/2π)√(A/(V L_eff)) | Fluid (air/gas oscillating in the neck), phonons into the core | Grounded (law); cavity–core coupling Plausible-untested | Not measured. Sweep a speaker, find the cavity peak | textbook; [core §7c (Helmholtz)](tungsten_bismuth_core.md) |
| Embedding depth of the core in the cavity | Sets the overlap of the cavity's pressure field with the piezo (pressure → stress → charge, via D = d·T) | Phonons → charge | Plausible-untested | Measure the piezo voltage vs cavity drive | [core §4, §7d](tungsten_bismuth_core.md) |
| Matching cavity f to the lattice thickness-mode f | Resonance matching: f_Helmholtz ≈ (1/2t)√(c/ρ) | Phonons | Plausible-untested (typically very different frequency ranges, kHz vs MHz; values unknown) | — | §2 table above |
| Top ionic-wind cavity: corona current I, gap d, ion mobility μ_ion | EHD thrust F ≈ I·d/μ_ion (1-D textbook estimate) | Charge (ions) → fluid (air) | Grounded (law); 6.25–50 N/kW observed elsewhere | Bench 1 (lift doc): thrust vs W | [lift §4](lift_and_equilibrium_systems.md) |
| Top-cavity voltage | Corona onset; HV safety | Charge | Grounded | — | [lift §4, bench 1](lift_and_equilibrium_systems.md) |
| Ion wind near the W/Bi/quartz surface | Surface charging, ozone; heat removal by forced convection | Charge, heat, fluid | Plausible-untested | — | — |

**Unknowns (recovered TBQ layout):** cavity A, V and L_eff; embedding depth; corona voltage, current and gap; electrode geometry; whether the cavity drives the lattice or the lattice drives the cavity.

## 3. Tungsten–Bismuth core: materials, plasma, diagnostics
Source: [tungsten_bismuth_core.md](tungsten_bismuth_core.md). Section numbers (§) refer to that file.

### 3a. Tungsten shell: heat and induced current
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| W thermal conductivity k(T) (~174 W/m·K at room temperature, falling to ~100–120 W/m·K near 1000 °C) | Fourier: q = −k∇T | Heat (conduction through the shell) | Grounded | Not measured here. Bench 3: heat a W rod, log T, fit k(T) | §1, §9 |
| W shell thickness / temperature gradient ∇T | q = −k∇T (heat flux is set by the gradient and the thickness) | Heat | Grounded | — | §1 |
| W operating temperature | ρ(T) rises with temperature, so δ grows; k(T) falls | Heat, charge | Grounded | — | §1, §7a-math |
| W resistivity ρ ≈ 5.6×10⁻⁸ Ω·m × drive frequency f | Skin depth δ = √(ρ/(πfμ₀)) = √(2/(ωμσ)): ~3.8 mm at 1 kHz, ~0.12 mm at 1 MHz | Charge (induced eddy current confined to depth δ), field | Grounded (calculated) | Calculated only. Coil-impedance sweep (§7a-inv) | §7a-math |
| He/neutron exposure of the plasma-facing surface | Materials damage (fuzz, embrittlement, transmutation): no single force law | Material degradation | Grounded (phenomenon) | — | §1 |

### 3b. Bismuth layer: diamagnetism and carriers
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Bi volume susceptibility χ ≈ −1.6×10⁻⁴, volume V | Diamagnetic force F = (χV/μ₀) B ∇B (textbook; equivalent to −∇(−χVB²/2μ₀)) | Force on the Bi piece (repulsion from high field); magnetization | Grounded | Bench 2: levitate Bi over NdFeB, measure gap vs field | §2, §9 |
| Field product B∇B of the magnet array | Same F = (χV/μ₀)B∇B; must at least balance ρ_Bi·V·g to lift (textbook) | Force | Grounded | Bench 2 | §2, §7c |
| Bi melting point (~271 °C) vs core temperature | Thermal limit (Fourier heat reaching the Bi layer through the W) | Heat | Grounded | — | §2, §6 |
| Bi resistivity ~1.3×10⁻⁶ Ω·m × f | δ = √(ρ/(πfμ₀)): ~18 mm at 1 kHz, ~0.57 mm at 1 MHz | Charge, field (Bi is far more transparent than W) | Grounded (calculated) | Calculated only | §7a-math |
| Bi carrier density n, effective mass m* | Drude ω_p = √(n e²/(ε₀ m*)) | Charge (free-carrier plasma oscillation, infrared edge) | Grounded | — | §2 |
| Bi nanoparticle size | LSPR resonance condition | Field (optical absorption) | Grounded | Bench 4 (optional): absorption vs size | §2, §9 |
| W–Bi composite fill fraction / layering | Effective-medium mixing for k and permittivity | Heat, field | Plausible-untested | — | §6 |

### 3c. Quartz / piezo partner
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Piezo phase choice (α-quartz, BNT, BiFeO₃; *not* elemental Bi) | Symmetry rule: a centrosymmetric crystal has d = 0. Quartz is point group 32, so d ≠ 0 | Charge ↔ strain | Grounded | — | §0, §7d |
| Quartz d-coefficients (d₁₁, d₁₄ nonzero for class 32; values not in repo) | Direct effect D = d·T + ε^T E; converse S = s^E·T + dᵀE (textbook) | Charge (surface charge from stress); phonons (strain from field) | Grounded (law); values — | Not measured | §7d |
| Shunt L, C | f = 1/(2π√(LC)); piezo shunt damping | Charge (through the shunt) → heat; phonon energy removed | Grounded (mechanical structures); Plausible-untested for a core | Bench 1: Q / ring-down with and without the shunt | §4, §9 |
| Heartbeat frequency and geometry | Mode frequencies of the lattice: no drive law given | Phonons | Speculative (missing) | — | §0, §10 |
| Coherent-phonon excitation | Electron–phonon coupling (pump–probe) | Phonons ↔ charge | Grounded (phenomenon); plasma coupling Plausible-untested / Speculative (only through surface, sheath, wall) | — | §7d |

### 3d. Z-pinch / plasma
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

### 3e. Diagnostics: MT / CSAMT on the core
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Probe frequency sweep (e.g. 1 kHz–1 MHz) | Faraday ∇×E = −∂B/∂t, J = σE, ∇×B = μ₀J; δ sets the probing depth | Charge (induced currents), field | Grounded | — | §7a-math, §7a-csamt |
| Measured E/H at the surface | ρ_a = (1/ωμ₀)\|E/H\|², φ = arg(E/H); E = ZH | Field (impedance data) | Grounded | Not built. Coil sweep + inversion | §7a-math, §7a-inv |
| Inversion trade-off λ, model mesh | Occam Φ = Φ_d + λΦ_m; Gauss–Newton Δm update | Information (layer conductivity) | Grounded (method); Plausible-untested on the core | — | §7a-inv |
| Source–sample distance | Far field only beyond several δ; at bench scale it is near field | Field | Grounded | Use a full coil forward model | §7a-csamt |
| Telluric / geomagnetic tuning | mV/km natural fields | Charge | Speculative (for tuning) | — | §7a |
| Toroidal "photon chase", phi standing waves | No force law given | — | Speculative / Symbolic | — | §7, §8 |

## 4. POL lift: eddy currents, EDS, Halbach
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
| Quasi-zero-stiffness stage (cf. CN121142094A) | Positive + negative stiffness offset → k_net ≈ 0, so displacement per force is large | Force sensing; field (tuned by soft-iron gap) | Plausible-untested for POL | — | prior-art note below |
| Ferritic steel (early hoverboard) | Ferromagnetic attraction; flux path / back-iron; EMS-style (needs feedback) | Field (flux guided), force (attractive) | Grounded (physics); role: perforated-screen back-iron (confirmed) | — | Channing 2026-10-12 |

**Related prior art (comparison, not legal advice).** CN121142094A is a diamagnetic-levitation accelerometer with a quasi-zero-stiffness structure: a Bi disc plus pyrolytic graphite levitated over a permanent-magnet array, with field tuning by moving soft iron. Channing says it is closer to the hoverboard (POL) design than to the TBQ core. Takeaway: quasi-zero stiffness means positive and negative stiffness cancel, leaving near-zero restoring stiffness and so high force/displacement sensitivity. That is a possible idea for the POL height-control loop as a sensitive gap/load sensor or a soft stage (**Plausible-untested**). Link: https://patents.google.com/patent/CN121142094A/en

**Recovered detail (Channing, 2026-10-12): "we used ferritic steel as well"** in the early hoverboard design. Ferritic steel is ferromagnetic: it is *attracted* to fields, serves as a flux path or back-iron, and gives EMS-style attraction (unstable without feedback, per Earnshaw). That contrasts with diamagnetic Bi/graphite, which is *repelled* and passively stable. **Grounded** physics. Its role: used as **back-iron in the form of perforated screens** (Channing confirmed, 2026-10-12).

**Perforated ferritic-steel back-iron screens: mapping** (physics **Grounded**; benefit for POL **Plausible-untested**):
- **Perforation pattern (hole size, pitch, open-area fraction, thickness) → mass.** Mass scales with (1 − open fraction) × thickness, so it is lower than a solid plate.
- **→ eddy currents.** Holes interrupt the current loops, giving shorter paths and less eddy loss than a solid plate (loss also scales with thickness relative to skin depth).
- **→ flux guiding.** Guiding is partial. Effective permeability falls with open fraction, so the screen carries less flux than solid back-iron of the same thickness.
- **→ airflow.** Air passes through the holes, which helps cooling and ties to the ion-wind/air-flow paths (§5 ionic wind).
- **→ saturation.** Thin webs between holes concentrate flux and can saturate locally, which limits how much flux the screen can carry.
- **Unknowns:** hole size, pitch, open area %, thickness, steel grade.


## 5. Buoyancy, Lorentz, ionic wind
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Envelope gas volume V, gas density | Archimedes F = (ρ_air − ρ_gas)gV (≈10.4 N/m³ for He) | Fluid (displaced air) | Grounded | Bench 1 (balloon trim) | [lift §1](lift_and_equilibrium_systems.md) |
| Conductor current I, length L, local B | F = q(E + v×B); F = IL×B; net external force needs an external field or medium | Charge; force | Grounded | — | [lift §2](lift_and_equilibrium_systems.md) |
| Corona voltage / electrode geometry | Electroaerodynamic thrust: 6.25 N/kW (aircraft) to ~50 N/kW (lab) | Charge (ions) → fluid (air) | Grounded; integration Plausible-untested | Bench 1: trim N vs W | [lift §4](lift_and_equilibrium_systems.md) |
| Coulomb egg charge (5 cm, 10 kV → ~5.6×10⁻⁸ C) | Coulomb; gyroscopic torque | Charge; torque, not lift | Grounded / Speculative for lift | Bench 5 (resonance transfer) | [lift §7](lift_and_equilibrium_systems.md) |

## 6. Multi-Egg / Elliptical Eye, ponderomotive, Maxwell stress
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Field gradient ∇⟨E²⟩, frequency ω | Ponderomotive F_p = −(e²/4mω²)∇⟨E²⟩ | Charge (electrons expelled from strong-field regions) | Grounded; free-air Newton lift Speculative | Prediction: depletion ∝ 1/ω² | [em_topo Dive A](em_topological_gravity_review.md) |
| Focus field strength (E, B at the foci) | Maxwell stress T_ij = ε₀(E_iE_j − ½δ_ijE²) + (1/μ₀)(B_iB_j − ½δ_ijB²); magnetic pressure B²/2μ₀ | Field momentum → force on boundaries | Grounded | — | [em_topo](em_topological_gravity_review.md) |
| Lens index profile | Luneburg n(r) = √(2 − (r/R)²) | Field (rays focused) | Grounded | — | [em_topo](em_topological_gravity_review.md) |
| Egg spin / eddy springs (C8) | Gyroscopic torque vs Lenz damping | Torque; charge → heat | Grounded (each); which dominates is open | — | [C1-C12](C1-C12_seed_map.md), [butterfly_node](butterfly_node.md) |
| Magnet/ferrofluid near copper (Butterfly-Node) | Lenz: velocity-proportional damping | Charge → heat | Grounded | Planned: copper control "to measure" | [butterfly_node](butterfly_node.md) |
| Multi-Egg rotors as gravity source | None ("gyro = torque not F_z") | — | Speculative | — | [em_topo](em_topological_gravity_review.md) |

## 7. Acoustic streaming and centrifugal buoyancy
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

## 8. Fluid loops: Tesla valves, fluidic RLC, ferrofluid, dual-oil
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

## 9. Mycelium skins and materials
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Mycelium composite k (0.04–0.08 W/m·K; Bath 0.0415) | Fourier q = −k∇T | Heat | Grounded (measured in literature) | Literature values | [mycelium_uses](mycelium_uses.md) |
| Porosity / hyphal structure | Acoustic absorption | Phonons (sound) → heat | Grounded | — | [mycelium_uses](mycelium_uses.md), [core §7c](tungsten_bismuth_core.md) |
| Helmholtz cavity in the skin | Acoustic pressure → stress → piezo charge | Fluid (pressure) → charge | Grounded components; Plausible-untested hybrid | — | [core §7c](tungsten_bismuth_core.md) |
| Ultrasound alignment during growth | Claimed to raise the chitin/cellulose d-coefficient | Phonons → charge | Plausible-untested | — | [core §7c](tungsten_bismuth_core.md) |
| Coil-former dielectric loss at 13.56 MHz / kHz | Dielectric heating | Heat | Plausible-untested | Check loss and moisture | [mycelium_uses](mycelium_uses.md) |

## 10. Wireless power, Casimir, plasma bench, reefs, Schumann
| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Coil Q, coupling, alignment | Coupled-mode resonant transfer (up to ~98.5 % at 11–20 kW) | Charge/field (near field) | Grounded | Bench: two-coil efficiency vs distance | [em_topo L6](em_topological_gravity_review.md), [ANALYSIS](ANALYSIS_2026-10-12.md) |
| Plate gap d | Casimir P = −π²ħc/(240d⁴) | Field (zero-point) → force | Grounded | — | [em_topo Casimir](em_topological_gravity_review.md) |
| Atom–wall distance z, polarizability α | U = −3ħcα/(8πz⁴) (retarded); F = −dU/dz | Force | Grounded | — | [em_topo Casimir](em_topological_gravity_review.md) |
| Ship net charge q, mass m; ambient filament B (~30–60 nG) | Cyclotron f = qB/(2πm) (~10⁻¹⁶ Hz for 1 C, 10 t); gyration along B | Charge → (negligible) force | Particles along B Grounded; cyclotron/magnetron "filament riding" of a ship Speculative/misapplied | Bench: e/m tube / electron beam in Helmholtz coils | [em_topo L5b](em_topological_gravity_review.md#l5b-filament-riding-casimir-resonance-chamber--quartz-tuning-grok-excerpt-recovered-2026-10-15) |
| Sail loop current / tether voltage (magsail, E-sail) | Plasma-flow deflection: magsail ~0.01 m/s² at 1 AU (Zubrin & Andrews); E-sail ~1 N per ~2,000 km tether (Janhunen) | Plasma momentum → thrust | Plausible-untested (solar wind); ~nil in intercluster filaments | Not flown at full scale | [em_topo L5b](em_topological_gravity_review.md#l5b-filament-riding-casimir-resonance-chamber--quartz-tuning-grok-excerpt-recovered-2026-10-15) |
| Casimir gap d; "resonance chamber"; quartz tuning | Static Casimir u ≈ −4×10⁻⁴ J/m³ at 1 μm; dynamical Casimir photons from pump energy (Wilson 2011); warp needs ≫ (Pfenning & Ford 1997) | Field (zero-point) | Casimir Grounded (tiny); recycling vacuum / warp bubble Speculative; quartz Q 10⁴–10⁶ Grounded | Bench: quartz Q / phase noise near plates (expect null) | [em_topo L5b](em_topological_gravity_review.md#l5b-filament-riding-casimir-resonance-chamber--quartz-tuning-grok-excerpt-recovered-2026-10-15) |
| Trim-coil set; planet↔space mode switch | Shim/trim fields correct a main field (Juchem & de Graaf 2017); near-surface EDS/ionic trim vs vacuum (no air, no conductor) | Field shaping; torque vs external B | Trim coils Grounded; switching concept Plausible-untested; design [Channing to supply] | — | [em_topo L5c](em_topological_gravity_review.md#l5c-to-recreate-planet-to-space-mode-switching-trimming-coils--aligning-in-the-magnetosphere) |
| Coil dipole m in Earth's field (25–65 μT surface, ∝1/r³) | Magnetorquer τ = m × B (no torque about B) | Torque (attitude), not thrust | Attitude alignment Grounded; magnetospheric propulsion Speculative | Bench: coil on air bearing / torsion fibre in Helmholtz field | [em_topo L5c](em_topological_gravity_review.md#l5c-to-recreate-planet-to-space-mode-switching-trimming-coils--aligning-in-the-magnetosphere) |
| Anode bias, gas pressure | Double-layer threshold ∝ 1/P + C (Baalrud 2009) | Charge (plasma bubble) | Grounded (prediction) | Dusty-plasma bench | [dusty_plasma_bench](dusty_plasma_bench.md) |
| Reef crest geometry | Wave breaking/friction: 86 % energy at the crest, 97 % whole reef | Fluid (wave energy) → heat | Grounded | Meta-analysis | [coral_wave_barriers](coral_wave_barriers.md) |
| Earth–ionosphere cavity radius | f_n = (c/2πR)√(n(n+1)) | Field | Grounded | — | [bioelectric_coupling](bioelectric_coupling.md) |
| EZ water / H₃O₂ | None measured | — | Speculative / debated | Bench 4: EZ vs ion concentration | [lift §5](lift_and_equilibrium_systems.md) |

## 11. POL v0.1 zone images (AI concept art, 2026-10-12)
Source: [pol_v0_1_zones.md](pol_v0_1_zones.md). The labels in these images are AI art, not measurements.

| Design parameter | Governing force / equation | Resulting flow | Status | Measured? / bench test | Source |
|---|---|---|---|---|---|
| Larmor "clock" field B₀ and spin sample | f = γB/2π (needs a polarized spin ensemble + pickup) | Magnetization (precession) → induced charge in pickup | Grounded (law); clock role Plausible-untested; "φ-stable" Speculative | — | [zone 1](pol_v0_1_zones.md#1-larmor-precession-clock-zone) |
| Coil current / resistance (hot zones) | Joule heating P = I²R (not "Lorentz heating"); q = −k∇T | Heat | Grounded; >400 K flagged (mycelium damage) | IR thermometer on the coil plate | [zone 2](pol_v0_1_zones.md#2-thermal-polarity-zones) |
| Peripheral "cold zones" | No sub-ambient cooling without a heat pump; cooler periphery only | Heat | Relabeled (was "adiabatic") | — | [zone 2](pol_v0_1_zones.md#2-thermal-polarity-zones) |
| hBN sheet orientation and thickness | Anisotropic Fourier conduction: k_in-plane ≫ k_through | Heat (lateral spreading) | Grounded; ~600 W/m·K upper bound flagged | — | [zone 3](pol_v0_1_zones.md#3-bn-heat-spreading-layers) |
| Mycelium-hemp density (~0.65 g/cm³ per image) and liveness | Mass budget (buoyancy/lift); living growth for repair | Mass; biological (repair) | Plausible-untested | — | [zone 4](pol_v0_1_zones.md#4-mycelium-hemp-structural-envelope) |
| Amide interface (functionalized BN ↔ chitosan/–NH₂) | Covalent bonding; interface shear strength | Stress (load transfer) | Plausible-untested; 4.8 eV/bond unverified | Lap-shear test | [zone 5](pol_v0_1_zones.md#5-amide-bond-interface) |
| Coil ω vs conductive plane δ | P/F ≥ ωδ | Charge (eddy) → heat; lift | Grounded (hard constraint) | Al-plate bench (ANALYSIS) | [zone 6](pol_v0_1_zones.md#6-eddy-current-lift-field) |
| Micro Tesla-valve channels | Diodicity at Re ≳ 200; small at micro/low Re | Fluid | Grounded; Optional; lift claim Speculative | — | [zone 7](pol_v0_1_zones.md#7-micro-tesla-valve--density-accents-optional) |
| CNT–graphene transition zone (pillar spacing, junction quality) | Fourier conduction in 3D network; limited by interface (Kapitza) resistance | Heat, charge | Grounded (materials); Plausible-untested in POL | — | [stacks](pol_v0_1_zones.md#possible-material-stacks-reconstructed-from-channings-memory-2026-10-12-replace-if-original-found) |
| He pressure ratio p₂/p₁ (piezo-driven cycle) | Adiabatic T₂/T₁ = (p₂/p₁)^((γ−1)/γ), γ = 5/3; active cycle pumps heat with work input | Heat (pumped), fluid (gas oscillation) | Grounded (Stirling/pulse-tube/thermoacoustic); Plausible-untested in POL | — | [stacks](pol_v0_1_zones.md#possible-material-stacks-reconstructed-from-channings-memory-2026-10-12-replace-if-original-found) |
| Diamond sheet thickness | q = −k∇T, k ~2000 W/m·K | Heat (spreading) | Grounded | — | same |
| Perimeter piezo-He loop alternating diamond/quartz sections ("bouncing") | Acoustic/thermal reflection and transmission at impedance steps; diamond spreads heat, quartz drives | Heat, phonons, fluid (He) around the outer edge: controlled leaky boundary. Originally labeled "multipurpose and a protection layer" (cooling, guard, leaky-boundary control) | Guard loop Plausible-untested; field "leaky boundary" analogy Speculative | — | same; [R6](em_topological_gravity_review.md) |
| Bi cavity | Diamagnetic F = (χV/μ₀)B∇B; melts ~271 °C | Force, field | Grounded; role unconfirmed | — | same |
| He containment material | Permeation/leak rate | Fluid (He loss) | Grounded (issue) | Leak-rate test | same |
| Water circulation rpm, radius (He–water loop) | Centrifugal buoyancy; Δp(wall−axis) = ½ρω²r² (axis lowest) | Fluid (He to core, water outward); He expands at core, not compresses | Grounded (physics); Plausible-untested in POL; "compress to center" contradicted | Spinning-cylinder bench, axis vs wall taps | [helium_water_circulation](helium_water_circulation.md) |
| External heating of rotating He–water loop (power, location, rpm) | Rotating convection; Taylor–Proudman; Ro = U/ΩL, E = ν/ΩL², Ra = gαΔTL³/νκ | Fluid (convection vs vortex; bands/jets if locked), heat | Grounded (physics); band-locking Plausible-untested | Rotating tank + heating ring, map (Ro, Ra) | [helium_water_circulation §7](helium_water_circulation.md) |
| Spring check/relief valve (preload, seat area) | Cracking Δp = preload/area | Fluid (one-way above threshold; seat leak, hysteresis) | Grounded | — | [He–water §8](helium_water_circulation.md) |
| Tesla diode in water loop (geometry, Re) | Inertial separation; Di ≈ 2 at Re 300–1500 (Nguyen 2021) | Fluid (rectified oscillating flow; no seal) | Grounded | Diodicity bench: Δp fwd vs rev at fixed Q | [He–water §8](helium_water_circulation.md) |
| Piezo active valve (stroke, timing vs drive phase) | Piezo force/stroke; phase-locked actuation | Fluid (hard seal on command) | Grounded tech; sync Plausible-untested | — | [He–water §8](helium_water_circulation.md) |
| Orifice + inertance tube + reservoir (He loop) | Fluidic R–L–C; phase between pressure and mass flow (~60° lag target) | Fluid (He oscillation), heat (pumped) | Grounded (pulse tubes); Plausible-untested in POL | — | [He–water §8](helium_water_circulation.md) |
| Sinks in ferrofluid/water/CBD/air loops with a Tesla coil opposite; Tesla valves gate inflow + separated return (sink volume, coil distance, f, modulation) | Kelvin force μ₀(M·∇)H on ferrofluid (weak at 50 kHz–MHz: relaxation → heating; solid-state transistor-driven coil + interrupter envelope Hz–~1 kHz gives pulsed force, carrier still heats; envelope sync to heartbeat Plausible-untested); separated return routed to outer perimeter He loop: closes thermal loop (coil heats sink → perimeter He absorbs), cooler fluid denser and ferrofluid M higher → faster resettling (Grounded physics, net Plausible-untested); water phase change near the cold perimeter as a thermal buffer: latent heat 334 kJ/kg fusion (vs 4.18 kJ/kg·K) clamps T near 0 °C, or 2260 kJ/kg vaporization; caveats: 9 % ice expansion jams valves, ferrofluid destabilizes on freezing, slurry option; which phase shift [Channing to clarify]; Plausible-untested; buoyancy separates air; density layers water/oil; diodicity under pulsatile flow | Fluid (gated inflow, separation, rejoining main path), heat (HF loss) | Valves/separation Grounded; coil force on ferrofluid Plausible-untested (frequency flag); EM-reconnection reading Speculative (footnote) | — | [He–water §9](helium_water_circulation.md) |
| Hub-to-rim topology: gyroscopic eggs → radial paths → branch sinks → perimeter He loop (egg ω, radius) | Centrifugal pumping dp/dr = ρω²r; egg friction/Ekman dissipation heat rejected at rim | Fluid (hub-to-rim circulation), heat (hub → rim) | Grounded physics; Plausible-untested | — | [He–water §10](helium_water_circulation.md) |
| Electrolyte in loops (σ, concentration, B, electrodes) | Lorentz f = J×B (MHD pump, Yamato-1); induced currents → Joule J²/σ | Fluid, charge, heat; gas (H₂/O₂) at electrodes | Grounded physics; Plausible-untested; corrosion, ferrofluid destabilization, freezing-point shift | — | [He–water §10](helium_water_circulation.md) |
| Loop liners for salt/electrolyte: hBN (hot sinks) vs PP film (cool runs) | Corrosion/scale barrier; Fourier heat path (hBN high in-plane k vs PP ~0.1–0.2 W/m·K); He permeation through PP | Heat, fluid (containment), charge (insulating) | Grounded properties; placement Plausible-untested; BeO recall ruled out (toxic); BOM [Channing to supply from Grok BOM] | — | [He–water §10c](helium_water_circulation.md) |
| Castor oil as oil-based ferrofluid carrier separate from brine (μ, T, channel D, U) | Immiscibility; Kelvin force on carried particles; Re = ρUD/μ ≈ 0.7 at 5 mm, 0.1 m/s (μ ≈ 0.7 Pa·s) ≪ Tesla turn-on Re ≈ 100–300 | Fluid (ferrofluid phase), no electrolysis/corrosion | Grounded properties; role Plausible-untested; brine recipe [Channing to supply] | — | [He–water §10d](helium_water_circulation.md) |
| Bubble gas volume vs depth (transmedium craft) | F_b = ρ V_disp g; Boyle pV = const (≈1 atm per 10 m) | Fluid (displacement), gas compression | Grounded; depth-dependent control | — | [bubbles_arcs_frc](bubbles_arcs_frc.md) |
| Microbubble / air-layer injection (gas flux, bubble size) | Turbulent boundary-layer modification; air-layer lubrication (Ceccio 2010) | Fluid (skin-friction drag ↓; up to ~80 % lab, much less at scale) | Grounded (lab); Plausible-untested on craft | — | [bubbles_arcs_frc](bubbles_arcs_frc.md) |
| Magnetic arcs / mirrors near bubbles | Mirror force on charged particles only; bubbles steerable only via ferrofluid (magnetic hole) or MHD J×B in electrolyte | Charge (ions); fluid indirectly | Correction; Plausible-untested | — | [bubbles_arcs_frc](bubbles_arcs_frc.md) |
| FRC plasmoid (s-parameter, shaping, end bias, NBI) | Kinetic stabilization at low s; tilt n=1 / rotational n=2 control (Steinhauer 2011; Binderbauer 2015) | Charge/plasma, field (closed poloidal flux) | Grounded (physics); craft use Plausible-untested (needs vacuum) | — | [bubbles_arcs_frc](bubbles_arcs_frc.md) |
| B₄C surface treatment (valve seats, sink inlets) | Hardness/wear and cavitation-erosion resistance | Fluid (brine erosion resisted) | Grounded properties; role Plausible-untested | — | [He–water §10e](helium_water_circulation.md) |
| Carboxyl (–COOH) binding chemistry | Covalent/coordination anchoring (amide/ester to chitosan; carboxylate to Fe-oxide; GO edges) | Stress (interface load transfer) | Grounded chemistry; role Plausible-untested | — | [He–water §10e](helium_water_circulation.md) |
| Terpenes (sealant/solvent/antimicrobial) | Hydrophobicity, interfacial tension | Fluid (interface), biological | Grounded properties; role Plausible-untested; next step [Channing to supply] | — | [He–water §10e](helium_water_circulation.md) |
| Mycelium condensation pore leak + frequency (pore r, f) | Capillary condensation (Kelvin equation); acoustic droplet coalescence | Fluid (water vapor → liquid entry) | Grounded analogs; frequency role Plausible-untested; values [Channing to supply] | — | [He–water §10e](helium_water_circulation.md) |
| Water cavitation transition, "riding the well" (p, v, geometry) | Cavitation number σ = (p − p_v)/(½ρv²) near inception; supercavitation drag reduction; collapse erosion | Fluid (liquid ↔ vapor), phonons (collapse shocks) | Grounded metric; operating at threshold Plausible-untested; "dovetail" [Channing to clarify] (cf. C7, R6) | — | [He–water §10e](helium_water_circulation.md) |
| Patterned hull wettability (hydrophobic tracks, hydrophilic trailing edge) | Surface-energy / Laplace-pressure gradients; plastron air layers (Song 2019; Zhu 2020) | Fluid (gas bubbles guided along hull and shed) | Grounded (lab); craft use Plausible-untested; corrects "hydrophilic carries bubbles" | — | [He–water §10e](helium_water_circulation.md) |
| Electrolysis filtering + O₂ life support (cell current, electrodes) | Faraday electrolysis; electrocoagulation | Charge → chemistry; fluid (cleaned water), gas (O₂, H₂) | Grounded (ISS OGA, submarines); integration Plausible-untested | — | [He–water §10f](helium_water_circulation.md) |
| H₂ lift gas for ascent / underwater buoyancy cells | F_b = (ρ_medium − ρ_H₂)gV (≈1.14 vs He ≈1.06 kg/m³ in air); Boyle compression with depth; ~50 kWh/kg H₂ | Fluid (displacement), gas | Grounded; hazards: 4–75 % flammable, permeation, ferritic-steel embrittlement | — | [He–water §10f](helium_water_circulation.md) |
| Living mycelium skin vs cured (melanized strain?) | Growth/repair (living only); radiation attenuation ~2 % per ~1.7 mm C. sphaerospermum (Averesch 2022) | Biological; radiation (particles) | Grounded (small effect); shielding claims overstated; self-repair Plausible-untested | ISS data (literature) | [living_habitat](living_habitat_life_support.md) |
| Ice / cyanobacteria / mycelium layered shell (NASA mycotecture) | Photosynthesis O₂/CO₂ exchange; water shielding | Gas (O₂, CO₂), water, radiation | Grounded concept (NASA); craft closed loop Plausible-untested | — | [living_habitat](living_habitat_life_support.md) |
| Cabin vibration platform (f ~20–90 Hz, ~0.3 g; purr-inspired 25–150 Hz) | Mechanical loading → bone anabolic signal (Rubin 2001); avoid 4–8 Hz whole-body resonance (ISO 2631) | Phonons/mechanical vibration into the body | LMHF Grounded research (mixed in humans); purr-healing Plausible-untested | — | [living_habitat](living_habitat_life_support.md) |
| Electrolyzer stack (PEM/alkaline, partial load) fed from mycelium loop | Faraday electrolysis; DI bed before stack; rotary H₂/water separation (ISS OGA) | Charge → O₂, H₂; fluid (water) | Grounded (ISS OGA); bio-fed feedwater Plausible-untested | — | [living_habitat §Electrolysis](living_habitat_life_support.md) |
| Co–MnO on carbonized mycelium catalyst | HER/OER overpotentials (105 mV @10, 250 mV @50 mA/cm², 1.61 V cell; Li et al. 2026) | Charge → gas | Grounded (lab, alkaline); craft use Plausible-untested; space durability Speculative | — | [living_habitat §Electrolysis](living_habitat_life_support.md) |
| Silver-ion biocide dosing (~200–400 ppb) | Electrolytic Ag⁺ release | Chemistry (microbial control) | Grounded (Russian segment; NASA development) | — | [living_habitat §Electrolysis](living_habitat_life_support.md) |
| Sabatier (H₂ + CO₂) | CO₂ + 4H₂ → CH₄ + 2H₂O | Gas → water recovery | Grounded (ISS since 2010) | — | [living_habitat §Electrolysis](living_habitat_life_support.md) |
| Sodium acetate (electrolyte / buffer / trihydrate PCM) | Buffer pKa 4.76; PCM melt ~58 °C, ~250–265 kJ/kg, supercooling; Na⁺ exchange poisons PEM | Heat (warm-side store), charge (ionic conduction), biological (deliberate mycelium carbon feed, confirmed) | Grounded properties; feed use confirmed; dosing control Plausible-untested; "ionic bonding" [Channing to clarify] | — | [living_habitat §Na acetate](living_habitat_life_support.md) |
| Copper feed tubing for acetate (multipurpose) | k ≈ 400 W/m·K heat path; oligodynamic antimicrobial; conductor; Cu²⁺ leaching (fungitoxic), acetate corrosion, galvanic couples | Fluid (feed), heat, charge | Grounded properties; use recalled; roles [Channing to supply]; Plausible-untested | — | [living_habitat §Na acetate](living_habitat_life_support.md) |
| Living vs non-living zoning (barriers, return paths) | Separation of fungitoxic/biocidal materials from fed mycelium | Biological, fluid (separated returns) | Recalled design fact; Plausible-untested | — | [living_habitat §zones](living_habitat_life_support.md) |
| Petrified / mineralized tubes (MICP, fungal or silica mineralization) | Biomineral precipitation (CaCO₃); scaling vs wall shear; acid/acetate dissolution | Fluid (channel flow; bore narrows with deposits) | Grounded analogs; designed branches Plausible-untested | — | [living_habitat §zones](living_habitat_life_support.md) |
| MICP ammonium (NH₄⁺) used for work | Ionic conduction (J×B, conductivity); N nutrient; NH₃ fuel/H₂ carrier; NH₄⁺/NH₃ pKa 9.25 | Charge, biological (nutrient), chemistry | Grounded pieces; new open thread; charge-separation use Speculative | — | [living_habitat §zones](living_habitat_life_support.md) |
| Periodic H₂O₂ flush (non-living zones) | Oxidation (biocide, descaling); 2H₂O₂ → 2H₂O + O₂ (Cu-catalyzed) | Chemistry; gas (O₂ bubbles) | Grounded; protocol Plausible-untested; avoid living zones and copper | — | [living_habitat §zones](living_habitat_life_support.md) |
| Copper mandrels for petrified branch panels, removed before install, then BN coat | Template mineralization; mold release; coating adhesion | Fluid (final channel geometry), structure | Recalled decision; resolves Cu conflicts; process Plausible-untested | — | [living_habitat §zones](living_habitat_life_support.md) |
| Ion set for mineral transport (Ca²⁺ + K⁺; Mg²⁺; K citrate; K phosphate; Be ruled out) | Ion transport and precipitation (CaCO₃; Ca-phosphate and struvite with Mg/NH₄/PO₄) | Charge, fluid (mineral deposition) | Open, never settled | — | [living_habitat §zones](living_habitat_life_support.md) |
| Potassium citrate (post-formation flush) | Chelation of Ca²⁺/Mg²⁺: scale inhibition; also inhibits calcite (conflicts with MICP) | Chemistry; fluid (bore kept clear) | Grounded; flush use Plausible-untested | — | [living_habitat §zones](living_habitat_life_support.md) |
| Potassium phosphate (buffer, P+K nutrient) | pH buffering; precipitation as Ca-phosphate / struvite (with NH₄⁺) | Biological (nutrient); fluid (scaling risk) | Grounded; scaling risk | — | [living_habitat §zones](living_habitat_life_support.md) |
| Permanganate (MnO₄⁻, KMnO₄) + zinc oxide (ZnO: white residue, fungitoxic) | MnO₄⁻: strong oxidizer/disinfectant, reduces to MnO₂ deposits, violent with conc. H₂O₂/organics, toxic to living mycelium; Mn: peroxidase cofactor; Zn: antimicrobial, scale/corrosion inhibition | Biological, chemistry, fluid (deposits vs inhibition) | Grounded properties; roles Open | — | [living_habitat §zones](living_habitat_life_support.md) |
| Potassium "carry out and repel" calcium strategy | Chelation, K⁺/Ca²⁺ ion exchange, charged-surface anti-scaling | Charge, fluid (Ca kept in solution / removed) | Grounded analogs; "repel" Plausible-untested; flushing still needed; Open, never closed | — | [living_habitat §zones](living_habitat_life_support.md) |
| Phospholipid layers / lecithin liposomes | Bilayer self-assembly; phosphorylcholine antifouling; Ca²⁺ headgroup bridging; oxidation | Fluid (slip, antifouling), charge/nutrient carriage | Grounded properties; roles Plausible-untested; led into ion-exchange resin with potassium (Ca²⁺ ↔ K⁺, KCl-regenerated; resolved) | — | [living_habitat §zones](living_habitat_life_support.md) |
| Oils for beading-type transport / slippery liners (castor: iron self-organizing; CBD: bulk conductivity unsupported (no studies found; oils insulate); CBD modulates biological Na⁺ channels and bilayer elasticity (Grounded, SFU Canada); transport only via additives/water/interfaces; thread moved to receptor sites (CB1 NAM, TRPV1, 5-HT1A, GPR55, PPARγ; Grounded biology), RGRF role: speculative communication through living/non-living layers; no studies found, dropped) | Oil-infused slippery surfaces (SLIPS, Wong 2011): low adhesion, scale/fouling resistance; lubricant washout | Fluid (bead/droplet carriage, easy flush) | Noted, never applied; Plausible-untested | — | [living_habitat §zones](living_habitat_life_support.md) |
| Mycelium electrical spiking read by CNT node electrodes (stress signaling) | Fungal extracellular potential spikes, 0.03–2.1 mV over 1–21 h (Adamatzky 2022); differential electrode readout | Charge / bio-signal → stress feedback; nodes concentrated in Tesla-coil perturbation zones; spike → Na acetate dosing for self-healing (living zones); infeasible zones fall back to cured borax/BN, flush and replace, which zones [Channing to supply] | Spiking Grounded; CNT node readout and spike→acetate loop Plausible-untested; zone densification over time Speculative; in use in design | Not measured; bench test: CNT vs needle electrodes on colonized panel under a stress stimulus; node spacing [Channing to supply] | [living_habitat_life_support.md (g)](living_habitat_life_support.md) |
| Strain genotype × crosslinker (S. commune) | Nuclear–mitochondrial genotype and crosslinker set film modulus/elongation (Whabi & Xu 2025) | Stress/strain response of film | Grounded (films); POL Plausible-untested | Not measured for POL | [living_habitat_life_support.md (levers)](living_habitat_life_support.md) |
| Nutrient-patterned aerial hyphae (node placement) | Local nutrient supply → directed hyphal growth (Li et al., Sci. Adv. 2026) | Biomass/new nodes where dosed | Grounded (textile); craft/POL Plausible-untested | Not measured | [living_habitat_life_support.md (levers)](living_habitat_life_support.md) |
| Hot-press densification / targeted high-stress nodes | Collapse of free volume → more contact points → stiffness | Load paths; damping | Direction Grounded; POL 420–480 kg/m³ / 2.1–2.8 MPa Plausible-untested | Gap: node topology → damping (micro-CT + cyclic/DMA test). Refs: Sun et al. 2022 (hot-press, Maine/FPL); MSU Viles…Heveran 2025 (mineralized mycelium architectures, moderate match); MSU attribution [Channing to clarify which items] | [living_habitat_life_support.md (levers)](living_habitat_life_support.md) |
| Substrate choice (Guadua / bamboo fiber, particle size, ratio, growth time) | Substrate nutrition + fiber reinforcement set hyphal density and load transfer | Stress paths; density | Substrate effects Grounded (bamboo-mycelium ~0.05–0.2 MPa as-grown); Guadua–mycelium Plausible-untested (no study found) | Not measured; coupon test Guadua fiber vs hemp hurd, pressed/unpressed | [living_habitat_life_support.md (Substrate: Guadua)](living_habitat_life_support.md) |
| Mechanical load during colonization (static/cyclic compression, bending) | Hyphal mechanosensing (stretch-activated Ca²⁺ channels, thigmotropism); compression → denser, more branched hyphae (F. fomentarius, Mater. Adv. 2025) | Biomass/node density along stress paths | Single-study Grounded (manual compression); cyclic/bending regime Plausible-untested | Not measured; bench test: loaded vs unloaded colonization, micro-CT + modulus | [living_habitat_life_support.md (Mechanical pressure during growth)](living_habitat_life_support.md) |
| Microtubule state (stabilized vs not) under anesthetic | Isoflurane binding to MTs; MT stabilizer delays LORR by 69 s (Khan 2024); exciton migration 6.6→5.8 nm with isoflurane (Kalra 2023) | Excitation energy (phonons/excitons), neural function | MT as anesthetic target Plausible (weak support); Orch-OR consciousness Speculative | Rat study N=8; replication needed | [consciousness_fields.md §1](consciousness_fields.md) |
| Red/NIR light dose on mitochondria (wavelength, irradiance) | Photon absorption by respiratory chromophores (CCO contested) → ATP/ROS/NO | Charge (electron transport), chemical energy | PBM effect Grounded; CCO mechanism contested; habitat use Plausible-untested | Not measured in RGRF | [consciousness_fields.md §2](consciousness_fields.md) |
| "Informed" neutrinos / collective-consciousness fields | No known coupling (neutrino cross-section negligible; no-signalling) | None demonstrated | Speculative / Symbolic | — | [consciousness_fields.md §3](consciousness_fields.md) |
| Vagal tone / HRV (crew interoception) | Vagal efferent control of heart (RSA/HRV as index); polyvagal ventral/dorsal hierarchy contested (Grossman 2023) | Neural signal, heart rhythm | Vagus/HRV/interoception Grounded; polyvagal hierarchy contested; RGRF role [Channing to supply] | Not measured; possible HRV monitor with cabin-vibration item | [consciousness_fields.md §3b](consciousness_fields.md) |
| Chronic negative affect (stagnant stress) | Allostatic load (McEwen 1998); GR resistance → cytokines (Cohen 2012); inflammation↔mood (Miller & Raison 2016) | Hormonal/immune signaling | Grounded; "written into fascia / readable map" Speculative | Biomarkers (CRP, IL-6, HRV) measurable | [consciousness_fields.md §3c](consciousness_fields.md) |
| Heart field as "resonant carrier"; pineal receiver | Magnetocardiography pT, ∝1/r³ near body; pineal calcite exists (Baconnier 2002) | Magnetic field (weak, local) | Field Grounded; interpersonal carrier / pineal antenna Speculative; coherence framework Symbolic | — | [consciousness_fields.md §3d](consciousness_fields.md) |
| Stress / disease VOCs (incl. aromatics: indole, benzaldehyde, toluene) | Molecular diffusion of volatiles → olfactory receptor binding (dogs ~ppt; Wilson 2022 93.75 % stress discrimination); human fear chemosignals (de Groot 2012) | Chemical (volatile molecules) → electrical (GPCR→G_olf→cAMP→CNG→spike; Buck & Axel 1991); aromatic π-electron UV absorption | Grounded; vibrational (Turin) theory Speculative/contested (Keller & Vosshall 2004); cabin VOC sensor and unified chemical→electrical sensing with CNT mycelium readout Plausible-untested | Not measured; e-nose/GC-IMS bench | [consciousness_fields.md §3e](consciousness_fields.md) |
| Breath rate / bodily anchors in practice (intent as alignment) | Slow breathing (<10/min) → ↑HRV/RSA, vagal activity (Zaccaro 2018) | Neural/autonomic signal | Grounded; embodied > mental effort Plausible; "field writing" Symbolic | Measurable with HRV monitor | [consciousness_fields.md §3g](consciousness_fields.md) |
| Fingerprint ridge spacing λ | Texture vibration f = v/λ band-pass into Pacinian range (Scheibert 2009) | Mechanical vibration → afferent signal | Grounded; "design feature" Symbolic | — | [consciousness_fields.md §3f](consciousness_fields.md) |
| Regeneration patterning (antler ABPCs, hair-cycle BMP/WNT waves, Vmem patterns) | Stem-cell niche signalling; dermal BMP rhythm (Plikus 2008); membrane-voltage patterning (Levin lab; Xenopus limb, planaria) | Cells/biomass, chemical & bioelectric signals | Biology Grounded; bioelectric control Plausible (model organisms); link to entropic/information fields Speculative/Symbolic; habitat regenerative-zone analogy Plausible-untested | — | [consciousness_fields.md §3h](consciousness_fields.md) |
| Frisson / aesthetic chills (peak engagement) | Striatal dopamine release (Salimpoor 2011); sympathetic → arrector pili piloerection; sympathetic–APM niche activates hair-follicle stem cells (Shwartz 2020, cold) | Neural/autonomic signal → skin conductance, piloerection | Grounded; insight-chills Plausible; "resonance between minds" Speculative | Measurable (skin conductance, piloerection video) | [consciousness_fields.md §3i](consciousness_fields.md) |
| Empathic resonance (vicarious autonomic response, mirror/shared representations) | Physiological linkage (Levenson & Ruef 1992); vicarious SCR → helping (Hein 2011); AI/ACC shared pain network (Singer 2004; Lamm 2011); mirror neurons (di Pellegrino 1992; Mukamel 2010) | Sensory input → neural/autonomic signal (SCR, HR) synchronized between people | Grounded mechanisms; "much higher sympathetic in empathic people" not supported as stated (synchrony > magnitude); mirror-empathy link modest; field-coupling Speculative/Symbolic | Measurable (dyadic SCR/HRV synchrony) | [consciousness_fields.md §3j](consciousness_fields.md) |
| Fascial tone (myofibroblast contraction, sympathetic innervation) | TGF-β1 / Rho-kinase-driven myofibroblast contraction, force ∝ myofibroblast density (Schleip 2019, in vitro; minutes to hours); sympathetic TH+ fibres (Tesarz 2011) | Mechanical tension; afferent interoceptive signal → insula | Innervation and contractility Grounded; sympathetic→fascial stiffness Plausible-untested; myofascial→HRV Plausible (low quality); fascia→empathy Speculative | Shear-wave elastography + HRV under stress (untested) | [consciousness_fields.md §3j](consciousness_fields.md) |
| Epigenetic marks (GR/FKBP5 methylation, HDAC, clocks) | Experience-dependent DNA methylation / histone acetylation sets GR expression and HPA tone (Weaver 2004; McGowan 2009; Klengel 2013); methylation clock (Horvath 2013) | Information (chromatin state) → gene expression → hormonal flow | Mechanisms Grounded; human transgenerational Plausible-contested (Dias & Ressler 2014; Yehuda 2016 critiques); meditation effects Plausible (Kaliman 2014; Chaix 2017/2020) | Measurable (methylation arrays, clocks) | [consciousness_fields.md §3k](consciousness_fields.md) |
| Predator cue → offspring defence/stress | Kairomone-induced maternal defence (Daphnia, Agrawal 1999); maternal glucocorticoid programming (hares, Sheriff 2009/2010); perceived risk → −40% offspring (Zanette 2011) | Chemical/acoustic cue → hormonal signal → offspring phenotype | Grounded (intergenerational) | Measurable (cortisol metabolites, morphology) | [consciousness_fields.md §3l](consciousness_fields.md) |
| Multi-generation maze learning ("learning across distance") | McDougall water-maze (1927–38); Crew 1936 null; Agar 1954: control lines improved too, tied to colony health | Learning-rate trend across generations | Data Grounded (historical); Lamarckian reading refuted; morphic resonance (Sheldrake 1981) Speculative | Would need blinded, pre-registered, geographically separated replication | [consciousness_fields.md §3l](consciousness_fields.md) |
| Generational tech fluency ("preconditioned for the future") | Sensitive-period plasticity (Knudsen 2004); environmental IQ gains ~2.8 pts/decade (Flynn 1987; Pietschnig & Voracek 2015); digital-native myth (Kirschner & De Bruyckere 2017) | Experience → neural circuit stabilization | Faster uptake Grounded (environmental); inherited/morphic preconditioning Speculative; genetic too slow; epigenetic untested | — | [consciousness_fields.md §3l](consciousness_fields.md) |
| Reactive (threat) state vs reflective control | Uncontrollable stress → high catecholamines → PFC network weakening (Arnsten 2009); acute stress impairs working memory/flexibility (Shields 2016); arousal narrows cue use (Easterbrook 1959); evolutionary mismatch framework (Li, van Vugt & Colarelli 2018) | Threat signal → neuromodulator surge → narrowed attention, reduced PFC control | Mechanisms Grounded; mismatch explanation of belief resistance Plausible | Measurable (working-memory tasks, cortisol, HRV) | [consciousness_fields.md §3m](consciousness_fields.md) |
| Information environment → belief (repetition, conformity, identity) and counter-measures | Illusory truth (Hasher 1977; Fazio 2015); conformity (Asch 1956; Bond & Smith 1996); identity-protective cognition (Kahan 2013; Tappin 2021 counterpoint); prebunking (Roozenbeek 2022); lateral reading (Wineburg 2022) | Repeated/consensus signal → perceived truth; pre-exposure training → resistance | Effects Grounded; "don't see it" as single construct Plausible; interventions Grounded but small at scale | Measurable (truth ratings, discernment, ROC/response bias) | [consciousness_fields.md §3m](consciousness_fields.md) |
| Observer attention / intention on physical or physiological signals (psi claims) | Proposed: presentiment (Mossbridge 2012 ES 0.21), double-slit attention (Radin 2012/2016), ganzfeld (Storm 2010), precognition (Bem 2011); no known carrier (no-signalling) | Claimed attention → photon fringe / pre-stimulus physiology; no accepted mechanism | Papers exist (Grounded); effects Speculative/contested: Bem replications null (Ritchie 2012; Galak 2012), double-slit reanalysis n.s. (Tremblay 2019) | Would need preregistered, multi-lab adversarial replication | [consciousness_fields.md §3n](consciousness_fields.md) |
| Borax-treated cured panels with BN-coated branch channels (alt. to petrification) | Borate fungicide/fire retardant; BN barrier against leaching and scale | Fluid (channel flow without mineral scaling), heat | Grounded treatment; design open; non-living zones only | — | [living_habitat §zones](living_habitat_life_support.md) |

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
0. **Egg precession and lattice pulse (Channing's priority).** Egg: L, aspect ratio, Ω, ν. Lattice: t, f, drive amplitude. These set Re/E/Po and f/Q/δ.
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
