# Mycelium uses in POL / RGRF: inventory with honest labels

License: CC0 1.0. Evidence labels: **Grounded** / **Plausible-untested** / **Speculative**.

## Verified reference data
Jones, Mautner, Bismarck & John, "Engineered mycelium composite construction materials from fungal biorefineries: a critical review", *Materials & Design* 187, 108397 (2020). Citation verified.
- As-grown composites: density **~87–552 kg/m³**; compressive strength typically **~0.2–1.1 MPa** (e.g. wheat straw 0.17 MPa, white-oak sawdust 1.1 MPa).
- Insulation grades (straw/hemp): **57–99 kg/m³**, thermal conductivity **0.04–0.08 W/m·K**, comparable to glass wool or XPS.
- High acoustic absorption and good fire performance.
- Foam-like mechanics and high water absorption. The review recommends **non- or semi-structural** use.

**Discrepancy to flag:** the archive's POL frame spec (420–480 kg/m³, 2.1–2.8 MPa, "up to ~3.6 MPa optimized") is at or above the top of this range. That may be possible with heat-pressing or densification, but it needs a source or coupon tests.

## Uses found in the archive
| Use | Source (archive file) | Label |
|---|---|---|
| POL structural frame/deck: *Trametes versicolor* on hemp hurds/shives, ~18–22 kg | `docs/baseline_pol_v0.1.md`; `attachments/drafts/POL_RGRF_Specs_and_Blueprints_Plain_Text_2026-10-11.md`; `emails/2026-07-24_new-mycelium-bom-v0-2-ready.md` | Plausible-untested (as a deck under a rider; strength needs coupons) |
| Alternative species: *Ganoderma* in BOM | `emails/2026-05-29_updated-pol-bom-with-ganoderma-mycelium.md` | Grounded (common composite fungus) |
| Hover damping ("mycelium damping active") | `docs/hover_results.json`; Specs compilation | Speculative as hover stabiliser (cannot damp rigid-body heave; see `shifting_phase_order_review.md`). Material vibration damping itself is Plausible. |
| Thermal insulation / fire resistance ("Bath University 2026 OSB waste colonization") | Specs compilation; `docs/baseline_pol_v0.1.md` | Grounded in general (Jones 2020). The specific Bath 2026 work was not verified. |
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
