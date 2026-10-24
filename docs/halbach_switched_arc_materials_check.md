# Switched 45° Halbach arc: hybrid PM + coil zones, hard vs ramped switching, and magnet materials (NdFeB, SmCo, nickel, AlNiCo, ferrite)

*License CC0. Requested by Channing (2026-10-24): the POL impedance zone is currently driven by Tesla coils. He wants a 45°-per-segment Halbach arc (M = 8, matching the drag sim), switching zones on/off to steer the field angle and boost the field, and is worried about warping and damage. He also asked about cost, samarium cobalt and nickel. Sim: [`sims/halbach_switched_arc_check.py`](../sims/halbach_switched_arc_check.py) → [`sims/halbach_switched_arc_check_output.txt`](../sims/halbach_switched_arc_check_output.txt), plots `sims/halbach_arc_eddy_heating.png`, `sims/halbach_arc_demag_margin.png`. Labels: **Grounded** (physics / model output), **Plausible-untested** (hardware), **Speculative**. There are no Grok-reported numbers here. Datasheet values are typical (MMPA 0100-00 standard; Arnold Magnetic Technologies, Electron Energy and similar catalogues) and are marked [to verify] against a specific supplier grade before purchase.*

**Geometry assumed:** λ = 10 cm, M = 8 (45° steps), 5 % insulating gaps, segments 11.9 × 25 × 50 mm. Hybrid: permanent-magnet segments set the base field; low-voltage litz trim coils in "zones" add ±0.15 T to steer or boost it.

## 1. Mechanical (warping/damage)
| Quantity | Value | Label |
|---|---|---|
| Surface field / magnetic pressure (N42-class, B_r 1.30 T) | B₀ ≈ 0.96 T → **0.36 MPa** | **Grounded (model)** |
| Peak net inter-segment force (3-D surface-charge model, rigid magnets) | **~370–920 N per 12 × 50 mm segment** (grid not fully converged; scale B_r²/2μ₀ × side face = 840 N). Design value 920 N, about 1.6 MPa on the footprint. Segments alternately push out and pull in, so the retainer must hold every other segment against ejection | **Grounded (model)**, ±factor 2 |
| Pressure change per trim-zone event (0.15 T on 0.96 T) | **123 kPa** (34 % of static) | **Grounded (model)** |
| Hard switch vs ramp (first retainer mode assumed ~800 Hz) | Dynamic amplification: hard **2.0** → 246 kPa peak; 1 ms ramp 1.23; ≥ 5 ms ramp **1.00** → 123 kPa. **Ramping halves the peak load** | **Grounded (model)** |
| Sin/cos blending of adjacent zones (I_A = I cos θ, I_B = I sin θ) | Steers the trim-field angle with constant amplitude. The pressure swing over a 90° steer is 114 kPa quasi-static, versus 246 kPa dynamic for hard on/off | **Grounded (model)** |
| Retainer strip, 50 mm span, 5 mm thick, 2.17 MPa design load | Ti-6Al-4V: σ 162 MPa, SF 5.4, deflection 0.15 mm. Al 7075-T6: SF 3.1 (fatigue SF ~0.9), deflection 0.24 mm. CFRP: SF 3.7, 0.28 mm. G10: SF 1.85 (fatigue ~0.55), 0.94 mm | **Grounded (model)** |
| Mycelium composite (raw, ~0.2–1.1 MPa published, e.g. Jones et al. 2020, *Mater. Des.* [to verify]) | Fails by orders of magnitude; **inadequate for magnet retention** unless densified/hot-pressed, and even then use it only as a filler/damper behind a metal or composite retainer | **Grounded** |

**Fatigue:** each switching event is a load cycle. Al 7075 has no true endurance limit and sits at fatigue SF ≈ 0.9 for hard switching, so use Ti or CFRP, or thicken the Al and ramp. Ramping (≥ 5× the structural period) removes the ×2 dynamic factor.

## 2. Thermal: eddy heating at Tesla-coil frequencies
Assumes ripple field B_ac on the magnets and forced-air cooling h = 50 W/m²K. Magnet resistivity: NdFeB ~1.4–1.6 µΩ·m, SmCo ~0.5–0.9 µΩ·m [to verify].

| Case (per segment) | 100 kHz | 1 MHz | Label |
|---|---|---|---|
| NdFeB solid, B_ac 5 mT | 15 W, **ΔT ≈ 71 K** | 48 W, 225 K | **Grounded (model)** |
| NdFeB 1 mm laminations, 5 mT | 0.34 W, **ΔT ≈ 1.6 K** | 34 W, 160 K (skin-limited, so lamination no longer helps) | **Grounded (model)** |
| SmCo solid / laminated, 5 mT | 52 K / 3 K | 164 K (skin-limited) | **Grounded (model)** |
| B_ac 20 mT | ×16 (solid NdFeB > 1000 K: destroyed) | — | **Grounded (model)** |

- Skin depth at 100 kHz: NdFeB 1.95 mm, SmCo 1.42 mm; at 1 MHz: 0.62 / 0.45 mm.
- **Takeaway:** keep the Tesla-coil HF field off the magnets. Use a copper/aluminium shield sheet or distance, and segment/laminate the magnets (≤ 1 mm) wherever ripple remains. At ≳ 500 kHz lamination stops helping, so shielding is the only fix.
- **Litz strand sizing** (strand ≤ ½–1 copper skin depth): 50 kHz 0.15–0.29 mm (~AWG 31); 100 kHz 0.10–0.21 mm (~AWG 34); 500 kHz 0.05–0.09 mm (~AWG 41); 1 MHz 0.03–0.065 mm (~AWG 44). **Grounded.** The proximity effect needs bundle twisting; it is not modelled in detail.

## 3. Demagnetisation margin
The worst segment's internal reverse field from the charge model, including self-demag, is **μ₀H ≈ 0.72 B_r** (points 15 % in from the corners; true corners are worse). A **0.15 T opposing coil field** is added on top, and HcJ is derated with temperature. This is a knee approximation: margin = HcJ(T) − |H_rev|.

| Material (typical) | B_r (T) | HcJ (kA/m) | T_max (°C) | T_Curie (°C) | Margin 20 °C | 80 °C | 120 °C | 150 °C |
|---|---|---|---|---|---|---|---|---|
| NdFeB N42 | 1.30 | 1000 | 80 | 310 | +136 (marginal) | **demag** | demag | demag |
| N42SH | 1.30 | 1590 | 150 | 340 | +726 | +255 | **demag** | demag |
| N42UH | 1.29 | 1990 | 180 | 350 | +1132 | +588 | +226 | **demag** |
| N42EH | 1.28 | 2390 | 200 | 350 | +1538 | +873 | +431 | +99 (marginal) |
| Sm₂Co₁₇ (30 MGOe) | 1.10 | 1990 | 300 | 820 | +1241 | +956 | +765 | **+623** |
| SmCo₅ (20 MGOe) | 0.90 | 1990 | 250 | 720 | +1355 | +1011 | +781 | +609 |
| AlNiCo 5 | 1.25 | 51 | 525 | 860 | **demag** | demag | demag | demag |
| AlNiCo 8 | 0.82 | 150 | 550 | 860 | **demag** | demag | demag | demag |
| Ferrite C8/Y30 | 0.39 | 240 | 250 | 450 | demag* | demag* | marginal | marginal |

- Label: **Grounded (model)**; datasheet values [to verify].
- Temperature coefficients used (B_r / HcJ, %/K): NdFeB −0.12 / −0.5 to −0.6; Sm₂Co₁₇ −0.035 / −0.25; SmCo₅ −0.045 / −0.30; AlNiCo −0.02 / ~0; ferrite −0.20 / **+0.27**.
- *Ferrite fails here mainly because of the 0.15 T opposing coil field (comparable to its own B_r). Without the coil it sits near the knee at 20 °C. Ferrite's HcJ *rises* with temperature, so cold is its worst case. To use ferrite, keep the opposing coil field ≲ 0.05 T on ferrite segments.

## 4. Switching transients (design level)
- Example trim coil: L = 20 µH, I = 50 A, stored energy ½LI² = 25 mJ per zone.
- L·di/dt: 10 kV for a 100 ns hard turn-off, 1 kV at 1 µs, 10 V at 100 µs, 1 V for a 1 ms ramp. **A 1 ms ramp cuts the spike ~10⁴× versus a 100 ns hard switch.** **Grounded.**
- Snubber/clamp to 200 V: an RC of C ≈ 1.25 µF, R ≈ 4 Ω, or a TVS/flyback path back to the bus. **Grounded.**
- **Creepage/clearance:** IEC 60664-1 tables give roughly 5 mm creepage per kV rms (pollution degree 2, material group IIIa) and ~1–1.5 mm clearance per kV impulse [to verify against the tables for the actual voltages]. Paschen: ~3 kV/mm uniform-field breakdown in air at 1 atm, lower at sharp edges.
- A 1–2 mm insulating gap stands off hundreds of volts to ~1 kV, **not Tesla-coil secondary voltages (tens to hundreds of kV).** Keep the switched trim zones on a separate low-voltage litz bus, galvanically isolated and physically distant from the Tesla secondary.

## 5. Materials, cost and supply
| Material | Price, 2025–26 (finished magnet) | Brittle / corrosion | Supply, ethics, regeneration | Role here |
|---|---|---|---|---|
| NdFeB N42 | ~$40–85/kg (spot blanks ~$38–46 on magsees.com; trade $65–120 per datadeep.tech) | Brittle; corrodes, needs Ni-Cu-Ni or epoxy coating | Nd/Pr mining concentrated in China (export controls since 2025); Dy/Tb for SH/UH grades. Recycling (hydrogen decrepitation) is emerging | Base segments, cool positions |
| NdFeB SH/UH/EH | ~$45–175/kg (high-coercivity premium ~60 %) | Same | Heavy-rare-earth (Dy/Tb) intensive | Most segments if T ≤ 120 °C (UH) |
| Sm₂Co₁₇ / SmCo₅ | **~$150–300/kg** trade (datadeep.tech). Procurementresource.com shows an index of ~$42/kg FOB (Aug 2026), which conflicts [to verify] | Very brittle (chips); excellent corrosion resistance | ~50 % cobalt (DRC export quota from Oct 2025; artisanal-mining ethics); samarium under Chinese export licensing | Hottest / highest-reverse-field segments, and anything near the HF coil |
| AlNiCo 5/8 | ~$40–100/kg [to verify] | Tough, machinable; good corrosion resistance | Contains Ni and Co; no rare earths | **Unsuitable** in a Halbach (demagnetises); only for low-reverse-field sensors |
| Ferrite (Sr/Ba) | ~$8–12/kg | Brittle; inert (oxide), no coating needed | Abundant iron oxide; lowest footprint; widely recycled | Low-cost, regenerative option at low field |
| **Nickel (pure)** | ~$15–18/kg metal [to verify] | Ductile; good corrosion resistance | Mining footprint (Indonesia, laterites) | **Not a permanent magnet.** A soft ferromagnet (B_s ~0.6 T, near-zero coercivity): used as plating on NdFeB, a weak flux guide, or as **Ni–Fe permalloy** soft back-iron and shielding |

**Field and lift per dollar** for the 88 kg (863 N) array. Assumptions: flat array, λ = 10 cm, d = λ/4, gap 10 mm, lift factor 0.9, magnet mass only (no coils, retainer or labour). **Plausible-untested** estimate.

| Material | B₀ (T) | Area for 863 N | Magnet mass | Magnet cost | Lift per $ |
|---|---|---|---|---|---|
| N42 | 0.96 | 93 cm² | 1.65 kg | $66–140 | 6–13 N/$ |
| N42UH | 0.95 | 94 cm² | 1.68 kg | $84–293 | 3–10 N/$ |
| Sm₂Co₁₇ | 0.81 | 129 cm² | 2.6 kg | $390–775 | 1.1–2.2 N/$ |
| SmCo₅ | 0.66 | 193 cm² | 3.9 kg | $580–1160 | 0.75–1.5 N/$ |
| Ferrite | 0.29 | 1030 cm² | 12 kg | $96–144 | 6–9 N/$ (but 7× the mass, a big hit for an 88 kg craft) |

(The drag sim's rotor geometry uses more magnet than this flat-array minimum. Scale the cost by the actual volume.)

## 6. Recommendation
1. **Hybrid arc: NdFeB UH/EH for most segments, Sm₂Co₁₇ for the hottest and highest-reverse-field segments** (the transverse/"push-out" positions and any segment within the HF coil's reach). SmCo keeps > 600 kA/m of margin at 150 °C; N42 fails by 80 °C. **Grounded (model)**; final grade choice **Plausible-untested**.
2. **Ramp, don't hard-switch.** Use sin/cos blending of adjacent zones with ramps ≥ 5× the retainer's structural period (≥ 5 ms for an ~800 Hz retainer). This halves peak mechanical load and cuts L·di/dt spikes by orders of magnitude. **Grounded (model).**
3. **Keep the Tesla-coil HF off the magnets.** Shield them and laminate to ≤ 1 mm, and put the trim zones on an isolated low-voltage litz bus with snubbers. **Grounded.**
4. **Retainer:** Ti-6Al-4V or CFRP (G10 only with thicker sections), never raw mycelium. Mycelium can serve as a damping or filler layer behind the retainer. **Grounded / Plausible-untested.**
5. **Cost/regenerative option:** ferrite segments with ≤ 0.05 T opposing coil field, accepting about 7× the magnet mass. **Plausible-untested.** **Nickel** belongs in plating and permalloy back-iron, not as the magnet. AlNiCo is out.

## 7. Caveats
- The charge model assumes rigid magnets with μ_r = 1, a straight array and no adhesive layer. The peak force is only converged to a factor of ~2 (370–920 N).
- Reverse fields were evaluated 15 % in from the corners; actual corners are worse, so use FEM (e.g. FEMM or Elmer) before choosing a grade.
- The retainer's structural period (800 Hz), the ripple amplitude (5 / 20 mT), cooling (h = 50) and the coil values (20 µH, 50 A) are assumptions.
- Prices are volatile and the trade sources conflict [to verify].
- No bench data exists.

*See also: [halbach_litz_drag_reduction.md](halbach_litz_drag_reduction.md), [halbach_rotor_control_vs_perturbation_sections.md](halbach_rotor_control_vs_perturbation_sections.md), [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md).*
