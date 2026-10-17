# Floquet drive, 196 Hz, the living panel stack and the Tungsten-Graphene-Quartz core: labelled review (2026-10-17)
*License CC0. Review of the Grok share "Floquet Engineering: Quantum Physics Control" (capture `d6ce2c90`, 44 messages). Verbatim archive: [grok_archive/2026-10-17_floquet_engineering_quantum_physics_control.md](grok_archive/2026-10-17_floquet_engineering_quantum_physics_control.md). Numerical checks: [sims/grok_claim_checks_2026_10_17.py](../sims/grok_claim_checks_2026_10_17.py) ([output](../sims/grok_claim_checks_2026_10_17_output.txt)).*

**Cross-links (not repeated here):**
- Floquet theory and the SSH π-mode toy model already in the repo: [shifting_phase_order_review.md §F](shifting_phase_order_review.md) and [sims/floquet_ssh_pi_modes.py](../sims/floquet_ssh_pi_modes.py).
- Tungsten–bismuth core: [tungsten_bismuth_core.md](tungsten_bismuth_core.md).
- Opposing vortices (equal counter-rotating fields cancel the twist): [tungsten_toroid_review.md §4](tungsten_toroid_review.md#4-stellarators-and-opposing-vortices-messages-1116).
- Materials (mycelium, hemp, algae): [regenerative_materials_review.md](regenerative_materials_review.md).
- Craft: [manta_butterfly_craft.md](manta_butterfly_craft.md). Book: [book_blueprint_structure.md](book_blueprint_structure.md).

**Labels:** Grounded · Plausible-untested · Speculative · Symbolic. φ is **Symbolic** unless a test shows otherwise. Every simulation number here is **Grok-reported**: no code was shown [Channing to supply].

## 1. Floquet engineering (messages 1–2, 29–30)

Channing: "What is floquet engineering?" and later "Explore Floquet topological effects"

| Claim | Label | Check / source |
|---|---|---|
| A periodic drive H(t + T) = H(t) gives quasienergies and an effective Hamiltonian; light can open gaps and make topological bands | **Grounded** | T. Oka & H. Aoki, *Phys. Rev. B* 79, 081406 (2009); M. S. Rudner et al., *Phys. Rev. X* 3, 031005 (2013); Floquet–Bloch states on a topological insulator: Y. H. Wang et al., *Science* 342, 453 (2013); photonic Floquet TI: M. C. Rechtsman et al., *Nature* 496, 196 (2013); light-induced anomalous Hall effect in graphene: J. W. McIver et al., *Nat. Phys.* 16, 38 (2020). |
| A 196 Hz drive "creates an effective Hamiltonian where the graphene" bands become topological (msg 30) | **Not supported** | ħΩ at 196 Hz is 8.1 × 10⁻¹³ eV, about 10¹² times smaller than graphene's electronic energy scales. Floquet band engineering needs drive photons comparable to the band energies (THz–optical). Grok itself notes "microwave to optical" in msg 30. At 196 Hz, Floquet ideas apply only to **mechanical/acoustic** lattices (§5). |

## 2. Temperature and 196 Hz (messages 3–4, 17–18)

Channing: "Yes in our book let’s have them explore floquet-inspired drive while we also do, we already have the materials to stabilize. Can we investigate temperature controlled fluctuations on the magnetic field as well as vibration re explore 196hz and do a simulation."

| Claim | Label | Check |
|---|---|---|
| "~ -0.1% to -0.2% per °C for many materials" | **Grounded for permanent magnets; wrong for electromagnets** | NdFeB ≈ −0.12 %/K, ferrite ≈ −0.20 %/K, SmCo ≈ −0.035 %/K. So ±0.5 K moves 1 T by ±0.60, ±1.00 and ±0.17 mT. An electromagnet's field follows its **current**: under constant-current drive it barely changes with temperature; under constant-voltage drive copper's +0.39 %/K resistance lowers the field by about that much. |
| 196 Hz "near G3 note" | **Grounded** | G3 = 196.00 Hz (A4 = 440 Hz equal temperament). Choosing it is **Symbolic**. |
| "Mean effective field stayed very close to 1 T (~1.0007 T)" (msg 4); "~1.00085 T" (msg 18) | **Grok-reported; window artefact** | Averaging 1 T + 5 % sin(2π·196 t) over 0.1 s covers 19.6 cycles, giving 1.00073 T; at 6 % it gives 1.00088 T. Over a whole number of cycles the mean is exactly 1.00000 T. The "stability" figure is the leftover partial cycle, not physics. |
| Graphene "damping thermal envelope by ~40%" (msg 18) | **Grok-reported; not reproducible** | No model of how a conductor would damp a temperature envelope. |

## 3. Aerogels, bioluminescent mycelium, algae (messages 5–10)

| Claim | Label | Check / source |
|---|---|---|
| Silica aerogel thermal conductivity ~0.013–0.017 W/m·K; first made by Kistler; ambient-pressure drying route | **Grounded** | S. S. Kistler, *Nature* 127, 741 (1931); S. S. Prakash, C. J. Brinker et al., *Nature* 374, 439 (1995). |
| Aerogels "ideal" for quantum-computer cooling | **Partly** | Dilution refrigerators rely on vacuum and multilayer insulation (MLI); aerogel is not standard there. Good for room-temperature walls and acoustic damping (Plausible-untested at 196 Hz: low-frequency sound needs mass or thickness, not just porosity). |
| Fungal bioluminescence | **Grounded** | Luciferin/luciferase pathway: A. G. Oliveira et al., *Curr. Biol.* 25, 964 (2015); K. Kotlobay et al., *PNAS* 115, 2894 (2018). |
| Bioluminescence via Trametes versicolor networks | **Corrected** | *Trametes versicolor* is not bioluminescent. Luminous species include *Neonothopanus*, *Panellus stipticus* and *Armillaria*. |
| Algae with aerogel vs a layered stack (msg 10) | **Plausible-untested** | Algae need light, water and CO₂; a hydrophobic aerogel blocks water. A separate algae layer is the workable option. |

## 4. CNT nodes, graphene-hemp braids, hemp graphene, mercury, aluminium skin (messages 11–20)

Channing: "Perhaps we have the CNT at the nodes and graphene-hemp braided lines or copper core myclium-hemp cord.."

| Claim | Label | Check / source |
|---|---|---|
| CNT strength | **Grounded for single tubes** | Up to ~63 GPa measured on individual multiwall tubes (M.-F. Yu et al., *Science* 287, 637 (2000)). Bulk CNT yarns are far weaker (≈1–5 GPa [to verify]). Long, rigid CNTs show asbestos-like inhalation hazard: C. A. Poland et al., *Nat. Nanotechnol.* 3, 423 (2008). Handle with containment. |
| Hemp-derived carbon nanosheets | **Grounded** | H. Wang, D. Mitlin et al., *ACS Nano* 7, 5131 (2013) (hemp bast fibre, hydrothermal + activation, supercapacitors). These are graphene-like carbons, not single-layer graphene. Acid and autoclave steps are a safety item (pressure vessel, corrosives). |
| Mercury | **Grounded** | Resistivity ≈ 96 µΩ·cm (poor for a metal); toxicity: Minamata disease and the Minamata Convention. Channing (msg 19): "I don’t plan on using mercury I’m just curious about its properties.." |
| Aluminium skin with algae film | **Plausible-untested** | Al skin depth: 5.85 mm at 196 Hz (a thin skin does little), 22 µm at 13.56 MHz. Biofilms on aluminium raise microbially influenced corrosion (MIC) risk; needs a coating. |
| "Saved" stack design (msg 20) | **Plausible-untested** as a layout | Layers: Al/algae skin, piezo feedback, CNT nodes, braids or copper-core cords, aerogel-mycelium walls. |

## 5. Core EM field and phononic topology (messages 25–34)

Channing (msg 25): "We will get deep into Entanglements at some point because in our reality the Civil Rights movement will happen quicker etc. we will get into it eventually.. Right now I’d like to re visit our Tungsten-Bismuth core. Let’s also do a Tungsten-Graphene-Quartz lattice core( same resonant cavity set up as before). How intense is the EM field?"

| Claim | Label | Check |
|---|---|---|
| "Peak Electric Field (E): 1.24 × 10⁵ V/m", "Peak Magnetic Field (B): 1.12 T", "~1–10 kW input power, Q ≈ 450" (msg 28) | **Grok-reported; inconsistent** | At 196 Hz the wavelength is 1530 km, so the "cavity" is a lumped LC, not a resonator. The induced E from 1.12 T at 196 Hz over r = 0.1 m is about 69 V/m; 1.24 × 10⁵ V/m would need r ≈ 180 m. Storing 1 T in 1 L (398 J) at Q = 450 takes about 1.1 kW, so the power range is plausible for a litre. |
| Graphene "~35% local boost via plasmonic effects" | **Not supported** | Graphene plasmons are THz–mid-IR; nothing happens at 196 Hz. |
| W–Bi core "~15–20% lower peak intensity due to stronger diamagnetic shaping" | **Not supported** | Bi's χ ≈ −1.7 × 10⁻⁴ changes B by about 0.02 %. |
| Phononic topological insulators exist and are tunable | **Grounded** | R. Süsstrunk & S. D. Huber, *Science* 349, 47 (2015); L. M. Nash et al., *PNAS* 112, 14495 (2015); R. Fleury, A. B. Khanikaev & A. Alù, *Nat. Commun.* 7, 11744 (2016). A 196 Hz lattice is **Plausible-untested**: the unit cell must be roughly half a wavelength of the mechanical wave (metres in air, centimetres to metres in solids). |
| "This works better with our opposing vortices pressure system, right?" (Channing, msg 33); Grok: "~25–40% lower estimated losses in vortex maintenance" (msg 34) | **Not supported** | No model; see the cancellation point in [tungsten_toroid_review.md §4](tungsten_toroid_review.md#4-stellarators-and-opposing-vortices-messages-1116). |
| Acoustic or diamagnetic lift as a mechanism | **Grounded limits** | 100 Pa of acoustic radiation pressure needs ≈ 3760 Pa rms (165 dB). Diamagnetic levitation needs B·dB/dz ≥ 726 T²/m for bismuth and ≥ 60 T²/m for pyrolytic graphite. |

## 6. Book material: patents, Mana Ray, flight frequencies (messages 21–24, 35–44)
- **Patents "by the Wright brothers" and Tesla (msg 24, "Wright Resonance Levitator (1905–1908 filing…)")**: **fiction**, for *Entanglements*. Real record: Wright "Flying-Machine" patent US 821,393 (1906) is Grounded. Keep the invented ones clearly labelled as the book's alternate timeline.
- Channing (msg 21–23): "Dig deeper through our conversations and bring it all together" / "wright brothers.."
- **Mana Ray craft and patent abstract (msgs 35–40)**: **Symbolic / design fiction**; no dimensions or masses given that can be checked. See [manta_butterfly_craft.md](manta_butterfly_craft.md).
- **Flight frequencies (msg 42)**: take-off "40–80 Hz range with strong 196 Hz harmonic overlay", flight "196 Hz … with Floquet sidebands (e.g., 150–250 Hz)", landing "80–120 Hz transitioning down to 40–60 Hz". **Backwards for eddy-current lift**: over a conductive floor, lift rises with frequency until the skin depth is thin. The lowest frequency at take-off gives the **least** lift. Label: Symbolic.

## 7. Open questions for Channing
1. Code for the temperature/196 Hz sims (msgs 4, 18) and the EM-field sim (msg 28). [Channing to supply]
2. Is the core driven by permanent magnets or electromagnets? That decides which temperature figure applies.
3. Which fungus is meant for the glowing panels, since *Trametes* does not glow?
4. Should the flight-frequency table be kept as book fiction, or reworked for lift physics?
