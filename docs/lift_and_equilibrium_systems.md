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
