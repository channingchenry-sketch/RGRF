# Electrostatic isotropic tensor → Maxwell stress: review of Grok share `18a292a6` (2026-10-18)

*CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Numbers Grok gives without code shown are **Grok-reported** unless rerun here. **[to verify]** = not yet checked; **[Channing to supply]** = gap only Channing can fill.*

**Source (verbatim archive):** "Electrostatic Isotropic Tensor to Stress Tensor Conversion", 2 messages (1 user, 1 Grok): [grok_archive/2026-10-18_electrostatic_isotropic_tensor_to_stress_tensor_conversion.md](grok_archive/2026-10-18_electrostatic_isotropic_tensor_to_stress_tensor_conversion.md). Share #90 (`18a292a6`). No code in the share.

**Rerun:** [sims/electrostatic_maxwell_stress_check.py](../sims/electrostatic_maxwell_stress_check.py) ([output](../sims/electrostatic_maxwell_stress_check_output.txt)) — eigenvalues, trace, and heliosphere (E/cB)² ratios.

**Repo context (cross-links):**
- Core of RGRF, *spin/vortex tensors and scalars* pillar: [README.md → Core of RGRF](../README.md#core-of-rgrf).
- Isotropic electrostatic / Maxwell stress thread: [em_topological_gravity_review.md §L4](em_topological_gravity_review.md#l4-plasma-dynamics-around-an-em-field-the-isotropic-electrostatic-tensor-in-the-interstellar-medium), [§R3](em_topological_gravity_review.md#r3-pressure-gradients-isotropic-tensor--anisotropy-along-filaments-and-b), [§R4 leaky boundaries](em_topological_gravity_review.md#r4-leaky-boundaries-recurring).
- Maxwell stress eigenvalues (sheath / full EM): [inertia_sheath_stress_review.md](inertia_sheath_stress_review.md), [sims/s70_80_claim_checks.py §3](../sims/s70_80_claim_checks.py).
- Heliosphere: [heliosphere_fibonacci_review.md](heliosphere_fibonacci_review.md) (VLISM B ~0.4–0.5 nT).

## Channing (verbatim)

| Msg | Prompt |
|---|---|
| 1 | "One more thing, can we look at our electrostatic isotropic tensor converting to stress tensors? We already described it a little in the heliosphere context." |

## Plain summary

- **Grounded:** The electrostatic Maxwell stress σ_ij = ε₀ (E_i E_j − ½ δ_ij E²) is standard. Eigenvalues are +½ ε₀ E² along E (tension) and −½ ε₀ E² transverse (pressure/compression). Trace = −½ ε₀ E², **not zero** (unlike the 4D EM stress-energy tensor in vacuum). Force density on matter is ∇·σ minus the field-momentum rate ε₀ ∂_t(S/c²) when the magnetic / Poynting terms are restored.
- **Grounded:** Ambipolar E from the electron pressure gradient under quasi-neutrality is standard solar-wind physics.
- **Grounded (plausibility verified here):** Magnetic Maxwell stresses dominate the EM contribution at the heliopause; (E/cB)² ~ 10⁻⁹ for E ~ few μV/m and B ~ 0.1–0.5 nT.
- **Speculative:** Any φ-scaled or resonant "docking" reading of heliospheric boundary stresses (Grok labels this speculation; kept as such).

## A. Electrostatic Maxwell stress (msg 2)

| Claim | Check | Label |
|---|---|---|
| σ_ij = ε₀ (E_i E_j − ½ δ_ij E²); σ = ε₀ E⊗E − ½ ε₀ E² I | Standard vacuum electrostatic Maxwell stress (Jackson; Landau–Lifshitz) | **Grounded** |
| Outer product → tension along field lines and compression perpendicular; −½ ε₀ E² is the isotropic diagonal piece | Eigenvalues for E ∥ x̂: λ_∥ = +½ ε₀ E², λ_⊥ = −½ ε₀ E² (×2). Rerun: [sims/electrostatic_maxwell_stress_check.py](../sims/electrostatic_maxwell_stress_check.py) PASS | **Grounded** |
| Trace of the 3D electrostatic stress is −½ ε₀ E² (not zero) | Direct: tr σ = ε₀(E² − ³⁄₂ E²) = −½ ε₀ E². The **4D** EM stress-energy tensor is traceless in vacuum Minkowski spacetime; the **3D** Maxwell stress is not | **Grounded** (verified) |
| Force density recovered as divergence of σ (plus Lorentz terms when currents present) | Full local form (matter force density): f = ∇·σ − ε₀ ∂_t(S/c²) with S = E×H, reducing to ρE + J×B. Grok's wording is looser but points at the same conservation identity | **Grounded** (full form stated) |
| In linear isotropic dielectrics, ε replaces ε₀ | Standard (plus Kelvin / electrostriction terms when ε = ε(ρ); those extras are not in this share) | **Grounded** for the vacuum-like piece |

## B. Magnetic stress and heliosphere balance (msg 2)

| Claim | Check | Label |
|---|---|---|
| σ_ij^B = (1/μ₀)(B_i B_j − ½ δ_ij B²); magnetic pressure B²/2μ₀ and tension along B | Standard magnetic Maxwell stress | **Grounded** |
| Large-scale solar-wind / Parker-spiral / HCS / heliopause / termination-shock force balance carried mainly by magnetic stresses + plasma pressure tensor | Standard heliospheric MHD picture; VLISM \|B\| ~0.4–0.5 nT (Voyager; see [heliosphere_fibonacci_review.md](heliosphere_fibonacci_review.md), [em_topological L4](em_topological_gravity_review.md#l4-plasma-dynamics-around-an-em-field-the-isotropic-electrostatic-tensor-in-the-interstellar-medium)) | **Grounded** |
| Electrostatic piece smaller at heliospheric scales; secondary for global force balance at the heliopause | Order-of-magnitude: for E ~ 1–10 μV/m and B ~ 0.1–0.5 nT, (E/cB)² ∈ [1×10⁻⁹, 5×10⁻⁹] (sim §2). Magnetic stress wins by ~8–9 orders | **Grounded** (plausibility verified) |
| Exact E and B profiles used for the ratio at the heliopause / heliosheath | Share gives no numbers; sim uses a few-μV/m band. That band is the motional v×B field, not the ambipolar field (corrected 2026-10-18; see [Ambipolar field](#ambipolar-field-from-the-electron-pressure-gradient-2026-10-18)) | Band is **Plausible**; precise local values **[to verify]** |

## C. Ambipolar electric field (msg 2)

| Claim | Check | Label |
|---|---|---|
| Ambipolar E from quasi-neutrality + electron pressure gradient helps accelerate the solar wind | Standard: e n E ≈ −∇p_e (with ion inertia / charge neutrality), Parker / isothermal / polytropic wind models; also in exospheric / kinetic treatments | **Grounded** |
| Essential for small-scale charge-separation structures | Debye sheaths, double layers, etc. are real; scale separation from global heliopause balance is the point of §B | **Grounded** |

## D. Plasma pressure tensor vs scalar p (msg 2)

| Claim | Check | Label |
|---|---|---|
| Roughly isotropic plasma → scalar p; Maxwell stresses supply the EM anisotropy | Standard MHD closure | **Grounded** |
| Collisionless / weakly collisional → P_∥, P_⊥ relative to B, plus FLR corrections; total stress = plasma pressure tensor + Maxwell stress | Standard CGL / kinetic MHD | **Grounded** |

## E. Honest limits and RGRF framing (msg 2)

| Claim | Check | Label |
|---|---|---|
| Isotropic electrostatic approximation is a useful reduction, not a complete solar-wind description; kinetic anisotropies, heat flux, wave–particle effects matter | Agrees with modern heliospheric kinetic models | **Grounded** |
| Staying with observed plasma stresses and Maxwell’s equations is grounded physics | Matches the L4 / R3 framing | **Grounded** |
| φ-scaled or resonant "docking" interpretation of heliospheric boundary stresses | No equation or observation offered; Grok labels it speculation | **Speculative** |

## Relation to the L4 / R3 / R4 thread

Share #90 is a short follow-up on the **isotropic electrostatic tensor → Maxwell stress** conversion in the heliosphere context. It does **not** replace the lost L4 source conversation (that one also tied the isotropic tensor to Fuller's vector equilibrium). It does supply a clean, labeled statement of the conversion, the ambipolar role, and the magnetic dominance at the heliopause — all of which sit next to [L4](em_topological_gravity_review.md#l4-plasma-dynamics-around-an-em-field-the-isotropic-electrostatic-tensor-in-the-interstellar-medium), [R3](em_topological_gravity_review.md#r3-pressure-gradients-isotropic-tensor--anisotropy-along-filaments-and-b) (isotropic → anisotropic along B) and [R4](em_topological_gravity_review.md#r4-leaky-boundaries-recurring) (heliopause as a leaky boundary). L4's note that "no archived session uses 'isotropic' or 'tensor'" is outdated as of this archive; see the L4 pointer update.

## Contradictions with the repo

None. Tension-along-E / pressure-across-E matches [em_topological L4](em_topological_gravity_review.md#l4-plasma-dynamics-around-an-em-field-the-isotropic-electrostatic-tensor-in-the-interstellar-medium) and the eigenvalue picture in [inertia_sheath_stress_review.md](inertia_sheath_stress_review.md) (that file treats the full EM surface block, which is traceless in-plane when there is no z-component; the bulk 3D electrostatic stress here has trace −½ ε₀ E² — both statements are correct in their settings).


## Total stress form (Channing, 2026-10-18)

$$
\boldsymbol{\sigma}_{EM} = \epsilon_0 \Bigl( \mathbf{E}\otimes\mathbf{E} - \tfrac12 E^2\,\mathbf{I} \Bigr) + \frac1{\mu_0}\Bigl( \mathbf{B}\otimes\mathbf{B} - \tfrac12 B^2\,\mathbf{I} \Bigr)
$$

$$
\frac{\partial(\rho\mathbf{v})}{\partial t} + \nabla\cdot\bigl(\rho\mathbf{v}\mathbf{v} + \mathbf{P} - \boldsymbol{\sigma}_{EM}\bigr) = \rho\mathbf{g} + \text{other sources}
$$

**Grounded:**
- In (1), each part has tension +½ε₀E² (or B²/2μ₀) along its field and pressure −½ across it. The trace is −½(ε₀E² + B²/μ₀) = −u_EM.
- (2) is the momentum conservation law. Strictly, the left side also has ∂(ε₀ E×B)/∂t (the field momentum density S/c²). It is negligible for flows far below light speed, so dropping it is the standard MHD approximation. P is the plasma pressure tensor: p I if isotropic, or p⊥ I + (p∥ − p⊥) b b in CGL/gyrotropic form.
- For a static (∂/∂t = 0) axisymmetric shell with no flow other than rotation, (2) reduces consistently to the radial MHD force balance in [docs/poynting_vortex_force_balance_review.md](poynting_vortex_force_balance_review.md) (the share #66 corrected form: ρΩ²R = ∂(p + B²/2μ₀)/∂R + B_θ²/(μ₀R)). The sign convention matches exactly: centrifugal support balances the outward gradient of gas-plus-magnetic pressure plus the inward azimuthal-field tension term written on the same side.
- At the heliopause, (E/cB)² ~ 1e-9 (from [sims/electrostatic_maxwell_stress_check.py](../sims/electrostatic_maxwell_stress_check.py)), so the B term dominates the total stress. The same sim checks that the trace of (1) equals −u_EM for a random E and B.

## Ambipolar field from the electron pressure gradient (2026-10-18)

*Channing asked to follow up Grok's share #90 offer ("explicit ambipolar recovery"). Rerun: [sims/ambipolar_field_solar_wind.py](../sims/ambipolar_field_solar_wind.py) ([output](../sims/ambipolar_field_solar_wind_output.txt)); plot: [images/2026-10-18_ambipolar_field_solar_wind.png](images/2026-10-18_ambipolar_field_solar_wind.png).*

### Derivation (Grounded)

- Electron momentum with inertia dropped (m_e → 0): 0 = −e n_e (**E** + **u**_e × **B**) − ∇·**P**_e (+ collisional friction with ions).
- Along **B** (or with no B) the u_e × B term vanishes. With an isotropic electron pressure p_e:

  **E**_amb = −∇p_e / (e n_e)

- Isothermal (p_e = n_e k T_e, T_e constant): **E** = −(k T_e/e) ∇ln n_e.
- Polytropic (p_e ∝ n_e^γ): ∇p_e = γ k T_e ∇n_e, so **E** = −(γ k T_e/e) ∇ln n_e. The potential is then the electron enthalpy: e Φ(r→∞) = γ/(γ−1) k T_e(r).
- With n ∝ r⁻² (constant-speed wind): E_amb = 2γ k T_e(r)/(e r), pointing outward. For γ = 1.2, T_e ∝ r^−0.4.
- **History (verified):** Pannekoek, "Ionization in stellar atmospheres", *Bull. Astron. Inst. Netherlands* 1, 107 (1922); Rosseland, "Electrical state of a star", *MNRAS* 84, 720 (1924). In a static (hydrostatic) atmosphere with T_e = T_p the field gives eE = ½ m_p g (the "Pannekoek–Rosseland field"). Lemaire & Scherer showed that for an *expanding* atmosphere the zero-current condition needs a larger potential, and that drives the wind: "Kinetic models of the solar wind", *J. Geophys. Res.* 76, 7479 (1971). Kappa-distribution exospheric model: Maksimovic, Pierrard & Lemaire, *A&A* 324, 725 (1997).

### Solar-wind magnitudes (sim, n ∝ r⁻²)

| Case | r | E_amb | eE/(m_p g) |
|---|---|---|---|
| Isothermal, T_e = 40 eV | 0.1 AU | 5.3×10⁻⁹ V/m | 0.86 |
| Polytrope γ = 1.2, T_e0 = 40 eV at 0.1 AU | 0.1 AU | 6.4×10⁻⁹ V/m | 1.04 |
| Polytrope γ = 1.2, T_e0 = 100 eV at 0.1 AU | 0.1 AU | 1.6×10⁻⁸ V/m | 2.6 |
| Isothermal, T_e = 10 eV | 1 AU | 1.34×10⁻¹⁰ V/m | 2.16 |
| Polytrope γ = 1.2, T_e(1 AU) = 10 eV | 1 AU | 1.60×10⁻¹⁰ V/m | 2.59 |

- With an isothermal wind the ratio is 2 k T_e r/(G M m_p), so it grows linearly with r. A ratio above 1 means the electric force on a proton is larger than gravity. Above 0.5 means it is stronger than the hydrostatic Pannekoek–Rosseland field.
- **Corrections to the pre-sim estimates:**
  - 0.1 AU estimate (5×10⁻⁹ V/m, ratio ~0.9): **confirmed**.
  - 1 AU estimate (0.8–1.3×10⁻¹⁰ V/m, ratio 1.3–2.2): only the upper end holds for T_e = 10 eV with n ∝ r⁻². The 0.8×10⁻¹⁰ end needs T_e ≈ 6 eV, or a density slope of ~1.2 instead of 2. The γ = 1.2 polytrope gives 1.6×10⁻¹⁰ V/m and a ratio of 2.6.
  - n ∝ r⁻² is a poor fit inside ~0.1 AU, where the wind is still accelerating, so the 0.05 AU rows in the output are only indicative.
- **Potential drop (polytrope, γ = 1.2):** Φ(0.1 AU → ∞) = 6 k T_e0/e = **240 V (40 eV) to 600 V (100 eV)**. The numerical integral matches the analytic one. Φ(1 AU → ∞) = 96–239 V. The isothermal potential diverges logarithmically (2 k T_e/e · ln r), so it needs a closure such as γ > 1 or the exospheric cutoff.
- **Escape energy (correction):** the proton escape energy G M m_p/r is 199 eV at 10 R_sun but only **93 eV at 0.1 AU (21.5 R_sun)**. The 240–600 V drop is measured from 0.1 AU, so the like-for-like comparison is with 93 eV. On that basis the drop exceeds escape by ~150–510 eV, which by itself gives protons ~170–310 km/s. Measured from 10 R_sun the drop would also be larger, since T_e is higher there.
- **Parker Solar Probe measurement (verified):** Halekas et al., "The Sunward Electron Deficit: A Telltale Sign of the Sun's Electric Potential", *ApJ* 916, 16 (2021), doi:10.3847/1538-4357/ac096e. A sunward cutoff in SPAN-E electron distributions reaches ~10,000 km/s near perihelion, corresponding to **~285 V** between PSP and the outer heliosphere. Across the data the potential is **~50–300 V** for core T_e ~ 10–60 eV, scaling linearly with T_e with a slope of ~5. A slope of 5 corresponds to γ ≈ 1.25, close to the 6 that γ = 1.2 gives here. Follow-up: Berčič et al., *ApJ* 921, 83 (2021), doi:10.3847/1538-4357/ac1f1c, finds over 20.3–85.3 R_sun that Φ ∝ r^−0.66 and E_∥ ~ 1 nV/m ∝ r^−1.69. The exospheric estimate gives 77 % of the observed proton speed at 45 R_sun. The fluid E here (a few nV/m at 0.1 AU) is on the high side of that order of magnitude. The 240 V potential agrees well with the measured ~285 V. **Grounded.**
- These fields are far too small for in-situ electric-field instruments (Halekas et al. 2021). The potential is inferred from electron distributions.

### Comparison with the motional field (Grounded)

- At 1 AU, 400 km/s × 5 nT = 2 mV/m is an upper bound that uses the total B. With the Parker-spiral B_φ only (~47°), |**v** × **B**| = 1.5 mV/m. That is ~10⁶–10⁷ × E_amb at 0.05–5 AU (sim §4). The motional field is perpendicular to B and vanishes in the plasma frame, so it does not accelerate the wind along B.
- Heliosheath / VLISM: v B ≈ 10–20 μV/m (100 km/s × 0.1–0.2 nT) and ≈ 13 μV/m (26 km/s × 0.5 nT). Extrapolated to 120 AU, E_amb is only ~3×10⁻¹³ V/m.
- **Correction to §B / the stress-ratio sim:** the ~μV/m "E" in [sims/electrostatic_maxwell_stress_check.py](../sims/electrostatic_maxwell_stress_check.py) is the **motional** field, not the ambipolar field. The (E/cB)² ~ 10⁻⁹ conclusion stands, and for the ambipolar part alone it is far smaller: ~3×10⁻²⁰ at 1 AU (2.6×10⁻¹⁰ V/m, 5 nT) and ~10⁻²⁹ near the heliopause.
- **Bottom line:** the electrostatic (ambipolar) part matters for particle acceleration along B: it pushes protons out and holds most electrons back. It does not matter for the global boundary force balance, which is magnetic plus plasma pressure (§B).

### RGRF link: a measured leaky boundary

- The electrons' higher thermal speed would let them escape the Sun's gravity faster than the protons. The resulting charge separation sets up a potential that holds most electrons back and pulls protons out. The corona is a boundary that leaks plasma at a rate set by its own electric field, and PSP has measured that potential (~285 V).
- Ties to the *leaky boundaries* pillar: [README.md → Core of RGRF](../README.md#core-of-rgrf), [em_topological_gravity_review.md §R4](em_topological_gravity_review.md#r4-leaky-boundaries-recurring).
- **Labels:** the physics (ambipolar potential, exospheric acceleration, PSP measurement) is **Grounded**. Reading it as an instance of RGRF's recurring leaky-boundary pattern is **Plausible** (an analogy, not a shared mechanism).

### Grok's version (share #91)

*Share #91 (`753ca89b`) is the fuller capture of the share #90 conversation: [verbatim archive](grok_archive/2026-10-18_electrostatic_isotropic_tensor_to_stress_tensor_conversion_extended.md), 6 messages (3 user, 3 Grok). After msg 2, Channing asks "Can we do the next 2 steps?"; Grok does (1) the total-stress form plus a radial heliospheric-shell reduction and (2) the ambipolar field from the electron pressure gradient (msg 4). Channing then asks "Show the anisotropic total stress" and Grok gives the CGL form (msg 6). No code and no worked numbers in the share. Rerun of the one new checkable claim: [sims/electrostatic_maxwell_stress_check.py §5](../sims/electrostatic_maxwell_stress_check.py) ([output](../sims/electrostatic_maxwell_stress_check_output.txt)).*

| Grok (share #91) | Ours (sections above) | Verdict |
|---|---|---|
| σ_EM = ε₀(E⊗E − ½E²I) + (1/μ₀)(B⊗B − ½B²I); ∂(ρv)/∂t + ∇·(ρvv + P − σ_EM) = ρg + sources (msg 4) | Identical to [Total stress form](#total-stress-form-channing-2026-10-18), including the sign on σ_EM | **Agree. Grounded** |
| Same equation, no field-momentum term | We note the omitted ∂(ε₀ E×B)/∂t on the left and why it is negligible (v ≪ c) | **Grok loose:** drops the term without saying so. Not an error at MHD order |
| Radial shell: ρ v_r dv_r/dr = −d/dr(P + B²/2μ₀) **+** (B_θ² + B_φ²)/(μ₀ r) − ρGM_⊙/r² + F_es | Corrected (spherical, fields depending on r at the equator): ρ v_r dv_r/dr = −dP/dr − d/dr(B_⊥²/2μ₀) **−** B_⊥²/(μ₀ r) − ρGM_⊙/r², with B_⊥² = B_θ² + B_φ² | **Grok wrong (sign + extra term).** (a) Curvature (hoop) tension of transverse field lines pulls **inward**, so the term is −B_⊥²/(μ₀ r). (b) B_r must not sit in the pressure: B_r dB_r/dr from (B·∇)B cancels −d(B_r²/2μ₀)/dr exactly. For B_r ∝ r⁻², Grok's form leaves a spurious outward +2B_r²/(μ₀ r). **Grounded (sim §5)**: for a Parker spiral at the equator (B_φ ∝ 1/r, so r B_φ is constant), the finite-difference J×B and the corrected form both give ≈0 (roundoff, ~10⁻²⁸ N/m³ at 0.3 AU). Grok's form gives +1.2×10⁻¹⁹ N/m³ at 0.3 AU and +5.7×10⁻²² N/m³ at 1 AU. Uniform B_φ = 1 nT at 1 AU: corrected −5.3×10⁻²⁴ (inward), Grok +5.3×10⁻²⁴ N/m³ |
| (same) | Share #66 corrected form ρΩ²R = d(p + B²/2μ₀)/dR + B_θ²/(μ₀R) ([poynting_vortex_force_balance_review.md](poynting_vortex_force_balance_review.md)) puts tension on the **same side as the outward pressure gradient**, i.e. as an inward force balanced by centrifugal support | **Grok disagrees with #66 in sign.** The corrected spherical form above agrees with #66 (moving #66's right-hand side to the force side gives −dp*/dR − B_θ²/(μ₀R) + ρΩ²R = 0; θ in #66 is the azimuthal angle) |
| "Steady, spherically symmetric … no rotation" while keeping B_φ from the Parker spiral | B_φ needs solar rotation and is ∝ sin θ, so the shell is not strictly spherically symmetric; read it as the equatorial plane | **Grok loose** |
| F_es added as a separate body force; "or the force n_e e E_r can be kept as an explicit body force" | In the single-fluid equation the ambipolar force on protons (+n e E) and on electrons (−n e E) cancel; the net is ρ_c E ≈ 0. Its effect is already in −∇p_e inside P. ∇·σ_E = ρ_c E, and (E/cB)² ~ 3×10⁻²⁰ at 1 AU | **Grok loose / double-count risk:** adding n_e e E_r to a single-fluid equation whose P already contains p_e counts it twice. n_e e E belongs in the **proton** momentum equation |
| E∥ ≈ −(1/(n_e e)) ∂p_e/∂s; radial E_r ≈ −(1/(n_e e)) dp_e/dr; accelerates protons, restrains electrons, zero net current (msg 4) | Same as [Derivation](#derivation-grounded) (E_amb = −∇p_e/(e n_e)); sign: p_e falls outward, so E points outward | **Agree. Grounded** |
| "Observed values in the inner heliosphere are of order a few nV m⁻¹ and fall off … roughly as a power law" | Our fluid sim: 5–6×10⁻⁹ V/m at 0.1 AU (T_e 40 eV). Berčič et al. 2021 (*ApJ* 921, 83): E∥ ~ 1 nV/m ∝ r^−1.69 over 20–85 R_sun | **Grok-reported**; order of magnitude consistent. "Observed" is loose: the field is inferred from electron distributions, not measured by electric-field instruments (Halekas et al. 2021) |
| No potential value; "kinetic models (exospheric or SERM-type) are needed" for PSP | Our polytrope gives Φ(0.1 AU→∞) = 240 V (40 eV) vs the verified PSP **~285 V** (Halekas et al. 2021, *ApJ* 916, 16) | **Gap, not a conflict:** Grok gives no number to compare. "SERM-type" model name **[to verify]** |
| "The conversion of the isotropic electron pressure gradient into an electrostatic stress"; the ambipolar field "helps set p_e" (msg 6) | Causality runs the other way: ∇p_e sets E_amb. The electrostatic Maxwell stress ½ε₀E² of that field is negligible | **Grok loose** (wording) |
| CGL: P = p⊥I + (p∥ − p⊥)bb; invariants p∥B²/ρ³ and p⊥/(ρB); σ_tot = ρvv + P − σ_EM; isotropic limit p∥ = p⊥ (msg 6) | Matches the gyrotropic P already noted in [Total stress form](#total-stress-form-channing-2026-10-18) | **Agree. Grounded** (standard double-adiabatic closure) |
| "Mirror and firehose thresholds appear naturally when p⊥/p∥ becomes extreme" | Firehose does appear from the stress: the bb coefficient of the total stress is (p∥ − p⊥) − B²/μ₀, so field-line tension vanishes at p∥ − p⊥ = B²/μ₀ (β∥ − β⊥ = 2). The mirror threshold is not read off the stress; it needs the closure, and the CGL fluid mirror criterion differs from the kinetic one. Both depend on β, not only on p⊥/p∥ | **Grok loose. Grounded** as corrected |

**Net:** Grok's total-stress equation, ambipolar derivation and CGL tensor agree with ours (**Grounded**). The one substantive error is the radial-shell equation: wrong sign on the hoop-tension term, plus B_r² kept in the magnetic pressure. Use the corrected form above. It agrees with share #66. Grok's offered "worked 1 AU example" was never done in the share; the magnitudes above are from our sims.

## Items [to verify]

- Precise ambipolar \|E\| and \|B\| at the heliopause / heliosheath for a published (E/cB)² table (sim uses a few-μV/m band).
- "SERM-type" kinetic model named by Grok in share #91 msg 4 (identity not checked).
- Whether any earlier archived heliosphere session is the "we already described it a little" referent beyond [heliosphere_fibonacci_review.md](heliosphere_fibonacci_review.md) and L4.

## Open questions for Channing

1. Which of Grok's three follow-ups (radial total-stress shell, explicit ambipolar recovery, Blueprint / Entanglements aside) should be taken next, if any? *(Answered in share #91: Channing asked for the first two, then the anisotropic total stress; see [Grok's version (share #91)](#groks-version-share-91).)*

## Leaky-boundary stress jump and heliopause pressure balance (2026-10-22)

Channing's form of the RGRF leaky boundary is a stress jump across a thin boundary layer:

$$F_{net} = \oint \left(P_{in} - P_{out} - \sigma_{EM,in} + \sigma_{EM,out}\right)\cdot dA$$

with dA the outward normal. With B tangential to the heliopause, the normal EM stress reduces to B²/2μ₀, so per unit area this is the familiar p + B²/2μ₀ balance; flow adds ρvv terms. The electric part is negligible ((E/cB)² ~ 10⁻⁹, above).

[`sims/heliopause_pressure_balance.py`](../sims/heliopause_pressure_balance.py) checks it with Voyager numbers. Inside: 267 ± 55 fPa total effective pressure (Rankin et al. 2019, ApJ 883, 101) **Grounded**. Outside: n_e = 0.05-0.08 cm⁻³ (Gurnett et al. 2013, Science 341, 1489) and |B| = 0.486 ± 0.045 nT (Burlaga & Ness 2014, ApJ 784, 146) **Grounded**; T_out 7,500-30,000 K **[to verify]**. Nominal outside p + B²/2μ₀ is about 138 fPa; adding the far-field ISM ram ρv² (about 90 fPa at 26 km/s) gives about 229 fPa, inside the inside error band. The "roughly 10⁻¹³ Pa" figure is confirmed as the right order on both sides. Reading the near-balance as a leaky, near-equilibrium RGRF boundary is **Speculative**.
