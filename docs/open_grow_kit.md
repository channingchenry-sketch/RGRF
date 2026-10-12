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

*Note on the Living vs. inactivated row (added after the verbatim table): a grow-in-place-then-borate-cure route is a third option. It is cured, so it is not living; see "Grow in place, then cure" below.*
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

## Grow in place, then cure (borax + copper ventilation)
**Channing's idea:**
- Grow the living structure in situ, e.g. a bubble shell on its form.
- Then cure it in place with borax rather than moving panels to an oven.
- Run copper tubes through the shell for airflow and mould deterrence.

### Borates (borax / boric acid): Grounded for wood and bamboo
- **Preservative.**
  - Borates protect wood against decay fungi and insects, including all termite species.
  - About 1.5 kg/m³ boric-acid equivalent inhibits decay, and ≥3.2 kg/m³ protects against both decay and insects.
  - Source: Freeman, McIntyre & Jackson, "A critical and comprehensive review of boron in wood preservation", AWPA Proceedings (2008), verified.
- **Bamboo against *T. versicolor*.** 2 % and 6 % borax–boric-acid treatments put three bamboo species in European durability class I against *T. versicolor* and two brown-rot fungi. Source: "Fungal degradation of bamboo treated with crude lake salt and a mixture of borax and boric acid" (ScienceDirect, 2024), verified. *T. versicolor* was named among the test fungi.
- **Fire.**
  - Borates promote char and a glassy layer. Borax reduces flame spread but promotes smouldering; boric acid does the reverse, so the two are combined.
  - Borate levels high enough for biological protection are **usually too low for reliable fire retardancy**.
  - Source: USDA Forest Products Laboratory, "Flame-retardant design and protection for wood and wood products" (2024), verified.
- **Leaching.**
  - Inorganic borates are water-soluble. Standards limit them to above-ground uses **protected from rain wetting**: Obanda, Shupe & Barnes, "Reducing leaching of boron-based wood preservatives – a review of research", *Bioresource Technology* (2008), verified.
  - Wood treated with boric acid or borax lost fire resistance after a year of humid exposure (Vakhitova 2019, as cited in a zinc-borate study).
  - So an outdoor shell needs a weather skin or coating, and re-treatment.

### Does borate alone kill *T. versicolor* in a colonised composite? Not verified (flagged)
- **Verified:**
  - Borates *prevent* colonisation and decay by *T. versicolor* in pre-treated wood and bamboo. In poplar, 0.5–2 % boric acid stopped visible growth (BioResources 5(2), 2010).
  - Agar studies show complete growth inhibition for some fungi but not others at ≤0.5–1 %.
- **Not found:** any study showing that soaking or spraying an **already fully colonised** mycelium block with borax reliably kills *T. versicolor* throughout its thickness.
- **Recommendation:**
  - Treat the borate cure as **Plausible-untested** for inactivation.
  - Verify it with a re-growth test: put a core sample on malt agar for 14 days and look for no outgrowth.
  - Keep heat-kill as the reference method where possible.

### Copper ventilation tubes
- **Grounded but narrow.**
  - On 29 Feb 2008, the US EPA registered antimicrobial copper alloys (≥60 % Cu). The claim is limited to ">99.9 % of six specified **bacteria** within 2 h on regularly cleaned touch surfaces", as a supplement to cleaning (EPA fact sheet; Copper Development Association), verified.
  - It is **not** a registered claim against moulds, and the effect is **surface-contact only**.
- **Main mould control is airflow, drying and vapour management.** Tubes help mainly by moving air, and the metal adds little beyond its own surface.
- **Condensation risk.** Cold copper (high conductivity) running through a warm, humid shell will drop below the dew point and wet the adjacent mycelium. That is the opposite of the goal. Insulate or sleeve the tubes, route them so drips drain out, and monitor relative humidity.

### Tradeoff
- A cured shell is **not living**: no self-healing or regrowth.
- The living-repair-layer option in Table A remains **Speculative** and is incompatible with a borate-cured layer next to it, because borate would inhibit the repair growth.

**Labels:**
- Borate preservation and fire behaviour (wood/bamboo): **Grounded**.
- Borate cure of in-situ mycelium: **Plausible-untested**.
- Copper as mould deterrent: weak, surface-only.
- Ventilation itself: **Grounded**.

## Published mycelium test results (for comparison with the 2.1–3.6 MPa target)
| Study (verified) | Material / process | Result |
|---|---|---|
| Appels et al., *Materials & Design* 161:64–71 (2019), doi 10.1016/j.matdes.2018.11.027 | *Trametes multicolor* / *Pleurotus* on straw, cotton or sawdust; non-, cold- and hot-pressed | Flexural strength: non-pressed 0.05–0.29 MPa; **hot-pressed 0.62–0.87 MPa** ("cork- and wood-like") |
| "Mechanical properties of dense mycelium-bound composites under accelerated tropical weathering conditions", *Scientific Reports* (2021), doi 10.1038/s41598-021-01598-4 | Hot-pressed at 120 °C / 20 MPa / 50 min, ~954 kg/m³ | **Compressive ~4.4 MPa before weathering**; after 35 days of tropical weathering ~0.7 MPa uncoated, ~2.2 MPa coated (figures from abstract/search summary) |
| Jones et al., *Materials & Design* 187, 108397 (2020), review | As-grown composites | Compressive ~0.2–1.1 MPa; densities 87–552 kg/m³ |
| Jones et al., "Thermal degradation and fire properties of fungal mycelium and mycelium–biomass composite materials", *Scientific Reports* 8 (2018), doi 10.1038/s41598-018-36032-9 | Cone calorimeter at 50 kW/m² | Peak heat-release rate ~180 kW/m² for composites vs ~200 kW/m² for the uncolonised substrate (~10 % lower); char layer protective |
| Hy-Fi, The Living with Ecovative and Arup, MoMA PS1 (2014) | ~10,000 corn-stalk / mycelium bricks, ~13 m (40 ft) temporary tower | Stood for a summer (scaffold planks limited wind sway), then composted. No published compressive value found; Arup's first strength check was literally a structural engineer standing on a brick. |

**Takeaway.**
- The POL 2.1–3.6 MPa target is reachable in principle only with heavy densification (~950 kg/m³, about double the POL 420–480 kg/m³ density target).
- At 420–480 kg/m³, published values suggest ~1 MPa or less.
- Weathering cut strength by ~50–85 %, so a protective skin is essential.
- **Coupon testing remains required.**

## Selective living / long-term vision
*Left here for now; more material will follow.*

Channing's ultimate goal is to **keep panels living where living is useful**, rather than inactivating everything.

| Element | Description | Label |
|---|---|---|
| Selective zones | Cured or inactivated structural shell (heat-killed or borate-cured), plus separately contained living layers (interior living wall, repair layer) | Speculative as an integrated building system. The two zones must be isolated: borate or heat in one zone kills or inhibits the other. |
| Food-growing panels | Fruiting surfaces of edible species, e.g. oyster mushroom (*Pleurotus ostreatus*). **Note: *T. versicolor* (turkey tail) is not a culinary mushroom.** It is tough and leathery, and is used mainly for teas and extracts. | Mushroom cultivation on lignocellulose is Grounded. Fruiting *on a building panel* is Plausible-untested (spore load, humidity and indoor-air issues; see Safety). |
| Living walls | Plant or moss green walls on a cured mycelium backing | Green walls are Grounded. A mycelium backing is Plausible-untested (moisture and decay). |
| Petrification / mineralisation | Microbially induced calcite precipitation (MICP): ureolytic *Sporosarcina pasteurii* hydrolyses urea, raising pH, and CaCO₃ precipitates and binds the matrix. MICP is reviewed in "Microbial-induced carbonate precipitation (MICP) technology: a review on the fundamentals and engineering applications" (2023, PMC open access), verified. *N. crassa* mycelium scaffolds mineralised by the fungus or *S. pasteurii* stayed viable for ≥4 weeks (*Cell Rep. Phys. Sci.* 2025, cited above). | MICP Grounded. A "petrified" living building panel is Speculative (ammonium by-product, uniformity, scale). |

**Maintenance protocol outline (draft; Plausible-untested):**
1. **Moisture:** log relative humidity and panel moisture weekly. Keep living zones moist and structural zones dry, with a vapour break between them.
2. **Feeding:** add a periodic nutrient or substrate top-up for the living layers only.
3. **Contamination checks:** look for green, black or orange moulds, odour and soft spots. Remove and replace affected panels.
4. **Fruiting harvest:** harvest before spore drop. Ventilate during fruiting, and don't fruit in sleeping areas.
5. **Pest inspection:** check for fungus gnats, mites, beetles and termites. A borate-cured shell resists insects; living layers don't.
6. **Replacement:** design living panels as removable cassettes with a defined service life.

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
