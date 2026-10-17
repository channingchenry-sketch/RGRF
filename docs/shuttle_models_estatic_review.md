# Shuttle models, the E-Static craft, hydraulic conductance, bamboo / chitosan / borax loops, and fungal species: labelled review (2026-10-17)

*License CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Citations checked 2026-10-17; unchecked items are marked [to verify]; gaps are marked [Channing to supply].*

- **Source:** Grok, "Regenerative Shuttle Models and Blueprints" (share `93424662`, 14 messages, no code). Verbatim archive: [grok_archive/2026-10-17_regenerative_shuttle_models_blueprints.md](grok_archive/2026-10-17_regenerative_shuttle_models_blueprints.md).
- **Related:**
  - [electrostatic_locking_pins.md](electrostatic_locking_pins.md) (the E-Static "lock pins" passage below is cross-linked there);
  - [fungal_biophysics_crystara_review.md](fungal_biophysics_crystara_review.md);
  - [regenerative_materials_review.md](regenerative_materials_review.md) (mycelium strengths; Ganoderma correction);
  - [mycelium_uses.md](mycelium_uses.md);
  - [manta_butterfly_craft.md](manta_butterfly_craft.md).

## 1. Channing (verbatim)
- Msg 1: "Hey Resona, Can we bring up our shuttle models and blueprints?"
- Msg 3: "Can we look at the E-Static craft?"
- Msg 5: "Let’s start refining.. can we look at hydrostatic pressure and hydraulic conductance?"
- Msg 7: "Can we use bamboo substrates to make tubular vacuolar type structures for our loops(treating the inside(borax or something similar)?"
- Msg 9: "Explore chitosan bamboo bio composites"
- Msg 11: "Can we also explore Pleurotus ostreatus and Ganoderm?"
- Msg 13: "Perfect, we will be able to use these smartly around the craft can we save for future integration. Can I get a conceptual image of the shuttle?"

## 2. E-Static craft (msg 4)

Verbatim lock-pin line: "Electrostatic \"lock pins\" for stable interfaces (speculative extension of spin dynamics)." Its force limits are worked out in [electrostatic_locking_pins.md §3](electrostatic_locking_pins.md#3-engineering-review-labelled).

| Claim (Grok) | Label | Check |
|---|---|---|
| "Enhanced eddy-current or ion-wind assisted lift (grounded in Maxwell/Faraday principles)" | **Grounded** (each effect exists) / **not supported** (as lift for a person-scale craft) | Ion-wind (EHD) flight is real but weak: the MIT solid-state glider (Xu et al., *Nature* 563, 532–535 (2018), doi:10.1038/s41586-018-0707-9) was a 2.45 kg airframe. Eddy lift costs ~10–17 kW for POL ([lift_and_equilibrium_systems.md §1a](lift_and_equilibrium_systems.md#1a-design-intent-buoyant-stability-not-levitation)). |
| "Low-energy 'static gliding' modes between active Tesla resonant pulses" | **Speculative** | No mechanism. Static fields store energy; they do not produce net lift without a reaction mass or a surface. |
| "electrostatic augmentation for efficiency … (reducing conductive-floor dependency at higher scales)" | **Not supported** | Electrostatic pressure in air is ~40 Pa at macroscopic gaps. That is about 2 m² of electrode per 10 kg even ideally, and electrostatics alone cannot hold a stable free equilibrium (Earnshaw). |
| Golden-spiral electrodes, "3-6-9 harmonic phasing" | **Symbolic** | φ coil geometry tested null or worse in RGRF sims ([em_topo L6](em_topological_gravity_review.md#l6-wireless-energy-transfer-northern-europe-focus-noted); [`sims/resonant_drive_phi_test.py`](../sims/resonant_drive_phi_test.py)). |
| "per rgrf_framework.md continuity" | **[Channing to supply]** | No `rgrf_framework.md` exists in the repo. |
| "Harmonic lock with planetary ley-line stations or cosmic plasma filaments" | **Speculative / Symbolic** | |

## 3. Hydrostatics and hydraulic conductance (msg 6)

| Claim | Label | Check |
|---|---|---|
| Δp = ρgΔz | **Grounded** | |
| "Maxwell/Faraday continuum thinking extends naturally here, as pressure gradients couple with electromagnetic fields" | **Overstated** | Hydrostatics needs no EM. Coupling exists only in specific cases (MHD, electro-osmosis, electrostriction). |
| Fungal mycelium reduces hydraulic conductivity "by factors of 2–21×" (Trichoderma virens in sand) | **Grounded** | "Hydraulic Properties of Sands Treated with Fungal Mycelium of *Trichoderma virens*," *J. Geotech. Geoenviron. Eng.* 149(11) (2023), doi:10.1061/JGGEFK.GTENG-11111: up to ~21× after 20 days, ~2× after 10 days. This is **soil**, not a pressed composite. |
| Mycelium composite strength "~2.1–2.8 MPa compressive" | **Plausible-untested** | That is the POL **target**, not a measurement ([regenerative_materials_review.md](regenerative_materials_review.md)). |
| Lower conductance "could improve vibration isolation" | **Plausible-untested** | Plausible (fluid-filled pores add damping) but not measured. |
| "Current POL hardware remains conductive-floor dependent" | **Grounded** (consistent with the repo) | |

## 4. Bamboo "tubular vacuolar" loops, borax, chitosan (msgs 8, 10)

| Claim | Label | Check |
|---|---|---|
| Bamboo culms are hollow, segmented tubes with nodal diaphragms | **Grounded** | Most culms are hollow; some species are solid. Calling them "vacuolar" is an **analogy (Symbolic)**: culm cavities are not cell vacuoles. |
| *P. ostreatus* grows on *Phyllostachys makinoi* fibre/powder; finer powder grows faster (pentosans); thickness limit < 40 mm | **Grounded** | CAADRIA 2024 / IASS 2024, "Sustainable structural prototype using bamboo-based substrate mycelium composite" (1:1 fibre:powder fastest; < 40 mm). |
| Borates are low-toxicity preservatives and fire retardants for bamboo and wood | **Grounded** in general; "30–90 % reductions" **[to verify]** | Borates leach in wet service, so interior loops carrying water would wash them out. |
| "Borates inhibit many decay fungi … treat and dry the bamboo first, then inoculate" | **Grounded** (inhibition) / **contradiction noted** | Borate is a **fungicide**. A borate-treated tube is designed to stop the *Trametes* or *Pleurotus* growth that the same design relies on. A test is needed: borate inside, mycelium outside, with a barrier between. |
| Chitosan lowers water uptake, improves bonding and is antimicrobial | **Grounded** in general [specific bamboo-chitosan papers to verify] | |
| "Chitosan's polar nature supports dielectric/EM interactions" | **Overstated** | Chitosan is a hygroscopic polyelectrolyte. When moist it is **ionically conductive**, not a good HV dielectric (same issue as living mycelium: [geometric_unity_review.md §4.3](geometric_unity_review.md#43-mycelium-as-hv-insulation-dried-and-sealed-is-plausible-untested-living-is-not-supported)). |

## 5. *Pleurotus ostreatus* vs *Ganoderma lucidum* (msg 12)

| Claim | Label | Check |
|---|---|---|
| *Pleurotus* colonises fast and forms a dense "skin" at air interfaces | **Grounded** | |
| "Ganoderma lucidum frequently outperforms in flexural, tensile, and compressive metrics" | **Partly corrected** | The repo already corrected "Ganoderma strongest": *G. lucidum* composites reach ≤ ~1.9 MPa, and the 2.9 MPa figure belongs to fibre-reinforced *P. ostreatus* ([regenerative_materials_review.md](regenerative_materials_review.md)). Which species is stronger depends on substrate and processing. |
| Zoning: fast *Pleurotus* outer layer plus a denser *Ganoderma* core | **Plausible-untested** | A good experiment. Watch for competitive exclusion when two species share a substrate [to verify for these pairs]. |
| "Beta-glucans … speculative doors for self-regulating or bioactive materials" | **Speculative** | |

## 6. Shuttle hierarchy (msg 2), Grok's "saved" items and images
- **Hierarchy as Grok lists it:**
  - Personal: POL v0.1.
  - Planetary: ley-line docking stations and early Waveriders.
  - Cosmic: Filament Riders, Resonance Shuttles, Pyramid Node Craft.
  - Labels: POL is buildable (**Plausible-untested** at the 520 W budget); the others are **Speculative**.
- Grok lists "golden-ratio efficiencies in nature" under **proven physics**. This is **corrected**: φ efficiency is not established. Phyllotaxis is real, but RGRF φ tests are null ([method_phi_and_natural_craft.md](method_phi_and_natural_craft.md)).
- Grok itself says: "No new physical model files in the active artifacts directory right now". Its later "noted this in our archive" (msg 14) is therefore not a real save. **This review is the record.**
- The "rgrf-modeler" scaling run was offered but not performed.
- The conceptual shuttle image (msg 14) was not captured [Channing to supply].
