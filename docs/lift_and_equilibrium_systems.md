# Lift & equilibrium systems (living doc)

*Living document: more pieces to be added.* License CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative**. Prepared with Channing.

**Architecture under discussion:**
- **Buoyancy** carries the weight (primary lift).
- **EM envelope / sheath manipulation** provides trim and dynamic control.
- Everything is held to a **power ledger** (watts in → newtons out) per mechanism.

## 1. Buoyancy as primary lift (Grounded)
- **Archimedes:** net lift = (ρ_air − ρ_gas)·g·V.
- At sea level ρ_air ≈ 1.225 kg/m³, ρ_He ≈ 0.169 kg/m³, giving **≈1.06 kg (≈10.4 N) per m³ of helium**. Hydrogen gives ≈1.14 kg/m³ but is flammable.
- **Power ledger:** ~0 W to *hold* altitude, because lift costs no continuous power. Power goes only to trim, propulsion and envelope losses.
- **Scale:** 100 kg payload plus structure needs ~100–150 m³ of helium, e.g. a ~6–7 m diameter sphere.
- **Contrast:** eddy-current hover costs ~10–17 kW for 88 kg (Resona-POL-Modular-Core sim). Buoyancy is the only mechanism here that pays the weight bill for free.

## 2. Lorentz force (Grounded)
- **F = q(E + v×B)**; on a conductor, **F = I L × B**.
- **Power ledger:**
  - A current-carrying wire in Earth's field (~50 μT) gives 5×10⁻⁵ N per A·m, which is negligible.
  - Useful force needs a strong local B *and* a reaction body (magnet ↔ conductor, or plasma ↔ coil).
  - Losses scale with I²R.
- **Use here:** trim and control of an envelope that carries currents near onboard magnets (internal forces), or MHD pumping of a conducting fluid.
- **Limit:** internal Lorentz forces cannot give net external lift (momentum conservation). It needs an external field or medium to push against.

## 3. Tesla work (Grounded history; see `tesla_and_ancient_alignments.md`)
- **Resonant wireless power** is real and modern: 11–20 kW EV chargers at up to ~98.5 % efficiency (see `em_topological_gravity_review.md`). It delivers power; it does not lift.
- **Valvular conduit:** **US 1,329,559** (filed 21 Feb 1916, granted 3 Feb 1920). A no-moving-parts check valve whose pockets and baffles let fluid pass freely one way and force "rapid reversals of direction" the other way (claim 1). It is used today in microfluidics and pulsating heat pipes. Its diodicity, the reverse/forward pressure-drop ratio, is only significant at higher Reynolds number and for pulsating flow.

## 4. Ionic wind / electroaerodynamics (Grounded)
- **Xu et al.**, "Flight of an aeroplane with solid-state propulsion", *Nature* 563:532–535 (2018), doi 10.1038/s41586-018-0707-9 (MIT).
  - 5 m wingspan, 40 kV onboard converter, steady flight for ~10–12 s.
  - The aircraft configuration gave **6.25 N/kW** at a thrust density of ~3 N/m². Lab-scale EAD has reached ~50 N/kW (Masuyama & Barrett). For comparison, jet engines are ~3 N/kW and helicopter rotors ~50 N/kW.
- **Power ledger:**
  - Hovering 1,000 N (~100 kg) by ionic wind at 6–50 N/kW would need **~20–160 kW**. Not viable as primary lift.
  - As **trim** on a buoyant body, 10 N needs ~0.2–2 kW. Feasible.
- **Fit:** ionic thrusters are a good silent trim and propulsion actuator for a buoyant envelope. **Plausible-untested** for this integration.

## 5. H₃O₂ / exclusion-zone (EZ) water (debated)
- **Claim (Pollack):** a "fourth phase" of water, H₃O₂ in hexagonal sheets, forms near hydrophilic surfaces and separates charge under light.
- **Grounded part:** micron-to-100s-μm exclusion zones that push out microspheres are reproducible.
- **Debated or contradicted part:** the H₃O₂ structure and light-driven charge separation. Quantum-chemistry calculations find the structure unstable, and diffusiophoresis/chemotaxis explains much of the observed behaviour. See "Exclusion Zone Phenomena in Water—A Critical Review", *Int. J. Mol. Sci.* 21:5041 (2020). Pollack's book itself calls the layered structure speculative.
- **Label:** EZ effect **Grounded**; H₃O₂ phase **Speculative/debated**; any use for lift **Speculative**.
- **Power ledger:** no measured usable power or force exists at relevant scales.

## 6. Multi-fluid loop with Tesla valves (Channing's concept)
**Concept:**
- A closed loop of **ferrofluid, water, CBD oil and air** segments.
- Tesla valves create direction-dependent **impedance zones**.
- An **applied perturbation** is then added (pulsed field, pump or vibration).

**Grounded components:**
- **Ferrofluids** respond to magnetic gradients (body force μ₀M∇H) and can be pumped magnetically with no moving parts.
- **Tesla valves rectify pulsating flow**, so an oscillating perturbation becomes net circulation. Pulsating heat pipes use the same idea.
- Immiscible segments (water | oil | air) create interfaces with surface tension and viscosity contrasts, i.e. impedance steps.

**Physics of what it would do:**
- A pulsed magnet acting on the ferrofluid slug acts as a piston. The Tesla valves turn that into one-way flow, and the oil and water slugs ride along.
- This is a solid-state **pump or heat mover**. It produces no net external force on the closed loop (internal momentum).
- **CBD oil:** chemically it is just a carrier oil plus cannabidiol. Any oil of matching viscosity behaves the same, and there is no known EM role.

**Labels:**
- Pumping and heat transfer: **Plausible-untested**, with components Grounded.
- Lift or "equilibrium field" from the loop: **Speculative, and contradicted by momentum conservation** unless it pushes on air or an external field.

**Power ledger:** input = coil I²R plus viscous dissipation; output = flow work ΔP·Q. Expect efficiency of a few % at small scale.

## 6b. Dual-Oil Module (bench)
*Channing's recovered text, saved faithfully. It arrived out of order. Sits next to the multi-fluid Tesla-valve loop (§6).*

**Concept (as given).**
- **Two fluid domains** share a **controllable interface**.
- **Castor domain:** a high-viscosity dielectric that hosts **electrostatic self-organization**, i.e. ball-bearing or particle **chaining under an applied E-field**.
- **CBD / mycelium-compatible domain:** lower or tunable viscosity; the **bioactive phase**.
- **Interface:** tension and viscosity are **modulated by terpenes or spice extracts** (a "soap" analogue).
- **Electrodes,** or VE-shaped electrodes, go on the castor side. **Living or passive particles** go on the CBD side.
- **Track:** particle trajectories, interface deformation, and **cross-talk** between chaining and the second fluid.

**Grounded:**
- **Electrorheological chaining:** Winslow, "Induced fibration of suspensions", *J. Appl. Phys.* 20:1137–1140 (1949), doi 10.1063/1.1698285.
  - Polarizable particles in an insulating oil form field-aligned chains, raising shear resistance reversibly in milliseconds.
  - Castor oil is a reasonable host: dielectric constant ~4.8, very viscous.
- **Electrohydrodynamic interface deformation:**
  - Taylor, "Studies in electrohydrodynamics I. The circulation produced in a drop by an electric field", *Proc. R. Soc. A* 291:159–166 (1966), doi 10.1098/rspa.1966.0086.
  - Melcher & Taylor, "Electrohydrodynamics: a review of the role of interfacial shear stresses", *Annu. Rev. Fluid Mech.* 1:111–146 (1969), doi 10.1146/annurev.fl.01.010169.000551.
  - In this **leaky-dielectric model,** free charge collects at a fluid–fluid interface and drives circulation. Whether a drop goes prolate or oblate is set by the ratios of conductivity, permittivity and viscosity.

**Miscibility check (important):**
- **Castor oil is miscible with ethanol and with other vegetable oils.** It is reported to blend with MCT, and as a triglyceride it very likely blends with hemp-seed oil too. So **castor + an MCT- or hemp-carried CBD oil probably gives one phase, not an interface.** Test in a vial before building: a cloudy line means two phases, a clear blend means one.
- **Castor is practically insoluble in mineral oil** (pharmacopoeia data), and the classic Taylor drop experiments use **castor in silicone oil**.
- **Interface options:**
  - (a) Castor | **silicone or mineral oil** carrying the bioactive, if it is oil-soluble enough.
  - (b) Castor | **water or glycerol–water** for a mycelium-compatible aqueous phase, with CBD as an emulsion.
  - (c) A thin membrane or hydrogel separator.
- **Labels:** interface physics **Grounded**; the specific castor/CBD pairing **needs a check**; **terpenes as interface modulators are Plausible-untested** (some are surface-active, and the size of the effect is unknown).

**Low-cost test design (~$40–80):**
- **Cell:** a glass cuvette or petri dish holding castor (bottom) and the second phase (top or side). Use two copper-tape or stainless electrodes on the castor side, with 2–10 mm gap.
- **Drive:** a 1–5 kV DC or low-frequency AC source, current-limited (e.g. a negative-ion generator module or a small HV module). **HV safety:** enclosure, one hand, bleeder resistor.
- **Particles:** castor side, 50–200 μm glass beads, cornstarch or TiO₂ to chain. Second phase, passive tracers or, later, mycelium fragments or spores.
- **Diagnostics:** phone macro video at 60–240 fps. Use free tracking software (Trackpy, or Fiji/TrackMate) to measure chain-formation time, interface deflection vs voltage, and tracer motion in the second phase.
- **Runs:**
  1. Chaining alone.
  2. Interface alone, compared with the Taylor prediction (prolate vs oblate).
  3. Both together, to look for cross-talk: does chaining change interface flow, or does second-phase motion change chain stability?
  4. Add 0.1–1 % terpene (e.g. limonene) and re-measure interface deflection and tension (pendant-drop photo).
- **Falsifiable:** if terpenes don't measurably change the deformation-vs-voltage curve, the "soap" knob is negligible.

## 7. Coulomb eggs, EM field generation & sympathetic resonance (link **C8** Multi-Egg)
- **Grounded:**
  - Charged or magnetised rotors ("eggs") generate fields. Spinning charge is a current loop.
  - Coupled resonators exchange energy when tuned (sympathetic resonance, e.g. tuning forks or WPT coils).
  - Gyroscopic stabilisation is real (C8: "Does Multi-Egg stability come from gyro eggs or from eddy springs?").
- **Limits:**
  - A charged sphere of radius 5 cm at 10 kV holds ~5.6×10⁻⁸ C, so the forces are mN-scale at most.
  - Resonance transfers energy; it does not create it.
  - Internal precession gives torque, not lift (`shifting_phase_order_review.md` §A3).
- **Label:** attitude control and stabilisation **Grounded**; field-generated lift **Speculative**.

## 8. Chirp packets: rapid adaptation to external stimulus
**Idea:** send a short frequency-swept probe (a "chirp packet"), read how the system responds across the sweep, and retune fast.

**Grounded:**
- **Chirp radar / pulse compression.** Sweep a long pulse linearly in frequency, then compress it with a matched filter. This gives the range of a long pulse with the resolution of a short one: Klauder, Price, Darlington & Albersheim, "The theory and design of chirp radars", *Bell Syst. Tech. J.* 39:745–808 (1960).
- **Biosonar.** Many bats emit FM sweeps, which are natural chirps (IET *Electronics & Power*, 1980: bats use "short pulse, f.m. chirp or Doppler modes"). **Dolphins** mostly use short broadband *clicks* rather than FM sweeps. They are still a wideband probe, but not a chirp in the strict sense.
- **Adiabatic rapid passage.** Sweeping the drive frequency through resonance fast compared with relaxation, but slow enough for the system to follow, inverts a population robustly and is insensitive to drive-amplitude errors. This goes back to Bloch, "Nuclear induction", *Phys. Rev.* 70:460 (1946). It is used today as chirped / hyperbolic-secant pulses in NMR/MRI and atomic physics.
- **DRAG pulses (superconducting qubits).** Adding a second quadrature proportional to the drive's time derivative suppresses leakage to higher levels: Motzoi, Gambetta, Rebentrost & Wilhelm, *Phys. Rev. Lett.* 103:110501 (2009), doi 10.1103/PhysRevLett.103.110501.
- **Closed-loop adaptive control.** A learning loop uses lab measurements to improve pulse shapes, with the experiment itself acting as the "analog computer": Judson & Rabitz, "Teaching lasers to control molecules", *Phys. Rev. Lett.* 68:1500 (1992), doi 10.1103/PhysRevLett.68.1500.
- **Chirped-pulse amplification.** Stretch a pulse with chirp, amplify it, then recompress it: Strickland & Mourou, "Compression of amplified chirped optical pulses", *Opt. Commun.* 55:447 (1985; corrected reprint 56:219). Nobel Prize in Physics 2018.

**RGRF extension:**
- **Chirp probes for sheath or field state (Plausible-untested).**
  - Inject a low-power chirp on the POL drive coil (or on a sheath electrode) alongside the main drive.
  - The response vs frequency gives the gap, plate coupling and resonance shift in a single sweep.
  - Feed that to the PID height loop (`piezo_helium_feedback_loop.md`; Resona-POL-Modular-Core `height_control.py`).
  - This is standard system identification, so the open question is speed and robustness, not principle.
- **Coulomb eggs / Multi-Egg (C8): Speculative.** Chirp each rotor's drive to find and track its resonance, and retune adiabatically instead of re-locking hard.
- **Quantum-computing analogy: Speculative.** DRAG-like derivative corrections to suppress "leakage" into unwanted craft modes, or Judson–Rabitz-style learning for disturbance rejection. This is an analogy only. Classical coupled oscillators can use the same control math, but nothing quantum is involved.

**Power ledger:** the probe is a small add-on (mW–W) on top of the drive. The benefit is control bandwidth, not lift.

**Falsifiable bench test (~$40–100):**
- Use a series-resonant coil (a few hundred kHz) with an aluminium plate at variable gap, driven by an ESP32 DDS or a sweep generator, plus a current-sense resistor and scope or ADC.
- **Step 1.** Measure resonance shift vs gap with a ~1 ms chirp. Prediction: a monotonic shift, from which gap can be inferred to about ±0.5 mm.
- **Step 2.** Step the gap or load, then measure **retuning latency**, the time from disturbance to drive back on resonance. Compare chirp tracking against a fixed-frequency PLL or hill-climb.
- **Pass:** faster recovery at the same probe power.
- **Fail:** no advantage, in which case a conventional PLL is good enough.

## Grounded loop mechanisms (1–7)
*Channing's recovered text, labeled. Each mechanism is standard physics; the open question is whether they integrate into one loop, and with what energy ledger (see Power ledger summary).*

1. **Lorentz and magnetic-gradient forces (Grounded).**
   - Conductive fluids feel the J×B force. Ferrofluids feel the Kelvin force (μ₀M·∇H).
   - Together these can position fluid, shift density, impose shear and drive directed circulation. MHD pumps and ferrofluid seals are existing devices.
2. **Joule heating with a steerable hot zone (Grounded).**
   - Heating goes as I²R (or J²/σ).
   - Shaping the magnetic field (current paths, eddy and induction zones) places and moves the hot zone, as in induction heating.
3. **Adiabatic compression and expansion (Grounded).**
   - Expansion cools the gas, and vapor condensing there gives a controllable cold zone. This is the same principle as refrigeration cycles and cloud chambers.
4. **Closed multiphase circulation (integration Plausible-untested).**
   - Magnetic body force, localized heating, and expansion/compression pulses together give directed flows. Mass is recovered by condensation.
   - **No new physics.** The analogs are heat pipes, loop thermosyphons and MHD / ferrofluid pumps.
   - **In microgravity** the EM and thermal terms persist and buoyancy becomes secondary. That makes this the cleanest continuity from ground to space; ferrofluid and heat-pipe flight heritage exists generically.
   - **Needed:** a full energy ledger (electrical in → heat + work + losses). No net-energy claims.
5. **Larmor precession timing (Grounded in principle).**
   - Magnetized elements precess at ω = γB. Timing the precession can modulate when force density or pressure peaks.
   - **The coupling efficiency is a design parameter,** not yet measured. For ferrofluid nanoparticles, Néel/Brownian relaxation usually dominates.
6. **Vortex organization (Grounded).**
   - Counter-rotating vortex pairs and shear interfaces (Kelvin–Helmholtz) are standard flow structures.
   - So are 180°-phase-offset "bridges," in the sense of coupled oscillators locked in antiphase.
7. **Carried-forward materials and hardware (standard engineering).**
   - **Structure:** mycelium–hemp composites (Trametes and hybrids; see `mycelium_uses.md`), bamboo hierarchical framing, and chitosan / borax binders or crosslinkers.
   - **Sensing and actuation:** piezo sensors and actuators, quartz resonators, and helium as a low-damping acoustic medium. Note that helium's high sound speed shifts resonances, and it is hard to contain.
   - **Flow and heat:** Tesla-valve rectification (section above), Al–Cu thermal networks (watch for galvanic corrosion at the junctions), and magnetic centering.
   - Material claims beyond the cited docs: **Plausible**, pending tests.

**Bench test:**
- Run a sealed ferrofluid or salt-water loop with a permanent-magnet gradient, a resistive heater and a piezo pulse.
- Measure flow rate and ΔT against input watts.
- Repeat with the magnet removed, and with the system inverted (a gravity-independence check).

## Power ledger summary
| Mechanism | Force per power | Role | Tag |
|---|---|---|---|
| Buoyancy (He) | ~10 N/m³ at ~0 W | Primary lift | Grounded |
| Eddy-current EDS (POL sim) | ~0.05–0.1 N/W (52 N/kW) | Not viable for a free vehicle | Grounded (numbers) |
| Ionic wind | 6–50 N/kW | Trim / propulsion | Grounded |
| Lorentz on onboard currents | Needs external B or medium | Control, MHD pump | Grounded |
| Tesla-valve ferrofluid loop | Internal only | Pump / heat mover | Plausible-untested |
| EZ water / H₃O₂ | None measured | — | Speculative |
| Coulomb eggs / resonance | mN-scale; torque | Attitude | Grounded / Speculative for lift |

## Bench tests
1. **Helium balloon trim with an ionic thruster (~$60–150).** Party balloon cluster, 2 wire/foil corona electrodes, ≤10 kV module (**HV safety**), scale. Measure trim force vs input W, and compare with 6–50 N/kW.
2. **Tesla-valve rectification (~$30–80).** 3D-printed Tesla valve, syringe or speaker-driven pulsation, tubing. Measure net flow vs drive frequency (diodicity), first with water, then with an oil slug.
3. **Ferrofluid magnetic pump (~$40–100).** Ferrofluid slug in a loop with one Tesla valve and a pulsed electromagnet. Measure flow rate and coil watts. Hold the loop on a scale to confirm no net weight change.
4. **EZ replication (~$50).** Nafion sheet, microspheres, microscope or phone macro lens. Record EZ width with and without light. Test the competing diffusiophoresis explanation by changing ion concentration.
5. **Sympathetic resonance between rotors (~$30).** Two tuned pendulums or coils; measure energy-transfer efficiency vs detuning.

## Missing pieces
- Target vehicle mass, volume and trim-force budget (newtons and response time).
- Envelope material and helium leakage rate. A mycelium-composite or film envelope is not yet specified.
- A quantity for "impedance zone" and "equilibrium". What is measured, in what units?
- How sheath or envelope EM manipulation reacts against the *external* air or field. Without this there is no net force.
- Weight of HV supplies and batteries for ionic trim.
- Any primary source for EZ-water energy or force claims.
