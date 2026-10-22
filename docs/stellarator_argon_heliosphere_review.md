# Review: Stellarators, argon, the argon microwave filament, and the heliosphere as a leaky boundary (share #94)

- **Archive:** [grok_archive/2026-10-22_stellarators_and_argon_review.md](grok_archive/2026-10-22_stellarators_and_argon_review.md) (share `3fcd1ac6`, 6 messages: 3 Channing, 3 Grok).
- **Checks:** [sims/stellarator_argon_s94_checks.py](../sims/stellarator_argon_s94_checks.py) ([output](../sims/stellarator_argon_s94_checks_output.txt)).
- **Related:** [heliosphere_fibonacci_review.md](heliosphere_fibonacci_review.md), [electrostatic_isotropic_stress_review.md](electrostatic_isotropic_stress_review.md), [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md), [zpinch_tungsten_nodes_review.md](zpinch_tungsten_nodes_review.md), [tungsten_toroid_review.md](tungsten_toroid_review.md), [sims/heliopause_pressure_balance.py](../sims/heliopause_pressure_balance.py), [sims/ambipolar_field_solar_wind.py](../sims/ambipolar_field_solar_wind.py), [sims/grok_toroidal_mhd_1d_rerun.py](../sims/grok_toroidal_mhd_1d_rerun.py).
- **Labels:** Grounded = established in peer-reviewed literature or rerun here; Plausible-untested; Speculative; Symbolic (φ and similar, unless tested).

## 0. Context: a rework of an earlier discussion

Channing notes this conversation reworks a prior discussion of **friction from inertial momentum setting up opposite angular momentum** (counter-rotation through viscous or drag coupling).

- **Grounded:** total angular momentum is conserved, so a torque applied through viscous/drag coupling spins up one body or layer while an equal and opposite reaction acts on its partner. Counter-rotating flows and shear layers are standard fluid and plasma physics (Taylor-Couette flow, counter-rotating vortex pairs, ion-electron counter-drift, sheared flows at the heliopause flanks).
- **Plausible-untested:** the specific claim that this friction-driven counter-rotation helps set up the stellarator/argon/heliosphere structures discussed here. No model or data in this share tests it.
- Earlier docs: [magnus_floquet_inertial_copv_review.md](magnus_floquet_inertial_copv_review.md) (inertial vectors), [acoustic_streaming_and_centrifugal.md](acoustic_streaming_and_centrifugal.md), [alcubierre_plasmoid_turbine_vortex_review.md](alcubierre_plasmoid_turbine_vortex_review.md), [wick_phi4_vortex_adaptogens_review.md](wick_phi4_vortex_adaptogens_review.md), [tungsten_toroid_review.md](tungsten_toroid_review.md), [tungsten_bismuth_core.md](tungsten_bismuth_core.md).

## 1. Stellarator physics (msg 2)

| Claim | Label | Note |
|---|---|---|
| W7-X uses non-planar modular coils; rotational transform ι comes from external 3-D shaping, not plasma current; hence steady-state and disruption-free by design | **Grounded** | Standard stellarator physics (Spitzer 1958; Klinger et al., Nucl. Fusion 2019). "Disruption-free" is better stated as "no current-driven disruptions"; stellarators still have density/radiative limits. |
| Optimization targets nested surfaces, good ι profile, low neoclassical transport, MHD stability | **Grounded** | Correction/precision: W7-X is **quasi-isodynamic** (drift-optimized, low bootstrap current), not quasi-symmetric; quasi-symmetry (QA/QH, e.g. HSX, NCSX design) is the other optimization family. Low neoclassical (1/ν) transport verified on W7-X: Beidler et al., *Nature* 596, 221 (2021). |
| ~1.8 GJ injected in a 360 s discharge; triple product competitive with tokamaks for long pulses | **Grounded** (Grok-reported figures) | Matches IPP's 2025 OP2.3 announcements (43 s high triple-product record; 1.8 GJ over 360 s) [to verify exact figures]. "Fully detached, f_rad > 80%" Grok-reported [to verify]. |
| OP2.4 campaign running to Dec 2026, aiming at >500 s and ~6 GJ | **Plausible-untested** | Long-term W7-X goal is 18 GJ / 30 min; the specific OP2.4 numbers are Grok-reported [to verify]. |
| Rotational transform near 1/φ minimizes islands (Hurwitz, "most irrational") | **Symbolic** | KAM intuition: 1/φ = 0.618 has the slowest-converging continued fraction, so it is farthest from low-order rationals. But real designs care about the whole ι profile; W7-X deliberately puts ι = 5/5 at the edge to make the island divertor. No hardware or optimization result shows a 1/φ advantage. Citation for the proposal [to verify]. |
| SIMSOPT, VMEC, DESC as optimization tools | **Grounded** | Correct; all are real open codes. |

## 2. Argon (msgs 2 and 4)

| Claim | Label | Note |
|---|---|---|
| Argon (with Ne, N₂) seeded for radiative divertor / detachment | **Grounded** | Common on W7-X, ASDEX Upgrade, JET. Argon radiates more in the core than N₂, so it is favoured for mantle radiation; "lower dilution" Grok-reported. |
| XICS sees Ar¹⁵⁺–Ar¹⁷⁺; ionization energies | **Grounded** (rerun) | NIST ASD: Ar 15.760 eV; Ar¹⁵⁺→¹⁶⁺ 918 eV; He-like Ar¹⁶⁺→¹⁷⁺ 4121 eV; Ar¹⁷⁺→¹⁸⁺ 4426 eV. The closed-shell He-like stage persists over keV temperatures, which is why it is the XICS workhorse. |
| CERC: D ≈ 1.5–3 m²/s, no accumulation; ion root / post-pellet: D ≈ 0.2 m²/s, V to −4 m/s, order-of-magnitude peaking; D ~0.02 m²/s locally | **Plausible-untested** (Grok-reported) | Qualitatively matches Geiger et al., Nucl. Fusion 59 (2019) and Langenberg et al. (W7-X impurity transport) [to verify specific numbers]. The physics (Er < 0 in ion root drives inward neoclassical convection ∝ Z) is Grounded. |
| Shattered argon pellets for runaway-electron mitigation | **Grounded** | SPI with Ne/Ar mixtures tested on DIII-D, JET, KSTAR; baseline for ITER disruption mitigation. Tokamak-relevant, as Grok says. |

## 3. Argon microwave filament (msg 4)

- Critical density at 24 GHz: rerun gives **7.14 × 10¹² cm⁻³**, matching Grok. Free-space wavelength is 1.25 cm ("~1 cm" fine). **Grounded.**
- Ne ~10¹⁴–10¹⁵ cm⁻³ is 14–140× n_cr ("one to two orders of magnitude"), consistent. Filament radius 0.03 cm, T_gas (3–7)×10³ K: Grok-reported; source "2024 Physics of Plasmas" [to verify: authors, volume].
- Resonance at the n_e = n_cr surface with field enhancement ~ω/ν_en: **Grounded** (standard plasma-resonance absorption, cf. Ginzburg).
- Stellarator ↔ filament "geometric parallel": **Speculative** as a design motif (an analogy; the physics of magnetic surfaces and critical-density surfaces are unrelated). Grok labelled it "grounded"; that label is corrected here.

## 4. Heliosphere as a leaky boundary (msgs 5–6)

Channing's idea: the leaky boundary helps create the solar system's "vacuum".

- Solar-wind density ~1/r² (rerun: 5 cm⁻³ at 1 AU → ~3×10⁻⁴ cm⁻³ at 120 AU before termination-shock compression). **Grounded.**
- Heliopause ~120 AU at the nose (V1 121.6 AU, V2 119 AU); n_e jump ~40× (heliosheath ~0.002 → VLISM ~0.08 cm⁻³, Gurnett et al. 2013). **Grounded.**
- Porous, reconnection-structured boundary, ACR leakage, GCR entry, neutral crossing via charge exchange: **Grounded** in kind; "many AU thick" transition layer is Plausible-untested [to verify].
- Grok's correction is right and kept: the low density comes from source outflow plus pressure balance (see [sims/heliopause_pressure_balance.py](../sims/heliopause_pressure_balance.py)); leakiness is secondary. Claim that "without a boundary... the cavity would collapse or fill" is **Plausible-untested** (the cavity's size is set by pressure balance; the boundary is the consequence, not a separate agent).
- Heliosphere as a "cell" bounded by double layers / current sheets (Alfvén cellular picture): **Speculative** framing; the heliopause is a tangential-discontinuity-like contact surface, not an observed double layer.

## 5. Rayleigh-Taylor

Not discussed in the share. (The heliopause nose and flanks are studied for Rayleigh-Taylor and Kelvin-Helmholtz instability in MHD models; that is a possible follow-up, not a claim made here.)

## 6. Gaps

- The 1/φ rotational-transform proposal: author and paper [Channing to supply / to verify].
- Which W7-X discharge numbers to use for a D/V profile rerun [Channing to supply].
- The note Channing asked to "make" in msg 5 (park stellarator/argon) is this review.

- **See also (share #97):** [sumerian_noether_arnold_ratchet_review.md](sumerian_noether_arnold_ratchet_review.md): Noether symmetry/conservation, friction-coupled counter-rotation (total L conserved), inner/outer sum vs difference circulation channels.
