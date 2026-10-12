# Open grow kit (draft)

> **Draft: more material is being rebuilt.** Channing-approved; CC0 1.0.
> Evidence labels: **Grounded** / **Plausible-untested** / **Speculative**.

## Table A: From POL protocol to bubble homes (Channing, verbatim)
| Requirement | Current POL protocol | Needed for bubble homes | Status |
|---|---|---|---|
| Safety & air quality | Basic ventilation note | Indoor air, spore control, fire performance of full assembly | Incomplete |
| Moisture & weather | Basic water-uptake note | Long-term outdoor envelope performance, vapor control, UV/skin | Needs testing plan |
| Form geometry | Flat or simple moulds | Inflatable or rigid dome forms, geodesic or free-form bubbles | Not written |
| Living vs. inactivated | Heat-kill required for service | Possible hybrid: inactivated structural shell + living repair layer or interior living wall | Speculative |
| Joints & nodes | Not addressed | Overlapping hyphal bonds, mechanical fasteners, or grown-in connection nodes | Open |
| Open kit packaging | Protocol text only | Actual spawn + substrate starter quantities, mould suggestions, measurement log sheet | Not assembled |
| Layering | Single substrate | Multi-layer (structural core + insulation + living or weather skin) | Conceptual only |
| Scale | ~0.3 m panels | 2-6 m diameter shells or segmented panels that assemble into a bubble | Scale-up notes missing |

## Table B: Starter panel spec (Channing, verbatim)
| Parameter | Specification | Notes |
|---|---|---|
| Panel size | ~300x300x30 mm | small test/starter |
| Substrate | hemp hurds (primary) or chipped waste OSB | two tracks |
| Spawn rate | ~10% wet mass | T. versicolor |
| Target density | 420-480 kg/m3 (structural hemp) | OSB track ~258 (insulation) |
| Compressive strength | 2.1-2.8 MPa baseline (up to ~3.6 optimized) | structural target |
| Thermal conductivity | bonus; Bath OSB 0.0415 W/mK | competitive |
| Colonization | 5-14 days at 20-24 C | until white bind |
| Finish | heat-inactivate + dry; optional modest hot-press | living tissue not left in service |
| Role | deck, rails, damping (POL); skins/thermal breaks (OSB) | not full structural lumber |

**Strength caveat.** The 2.1–3.6 MPa target is above the range published for as-grown mycelium composites in Jones et al., *Materials & Design* 187, 108397 (2020): roughly 0.2–1.1 MPa. Treat it as **Plausible-untested** until coupon tests confirm it (see `mycelium_uses.md`).

## Starter quantities for one 300 × 300 × 30 mm panel (estimate)
- Panel volume: 0.3 × 0.3 × 0.03 m = **2.7 L**.
- Dry finished mass at 420–480 kg/m³: **~1.13–1.30 kg**.

**Hemp track.** All assumptions below are rough; adjust them using your log.
- **Dry hurds ~1.2–1.5 kg.** This assumes ~5–15 % dry-mass loss to fungal metabolism.
- **Hydrated substrate ~3.2–3.9 kg.** This assumes ~60–65 % moisture, wet basis (dry ÷ 0.38).
- **Spawn ~0.3–0.4 kg** (~10 % of wet mass).
- **Densification is required.** Loose hemp hurds are roughly 100–150 kg/m³, so 1.3 kg of dry hurds fills ~9–13 L loose. Reaching 420–480 kg/m³ in 2.7 L means compressing the mix ~3–4× in the mould, or hot-pressing after colonisation. Unpressed packing will land near insulation density.

**OSB track (insulation, ~258 kg/m³).** About 0.7 kg dry mass, ~0.75–0.8 kg dry chips, and ~0.2 kg spawn.

## Citizen-science measurement log
A CSV copy is at [`grow_log_template.csv`](grow_log_template.csv).

| Field | Example / unit |
|---|---|
| batch_id | 2026-10-A1 |
| date_inoculated | YYYY-MM-DD |
| substrate | hemp hurds / OSB chips (source) |
| spawn_pct | % of wet mass |
| moisture_pct | % wet basis (weigh, oven-dry a sample) |
| temp_C | mean / min / max |
| days_to_bind | days to full white bind |
| wet_mass_g / dry_mass_g | g |
| L_mm, W_mm, T_mm | mm |
| density_kg_m3 | dry_mass_g / (L·W·T mm³) × 10⁶ |
| hot_press | none / temp °C, pressure, minutes |
| contamination_notes | green/black/orange moulds, smell, wet spots |
| photo_refs | file names |
| crush_test | see below |
| water_uptake_24h_pct | (wet − dry)/dry after 24 h soak |
| burn_test_notes | see below |

**Simple home tests.** These are indicative only, not engineering data.
- **Crush test (bathroom scale).** Place a 50 × 50 mm cube on the scale and press with a flat board until it cracks or reaches 10 % strain. Stress ≈ reading (kg) × 9.81 / 0.0025 m². For example, 100 kg on the scale is ≈ 0.39 MPa. Bathroom scales max out at ~150 kg (~0.6 MPa), so higher-strength samples need a lab press. Wear eye protection and keep your hands clear.
- **24 h water uptake.** Weigh, submerge for 24 h, blot, and weigh again.
- **Burn test.** Do this outdoors only, on bare ground or masonry, away from anything flammable, with water or an extinguisher at hand and never indoors. Hold a small offcut in a flame for 10 s, then note char, flaming, afterglow and self-extinguishing time. This is a rough comparison, not a fire rating.

## Safety notes
- **Spores and respiratory health (Grounded).** Wear an N95/FFP2 mask when opening bags, breaking up or sanding material. Work in ventilated spaces. Don't let panels fruit indoors.
- **Contamination (Grounded).** Green, black or orange moulds (e.g. *Trichoderma*, *Aspergillus*, *Neurospora*) mean the batch should be bagged and discarded. Don't dry contaminated panels indoors.
- **Heat-kill before use (Grounded practice).** Finished panels should be oven-inactivated and fully dried. The protocol does not leave living tissue in service.
- **Who should not grow.** People who are immunocompromised, or who have asthma or mould allergies, should not handle cultures or contaminated batches.
- This is a hobby and research kit, not a certified building product.

## Toward a housing-first protocol (draft placeholder)
Channing's goal is that open, low-cost grown materials help people get safe shelter.

**Reality check:**
- Mycelium shells and bubble homes are **not code-approved for occupancy**.
- Any public program would need structural, fire, moisture and indoor-air-quality testing and certification under local building codes. Until then, uses are limited to prototypes, non-habitable structures and supervised research.
- See `regenerative_housing.md` for code context.

**Housing First (Grounded policy evidence).** Housing First provides housing without treatment or sobriety preconditions.
- In a randomized trial, it housed people earlier and kept them more stably housed, with no worsening of substance use or psychiatric symptoms: Tsemberis, Gulcur & Nakae, "Housing First, Consumer Choice, and Harm Reduction for Homeless Individuals With a Dual Diagnosis", *Am. J. Public Health* 94(4):651–656 (2004), doi 10.2105/AJPH.94.4.651 (verified).
- RGRF materials work could someday supply housing. The policy evidence is about access and support, not building materials.

**Missing:** form and dome protocols, joint design, multi-layer specs, scale-up, an outdoor weathering plan, and a certification pathway.
