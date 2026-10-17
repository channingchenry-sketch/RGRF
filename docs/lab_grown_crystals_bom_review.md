# Lab-grown crystals, the gemstone BOM, bio-composites and VE waves: review of share 1a396707

*License CC0. Source: Grok conversation "Lab-Grown Crystals and Gemstones" (46 messages), archived verbatim at [grok_archive/2026-10-17_lab_grown_crystals_gemstones.md](grok_archive/2026-10-17_lab_grown_crystals_gemstones.md). Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Grok's numbers and "simulations" are **Grok-reported** unless rerun. No code was visible in the capture. Message numbers [n] follow the archive.*

**Related docs. Cross-linked rather than repeated:**
- Mycelium strength data and the POL frame target: [mycelium_uses.md](mycelium_uses.md), [regenerative_materials_review.md](regenerative_materials_review.md).
- Bamboo, borax and chitosan loops: [shuttle_models_estatic_review.md §4](shuttle_models_estatic_review.md#4-bamboo-tubular-vacuolar-loops-borax-chitosan-msgs-8-10).
- Bamboo, hempcrete and mycelium domes: [geodesic_organic_design_review.md §3](geodesic_organic_design_review.md#3-bamboo-dowels-in-hempcrete-overgrown-with-mycelium-messages-510).
- The shuttle's electric cavity: [shuttle_models_estatic_review.md](shuttle_models_estatic_review.md).
- Sacred-geometry background: [freemasonry_sacred_geometry_review.md](freemasonry_sacred_geometry_review.md).
- BNNT and h-BN dielectrics: [electrostatic_locking_pins.md](electrostatic_locking_pins.md).
- Rerun checks: [`sims/muon_g2_acoustic_checks.py`](../sims/muon_g2_acoustic_checks.py) §5.

## 1. Channing (verbatim, selection)

| # | Channing |
|---|---|
| 3 | "Can we look into gemstone properties? Some of them are better for optics and some can handle higher vibrations(amethyst). Can we group them by color see if they have similar properties?" |
| 5 | "Has there been any studies that show wavelength isolation(possible data packaging. Can we deep dive tourmaline and amethyst for our use? Can we explore emerald, ruby, and sapphires refractive/absorption properties?" |
| 7 | "Can we use Tourmaline as a dual photonic-phononic crystal? Can we save the others in a BOM for future possible wavelength isolation/transmission/vibrational extraction?" |
| 13 | "Can we have a crystal lattice around a diamond, would this work like a capacitor would it be better in our feed back system?" |
| 17 | "Can we use CNT to manage the mismatch? Also, our shuttle with the electric cavity and magnetic cavity. Can we place a stack in our electric cavity for higher static stability?" |
| 25 | "… Eventually in entanglements we will grow an entire shuttle, almost like it’s 3D printed.." |
| 27 | "We could submerge after, adding lime, flyash and borax treatment to bamboo before, right? Or hempcrete around bamboo frame, like ribs or boat architecture?" |
| 33 | "I just wanted to see this the circles as copper tubes for resonant wave propagation then it comes down to tuning 3 path propagation…, maybe or our spin dynamics that we talked about wave on triangles.." |
| 39 | "This is perfect we can now treat these kind of like quarks up and down spin, right? Also, does this translate to harmonics as well?" |
| 41 | "… can we have lengths land on 4th or 5th harmonics see if this creates natural balance or not" |

## 2. Gemstone physics [2]–[12]

| Claim | Check | Label |
|---|---|---|
| Hydrothermal synthetic quartz runs most precision oscillators [2] | Correct | **Grounded** |
| Quartz nₒ ≈ 1.544, nₑ ≈ 1.553, Δn = +0.009, uniaxial positive, Mohs 7 [4][6] | Correct | **Grounded** |
| Amethyst has "same piezo properties as clear quartz" and "handles higher vibrations" [3][6] | **Correction.** Amethyst is almost always **Brazil-law twinned**. The twin domains have opposite handedness, partly cancel the piezoelectric response, and make it unsuitable for resonators; oscillator quartz is grown untwinned on purpose. Colour comes from Fe⁴⁺ colour centres produced by irradiation of Fe³⁺ [to verify exact centre model]. "Higher vibration" in the metaphysical sense is **Symbolic**, and Grok says so too [4]. | **Grounded** (correction) |
| Quartz optical phonon near 3.855 THz (ordinary ray) [6] | The low-frequency IR-active E mode is near 128 cm⁻¹ (3.84 THz) | **Grounded** ([to verify] exact value) |
| Corundum (ruby, sapphire) RI ~1.76–1.77, Mohs 9; ruby gave the first laser (Maiman 1960) [4] | Correct | **Grounded** |
| Corundum "not strongly piezoelectric" [4] | **Correction.** Corundum (R3̄c) is centrosymmetric, so it is **not piezoelectric** at all | **Grounded** (correction) |
| Beryl (emerald) "weakly piezoelectric at best" [4] | **Correction.** Beryl (P6/mcc) is centrosymmetric, so it is not piezoelectric. Any reported weak response comes from defects or strain. | **Grounded** (correction) |
| Diamond as a piezo/phonon element in the BOM [12] | Diamond is centrosymmetric and not piezoelectric. It is valuable for thermal conduction, NV centres and as a betavoltaic converter, which is correct. | **Grounded** |
| Tourmaline is piezo- and pyroelectric, strongly pleochroic, uniaxial negative [4][6] | Correct | **Grounded** |
| Tourmaline pyroelectric coefficient "1–20 µC/m²·K" [6] | Typical reported ~4 µC/m²·K; the upper range is [to verify] | **Grounded** (magnitude) |
| "Tourmaline generally shows stronger piezo response" than quartz [10] | **Qualified.** Longitudinal coefficients are similar (tourmaline d₃₃ ~1.8 pC/N vs. quartz d₁₁ ~2.3 pC/N). Tourmaline's real distinction is a **non-zero hydrostatic coefficient**, which quartz lacks; that is why it was used in hydrostatic pressure gauges. "Historical work (1930s)" is [to verify]. | **Grounded** (corrected wording) |
| Tourmaline as a "dual photonic-phononic crystal" [7][8] | A photonic or phononic *crystal* needs a periodic structure at the wavelength scale. Bulk tourmaline is a homogeneous anisotropic crystal, so it is a candidate *material* for patterning, not a photonic-phononic crystal itself. | **Plausible-untested** (as a patterned device) |
| Rotation as a "photonic-phononic selector" [9]–[12] | Rotating birefringent or pleochroic plates between polarisers is a **Grounded** tunable filter (the Lyot/Šolc family). Rotation-tuned acoustic coupling is **Grounded** in principle because coupling depends on crystal cut. Combining both in one element is **Plausible-untested**. | see text |
| "Wavelength isolation … data packaging" [5] | Wavelength-division multiplexing uses dielectric filters and gratings, not gemstones. Gems can act as absorption filters. | Filters **Grounded**; gem-based data packaging **Speculative** |

## 3. Diamond core-shell "capacitor," epitaxy, CNT buffers [13]–[18]

- **Diamond core with crystal shell as a capacitor [14].** Diamond has high breakdown strength (~10 MV/cm) and low leakage, which is **Grounded**. **Correction:** Grok cites "high permittivity stability," but ε_r ≈ 5.7 is *low*, so energy density ½εE² is modest per volume; commercial film and ceramic capacitors are far cheaper. Curved core-shell geometry concentrates the field at the inner electrode, which *reduces* breakdown margin. Overall **Plausible-untested** and of low value. The benefit "in our feedback system" is not quantified: [Channing to supply] the required capacitance, voltage and response time.
- **Heteroepitaxy [16].** Diamond (a = 3.567 Å) on 3C-SiC (a = 4.36 Å) is ~22 % mismatch, which is **Grounded**. The established route to wafer-scale single-crystal diamond is Ir/YSZ/Si (Schreck group), which Grok omits. "Coherent local heteroepitaxy of SiC on (100) diamond" is [to verify].
- **CNTs to "manage the mismatch" [17][18].** **Speculative.** CNT forests are not single-crystal templates, so they decouple an overlayer rather than make it epitaxial. The real compliant-interlayer route is **remote epitaxy** through graphene (Kim et al., *Nature* 544, 340 (2017), doi:10.1038/nature22053), plus graded buffer layers.
- **Crystal stack in the shuttle's electric cavity for "higher static stability" [17][18].** A dielectric stack raises capacitance and changes field distribution, which is **Grounded**. A static-stability gain needs a specified force or field requirement; none exists for the cavity. See the E-Static lift correction in [shuttle_models_estatic_review.md](shuttle_models_estatic_review.md). **Speculative.**
- **Betavoltaic minerals [11][12].** Diamond and SiC are real betavoltaic converters, usually paired with ⁶³Ni or tritium, which is **Grounded**. Output is µW-scale per device, so betavoltaics suit trickle-charging sensors, not propulsion or cavity power. Sources are licensed radioisotopes; this is not a "growing material." **Plausible-untested** for node sensors only.

## 4. Bio-composites, Guadua, treatments [19]–[28]

- **Mycelium composite metrics [22][24].** Ranges consistent with the repo:
  - foams: compressive 0.1–1.2 MPa, flexural 0.2–1 MPa, tensile 0.03–0.87 MPa;
  - hot-pressed: 34–97 MPa.

  These match [mycelium_uses.md](mycelium_uses.md) and the Elsacker/Jones-type reviews. **Grounded**, with the individual figures [to verify] since sources weren't named. The POL frame target of 2.1–2.8 MPa still needs densification ([regenerative_materials_review.md](regenerative_materials_review.md)).
- **Plant-sugar doping [23][24].** Sugars feed contaminants as readily as mycelium. Use them as substrate supplements only, in sterile conditions. **Plausible-untested.**
- **Guadua angustifolia [26].** Grok gives density 600–800 kg/m³, "characteristic" compression 35–40 MPa and MOE 18.5 GPa.
  - Mean dry compressive strength of ~40–60 MPa is widely reported.
  - Characteristic (5th-percentile, ISO 22156 method) values are lower and depend strongly on moisture. Luna, Lozano & Takeuchi, *Maderas* 16(3), 2014, tested saturated culms and got lower values.
  - Grok's 18.5 GPa is above the NSR-10 Title G design modulus, about 12 GPa mean [to verify].
  - Overall **Grounded** in magnitude; numbers [to verify] before design use.
- **Lignin bio-adhesives for joints [26].** An active research area (lignin-phenol-formaldehyde, kraft-lignin epoxies) and **Plausible-untested** for structural joints. Grok rightly pairs them with mechanical fasteners.
- **Borax, lime, fly ash, submersion [28].**
  - Water-leaching (soaking) and borate treatment are **Grounded** traditional bamboo preservation.
  - **Contradiction:** Grok says borax "pairs excellently with mycelium (doesn't inhibit growth at moderate levels)." Borates are *fungicides*. The repo already says to treat and dry bamboo, then isolate it from the inoculated zone ([shuttle_models_estatic_review.md §4](shuttle_models_estatic_review.md#4-bamboo-tubular-vacuolar-loops-borax-chitosan-msgs-8-10)).
  - Lime is alkaline (pH ~12.5) and also suppresses fungal growth, so lime-hempcrete and live mycelium should be separate layers or stages.
- **Hempcrete around a bamboo rib frame (boat-style) [27][28].** **Grounded** as a construction method: hempcrete is non-load-bearing infill around a timber or bamboo frame. Grok's "superior overall stiffness" for the combined section is unquantified.
- **"Grow an entire shuttle" [25]–[28].** **Speculative** (Entanglements story concept).

## 5. Sacred-geometry panels, VE and 3-path waves [29]–[42]

- **Vesica Piscis panels [30].** The geometry is **Grounded**: two circles of radius r with centres r apart; lens height/width = √3. Any structural advantage is **Symbolic** unless tested.
- **Vector Equilibrium [32].** The cuboctahedron's centre-to-vertex radius equals its edge length, which is **Grounded**. Fuller's 12-around-1 packing and the jitterbug transform (VE → icosahedron → octahedron) are **Grounded** geometry. "Forces are neutralized" is **Symbolic**. A VE strut frame is not rigid on its own, because its square faces need bracing. See [geodesic_organic_design_review.md](geodesic_organic_design_review.md).
- **Copper-tube circles and a Tesla coil wrapped around them [33]–[36].** **Speculative.** Copper tubes are acoustic or EM waveguides only with defined dimensions and frequency, and none were given.
- **"Simulated 3-path wave propagation" with 120° offsets [38].** Grok-reported, and no code was shown. **Correction (rerun §5):** three equal-amplitude, equal-frequency waves with 120° offsets sum to **exactly zero** at a common node. This is balanced three-phase. Grok's "constructive and destructive patterns … modulated intensity peaks" needs unequal amplitudes, frequencies or path delays, none of which was specified.
- **4th/5th-harmonic paths "structured stability" [42].** Grok-reported. The rerun of fundamental + 4th + 5th with 120° offsets gives a periodic waveform with rms √(3/2), which is just three orthogonal sinusoids. There is no "natural balance" beyond that. Physical harmonic tuning would need tube lengths L = nλ/2, with λ from the tube's actual acoustic or EM mode: [Channing to supply] the frequency and medium.
- **"Like quarks up and down spin" [39][40].** **Symbolic** analogy. Quark colour neutrality and spin-½ statistics have no counterpart in classical waves in tubes. Grok's "without claiming literal quantum chromodynamics" is the right framing.

## 6. Archive review and memory update [43]–[46]

- Grok's "missed opportunities" list [44] is a recap, not new data.
- Its "Simulation-heavy, prototyping lighter" observation matches the repo's own view in [ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md).
- The "June 2026 Update" memory item on quantum biology [46] is noted. Cross-check it with [quantum_biology_regenerative_farm_review.md](quantum_biology_regenerative_farm_review.md).
- The "BOM v0.1–v0.3" artifacts Grok mentions were **not captured**: [Channing to supply] if they were saved.

## 7. Open items

- [to verify] Tourmaline pyroelectric range; the 1930s quartz-tourmaline comparison; SiC-on-diamond heteroepitaxy; Guadua characteristic values (NSR-10 Title G; Luna et al. 2014 table 9); quartz 3.855 THz mode.
- [Channing to supply] The BOM files (v0.1–v0.3); the capacitor requirement for the feedback system; tube frequency and medium for the VE copper-tube harmonics.
