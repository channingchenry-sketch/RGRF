# Geodesic Organic Design, Fuller domes, bamboo–hempcrete–mycelium, Heartbeat Engines: labelled review (2026-10-17)
*License CC0. Review of the Grok share "Geodesic Organic Design: Nature Meets Geometry" (capture `00fe7109`, 22 messages). Verbatim archive: [grok_archive/2026-10-17_geodesic_organic_design.md](grok_archive/2026-10-17_geodesic_organic_design.md). Grok's pulse-efficiency pseudocode (message 16): [sims/legacy_grok/heartbeat_pulse_efficiency.py](../sims/legacy_grok/heartbeat_pulse_efficiency.py), run by [sims/legacy_grok/run_s14_21_legacy.py](../sims/legacy_grok/run_s14_21_legacy.py). Numerical checks: [sims/grok_claim_checks_2026_10_17.py](../sims/grok_claim_checks_2026_10_17.py) ([output](../sims/grok_claim_checks_2026_10_17_output.txt)).*

**Labels:** Grounded · Plausible-untested · Speculative · Symbolic. φ is **Symbolic** unless a test shows otherwise. Grok's simulation results are **Grok-reported** unless rerun. A city name is removed from the archive, and one phrase in message 4 is omitted under the repo content rules.

## 1. The named files: what the capture actually contains

| File named by Grok | In the capture? | Archived as |
|---|---|---|
| `hover_dynamics.py`, `rgrf_scaler.py`, `resonance_calc.py` (msg 18) | **Results only**, no code | The results are quoted in the archive, message 18, and checked in §4. Code: [Channing to supply]. |
| `Updated_BOM_and_Build_Guide_Regenerative_Designs_v0.2.md` (12.45 KB, msg 10) | **File chip only** ("Some files couldn't be displayed") | Only the inline "Cross-Scale BOM Additions (excerpt from v0.2)" in message 14 is visible. Full file: [Channing to supply]. |
| `Heartbeat_Engines_Design_Paths_and_BOM_v0.1.md` (13.61 KB, msg 12) | **File chip only** | The three design paths are summarised inline in messages 12–14 and 20. Full file: [Channing to supply]. |
| `Inspirations_Nikola_Tesla.md`, `…_Leonardo_Da_Vinci.md`, `…_Buckminster_Fuller.md`, `…_Eric_Weinstein.md`, `…_Michio_Kaku.md` (msg 22) | **Inline summaries only** | Each summary is archived verbatim in message 22 (the visible content). Whether longer files exist: [Channing to supply]. |
| Pulse-efficiency pseudocode (msg 16) | **Yes** | Saved verbatim as `sims/legacy_grok/heartbeat_pulse_efficiency.py`. |

Grok also says in message 18: "No earlier simulation graphs existed in artifacts prior to this consolidation". So the "Latest Run (June 2, 2026)" numbers below are the only record.

## 2. Geodesic domes and Fuller (messages 1–4)

| Claim | Label | Check |
|---|---|---|
| Bauersfeld's 1920s planetarium dome (Zeiss, Jena) came first | **Grounded** | 1922–26. |
| Fuller's Black Mountain College prototypes (1948–49) | **Grounded** | |
| U.S. patent 2,682,235 (1954) | **Grounded** | "Building construction", granted 29 June 1954. |
| Expo 67 dome, 250 ft diameter; Ford Rotunda dome; Fuller's Carbondale home | **Grounded** | |
| Doubling the diameter quadruples area and multiplies volume by eight | **Grounded** | Area ∝ D², volume ∝ D³. |
| "~30% lower energy use for heating/cooling vs. traditional homes" | **[to verify]** | Commonly repeated; no measured study was cited. Less surface per volume does lower losses, so **Plausible-untested** as a figure. |
| Geoship builds factory domes | **Grounded** (company exists) | Bioceramic domes; status of deliveries [to verify]. |
| Domes have acoustic, furniture, precision and permitting drawbacks | **Grounded** | Grok's own honest list. |

## 3. Bamboo dowels in hempcrete, overgrown with mycelium (messages 5–10)

Channing: "Let’s add our bamboo dowel rods into hempcrete blocks covered in our mycelium substrate."

| Claim | Label | Check |
|---|---|---|
| Bamboo is strong in tension | **Grounded** | Culm tensile strength roughly 100–400 MPa depending on species and fibre content. |
| Hempcrete as structure | **Corrected** | Hempcrete (hemp hurd + lime) is an insulating infill with compressive strength of order 0.2–1 MPa. It is **non-structural**; it needs a frame. See [regenerative_materials_review.md](regenerative_materials_review.md). |
| Bamboo inside lime hempcrete | **Plausible-untested**, with a known risk | Lime is strongly alkaline (pH ~12). Natural fibres lose strength in alkaline binders over time; bamboo would need a coating or a lower-pH binder [specific study to verify]. |
| Mycelium overgrowth on hempcrete | **Plausible-untested**, with a known conflict | *Trametes versicolor* grows best in mildly acidic substrates (about pH 5–6) [to verify]. Fresh lime surfaces are far too alkaline. Grow the mycelium on its own substrate, then bond it, or wait for carbonation. |
| Mycelium composites are "fire-resistant" | **Plausible-untested** | Mycelium chars rather than flames, but this is not a fire rating: M. Jones et al., "Thermal degradation and fire properties of fungal mycelium and mycelium-biomass composite materials," *Sci. Rep.* 8, 17583 (2018) [details to verify]. |
| Living, carbon-sequestering walls | **Speculative** | A dried composite is no longer growing. Living walls need moisture that also degrades the structure. |

## 4. Grok-reported model results (message 18) and the contradictions

| Grok-reported result | Label | Check |
|---|---|---|
| `hover_dynamics.py`: 85 kg rider at 0.10 m, settle ~0.1 s, **88.3 % efficiency, 459 W delivered** | **Contradicted** | The repo's eddy-current models need ~10–17 kW ([ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md)); Maxwell stress gives ~14.6 kW for 88 kg ([lift_and_equilibrium_systems.md §9b](lift_and_equilibrium_systems.md#9b-maxwell-stress-magnetic-pressure-and-pol-lift-2026-10-17)). 459 W is the same order as the earlier 520 W claim and is about 30× too low. |
| `resonance_calc.py`: 8-turn φ coil → **636 µH**, 93 % at **13.56 MHz** | **Contradicted** | Resonating 636 µH at 13.56 MHz needs C = 0.217 pF, below any real coil's self-capacitance. With 2–10 pF of parasitic capacitance the coil self-resonates at about 2–4.5 MHz, so it cannot be tuned to 13.56 MHz. 636 µH from 8 turns would also need a very large or cored coil. |
| `rgrf_scaler.py`: docking station radius **26.18 m**, 41.9 MHz harmonic | **Symbolic** | 26.18 = 10·φ². φ was put in, so it comes out. |
| Pure Resonant Coil "80–95% potential efficiency at resonance" (msgs 16, 20) | **Plausible-untested** for mm-scale gaps only | Efficiency falls fast with distance: A. Kurs et al., *Science* 317, 83–86 (2007), about 40 % at 2 m. See [tesla_and_ancient_alignments.md](tesla_and_ancient_alignments.md). |
| POL "human-powered hoverboard" (msg 20) | **Contradicted** | See [legal_safety_and_grounding_review.md §3](legal_safety_and_grounding_review.md#3-the-human-powered-levitator-and-eddy-current-lift). |
| φ timing "for minimal damping" | **Symbolic**; tested null | [sims/resonant_drive_phi_test.py](../sims/resonant_drive_phi_test.py). |

### The pulse-efficiency pseudocode, run
As captured, `heartbeat_pulse_efficiency(1.0)` raises **NameError** (`omega_resonant` is never defined). Supplying `omega_resonant = 2π·1 Hz` gives **5592 "%"**: at resonance the function returns Q·e^(−0.1)·0.618·100 with Q = 100, so the "efficiency" is not bounded by 100 %. The φ weighting `(phi_ratio % 1)` is just the constant 0.618 (φ = 2.618 would give the same number). Grok's comment "High efficiency near resonance" describes a Lorentzian peak, not an efficiency.

## 5. Heartbeat Engines at ~0.8–1.2 Hz (messages 11–16)

| Claim | Label | Check |
|---|---|---|
| A ~1 Hz "heartbeat" pulse drives lift or eddy coupling | **Not supported** | Eddy-current lift scales with frequency. At 1 Hz the aluminium skin depth is ~8.2 cm, so a plate is almost transparent and the repulsive force is tiny. Practical eddy lift needs hundreds of Hz to kHz. A slow envelope on a fast carrier is fine; the 1 Hz itself does no lifting. |
| Fungal electrophysiology (spiking) exists | **Grounded** | A. Adamatzky, "Language of fungi derived from their electrical spiking activity," *R. Soc. Open Sci.* 9, 211926 (2022) [to verify]. Using it to time a power pulse is **Speculative**. |
| Low-voltage Arduino-style pulse drivers, copper phi-spiral coils (BOM excerpt) | **Grounded** parts | Buildable bench items. |

## 6. Inspirations (messages 15–16, 21–22)

| Person / claim | Label | Note |
|---|---|---|
| Tesla: resonant transformer (patent 454,622, 1891), Wardenclyffe | **Grounded** history | Long-range Earth transmission was never demonstrated (Grok says so). Cross-link: [tesla_davinci_threads.md](tesla_davinci_threads.md). |
| Da Vinci illustrated Pacioli's *De divina proportione* | **Grounded** | φ in his paintings "interpretive" (Grok's own note) is right; see [skinwalker_rf_music_vortex_review.md §5](skinwalker_rf_music_vortex_review.md#5-vortex-mathematics-rodin-coil-da-vinci-messages-1922). |
| Fuller: synergetics, tensegrity | **Grounded** history | |
| Eric Weinstein: Harvard PhD in mathematics; Geometric Unity "not fully published/tested" | **Grounded** / **Speculative** | GU itself: [geometric_unity_review.md](geometric_unity_review.md). "Pulse rhythms as connections on fiber bundles" is **Symbolic**. |
| Michio Kaku co-founded string field theory | **Grounded** | M. Kaku & K. Kikkawa, *Phys. Rev. D* 10, 1110 (1974). An "informed universe" as Kaku's own thesis: [to verify]; treat as **Symbolic** here. |

## 7. Open questions for Channing
1. Code for `hover_dynamics.py`, `rgrf_scaler.py`, `resonance_calc.py`, and the two saved documents (BOM v0.2, Heartbeat Engines v0.1). [Channing to supply]
2. Is the bamboo meant to carry load in a structural frame, with hempcrete only as infill? That is the version that works.
3. Is the ~1 Hz heartbeat meant as a modulation envelope on a kHz carrier? If so, the design can keep the name and drop the lift claim at 1 Hz.
