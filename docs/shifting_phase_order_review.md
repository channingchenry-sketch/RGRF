# "Shifting phase order" / Physics Pathways — critical review

Reviewed 2026-10-11. License: CC0 1.0. Sources: two Resona/Grok notes dated 11 Oct 2026, "POL/RGRF Physics Pathways, Laminar Precession Dynamics & Material Lists" and "Supporting Diagrams" (the 4 diagrams are in `images/`).

## 0. Important scope note
The source notes **do not mention** a re-entry plasma sheath, ferrofluid veins, a "double magnetic egg cavity", impedance sections, or the phrase "shifting phase order". What they actually contain:
- the eddy-lift core pathway;
- RGRF scaling;
- "Laminar Precession Dynamics" with "Multi-Egg"/"Egg-of-Columbus style rotors";
- four "Perturbation Sections";
- a materials BOM.

Section A reviews those pathways as written. Section B reviews the elements Channing described verbally:
- external field / plasma manipulation using the re-entry sheath as a guide;
- the double magnetic egg cavity;
- ferrofluid veins;
- impedance / perturbation sections.

Section B gives numbers for a ~10 m craft in re-entry plasma.

Tags:
- **GROUNDED**: a known phenomenon with a governing equation.
- **PLAUSIBLE-UNTESTED**: the physics allows it, but there is no demonstration in this form.
- **SPECULATIVE**: no known mechanism.

Where I name prior work, it is only work I am confident exists; nothing has been invented. Where I am unsure of a specific reference, I describe the field instead of citing it.

---

## A. Pathways as written in the drafts

### A1. Core pathway: coils → eddy currents → lift (POL v0.1)
Chain: battery/pedal → 13.56 MHz phi-spiral coil → AC B-field → eddy currents in Al/Cu floor → opposing field (Lenz) → lift. "Mycelium frame ... natural damping that helps stabilize the hover".

| Step | Tag | Notes |
|---|---|---|
| AC coil over conductor gives repulsive force | GROUNDED | Lenz / induction levitation (EDS maglev, levitation melting). Force per area ≈ B²/(2μ₀) for a thick plate. |
| Lift at the claimed ~520 W, "efficiencies in the high 80s to low 90s" | Not supported (see the hover-sim review in [Resona-POL-Modular-Core](https://github.com/channingchenry-sketch/Resona-POL-Modular-Core)) | Plate loss alone is P/F ≥ ωδ. At 13.56 MHz that is ~1.9 MW for 1030 N; at ~1 kHz it is ~16.7 kW. The "efficiency" is a wireless-link formula with no receiver coil. |
| Conductive floor is mandatory | GROUNDED | Correct, and stated honestly in the draft. |
| Mycelium frame damps hover oscillation | SPECULATIVE as a hover-stabiliser | Material damping inside the board cannot damp rigid-body heave relative to the floor. This needs active control (or eddy damping in a separate conductor). |

### A2. Scaling pathway (personal → planetary → cosmic)
| Step | Tag | Notes |
|---|---|---|
| Same EM foundation at larger scale over conductive tracks | PLAUSIBLE (engineering) | EDS maglev already exists at train scale. |
| φ / 3-6-9 scaling of size, frequency and power | SPECULATIVE | No physical scaling law. Lift ∝ area·B² and loss ∝ √f·area·B² are ignored (the RGRF scaler script multiplies by arbitrary level factors). |
| Plasma filaments as "rails", consciousness-geometry coupling, free-air operation | SPECULATIVE | The draft itself labels these as speculation, which is to its credit. |

### A3. Laminar precession base state (Multi-Egg rotors)
Chain: phi-spaced coils/rotors spin with 3-6-9 phasing → the axis precesses in a cone → the "laminar" organised mode → "lift assist and attitude control".

| Step | Tag | Notes |
|---|---|---|
| Spinning rotor under torque precesses | GROUNDED | Ω_p = τ/(Iω). |
| Fluid in a precessing container keeps a laminar "spin-over" mode below a threshold | GROUNDED (fluid dynamics) | Studied experimentally and theoretically (e.g. Kerswell; Lagrange, Meunier et al.). Control parameter is the Poincaré number Po = Ω_p/Ω. |
| Golden-ratio spacing "keeps the modes phase-locked" | SPECULATIVE, and likely backwards | φ is the "most irrational" ratio. In coupled-oscillator and KAM theory, irrational ratios *avoid* mode-locking. If φ does anything here it is to discourage locking, not create it. |
| Organised precession provides **lift assist** | SPECULATIVE (no mechanism) | Internal rotation or precession of a closed system cannot produce net external force (momentum conservation). Only torques are possible. The draft does say "Free-air residual forces remain very small". |
| Organised precession provides **attitude control** | GROUNDED | Control-moment gyros, as on spacecraft. |

### A4. Perturbation sections
1. **Height.** Chain: load step → h changes → the steep F(h) restores → damping → power/frequency modulation.
   - Steep F(h) restoring: GROUNDED.
   - Mycelium damping: SPECULATIVE (see A1).
   - Power modulation as feedback: GROUNDED (standard active control). The diagram's target ζ ≈ 0.7 is sensible but needs a sensor + controller; the current simulation gives ζ ≈ 0.024.
2. **Tilt.** Chain: lean → gyroscopic moment + differential coil power → corrective torque.
   - Gyroscopic resistance: GROUNDED. It resists *rate*, converting tilt into precession/nutation. On its own it does not produce a restoring stiffness toward level.
   - Differential coil power giving torque: GROUNDED (eddy force per coil).
   - "If laminar ... smooth; if turbulent mode coupling ... control lost": PLAUSIBLE-UNTESTED for an EM system. The analogy to fluid instability has no defined EM "turbulence" here.
3. **Lateral.** Chain: phase shift between coils → horizontal force.
   - GROUNDED: a travelling-wave field over a conductor is a linear induction motor, F_x ∝ slip.
   - "Boundary-layer style self-correcting EM layers": SPECULATIVE wording. Eddy-current drag does damp lateral motion over a plate (GROUNDED), but nothing "self-corrects".
4. **Mode / triadic resonance.** Chain: frequency ratio → spin-over mode parametrically excites secondary modes → detune to stay laminar.
   - Triadic resonance instability in precessing cylinders: GROUNDED (fluids).
   - Applying it to resonant coil arrays: PLAUSIBLE-UNTESTED. Parametric coupling between LC resonators is real (nonlinear circuits), but this system as specified is linear, so there is no triadic coupling to avoid unless magnetic cores or ferrofluids add nonlinearity.

### A5. Materials BOM
Mostly GROUNDED as stated:
- Al/Cu floor;
- 10 AWG/Litz wire;
- PP film capacitors;
- GaN/SiC Class-E driver.

Notes:
- **Inconsistency:** this BOM's coil (~8 turns, r₀ 0.30 m, 45–55 µH) differs from `resonance_calc.py` (389 µH, 30.7 m of wire).
- **Mycelium–graphene diamagnetic levitation:** "millimeter scale only" is honestly hedged. Diamagnetic levitation needs B·∇B on the order of 10³ T²/m for graphite.

---

## B. Channing's verbal pathways: external field / plasma manipulation

Assumed setting:

| Parameter | Value |
|---|---|
| Craft length | L ≈ 10 m |
| Velocity | u ≈ 7 km/s |
| Altitude | ~50–80 km; neutral density n_n ~1e21–1e23 m⁻³; mass density ρ ~5e-5 to 5e-3 kg/m³ |
| Electron density | n_e = 1e17–1e19 m⁻³ |
| Temperature | T_e ≈ 1 eV |

Collision estimates use σ_en ≈ 1e-19 m², σ_in ≈ 5e-19 m². These are order-of-magnitude only (order-of-magnitude script estimates).

### B1. Re-entry plasma sheath as a "guide": basic plasma scales
- **Debye length** λ_D = √(ε₀T_e/(n_e e²)):
  - 23 µm at 1e17 m⁻³;
  - 7.4 µm at 1e18 m⁻³;
  - 2.4 µm at 1e19 m⁻³.
  
  **GROUNDED.** The electrostatic sheath on the wall is only microns to tens of microns thick. The "sheath" in "re-entry plasma sheath" usually means the whole ionised shock layer (cm to tens of cm), which is quasi-neutral.
- **Plasma frequency** f_pe = 8.98√n_e Hz:
  - 2.8 GHz at 1e17 m⁻³;
  - 28 GHz at 1e19 m⁻³.
  
  This is why S/X-band links black out. **GROUNDED.**
- **"Using the sheath as a guide/waveguide"**:
  - Guiding signals along a plasma boundary (surface waves): PLAUSIBLE-UNTESTED for this use.
  - Guiding the *craft*: SPECULATIVE.

### B2. Magnetic manipulation of the shock-layer flow (MHD flow control / "magnetic window")
Chain: onboard magnet (B) → u×B drives current j in the conducting shock layer → j×B force decelerates the flow and moves the shock off the body → less heating and more drag; or, separately, B makes the plasma transparent to RF.

**MHD drag/heat-flux control: GROUNDED.**
- Proposed by Resler & Sears and Bush (late 1950s).
- Studied numerically and experimentally since. To my knowledge this includes arc-jet/wind-tunnel tests, including at DLR, and Japanese flight-oriented studies. Exact papers should be checked before citing.

Key parameters:

| Quantity | Formula | Value |
|---|---|---|
| Electron–neutral collision frequency | ν_en = n_n σ v_th | ~7e7–7e9 s⁻¹ |
| Electrical conductivity | σ_e = n_e e²/(m_e ν_en) | ~0.4 to 4,000 S/m across the range |
| Electron Hall parameter | β_e = ω_ce/ν_en | — |
| B for β_e = 1 | ν_en m_e/e | ≈ 0.4 mT (80 km) / 4 mT (~65 km) / 40 mT (~45 km) |
| B for ion Hall parameter β_i = 1 (ion slip) | — | ≈ 0.2 T / 1.7 T / 17 T |

So for any useful B (0.1–1 T), electrons are strongly magnetised (β_e ~ 10–3000).

**Magnetic interaction parameter** (Stuart number) Q = σ_e B² L/(ρu):

| Case | Q |
|---|---|
| n_e = 1e19, ~65 km, B = 1 T | ~10³ |
| n_e = 1e19, ~65 km, B = 0.1 T | ~10 |
| n_e = 1e17, ~65 km, B = 1 T | ~10 |
| n_e = 1e17, ~45 km, B = 0.1 T | ~10⁻³ |

Q ≳ 1 means the field significantly reshapes the flow.

**Hall-effect caveat (GROUNDED, and critical):**
- If the Hall current cannot circulate freely, the effective conductivity drops by 1/(1+β_e²) and Q collapses by 10³–10⁶.
- An insulating wall blocks the meridional Hall current; electrodes or body geometry that let it close restore part of it.
- Whether the effect is useful depends on electrode/geometry design, not on field strength alone. This is the real engineering question.

**Energy cost:**
- Stored field energy is B²/2μ₀: ~4 kJ/m³ at 0.1 T, ~400 kJ/m³ at 1 T.
- A 1 T field over a few m³ in front of a 10 m nose means MJ-class stored energy.
- Resistive copper magnets need on the order of 0.1–1 MW continuous. Superconducting magnets are near-zero power but carry cryogenic mass.
- The flow does work on the field (the MHD generator effect), so some power can in principle be extracted. That is GROUNDED (MHD energy bypass concepts), but not "free".

**Magnetic window for blackout: GROUNDED in principle.**
- For f_signal < f_ce = 28 GHz/T × B, waves propagate in the whistler (R-wave) mode through overdense plasma.
- 1.5 GHz (GPS) needs B ≳ 0.06 T at the antenna.
- To bring 1e19 m⁻³ plasma fully below cutoff you need B ≳ 1 T near the antenna.
- Collisions (ν ~ 10⁸–10⁹ s⁻¹ ≪ 2πf) are acceptable.
- Static-field and E×B-layer blackout-mitigation schemes have been analysed in the literature. I believe this includes Michigan work (Kim, Keidar, Boyd), but please verify the exact citation.

**E×B / Hall drift: GROUNDED.**
- v_E = E/B. Crossed electrodes plus a magnet near the antenna can push electrons out and locally deplete n_e (the E×B blackout-mitigation concept).
- Energy cost: ion current × sheath voltage. Power is kW-class per m² of window for 1e18–1e19 m⁻³ plasma (rough estimate).

**Magnetic mirror confinement of the shock layer** (field strengthening toward the coils reflects particles with v⊥/v > 1/√R): **GROUNDED** as a confinement principle. At these collision frequencies (ν ≫ bounce frequency) mirror trapping is mostly destroyed, so it is **PLAUSIBLE-UNTESTED** for re-entry and probably weak.

### B3. Double magnetic egg cavity with laminar precession
Chain: two nested egg-shaped field cavities → circulating plasma/fluid precesses laminarly → organised flow → lift / steering / stability.

| Step | Tag | Notes |
|---|---|---|
| Ellipsoidal cavities supporting laminar precessional flow | GROUNDED | Precession-driven flow in spheroids (geodynamo analogue experiments). |
| Larmor precession of charged particles / magnetic moments | GROUNDED | ω_L = γB for spins; ω_c = qB/m for charges (28 GHz/T for electrons). This is microscopic gyration, not macroscopic flow precession. Equating them is a category slip. |
| Rotating plasma in E×B in a closed cavity | GROUNDED | Plasma centrifuges, rotating-plasma devices. |
| Internal organised precession gives net lift or thrust | SPECULATIVE (no mechanism) | Closed-system momentum conservation applies (A3). |
| Internal precession reshapes the *external* re-entry flow | SPECULATIVE beyond the fringe B-field itself | Only the field that leaks outside matters, i.e. B2. |

### B4. Ferrofluid veins (magnetoviscous / impedance sections)
Chain: field across ferrofluid channels → viscosity or magnetisation changes → tunable damping, impedance or pumping.

| Step | Tag | Notes |
|---|---|---|
| Magnetoviscous effect | GROUNDED | Viscosity rises in a field (Rosensweig; Shliomis rotational viscosity; Odenbach's measurements). Effect is ~10–100 % for commercial ferrofluids at 10–100 mT; larger for chain-forming fluids. |
| "Negative viscosity" in AC/rotating fields | GROUNDED | Shliomis & Morozov theory; Bacri et al. experiments, mid-1990s. Small effect, lab scale. |
| Ferrofluid spin-up / pumping in rotating fields | GROUNDED | Rosensweig, Zahn et al. |
| Ferrofluid as a tunable damper (vibration absorbers, MR/ferrofluid dampers) | GROUNDED | Commercial MR dampers. |
| Ferrofluid veins as tunable *magnetic* impedance (shaping B with μ_r ~ 1.5–5) | GROUNDED but weak | Low permeability; also losses at 13.56 MHz (Néel/Brownian relaxation heating = magnetic hyperthermia, GROUNDED). Ferrofluid at MHz will heat. |
| Ferrofluid veins coupling to the external re-entry plasma | SPECULATIVE | It is shielded inside the structure; it affects only the near-field B distribution. |
| Temperature | — | Ferrofluids lose magnetisation near the Curie point and the carrier boils. The structure must stay ≪ 150–200 °C. Re-entry needs thermal isolation. |

---

## C. Strongest grounded pathway
**MHD shock-layer control plus a magnetic/E×B communications window, using an onboard ~0.1–1 T magnet.** It has:
- real physics;
- decades of literature;
- Q ≳ 1 achievable at 1e18–1e19 m⁻³ and 60–70 km;
- clear failure modes: Hall effect, magnet mass/power, low n_e at high altitude, the thermal environment.

For the personal-scale POL, the strongest grounded extension is perturbation sections 1–3 with an active controller: power modulation for height and phase-shifted coils for lateral force. The precession and φ elements add nothing physical yet.

## D. Bench experiments (small, cheap, decisive)

1. **Magnetic window / E×B depletion in a lab plasma.**
   - Setup: a low-pressure RF or DC glow discharge (n_e ~1e16–1e17 m⁻³, f_pe ≈ 1–3 GHz) in a glass tube. Transmit 2.45 GHz (or a sweep) through it with horn antennas.
   - Measure attenuation with and without a 0.1–0.3 T NdFeB magnet assembly (f_ce = 2.8–8 GHz) at the antenna. Optionally add biased electrodes for E×B depletion and use a Langmuir probe for n_e.
   - Prediction: transmission recovers once f_ce > f_signal in R-wave orientation.
   - This directly tests the "sheath as a guide/window" idea at bench scale.
2. **MHD flow deflection in a conducting flow.**
   - Setup: a salt-water or Galinstan flow channel (or a small plasma torch/jet) past a blunt body with an internal NdFeB magnet.
   - Measure shock/standoff or wake change, and drag on a load cell, versus B. Compute Q = σB²L/(ρu) for each run and check that the effect scales with Q.
   - Add segmented vs. insulating walls to see the Hall-current role (needs a plasma jet; brine has negligible Hall effect).
3. **Ferrofluid "vein" precession cell.**
   - Setup: a transparent spheroidal (egg) cavity of ferrofluid on a precessing turntable. Add Helmholtz coils for static or rotating fields (0–50 mT) and tracer particles or ultrasound Doppler velocimetry.
   - Measure the spin-over mode amplitude and the laminar→unstable threshold (Poincaré number) versus field, i.e. whether the magnetoviscous effect shifts the transition.
   - Also put the whole cell on a scale or load cell to confirm zero net vertical force from internal precession. That is a good, honest null test of the "lift assist" claim.

Cheaper option for A4.3: two phase-shifted coils over an Al plate, with a load cell measuring lateral force versus phase. This is a 1-day LIM-style test.
