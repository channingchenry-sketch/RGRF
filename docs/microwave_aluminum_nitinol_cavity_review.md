# Review: "Microwaves and Aluminum Electromagnetic Experiments" (share #62, 2026-10-17)

- **Archive:** [grok_archive/2026-10-17_microwaves_aluminum_electromagnetic_experiments.md](grok_archive/2026-10-17_microwaves_aluminum_electromagnetic_experiments.md) (14 messages: 7 user, 7 Grok-side; message 10 is an "interrupted" notice, not an answer).
- **Labels:** **Grounded** · **Plausible-untested** · **Speculative** · **Symbolic** (as in [REBUILD_INDEX.md](REBUILD_INDEX.md)). φ is Symbolic unless tested.
- **Sims:** no code shown. Skin depth and λ/10 were recomputed in [`sims/grok_claim_checks_shares_60_69.py`](../sims/grok_claim_checks_shares_60_69.py) ([output](../sims/grok_claim_checks_shares_60_69_output.txt)).
- **Lock pins:** none in this share.
- **Already covered elsewhere (cross-links, not repeated):**
  - Mantis-shrimp strike, cavitation and Bouligand club (Patek 2004/2005, Weaver 2012): [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md) and [nitinol_buga_resonant_node_review.md §5](nitinol_buga_resonant_node_review.md#5-mantis-shrimp-recap-14).
  - The Resonant Vortex-Spin Generator Node (Nitinol, quartz, water layer, helium jacket): [nitinol_buga_resonant_node_review.md §4](nitinol_buga_resonant_node_review.md#4-the-concentric-node-and-its-variants-512).
  - Lift budget (buoyancy first; full eddy-current lift ~10–17 kW): [lift_and_equilibrium_systems.md §1a](lift_and_equilibrium_systems.md#1a-design-intent-buoyant-stability-not-levitation).

## 1. Channing's prompts (verbatim)

1. "can we explore microwaves and aluminum in electromagnetic experiments"
2. "Explore it as a perforated would it work at nitinol junctions?"
3. "Elasromers with high kinetic transfer for interlayers/potential static displacement?"
4. "Would this potentially create micro shockwaves?"
5. "Maria shrimp punch almost literally" (interrupted, then re-asked as:)
6. "Peacock mantis shrimp punch almost literally if.. collapsing concentric cavity?"
7. "Can we harness seismic waves or thermal vents?"

## 2. Aluminium in microwave fields; perforated sheet at Nitinol (messages 2, 4)

| Claim | Check | Label |
|---|---|---|
| Aluminium reflects microwaves; sharp edges and thin foil can arc; closed loops carry large currents | Standard. Low-power, shielded test set-ups only, as Grok says. | **Grounded** |
| Skin depth in Al at 2.45 GHz is "only a few micrometers" | δ = 1.66 µm (recomputed). | **Grounded** |
| Perforated Al stays a good shield if holes are < λ/10 to λ/20, "i.e., a few millimeters" | λ = 12.24 cm, so λ/10 = 12 mm and λ/20 = 6 mm. Grok's "a few millimetres or less" is conservative but fine. Real leakage also depends on hole depth and spacing. | **Grounded** |
| "Eddy-current physics we already use for lift in POL" | **Contradicts the repo framing.** The POL design is buoyancy-first, with EM for trim; full eddy-current lift would need ~10–17 kW ([lift §1a](lift_and_equilibrium_systems.md#1a-design-intent-buoyant-stability-not-levitation)). Microwave eddy currents are irrelevant to lift. | **Corrected** |
| Al is anodic to NiTi, so it corrodes galvanically in moisture; isolate the joint | Correct galvanic order (NiTi forms a TiO₂ passive film; Al is far more active). | **Grounded** |
| Contact resistance rises with oxide or as the NiTi interface moves through its phase change | Reasonable; not quantified. | **Plausible-untested** |

## 3. Elastomer interlayers and micro-shockwaves (messages 6, 8)

| Claim | Check | Label |
|---|---|---|
| High-resilience, low-hysteresis elastomers (target > 70–90 % rebound), low compression set, −20 to +120 °C, low dielectric loss | Sensible spec list (e.g. silicone, polybutadiene-rich grades). Specific grades not checked. | **Grounded** (as a spec) |
| Pulsed electrical heating can trigger Nitinol in "tens of microseconds" | Plausible for thin wire heating; cooling (reset) is much slower, so the cycle rate is limited. | **Plausible-untested** |
| Fast Nitinol impulse through a stiff interlayer can launch steep stress waves; edges under strong microwave fields give micro-discharges | Both mechanisms are physical. Shock fronts need fast rise times and a liquid or confined gas. Grok's own "probably not" for a dry, slow junction is the honest answer. | **Plausible-untested** |

## 4. "Peacock mantis shrimp punch almost literally": collapsing concentric cavity (message 12)

| Claim | Check | Label |
|---|---|---|
| Club ~10,000 g, ~23 m/s, cavitation collapse with shock, sonoluminescence, local temperatures of thousands of kelvin | Patek et al. 2004 (speed and acceleration) and Patek & Caldwell 2005 (cavitation forces, sonoluminescence): see [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md). The "thousands of kelvin" figure is the general bubble-collapse estimate, not a mantis measurement. [to verify] | **Grounded** |
| A Nitinol pulse through the elastomer can drive a cavity in the node's water layer that collapses concentrically, focusing a micro-shockwave | Cavitation focusing is real (sonoluminescence, lithotripsy). Whether a Nitinol-elastomer drive gives a fast, symmetric enough collapse is untested. | **Plausible-untested** |
| A "phi-scaled" or fractal cavity "still focuses energy" | A sphere or cylinder is the focusing geometry; no φ advantage is known, and the repo's φ-drive tests showed none. | **Symbolic** |
| Microwave energy "timed correctly" assists vaporisation at the wall | Physically possible. It needs a shielded test cell, and microwave heating of water-filled cavities can superheat and burst. | **Plausible-untested** (safety-limited) |

## 5. Seismic and hydrothermal-vent harvesting (message 14)

| Claim | Check | Label |
|---|---|---|
| Vibration harvesters (1–80 Hz) give µW to tens of mW and power sensor networks | Standard figures for compact harvesters. | **Grounded** |
| A deep-sea vent thermoelectric converter delivered 2.6–3.9 W in situ | Xie et al., *Applied Energy* 164, 620 (2016), [doi:10.1016/j.apenergy.2015.12.036](https://doi.org/10.1016/j.apenergy.2015.12.036): Dragon Flag field, 2,765 m depth, 2.6–3.9 W. | **Grounded** |
| Natural sulfide chimneys show thermoelectric behaviour; ORC/sCO₂ vent concepts in the kW range | Chimney electrochemistry/thermoelectric reports exist; kW cycles are modelled only. [to verify] | **Plausible-untested** |
| Docking stations with "ley-line nodes" fed by seismic and vent "input ports" | Ambient harvesting is real, but the power density is low. "Ley-line" is design language. | **Speculative** (scale) / **Symbolic** (ley lines) |

## 6. Open items

- Node dimensions, water-pocket size and the drive energy needed for any collapse-pressure estimate: [Channing to supply].
