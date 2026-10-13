# Dusty plasma bench (pass-1 build)

License CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative**. Recovered from material pasted by Channing and saved faithfully; grounding and safety added. *Some numbers or terms may carry OCR artifacts from the source; check each value before buying parts.*

**Purpose:**
- Make a small, lab-grade bench where a **plasma crystal**, an anode **"bubble"** (double layer / fireball) and a biased **gate** can be watched together.
- Test the leaky-boundary, charge-separation and spin ideas (R4–R9 in `em_topological_gravity_review.md`) on real hardware.

## Grounded references
- **Plasma crystal:** Thomas, Morfill, Demmel, Goree, Feuerbacher & Möhlmann, "Plasma crystal: Coulomb crystallization in a dusty plasma", *Phys. Rev. Lett.* 73:652 (1994), doi 10.1103/PhysRevLett.73.652.
  - 7 μm grains in a 13.56 MHz argon discharge at ~2 mbar (~200 Pa) formed a hexagonal crystal visible to the eye.
  - Grain charge was ~10⁴ e, with coupling Γ > 20,000.
- **GEC reference cell:** Hargis et al., "The Gaseous Electronics Conference radio-frequency reference cell…", *Rev. Sci. Instrum.* 65:140–154 (1994), doi 10.1063/1.1144770.
- **Anode double layers / fireballs:**
  - Sanduloviciu & Lozneanu, "On the generation mechanism and the instability properties of anode double layers", *Plasma Phys. Control. Fusion* 28:585 (1986), doi 10.1088/0741-3335/28/3/005.
  - Stenzel et al., "Dynamics of fireballs", *Plasma Sources Sci. Technol.* (2008), UCLA.
  - Baalrud, Longmier & Hershkowitz, "Equilibrium states of anodic double layers", *Plasma Sources Sci. Technol.* 18:035002 (2009). Glow vs spot threshold Δφ_c ∝ 1/P + C; fireballs near small electrodes, firerods near large ones.
- **Rotation control:** rotating-wall physics (Huang et al. 1997; see R9) is the non-neutral-plasma analog of a rotating-field drive.

## Build (pass 1)
| Item | Spec (as given) | Notes |
|---|---|---|
| Chamber | 6-way ISO-K cross, or a GEC reference cell, ~20–30 cm, with an **equator viewport** | GEC geometry gives comparability with the literature |
| Pumps | Rotary + turbo | Base ≤10⁻³ Pa before backfill |
| Gas | **Ar 10–50 Pa** (crystal ~20–40 Pa). Optional 1–5 % O₂ or **trace** SF₆, **short tests only** | Electronegative gases add negative ions and change "attachment" |
| RF | **13.56 MHz, 10–50 W**, capacitive lower electrode, with matching network | Standard |
| Dust | **5–10 μm melamine-formaldehyde** spheres, or **carbonised hemp-char** grains, shaken in from a sieve above the electrode | Hemp-char is irregular and polydisperse, so expect a poorer crystal. Plausible-untested |
| "Bubble" anode | **8–16 mm** stainless or Al disk on a stalk, **+40 to +120 V DC** | Forms anode glow → spot/fireball (double layer) above the threshold |
| Gate | Thin Al plate with **3–7 holes of 3–6 mm**, **−20 to −80 V**, **1–2 cm from the anode** | A second potential step / colder region |
| Rotation (optional) | Insulated rotor, or rotating-field coils, under the dust plane. Counter-rotation later | Ties to R9 point 2 |
| Diagnostics | Fast camera + **laser sheet** (side illumination); **Langmuir probe**; **Rogowski/Pearson** coil on the anode lead; **photodiode** on the bubble | Crystal structure, n_e/T_e, current bursts, light flicker |

## Procedure knobs
1. **Crystal.** Tune pressure and RF power until Γ is high enough for hexagonal order. Check with pair-correlation and Voronoi analysis of laser-sheet images.
2. **Bubble.** Raise the anode bias.
   - A **sharp luminous edge** means a double layer has formed.
   - **Flicker or shedding** (photodiode and Rogowski bursts) marks the **plasmoid-train threshold**.
   - Record the bias vs pressure for both. Prediction: the threshold falls with pressure, roughly ∝ 1/P + C (Baalrud et al. 2009).
3. **Gate.** Bias it to create a **second potential step and a colder region**. Watch whether dust or plasma "leaks" through the holes selectively (R6 controlled leakage).
4. **Pressure knob.** Add 1–5 % O₂ to raise electron **attachment** and compare bubble stability and crystal order.
5. **Temperature zoning.** A heated or cooled electrode region gives thermophoretic force on the dust; separate it from electric effects.
6. **Rotation (later).** Spin the dust plane, then counter-rotate. Look for nested opposite-L layers vs plain heating (R9 falsifiable question).

**Labels:**
- Crystal and double-layer physics: **Grounded**.
- Gate-selective leakage and plasmoid-train thresholds as "leaky-boundary" analogs: **Plausible-untested**.
- Any lift, or extrapolation to cosmic flux tubes: **Speculative**.

## Safety (read first)
- **High voltage:** the DC anode and gate supplies and the RF can be lethal. Use interlocked enclosures, current-limited supplies, a single grounded chassis, and bleeder resistors. Never work live.
- **RF:** 13.56 MHz causes burns and interference. Shield the chamber, use matched coax, keep RF exposure within limits, and keep the matching network enclosed.
- **Vacuum:** viewports can implode. Use rated ISO-K glass, shields or polycarbonate guards, and proper clamps. Turbos store a lot of energy, so don't vent them while spinning.
- **Gases:**
  - O₂ with oil-sealed rotary pumps is a **fire and explosion risk**. Use PFPE (Fomblin) oil or a dry pump.
  - SF₆ is a potent greenhouse gas. Use only trace amounts, never vent it in bulk, and recover it if possible.
  - Plasma by-products of SF₆ (S₂F₁₀, HF, SOF₂) are **toxic**. Exhaust outdoors through a filter.
- **Dust:** wear respiratory protection when handling powders, and vent to a filter.
- **Lasers:** a laser sheet of class 3B or above needs goggles and controlled beam paths.

## Rough cost (pass 1)
- Used-market chamber, turbo and RF gear: ~$3–10 k.
- A new GEC cell: >$20 k.
- This is the most expensive RGRF bench. It is best done with a university or makerspace plasma group.

## Missing pieces
- Exact electrode spacing and the RF matching values.
- Calibration plan for the Langmuir probe in RF (needs RF compensation).
- Grain charging and sizing data for hemp-char.
- A quantitative definition of "plasmoid-train threshold" (frequency and amplitude criteria).
