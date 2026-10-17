# Nickel, copper, salt water and the magnetostrictive "spark plug": review of share 2bb73d17

*License CC0. Source: Grok conversation "Nickel Copper Magnetism" (10 messages), archived verbatim at [grok_archive/2026-10-17_nickel_copper_magnetism.md](grok_archive/2026-10-17_nickel_copper_magnetism.md). Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Message numbers [n] follow the archive.*

**Related docs:**
- [acoustic_streaming_and_centrifugal.md](acoustic_streaming_and_centrifugal.md): centrifugal buoyancy and the twisted toroid.
- [piezo_helium_feedback_loop.md](piezo_helium_feedback_loop.md) and [helium_water_circulation.md](helium_water_circulation.md): the helium loop.
- [muon_cathode_acoustic_water_review.md](muon_cathode_acoustic_water_review.md): electrolysis and the water claims.
- [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md) and [ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md): eddy lift and the hover power gap.

## 1. Channing (verbatim)

| # | Channing |
|---|---|
| 1 | "Can nickel and coppers properties change under magnetism?" |
| 3 | "What about in salt water, can copper attract nickel?" |
| 5 | "What if an electric wave struck it?" |
| 7 | "Can we explore magnetostrictive nickel applications possible entry into a cavity also water helium, like we talked about before, and our piezoelectric feedback system" |
| 9 | "Think of this as a sort of spark plug for our dual system twisting toroidal(centrifugal force lift), what would this do? (Highly pressurized dense gas?)" (resubmitted after an interrupted first wording; see the archive header) |

## 2. Material physics [2]

| Claim | Check | Label |
|---|---|---|
| Ni ferromagnetic, Curie ~627 K | Correct (627–631 K) | **Grounded** |
| Ni magnetostriction ~ −46×10⁻⁶ along [100] | Correct. λ₁₀₀ ≈ −46 ppm, λ₁₁₁ ≈ −24 ppm, polycrystal λ_s ≈ −33 ppm | **Grounded** |
| "Giant" magnetostriction in Ni nanowires | Reports exist, but values depend on method. [to verify] before relying on any number. | **Plausible-untested** |
| Cu diamagnetic; eddy currents and Lenz braking; magnet falling slowly through a copper tube | Correct | **Grounded** |
| Magnetic fields alter electrodeposition via Lorentz-force convection (magnetohydrodynamic electrodeposition) | Correct | **Grounded** |
| Ni or Ni-rich layers "could enhance resonant coupling or damping in mycelium-hemp composites" | No data | **Speculative** |

## 3. Salt water [4]

- "Copper does not magnetically attract nickel" is **Grounded**.
- **Correction (galvanic order).** Grok says nickel is "more active (anodic) than copper in the galvanic series for seawater" and would corrode to protect copper. In the standard seawater galvanic series the order is the other way round: copper ≈ −0.30 to −0.36 V, 90/10 and 70/30 Cu-Ni slightly nobler, and nickel ≈ −0.10 to −0.20 V (vs. SCE; exact ranges [to verify] against ASTM G82 / LaQue). Nickel is nobler, so in a Cu–Ni couple **copper** is the anode and corrodes preferentially. Passive nickel alloys sit even more noble. Grok's practical advice still holds: use Cu-Ni alloys or isolate dissimilar metals.
- Cu-Ni 90/10 and 70/30 are marine alloys with protective Cu₂O-based films. **Grounded.**
- "Cymatic structuring in water-based nodes" is **not supported**. See [muon_cathode_acoustic_water_review.md §4](muon_cathode_acoustic_water_review.md#4-water-acoustics-centrifugal-buoyancy-2158).

## 4. "An electric wave" striking Cu/Ni in salt water [6]

- Eddy currents, induction heating and electrolysis by-products (chlorine) are **Grounded**.
- **Correction (heating).** Grok says copper "excels" at Joule heating "(low resistance)." The reverse is true for induction heating. Low resistivity and a non-magnetic response make copper hard to induction-heat. Ferromagnetic nickel heats far more strongly below its Curie point, through hysteresis plus a small skin depth from μ_r ≫ 1. This is why induction cookware is ferromagnetic and coils are copper.
- **Missing limit.** Seawater (σ ≈ 4–5 S/m) absorbs RF strongly. Skin depth is ~0.25 m at 1 MHz and ~2.5 cm at 100 MHz, so a wave "striking" submerged metal from a distance mostly heats the water.
- "Golden-ratio spirals matching the wave" for efficient wireless power is **Symbolic**: the φ tests found no advantage ([method_phi_and_natural_craft.md](method_phi_and_natural_craft.md)).
- Plasma or arcing in conductive media is **Grounded** as a hazard.

## 5. Magnetostrictive nickel in a water/helium cavity with piezo feedback [8]

- Nickel-lamination ultrasonic transducers (sonar, ultrasonic cleaners) and magnetostrictive waveguide position sensors are **Grounded**. Nickel was the classic sonar transducer material; Terfenol-D and Galfenol now outperform it.
- A Ni driver plus piezo pickup in a closed loop is a **Plausible-untested** bench build: an ordinary self-oscillating transducer.
- **Contradiction.** Grok lists helium for "cryogenic stability … quantum-fluid behaviors in superfluid He-II" in the same cavity as liquid water. He-II exists only below 2.17 K, where water is solid. At water temperatures, helium is an ordinary light gas: high sound speed (~1007 m/s) and low acoustic impedance. It couples poorly to a water-loaded driver because of the impedance mismatch.

## 6. The "spark plug" for the dual twisting toroid [9][10]

- **Speculative.** No mechanism was given for how a strain pulse in pressurised gas would "ignite" lift.
- **Grounded constraint.** Centrifugal force in a rotating fluid inside the craft is an *internal* force. It stratifies the fluid (centrifugal buoyancy; see [acoustic_streaming_and_centrifugal.md §2](acoustic_streaming_and_centrifugal.md#2-centrifugal-buoyancy-grounded)) but cannot produce net lift on the closed system, because momentum is conserved. Lift still needs reaction against the floor (eddy currents), the air, or ejected mass.
- **Hover power.** Grok's "grounded eddy-current lift today" restates the 520 W premise. The repo model gives ~10–17 kW for 88 kg ([ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md)).
- "Dual-twist … reduces unwanted inductance … amplifying resonant Q" is **Speculative**. Bifilar winding does lower inductance, but that does not raise Q by itself.
- "Vortex math (3-6-9)" is **Symbolic** ([kolmogorov_rodin_ulam_smatrix_review.md](kolmogorov_rodin_ulam_smatrix_review.md)).
- **Safety.** A "highly pressurised dense gas" cavity is a pressure vessel. It needs a rated vessel and a relief valve before any bench test.

## 7. Open items

- [to verify] Seawater galvanic potentials for Cu, Cu-Ni and Ni (ASTM G82 table); the Ni nanowire "giant" magnetostriction values.
- [Channing to supply] The gas, pressure and frequency you had in mind for the "spark plug" cavity, and what "lift" means here: thrust on the craft, or internal flow organisation.
