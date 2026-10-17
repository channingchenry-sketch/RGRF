# Feynman diagrams, metamaterials, quartz and lead-free piezoceramics: review of a Grok share (2026-10-17)
*CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Why φ appears, and how it is tested: [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md).*

**Source (verbatim archive):** "RGRF and Feynman Diagrams in Resonance", 10 messages: [grok_archive/2026-10-17_rgrf_feynman_diagrams_resonance.md](grok_archive/2026-10-17_rgrf_feynman_diagrams_resonance.md).

**Repo context (cross-links):**
- Piezo and quartz "heartbeat": [tungsten_bismuth_core §4](tungsten_bismuth_core.md#4-resonant-piezo--quartz-feedback--the-heartbeat--plausible-untested) and [§7d](tungsten_bismuth_core.md#7d-quartz-partner-phonons--piezoelectric-quartz-balancing).
- PZT sensing numbers: [piezo_helium_feedback_loop.md](piezo_helium_feedback_loop.md).
- Piezo voltage and power from rock (granite ~10⁻³ of crystal): [pyramidion_node_review §3.4](pyramidion_node_review.md#34-piezoelectric-voltage-and-power-corrected-simspyramid_piezo_estimatepy).
- An earlier Feynman-diagram check: [pyramidion_node_review §8](pyramidion_node_review.md#8-labels-summary).
- φ null results: [transistor_drive_stages §5](transistor_drive_stages.md#5-sim-simsresonant_drive_phi_testpy-results) and [tungsten_bismuth_core §7b-dyn.3](tungsten_bismuth_core.md#7b-dyn3-source-conversation-found-earths-em-field-magnetic-pressure-2026-10-17).

**Channing's prompts (verbatim):**
1. "Are we reproducing Feynman diagrams in our EM harmonic/dissonance fields?"
2. "Perfect, let’s continue chopping away. Can you explore metamaterial resonance design and quartz piezoelectric properties?"
3. "Investigate PZT ceramic alternatives"
4. "Explore KNN phase boundary engineering"
5. "Let’s save here!"

## 1. Feynman diagrams and RGRF fields (message 2)

**Short answer to Channing's question: no.** Feynman diagrams are bookkeeping for the terms in a perturbative expansion of quantum scattering amplitudes. Classical standing-wave fields (coils, eddy currents, Maxwell) are described exactly by Maxwell's equations, and at the frequencies and field strengths in the repo QED corrections are negligible. Any resemblance between a field sketch and a diagram is visual.

| Claim | Check | Label |
|---|---|---|
| Diagrams: fermion lines, wavy photon lines, vertices, loops for virtual particles; terms in an amplitude | Standard QED | Grounded |
| "harmonic (resonant) and dissonant (off-shell, virtual) contributions" | Off-shell means E² ≠ p²c² + m²c⁴ for internal lines. It has nothing to do with harmony or dissonance | **Symbolic** (Grok's mapping) |
| RGRF spirals as "worldlines", resonance nodes as "vertices", closed circuits as "virtual loops" | Analogy only; Grok itself says "it's an analogy, not equivalence" | **Symbolic** |
| "harmonic fields correspond to constructive interference at φ-proportioned frequencies — stable lift, power transfer" | No repo test has found a φ advantage | **Speculative**; contradicted by the repo φ null results |
| "Classical harmonic modeling works beautifully for macro-scale POL prototypes (conductive floor coupling, eddy lift)" | No POL prototype has been built or measured. The repo's eddy-lift numbers show a power gap (~520 W available vs ~10–17 kW needed: [legal_safety §3](legal_safety_and_grounding_review.md#3-the-human-powered-levitator-and-eddy-current-lift)) | **Overclaim**; the classical method is right, "works beautifully" is not shown |
| "Tesla-style … longitudinal waves" | Free-space EM waves are transverse. Longitudinal fields exist only near sources, in plasmas, or as Tesla's ground-current claims | **Speculative** |
| Dissonance fields "risk unwanted heating … if φ-ratios drift — something we've noted in POL v0.1 limitations" | No such note found in the repo | [to verify] / [Channing to supply] |

## 2. Quartz and metamaterials (message 4)

| Claim | Check | Label |
|---|---|---|
| α-quartz: direct and converse piezo effect; Q ~10⁵ or higher; AT-cut thickness-shear with near-zero frequency drift; modest coefficients (d₁₁ ≈ 2.3 pC/N vs PZT ~200–600) | Standard crystal-oscillator data | Grounded |
| "low thermal expansion (~0.5 × 10⁻⁶/°C)" | That is **fused silica**. Crystalline α-quartz is anisotropic: ~7–8 ×10⁻⁶/K along c and ~13–14 ×10⁻⁶/K perpendicular near room temperature, and it rises sharply toward the 573 °C α–β transition | **Wrong** (corrected) |
| "Tesla appreciated quartz for its energetic interactions" | No source given; none found | **Not supported** [to verify] |
| Metamaterials: subwavelength unit cells (SRRs), negative ε/μ, perfect absorbers, cloaking, bandgaps; tuning by varactors or piezo shunts | Standard | Grounded |
| "Studies show φ-proportioned dimensions simplify fabrication while enhancing performance (e.g., in absorbers…)" | One such paper exists: "Tunable perfect metamaterial absorber design using the golden ratio and energy harvesting and sensor applications," *J. Mater. Sci.: Mater. Electron.* (2015), doi:10.1007/s10854-015-3642-7 (≈99.9 % absorption at 6.78 GHz) [authors to verify]. It uses φ to set dimensions; whether φ outperforms other ratios was not tested there [to verify] | Grounded that φ-sized absorbers work; "enhancing performance" **not shown** |
| Piezo-metamaterial composites for tunable bandgaps, shunt damping and harvesting | Active research area | Grounded |
| Quartz elements on POL "detect floor-coupling dissonance and harvest energy to stabilize lift" | Sensing: Plausible-untested. Harvesting: the power is µW–mW, far too small to matter against kW lift (see [pyramidion §3.4](pyramidion_node_review.md#34-piezoelectric-voltage-and-power-corrected-simspyramid_piezo_estimatepy)) | Sensing **Plausible-untested**; harvesting for lift **not supported** |
| Mycelium matrix hosting quartz inclusions | Composite concept; no data | **Plausible-untested** |

## 3. Lead-free alternatives to PZT (message 6)

| Claim | Check | Label |
|---|---|---|
| PZT lead content "~60% PbO" | For PbZr₀.₅₂Ti₀.₄₈O₃ (M ≈ 325.6 g/mol): PbO ≈ 68.5 wt %, Pb ≈ 63.6 wt % (ANALYSIS) | Corrected: ~64 % Pb / ~69 % PbO |
| RoHS and toxicity drive lead-free research | PZT currently sits under a RoHS exemption that is reviewed periodically | Grounded |
| KNN: Tc "~300–420 °C"; d₃₃ "200–400+" with doping or texturing | Pure KNN Tc ≈ 420 °C and d₃₃ ~80–160 pC/N. Doped KNN trades Tc down (often ~200–350 °C) for d₃₃ up. Saito et al., *Nature* 432, 84 (2004): textured (K,Na,Li)(Nb,Ta,Sb)O₃ reached d₃₃ ≈ 416 pC/N | Grounded (range loose) |
| Alkali volatilization makes KNN hard to process | Standard | Grounded |
| BNT(-BT): d₃₃ "100–300"; Curie "~200–300 °C" | BNT-BT d₃₃ is typically ~120–200 pC/N. The practical limit is the **depolarization temperature** T_d ~100–200 °C, below the dielectric maximum (~300 °C). The table's "Curie" column for BNT should read T_d | Corrected |
| BNT "lower density … higher resonance frequencies" | Lower density raises the sound speed; ρ ~5.8–6 vs ~7.5–8 g/cm³ is right | Grounded |
| BZT-BCT: d₃₃ "up to 330–650+"; Tc "~80–150"; ε_r ">10,000 in some cases" | W. Liu & X. Ren, *PRL* 103, 257602 (2009): d₃₃ ≈ 620 pC/N at an MPB, Tc ≈ 93 °C. ε_r > 10⁴ occurs near the dielectric peak; room-temperature values are lower [to verify the typical value] | Grounded; the low Tc is the main limit (Grok says so) |
| Densities: PZT ~7.5–8, KNN ~4.5, BNT ~5.5–6, BZT-BCT ~5.5–6 g/cm³ | Consistent with handbook values | Grounded |
| BZT-BCT or quartz hybrids "in φ-spiral coils for better self-powered dissonance feedback and eddy-lift tuning" | No coupling path or numbers | **Speculative** (φ **Symbolic**) |

## 4. KNN phase-boundary engineering (message 8)

| Claim | Check | Label |
|---|---|---|
| Pure KNN transitions: R–O at low T, O–T ~200 °C, T–C ~400 °C; dopants (Li, Bi, Sb, Ta, Zr, Hf; BNZ, CaHfO₃) shift them toward room temperature to make multiphase boundaries | Standard picture (R–O ≈ −123 °C, O–T ≈ 200–210 °C, T–C ≈ 410–420 °C) | Grounded |
| R–O–T multiphase with nanodomains: "ultrahigh d₃₃ (up to ~650 pC/N reported)" | H. Tao et al., *J. Am. Chem. Soc.* (2019), doi:10.1021/jacs.9b07188: d₃₃ = 650 ± 20 pC/N (verified) | Grounded |
| Textured KNN–Sb: "d₃₃ ~800 pC/N and k₃₃ ~88%" | Textured KNN-5Sb: d₃₃ ≈ 807 pC/N, k₃₃ ≈ 88 %, Tc ≈ 245 °C, *Nat. Commun.* (2025), doi:10.1038/s41467-025-56074-8 (verified) | Grounded (note the Tc drop) |
| Cu defect dipoles in O–T boundaries: "d₃₃ ~120 pC/N with Qₘ ~850" | A 2025 *Nat. Commun.* paper matches the wording ("Excellent hardening effect in lead-free piezoceramics by embedding local Cu-doped defect dipoles in phase boundary engineering," doi:10.1038/s41467-025-58269-5). A donor–acceptor co-doped KNN reports Qₘ = 850 and d₃₃ = 120 pC/N (PubMed 37655947) [to verify which paper the numbers are from] | Grounded [numbers to verify] |
| "pins domains for high Qₘ" | Ferroelectric **domain-wall pinning** by defect dipoles (acceptor hardening). This is materials science, **not** a mechanical lock pin | Grounded |
| φ-proportioned KNN unit cells in SRRs "echoing Feynman-like vertices" | Analogy | **Symbolic** |
| Mycelium matrix hosting doped KNN particles | 0–3 composites (ceramic powder in a polymer) are real but have low d₃₃; a living or biological matrix is untested | **Plausible-untested** |

## 5. "Let's save here!" (message 10)
- Grok reports "File saved: RGRF_KNN_Phase_Boundary_Engineering_Summary.md". No such file is in the share, and none is in this repo. **[Channing to supply]** if he has a copy.
- The phrase "personal levitation" (message 8) carries the repo's POL power-gap caveat ([legal_safety §3](legal_safety_and_grounding_review.md#3-the-human-powered-levitator-and-eddy-current-lift)).

## 6. Open items
- The full share URL and the three source lists ("[40 sources]", "[40 sources]", "[35 sources]"). **[Channing to supply]**
- Which POL v0.1 note mentions dissonance heating when "φ-ratios drift"? **[Channing to supply]**
- A useful bench step from this thread: a quartz or KNN disc as a vibration **sensor** on a test rig, read through a charge amplifier. It is cheap and measurable. Harvesting for lift is not worth pursuing (µW–mW).
