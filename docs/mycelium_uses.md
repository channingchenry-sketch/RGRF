# Mycelium uses in POL / RGRF: inventory with honest labels

License: CC0 1.0. Evidence labels: **Grounded** / **Plausible-untested** / **Speculative**.

## Verified reference data
Jones, Mautner, Bismarck & John, "Engineered mycelium composite construction materials from fungal biorefineries: a critical review", *Materials & Design* 187, 108397 (2020). Citation verified.
- As-grown composites: density **~87–552 kg/m³**; compressive strength typically **~0.2–1.1 MPa** (e.g. wheat straw 0.17 MPa, white-oak sawdust 1.1 MPa).
- Insulation grades (straw/hemp): **57–99 kg/m³**, thermal conductivity **0.04–0.08 W/m·K**, comparable to glass wool or XPS.
- High acoustic absorption and good fire performance.
- Foam-like mechanics and high water absorption. The review recommends **non- or semi-structural** use.

**Discrepancy to flag (updated):** the archive's POL frame spec (420–480 kg/m³, 2.1–2.8 MPa, "up to ~3.6 MPa optimized") is at or above the top of this range. That may be possible with heat-pressing or densification, but it needs a source or coupon tests.

**Note (2026-10-17):** a Grok figure of "up to ~1–2.9 MPa (Ganoderma lucidum strongest)" traces to two different results. *G. lucidum* reaches up to ~1.91 MPa; 2.9 MPa is fibre-reinforced *Pleurotus ostreatus* (Lewandowska, Sydor & Bonenberg, *Sustainability* 17(24), 11350 (2025)). Neither is *Trametes* on hemp, so the POL target is still unsourced. See [regenerative_materials_review.md §1.1](regenerative_materials_review.md#11-mycelium-based-composites-mbcs).

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

## Nodal structuring & mechanical conditioning
Source: screenshots `2026-10-11_nodal_1.png` and `_2.png` in the archive (Grok summary), plus Channing's new idea. Every citation was checked by web search.

### What controls "node" density today
| Lever | Evidence | Label |
|---|---|---|
| **Living-textile node patterning.** In *C. militaris* sheets, nutrient-induced aerial hyphae grow in deliberate patterns after the sheet is formed (Li et al., *Science Advances*, 2026, cited above). This is spatial control of new growth after fabrication. | Verified | Grounded (lab, textile scale) |
| **Hot-pressing / densification** after colonisation. It collapses free volume, raises contact-point density and increases stiffness. It is the practical lever from insulation grade (~250 kg/m³) toward the POL range (420–480 kg/m³). | General literature (e.g. Jones et al. 2020 review); already in the grow protocol | Grounded direction. POL-range strength still Plausible-untested. |
| **Mineralising scaffolds** (*N. crassa* ± *S. pasteurii*; *Cell Rep. Phys. Sci.* 2025, cited above). CaCO₃ stiffens the network, cells stay viable for ≥4 weeks, and bone-like internal geometries were shown. | Verified | Grounded (lab) |

### Gaps (listed by Grok)
- Quantitative models that link measured node topology (CT / micro-CT) to the damping coefficient and compressive strength under **cyclic rider loads**. The qualitative story exists; the closed-loop numbers are thin.
- Scalable methods to **place or reinforce high-stress nodes** (under foot pads or coil mounts) instead of relying on uniform colonisation.

### Two near-term paths
1. Keep **density + hot-press** as the primary node-density lever.
2. Use pure-mycelium or lightly reinforced **surface skins** (VTT-style sheets or living-textile methods) as a test bed for deliberate node patterning, without risking the main structural core.

### Channing's idea: mechanical stress conditioning to induce denser nodes
The idea: apply mechanical stress during growth to living mycelium, hemp and bamboo, so that they lay down denser nodes or reinforcement where loads act.

**Grounded analogs:**
- **Thigmomorphogenesis in plants.**
  - Jaffe, *Planta* 114:143–157 (1973), doi 10.1007/BF00387472. Rubbing internodes ~10 s once or twice daily significantly retarded elongation in several species; growth recovered 3–4 days after stopping. Possibly ethylene-mediated.
  - The response is shorter, stockier growth, not proven "denser nodes".
- **Bamboo nodes and diaphragms.**
  - In *Phyllostachys iridescens* (Wang et al., *Forests* 15(10):1740, 2024, doi 10.3390/f15101740; year verified), nodes with diaphragms gave ~+250 % radial stiffness and ~+92 % bending MOE versus internodes, with ~+10 % compressive strength and lower tensile properties.
  - Buckling studies are mixed: one found nodes had little effect on the critical buckling load (Suada et al., *ARPN J. Eng. Appl. Sci.*, 2020); modelling shows nodal and diaphragm thickness raises local buckling load.
  - So nodes help ring and bending stiffness more than axial strength.
- **Reaction wood (tension and compression wood).** Trees form specialised wood in response to sustained lean or load. This is textbook plant biology, so no single citation is given.
- **Hemp fibre response to wind or mechanical stimulation:** **no direct study found (flagged).** Hemp fibre properties do shift with cultivation stress (e.g. drought raised fibre modulus in one study), but controlled wind or flexing trials on fibre mechanics were not identified.
- **Fungal mechanosensing (verified):**
  - Fungi have stretch-activated, Ca²⁺-permeable channels: Zhou et al., *Science* 253:1415 (1991), *Uromyces*.
  - Hyphae show thigmotropism (*C. albicans* Mid1/Cch1).
  - Reviewed in Kumamoto, "Molecular mechanisms of mechanosensing and their roles in fungal contact sensing", *Nat. Rev. Microbiol.* 6:667–673 (2008), doi 10.1038/nrmicro1960 (verified).
  - So hyphae *can* sense force. Whether cyclic load changes branching or node density in a growing composite is untested.

**Tags:**
- Plants and bamboo responding to stress: **Grounded**.
- Stress-conditioned hemp fibre: **Plausible-untested**.
- Stress-conditioned mycelium node density: **Plausible-untested**.
- Targeted node placement under foot pads or coil mounts: **Speculative** until shown.

### Bench test: cyclic-loaded vs unloaded colonising blocks
1. Inoculate matched *T. versicolor* / hemp-hurd blocks (n ≥ 6 per group, same substrate batch and moisture).
2. During colonisation (days 3–14), apply gentle cyclic compression to one group, e.g. 1–5 kPa at ~0.1–1 Hz for a few minutes per hour, using a cam or servo press. Keep a sham-handled control group at the same temperature and humidity.
3. Heat-inactivate and dry both groups identically, with optional identical hot-press.
4. Measure:
   - density;
   - micro-CT network metrics (hyphal volume fraction, junction/node density, pore size);
   - compression (modulus, 10 % strength);
   - cyclic-compression damping (loss factor).
5. Pass/fail: the loaded blocks show a statistically higher node density **and** modulus or damping at equal density. A density-only increase means compaction, not conditioning.
