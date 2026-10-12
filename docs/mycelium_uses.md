# Mycelium uses in POL / RGRF: inventory with honest labels

License: CC0 1.0. Evidence labels: **Grounded** / **Plausible-untested** / **Speculative**.

## Verified reference data
Jones, Mautner, Bismarck & John, "Engineered mycelium composite construction materials from fungal biorefineries: a critical review", *Materials & Design* 187, 108397 (2020). Citation verified.
- As-grown composites: density **~87–552 kg/m³**; compressive strength typically **~0.2–1.1 MPa** (e.g. wheat straw 0.17 MPa, white-oak sawdust 1.1 MPa).
- Insulation grades (straw/hemp): **57–99 kg/m³**, thermal conductivity **0.04–0.08 W/m·K**, comparable to glass wool or XPS.
- High acoustic absorption and good fire performance.
- Foam-like mechanics and high water absorption. The review recommends **non- or semi-structural** use.

**Discrepancy to flag (updated):** the archive's POL frame spec (420–480 kg/m³, 2.1–2.8 MPa, "up to ~3.6 MPa optimized") is at or above the top of this range. That may be possible with heat-pressing or densification, but it needs a source or coupon tests.

## Uses found in the archive
| Use | Source (archive file) | Label |
|---|---|---|
| POL structural frame/deck: *Trametes versicolor* on hemp hurds/shives, ~18–22 kg | `docs/baseline_pol_v0.1.md`; `attachments/drafts/POL_RGRF_Specs_and_Blueprints_Plain_Text_2026-10-11.md`; `emails/2026-07-24_new-mycelium-bom-v0-2-ready.md` | Plausible-untested (as a deck under a rider; strength needs coupons) |
| Alternative species: *Ganoderma* in BOM | `emails/2026-05-29_updated-pol-bom-with-ganoderma-mycelium.md` | Grounded (common composite fungus) |
| Hover damping ("mycelium damping active") | `docs/hover_results.json`; Specs compilation | Speculative as hover stabiliser (cannot damp rigid-body heave; see `shifting_phase_order_review.md`). Material vibration damping itself is Plausible. |
| Thermal insulation / fire resistance ("Bath University 2026 OSB waste colonization") | Specs compilation; `docs/baseline_pol_v0.1.md` | Grounded; Bath 2026 work now verified (see Recent research) |
| Self-healing via mycelial regrowth | `docs/baseline_pol_v0.1.md`; `rgrf_framework.md` | Plausible-untested (needs live mycelium, which conflicts with heat-inactivation before use near coils) |
| Soft parts: VTT-style pulp-based mycelium leather (grips, covers) | Specs compilation | Grounded (mycelium leathers exist; VTT link not verified) |
| Non-conductive coil formers | Specs compilation; pathways note | Plausible-untested (check dielectric loss and moisture at 13.56 MHz / kHz) |
| Mycelium–graphene composites (high tensile, mm-scale diamagnetic gaps) | Specs compilation; `docs/baseline_pol_v0.1.md` | Speculative/unverified figures (">58 MPa", "0.14–0.16 mm gaps") |
| Mycelium–MXene EMI shielding | Specs compilation | Plausible-untested |
| Conductive mycelium (future floor) | Specs compilation | Speculative for eddy floors (needs ~10⁷ S/m) |
| Mycelium panels in housing; Mycobam blocks; bubble homes | `images/housing/body.txt`; `docs/regenerative_housing.md` | Insulation panels Grounded; structural blocks/shells Plausible-untested |
| Living-architecture docking stations, fleet surfaces (Manta-Butterfly) | `images/fleet/body.txt` | Speculative |
| "Living triad" bio-nodes (mycelium + bacteria + cyanobacteria) | RGRF `README.md` | Plausible-untested |
| Guild vs. single primary fungus (C11) | `emails/2026-08-26_mycelium-guild-vs-primary-fungus.md`; `rgrf_framework.md` | Open design question (snippet-only in archive) |
| Grow protocol (pasteurise/lime, inoculate, incubate, heat-inactivate, dry) | Specs compilation | Grounded practice |

## Gaps
- No coupon test data in the archive (density, compression, flexure, moisture, creep).
- No source for the 2.1–3.6 MPa figures.
- The self-healing claim conflicts with heat-inactivation.
- RF dielectric properties are untested.

## Recent research (2025–2026)
Source: screenshots `2026-10-11_mycelium_recent_1..5.png` in the archive. Every item below was checked by web search.

> Channing: some of this was speculated in May 2026 and is now being shown in research.

| Item | Verified source | Key facts | Label / POL relevance |
|---|---|---|---|
| Univ. of Bath: *T. versicolor* on waste OSB as insulation | "Valorisation of waste OSB into sustainable mycelium-based composites for insulation applications", *Scientific Reports* (2026), doi 10.1038/s41598-026-52430-w; Bath press release | λ = 0.0415 ± 0.001 W/m·K; ρ = 258 ± 3 kg/m³; GWP 0.1021 kg CO₂-eq/kg; >10× lower production carbon than EPS/XPS/mineral wool (press release); "fire-resistant" (press release); drying is the main emissions source | Grounded. Insulation, not structural. |
| Montana State: *Neurospora crassa* scaffolds mineralised by the fungus or by *Sporosarcina pasteurii* | "Mycelium as a scaffold for biomineralized engineered living materials", *Cell Reports Physical Science* (2025) | Viability retained ≥4 weeks; bacterial mineralisation stiffest; bone-mimetic internal geometries | Grounded as a living material. Self-healing not yet shown. |
| Hemp–mycelium ~0.040 W/m·K "review" | **Specific review not identified (flagged)** | Consistent with the Jones et al. 2020 band of 0.04–0.08 W/m·K | Grounded range; the exact citation is missing |
| CAS (SIAT): living *Cordyceps militaris* textiles | Li, An, … Zhong, "A programmable fungal platform for engineered living textiles", *Science Advances* (24 Jul 2026) | Pellet-cast sheets; a 4-strip rope held 1 kg; engineered yeast colours; melanised *A. niger* gives UV protection; regrowth repair; ~41-day soil degradation | Grounded (lab). The screenshot said "melanin-rich hyphae"; the paper attributes UV protection to *A. niger*. |
| Univ. of Maine: *T. versicolor* + cellulose nanofibril barrier coatings | "Growing Sustainable Barrier Coatings from Edible Fungal Mycelia", *Langmuir* (2025), doi 10.1021/acs.langmuir.5c03185 | Water contact angle 139°; oil/grease Kit Test 12; on paper, denim, felt and veneer | Grounded. Possible moisture skin for POL/housing. |
| Shiitake memristors | LaRocco et al., "Sustainable memristors from shiitake mycelium for high-frequency bioelectronics", *PLOS ONE* 20(10): e0328965 (10 Oct 2025) | Up to 5.85 kHz at 90 ± 1 % accuracy; preserved by dehydration | Grounded (lab). Not relevant to lift. |
| McMaster: *Schizophyllum commune* genetic "dial" | "Splitting the difference: Genetically-tunable mycelial films using natural genetic variations in *Schizophyllum commune*", *J. Bioresources & Bioproducts* (2025), doi 10.1016/j.jobab.2025.05.004 | Genotype × crosslinker (glycerol vs PEG-400) drives the properties; up to 98 % elongation | Grounded |
| VTT: continuous mycelium-leather sheet production | VTT news release; "Production of Mycelium-Based Nonwoven Fabrics via Submerged Fermentation", *ACS Appl. Bio Mater.* (2026) | Wet-cast onto a moving substrate at 1 m/min; tensile strength 11–19 MPa; pilot drying and winding not fully shown | Grounded (pilot) |

## Comparison table (Channing, verbatim)
| Property | POL v0.1 target | Bath 2026 OSB-MBC | Typical hemp-mycelium lit | Note |
|---|---|---|---|---|
| Density | 420-480 kg/m3 | ~258 | 99-150 | POL densified for structural loads |
| Thermal conductivity | Competitive/bonus | 0.0415±0.001 | ~0.0404 | same band as mineral wool/EPS |
| Compressive strength | 2.1-2.8 MPa (up to ~3.6) | not headline | 0.5-1.2 typical, higher hot-pressed/densified | POL needs higher end; densification or hybrid skins required |
| Carbon/GWP | low by design | >10x lower than EPS/XPS/mineral wool; 0.102 kg CO2-eq/kg | very low with agrowaste | strengthens regenerative case |
| Fire | expected favorable (char) | reported fire-resistant | generally good | |
| Primary role | structural frame + damping | insulation + waste remediation | insulation/packaging | |
| Living function | inactivated (heat-killed); self-healing experimental only | inactivated | usually inactivated | matches protocol |

**Notes:**
- The POL compressive target (2.1–2.8 MPa, up to ~3.6) exceeds the Jones et al. 2020 range for as-grown composites (~0.2–1.1 MPa). It needs coupon tests.
- The Bath column is verified.
- The "typical hemp-mycelium" column values (99–150 kg/m³, ~0.0404 W/m·K) are Channing's summary and were not traced to one source.
