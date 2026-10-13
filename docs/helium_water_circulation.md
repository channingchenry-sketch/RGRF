# Helium–water circulation: does helium "compress to the center"? (investigation)
*License CC0. Prepared with Channing, 2026-10-12. Labels: **Grounded** / **Plausible-untested** / **Speculative**. Links: [pol_v0_1_zones.md](pol_v0_1_zones.md) (material stacks, layers 3–4), [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md), [acoustic_streaming_and_centrifugal.md §2](acoustic_streaming_and_centrifugal.md), [piezo_helium_feedback_loop.md](piezo_helium_feedback_loop.md).*

> Channing (verbatim): "Yeah for some control of the helium loop we had circulation and water the thought was that the helium would compress to the center. I think we ended up not revisiting which was a ball drop on my part, can we investigate?"

## 1. Helium does collect at the center (Grounded)
- In swirling water, the radial pressure gradient dp/dr = ρv²/r pushes the dense phase (water) outward. Light gas bubbles feel a net inward force: **centrifugal buoyancy**, the same physics as [acoustic §2](acoustic_streaming_and_centrifugal.md) (dp/dr = ρω²r).
- The result is a **gas-core vortex**: bubbles migrate to the axis and merge into a gas column. This is how hydrocyclones form an air core and how vortex/cyclonic degassers strip gas from liquids.
- Helium (ρ ≈ 0.17 kg/m³ at 1 atm) against water (1000 kg/m³) has an enormous density contrast. **So helium WOULD collect at the center.** The original intuition about *positioning* is right.

## 2. Key correction: collection ≠ compression
- In a rotating fluid the pressure is **lowest on the axis** and rises outward (dp/dr = ρv²/r > 0).
- Helium gathered at the core therefore sits at the **lowest pressure** in the system, so it *expands* relative to the wall pressure. It does not compress.
- **Forced (solid-body) vortex:** Δp(wall − axis) = ½ ρ ω² r².

Example: water, ρ = 1000 kg/m³, radius r = 0.1 m:

| rpm | ω (rad/s) | Δp wall−axis (Pa) | as % of 1 atm |
|---|---|---|---|
| 60 | 6.28 | ~197 | ~0.19 % |
| 300 | 31.4 | ~4,930 | ~4.9 % |
| 1000 | 105 | ~54,800 | ~54 % |
| 3000 | 314 | ~493,000 | ~490 % (wall must be pressurized, or the core cavitates/boils) |

At low rpm the effect is a small pressure *drop* at the core. At high rpm, if the wall sits at 1 atm, the axis would go below vapor pressure: the core fills with water vapor and expanded gas. Either way, **spin does not compress helium at the center.**

```python
import math
rho, r = 1000.0, 0.1
for rpm in (60, 300, 1000, 3000):
    w = rpm * 2 * math.pi / 60
    dp = 0.5 * rho * w**2 * r**2
    print(rpm, round(w, 2), round(dp), f"{dp/101325:.1%} of 1 atm")
```

## 3. Ways the idea could still work (Plausible-untested)
- **Use the vortex for separation and positioning only.** It keeps the helium in a predictable central column, away from the walls, and lets it be tapped from the axis.
- **Get compression elsewhere:**
  - the **piezo stroke** (the existing piezo-helium loop);
  - **hydrostatic head** (a water column weighing on the gas, Δp = ρgh, about 9.8 kPa per metre of water);
  - a **liquid piston**: water moved by a pump or oscillation compresses the gas pocket.
    - Fluidyne / liquid-piston Stirling engines: C. D. West, *Liquid Piston Stirling Engines*, Van Nostrand Reinhold (1983).
    - Liquid-piston near-isothermal gas compression, from compressed-air energy storage research: J. D. Van de Ven & P. Y. Li, "Liquid piston gas compression," *Applied Energy* 86, 2183–2191 (2009), doi:10.1016/j.apenergy.2008.12.001.
- **Tradeoff (Grounded physics):**
  - Water's large heat capacity and contact area make compression **near-isothermal**, so there is a small temperature swing (T₂/T₁ well below the adiabatic (p₂/p₁)^0.4 for He). That is good for *heat transport*, efficiency and gentle thermal management.
  - It means **less cooling per cycle** if the goal is a cold zone from adiabatic expansion.
  - Choose by role: isothermal for protection and heat moving; adiabatic (dry gas, fast stroke) for cooling.

## 4. Phase separation and caveats
- **Low solubility (Grounded):** helium is among the least water-soluble gases (solubility-law constants compiled in R. Sander, compilation of gas-solubility constants for water (version 4.0), *Atmos. Chem. Phys.* 15, 4399–4981 (2015), doi:10.5194/acp-15-4399-2015). Little helium dissolves, so the phases stay separate, which is good.
- **Caveats:**
  - **Water vapor contaminates the helium.** It adds vapor pressure, changes γ and heat capacity, and condenses on cold surfaces. A dryer or condenser trap is needed if the dry-gas properties matter.
  - **Freezing below 0 °C.** Water freezes in any cold zone. Use antifreeze (glycol) or keep the water side above freezing.
  - **Containment:** helium permeates many materials (see [pol_v0_1_zones.md](pol_v0_1_zones.md)).

## 5. Status for the POL loop
- Vortex positioning of helium: **Grounded** (physics); **Plausible-untested** for POL.
- "Helium compresses to the center": **Contradicted.** The core is the low-pressure point.
- Liquid-piston or piezo compression with vortex positioning: **Plausible-untested**.

**Unknowns:** rpm or circulation speed, channel/loop radius, water and helium volumes, operating pressures (wall and core), piezo stroke and frequency, and the temperature range.

## 6. Bench test (~$30–80)
- **Setup:** a clear cylinder (e.g. a 10–20 cm acrylic tube or jar) on a variable-speed turntable or with a magnetic stirrer, filled with water and a small gas pocket. Use air first, then helium from a balloon.
- **Observe:** filming core formation vs rpm (bubbles to the axis, then a gas column).
- **Measure:** a pressure tap at the axis vs at the wall (two thin tubes to a differential manometer or a cheap pressure sensor). Compare with Δp = ½ρω²r². **Prediction:** the axis reads *lower*, by the amount in the table.
- **Optional:** gently drive a water column (syringe as a liquid piston) and log the gas-pocket pressure and temperature (thermocouple) to see a near-isothermal vs adiabatic swing.
- **Falsified if:** gas does not migrate to the axis, or the axis pressure is not lower than the wall pressure.

## 7. External heating and the jump to gas-giant dynamics
> Channing (verbatim): "Right, then we factored in the external heating but we had no way of controlling consistency. We ended up jumping to Saturns and Jupiters dynamics."

### (a) The problem: heating competes with the vortex (Grounded)
- Non-uniform external heating of a rotating fluid sets up buoyancy-driven **convection** (warm fluid rises, cool fluid sinks). That flow competes with the imposed vortex, so the gas core's **position and pressure wander**. This is the "no way of controlling consistency" problem.
- **Taylor–Proudman:** in rapidly rotating, slow, inviscid flow, velocity does not vary along the rotation axis (∂**v**/∂z ≈ 0). Convection is organized into columns aligned with the axis instead of overturning freely.
- **Rossby number** Ro = U/(ΩL) measures inertia against rotation. Small Ro means rotation dominates, giving geostrophic, column-like flow. Ro ~ 1 or larger means heating and inertia can break the pattern up.

### (b) Why Saturn and Jupiter (Grounded)
- They are rapidly rotating fluid shells, heated from inside (residual internal heat) and from outside (sunlight). Instead of chaotic overturning, they **self-organize** into stable zonal jets and bands, long-lived vortices and polar vortex clusters.
- **Saturn's north polar hexagon** is a stable jet-stream wave pattern, observed since the 1980s. It has been reproduced in rotating-tank experiments: A. C. Barbosa Aguiar, P. L. Read, R. D. Wordsworth, T. Salter & Y. H. Yamazaki, "A laboratory model of Saturn's North Polar Hexagon," *Icarus* 206(2), 755–763 (2010), doi:10.1016/j.icarus.2009.10.022 (verified). In the tank, barotropically unstable jets equilibrate into stable polygons, including hexagons. The wavenumber is set by jet width, shear and Rossby number.
- So the jump made sense: gas giants are natural examples of **heated, rotating fluid that stays organized.**

### (c) Design takeaway (Plausible-untested)
- **Don't fight convection; lock it.** Choose the rotation rate and heating geometry so that the heated flow organizes into stable bands or jets, and place the helium core where that pattern puts it.
- **Dimensionless knobs (standard):**
  - **Rossby** Ro = U/(ΩL): rotation dominance.
  - **Ekman** E = ν/(ΩL²): viscous vs rotational.
  - **Rayleigh** Ra = gαΔT L³/(νκ), or its rotating-frame form with g → ω²r: heating strength vs dissipation.
  - Stable banding needs small Ro and E with Ra above onset but not so large that flow becomes turbulent. Thresholds for the POL geometry are **unknown**.
- **Bench test:**
  - a rotating tank (turntable plus clear cylinder) with **a controlled heating ring** (resistive strip at the wall, or a heated bottom annulus) and/or **differential rotation** (a lid or inner disc spun at a different rate, as in the hexagon experiments);
  - dye or tracers to view jets and polygons;
  - a pressure tap at the axis to check whether the core pressure steadies once bands lock in;
  - sweep rpm and heater power, and map stable vs wandering regimes in (Ro, Ra).

### (d) Links
- Saturn hexagon and resonant-bottom tank: [em_topological_gravity_review.md §3](em_topological_gravity_review.md#3-saturns-north-polar-hexagon), in "Planetary & stellar reference threads".
- Jupiter fuzzy (dilute) core and metallic hydrogen: [em_topological_gravity_review.md §4](em_topological_gravity_review.md#4-jupiter-fuzzy-dilute-core--metallic-hydrogen).

**Unknowns:** heat source location and power, heating uniformity, rpm, fluid depth and radius, ΔT, the fluid's thermal expansion and diffusivity (α, κ), the resulting Ro/E/Ra, and which banded state places the helium core where it is wanted.

## 8. Pressure valves: flow vs force (unsettled, reopened 2026-10-12)
> Channing (verbatim): "Yeah, flow vs force we played around with pressure valves but never really settled"

In flow-vs-force terms, a valve converts a **force** (pressure threshold, spring, piezo actuator) into a **flow** outcome (direction, rate, leakage).

| Option | Force: what sets it | Flow: direction / rate / leakage | Status | Source |
|---|---|---|---|---|
| (1) Passive spring check / relief valve | Cracking pressure = spring preload ÷ seat area; relief opens at a set Δp | One-way; rate rises above cracking Δp. Small leak at the seat, hysteresis (opens and closes at different Δp), moving parts wear | Grounded (standard hardware) | textbook |
| (2) Tesla valve / fluidic diode | Geometry only: inertial flow separation, no actuator | Directional *resistance*, not a seal. Diodicity Di ≈ 1 below Re ≈ 100, turns on over Re ≈ 100–300, **Di ≈ 2 for Re ≈ 300–1500** (reported 2–4 for other geometries at Re 10³–10⁶). Boosted by pulsatile flow. Bridge rectifier pump effectiveness E ≈ 0.5. **Rectifies oscillating flow; never holds pressure** | Grounded | Q. M. Nguyen, J. Abouezzi & L. Ristroph, *Nat. Commun.* 12, 2884 (2021), doi:10.1038/s41467-021-23009-y (verified); [POL zone 7](pol_v0_1_zones.md#7-micro-tesla-valve--density-accents-optional) |
| (3) Piezo-actuated active valve | Piezo force/stroke (D = d·T, S = dᵀE) driven electrically, timed to the drive phase | Opens/closes on command, so it can seal hard. Timing locked to the piezo stroke / heartbeat; needs power and control | Grounded (technology); sync scheme Plausible-untested | [DESIGN_FORCE_FLOW_MAP §2](DESIGN_FORCE_FLOW_MAP.md) (lattice pulse) |
| (4) Pulse-tube orifice + reservoir / inertance tube | Flow impedance: orifice (resistive), inertance tube (gas inertia, inductive), reservoir (compliance, capacitive) | Sets the **phase between pressure (force) and mass flow**. Inertance can make the flow lag pressure (≈60° target at the warm end) | Grounded (pulse-tube cryocoolers) | R. Radebaugh, "A review of pulse tube refrigeration," *Adv. Cryog. Eng.* 35, 1191–1205 (1990) (verified via NASA NTRS); R. Radebaugh et al., "Inertance tube optimization for pulse tube refrigerators," *AIP Conf. Proc.* 823, 59–67 (2006) (verified) |

**Why (4) is "flow vs force" exactly:** in an oscillating gas, pressure is the force and mass flow is the flow. The orifice/inertance/reservoir network is an R–L–C circuit (as in the fluidic RLC section of [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md)) that chooses their phase relation. That phase decides whether the cycle pumps heat.

**Recommendation (Plausible-untested):**
- **Tesla diodes** for the *steady water circulation direction*: no moving parts, well suited to pulsatile drive. Keep Re in the hundreds or above; at low Re they barely work.
- **Orifice/inertance + reservoir** for *helium phase control* in the piezo-helium loop.
- **Active piezo valve** only where a **hard seal** is needed, e.g. isolating helium for storage or containment.

**Unknowns:**
- Water channel size and flow speed (and so Re)
- Drive frequency and stroke
- Helium mean pressure and pressure ratio
- Reservoir volume and inertance tube length/diameter
- Allowed leak rate
- Valve power budget

**Bench test (~$30–60):** measure diodicity.
- Use a 3D-printed Tesla valve in a water line with a pump, a flow meter (or a timed beaker) and two pressure taps (or water columns).
- At a **fixed flow rate**, measure Δp forward and Δp reverse: Di = Δp_rev/Δp_fwd. Repeat across flow rates to find the turn-on Re.
- Then drive it with an oscillating syringe or speaker and measure the net flow.
- **Compare with Nguyen et al.:** Di ≈ 1 below Re ≈ 100, ≈ 2 above ≈ 300.

## 9. Tesla valves in all loops and the Tesla-coil perturbation zones
> Channing (verbatim): "Yes we definitely used Tesla valves in all our loops and into our Tesla coil perturbation zones where we utilized phase shifts and dual purpose reconnection to flow pathways"

- **Tesla valves in every loop:** a **recalled design fact** (Channing, 2026-10-12). The loops fed into "Tesla coil perturbation zones" that used phase shifts and dual-purpose "reconnection to flow pathways".
- **Consistent with §8 (Grounded):** Tesla valves rectify best under pulsatile, oscillating flow. Nguyen et al. (2021) found that pulsatile forcing boosts pumping well beyond the steady-flow prediction. Pairing the valves with a **phase-shifted, oscillating drive** is therefore the right regime. They do not seal, so they set direction, not pressure.
- **Tesla coil:** a resonant air-core transformer (a separate Tesla invention from the valvular conduit, US 1,329,559). It produces high-voltage, high-frequency fields.
  - Using it to perturb the loops (EM or plasma perturbation of the fluid, e.g. corona or ionic wind near the gas phase, or induction in conductive or ferrofluid segments) is **Plausible-untested**.
  - Water and helium are not moved directly by its field unless charged, ionized or magnetic. The ferrofluid segment and ionized gas are the plausible coupling paths.
- **Layout (Channing, verbatim):** "So we made sinks in the ferrofluid, water, cbd, air loops , across from that a Tesla coil. The valves control flow both into the zone and steady separation back to the flow pathway."
  - **Sinks** are pockets/basins built into the ferrofluid / water / CBD / air loops.
  - A **Tesla coil** sits **opposite each sink**.
  - **Tesla valves** gate the **inflow** into the sink and a **steady, separated return** to the main loop.
- **"Reconnection" resolved:** it means **flow rejoining the main pathway** after the sink. That is a split-and-merge fluidic network, **Grounded** (see the fluidic RLC / rectification section of [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md)).¹
- **Physics of the sink zone:**
  - **Ferrofluid:** the coil's magnetic field exerts the Kelvin body force **f = μ₀(M·∇)H**, so the sink acts as a **magnetic perturbation / separation zone** for the ferrofluid phase. Grounded in principle.
  - **Frequency mismatch (flag):** ferrofluid magnetization follows a field only up to its relaxation rate (Brownian and Néel). Full response is typically in the kHz range or below, depending on particle size and carrier viscosity. Tesla coils run ~50 kHz–MHz.
    - At those frequencies the magnetization lags. The main effect is **heating** (the same loss mechanism used in magnetic-nanoparticle hyperthermia at ~100 kHz–1 MHz) rather than a strong net force.
    - Getting usable force likely needs a **low-frequency envelope/modulation** (pulsing the coil at Hz–kHz) or a separate DC/low-frequency magnet.
    - Also, much of a Tesla coil's near field is **electric** (high voltage), with a weak magnetic field at a distance.
    - **Plausible-untested.**
  - **"So, transistors?" (Channing).** Yes: a **solid-state Tesla coil** (SSTC/DRSSTC) drives the primary with transistors (a MOSFET or IGBT half- or full-bridge). That is Grounded, standard hobby and industrial practice.
    - An **interrupter** switches the drive on and off at a low rate, giving a low-frequency **envelope** (Hz to ~1 kHz) that can be matched to the ferrofluid's response. The ferrofluid then feels a **pulsed force** in the sink at the envelope rate.
    - The HF carrier inside each burst still causes **some heating**. The duty cycle trades force against heat.
    - The envelope could be **synced to the lattice heartbeat** ([DESIGN_FORCE_FLOW_MAP §2](DESIGN_FORCE_FLOW_MAP.md)) and to the Tesla-valve phase shifts: **Plausible-untested**.
  - **Air:** bubbles separate by **buoyancy** in the sink and rise out of the liquid (Grounded). Combined with the valves, this gives the "steady separation" back to the pathway.
  - **Water / CBD oil:** immiscible, so they layer by density in a quiet sink (Grounded). Neither responds directly to the coil unless charged or heated.

¹ *Footnote (demoted reading):* "reconnection" could also suggest magnetic-reconnection-inspired topology (field lines breaking and rejoining; Dungey magnetopause in [em_topological_gravity_review.md](em_topological_gravity_review.md); Hall-MHD resistive term in [tungsten_bismuth_core.md §7b-math](tungsten_bismuth_core.md)). Channing's layout shows the flow meaning; any EM-reconnection-to-flow coupling remains **Speculative** and is not part of the design.
- **Unknowns:** sink volume and shape, coil–sink distance, coil frequency and modulation envelope, coil power and the resulting heating of the ferrofluid, ferrofluid particle size/relaxation time, and how the phase shifts were set (drive timing, inertance/reservoir, or coil phasing).
