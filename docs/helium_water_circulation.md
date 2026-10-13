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
