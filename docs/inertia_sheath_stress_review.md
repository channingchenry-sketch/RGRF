# Inertia, plasma sheaths and sheath boundary stress: review of Grok share `f9e0da6d` (2026-10-17)

**Source:** [grok_archive/2026-10-17_inertia_in_mechanics_core_concepts.md](grok_archive/2026-10-17_inertia_in_mechanics_core_concepts.md). This is share #74: 12 messages, rebuilt from the PDF capture. No code was shown. Several key equations are garbled in the capture and marked `[MATH garbled]`.

**Rerun / check:** [sims/s70_80_claim_checks.py §3](../sims/s70_80_claim_checks.py), with output in [sims/s70_80_claim_checks_output.txt](../sims/s70_80_claim_checks_output.txt). It computes the exact surface-stress eigenvalues, tests Grok's eigenvalue formula and distinctness condition, and estimates the sheath pressure against the 88 kg load.

**Related:** [lift_and_equilibrium_systems.md §9b](lift_and_equilibrium_systems.md) (Maxwell stress and POL lift; ~14.6 kW for 88 kg), [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md) (ponderomotive "escape vectors") and [butterfly_node.md](butterfly_node.md) (double-ellipse geometry).

**Labels:** Grounded · Plausible-untested · Speculative · Symbolic.

## Channing (verbatim)

| Msg | Prompt |
|---|---|
| 1 | "Hey Resona, can we look at inertia in more detail?" |
| 3 | "We have already discussed a plasma like sheath what does that do to inertia.. can we look at source, sink again as well and aligned angular momentum" |
| 5 | "Lets look at the addition of Maxwell stress of a sheath as an additional boundary contribution and can we look into parallel and perpendicular angular shifting or flux guiding.. also let's go hypothetical and look at space and think about "well" tensors we have kind of touched on this.. where are we hypothetical and what seems to be missing" |
| 7 | "Derive sheath boundary stress equations" |
| 9 | "Can we specialize them to the double ellipse geometry(distinct eigen values appear?" |
| 11 | "This all helps with engineering.. can we save to be continued.." |

## A. Inertia (msg 2)

| Claim | Label | Check |
|---|---|---|
| F = ma, τ = Iα; inertia is resistance to change of motion, not a force | Grounded | |
| Equivalence of inertial and gravitational mass confirmed "to better than 10⁻¹⁵" | Grounded | MICROSCOPE final result: η = [−1.5 ± 2.3 (stat) ± 1.5 (syst)] × 10⁻¹⁵ (P. Touboul et al., *Phys. Rev. Lett.* 129, 121102 (2022)). |
| Mach's principle is open | Grounded (as an open question) | |
| POL must also supply the transient force to accelerate rider + board | Grounded | This adds to the ~10–17 kW steady-lift gap, not instead of it. |

## B. Sheath and inertia; sources and sinks (msg 4)

| Claim | Label | Check |
|---|---|---|
| A sheath (a few to tens of Debye lengths) does **not** change rest or inertial mass; it redistributes momentum exchange | Grounded | Correct and important. Grok states it clearly. |
| The sheath can be a "soft, distributed reaction partner" replacing the conductive floor | Speculative / **contradicts the repo's power finding** | Momentum must still go somewhere: into the ambient gas or plasma, as with ion thrusters and EHD. Sheath pressures are mPa to tens of Pa for lab plasmas (n ≈ 10¹⁶–10¹⁹ m⁻³, Te ≈ 3–10 eV), against ~863 Pa needed to carry 88 kg on 1 m² ([sim §3](../sims/s70_80_claim_checks_output.txt)). That is 1.5–6 orders of magnitude short, before counting the power to sustain the plasma. |
| Continuity and momentum equations with source/sink terms; Tesla valves as "directed sinks of reverse flow" | Grounded (equations) / Plausible-untested (valve description) | |

## C. Maxwell-stress boundary term, flux guiding, "well" tensors (msg 6)

| Claim | Label | Check |
|---|---|---|
| Force on a wall = jump of the normal Maxwell stress plus kinetic momentum flux across a pill-box straddling the sheath | Grounded | A standard derivation. |
| Normal E with mixed normal/tangential B gives both pressure and shear | Grounded | The shear is B_nB_t/μ₀. **Caveat:** if no surface current flows in the wall or sheath, B is continuous across the layer and the **magnetic** terms cancel in the jump. They act on the wall only through a surface current (K = Δ**B**×**n**/μ₀). Grok keeps them without stating that condition. |
| Parallel vs perpendicular transport along B (free streaming vs cross-field drifts; Alfvénic coupling) | Grounded | |
| "Well" tensors in space (stress-energy wells, EM-gravitational wells) | Speculative | Grok labels these hypothetical. |

## D. Sheath boundary stress equations (msg 8)

| Claim | Label | Check |
|---|---|---|
| f_EM = ρ_cE + j×B = ∇·T − ε₀μ₀ ∂S/∂t | Grounded | |
| f_s = n̂·⟦T_EM + Π_kin⟧; the ion ram pressure at the sheath edge (Bohm speed) dominates the kinetic term | Grounded | Bohm criterion: u_i ≥ c_s = √(kTe/m_i) (D. Bohm, 1949). Child–Langmuir sheath scaling (C. D. Child, 1911; I. Langmuir, 1913). |
| f_n = (ε₀/2)(E_n² − E_t²) + (B_n² − B_t²)/2μ₀ + p_i,edge; f_t = ε₀E_nE_t + B_nB_t/μ₀ + Π_nt | Grounded | This is the Maxwell-stress normal and shear for this field decomposition. The legible terms in the capture match. |

## E. Double-ellipse specialisation and eigenvalues (msg 10)

| Claim | Label | Check |
|---|---|---|
| Working form f_n ≈ ε₀E_n²/2 + p_i − B_t²/2μ₀ | **Correction** | Grok drops +B_n²/2μ₀ here, but its full expression one line earlier keeps it. On the open arcs, where Grok says B_n dominates, that is the term it dropped. |
| 2×2 in-plane block of the surface Maxwell stress, eigenvalues λ± = (T_nn + T_tt)/2 ± √(((T_nn − T_tt)/2)² + T_nt²) | Grounded (formula) / **Correction** (Grok's entries) | With no z-components the in-plane block is **traceless**: T_nn + T_tt = 0, so λ± = ±r with r = √((ε₀E_n²/2 + (B_n² − B_t²)/2μ₀)² + (B_nB_t/μ₀)²). As far as the garbled capture can be read, Grok's entries give a nonzero mean (B_n² − B_t²)/4μ₀, so its λ± are shifted. The sim compares both over random fields (§3). |
| "Distinct eigenvalues wherever E_n ≠ 0 or B_nB_t ≠ 0" | **Correction** | λ+ ≠ λ− exactly when r ≠ 0. The eigenvalues are degenerate only if B_nB_t = 0 **and** ε₀E_n² = (B_t² − B_n²)/μ₀, e.g. B_n = 0 with E_n = cB_t. So E_n ≠ 0 does not guarantee distinct eigenvalues. A purely normal B with E_n = 0 *does* give distinct eigenvalues (±B_n²/2μ₀). The sim checks both cases. In practice E_n = cB_t needs ~3 MV/m per 10 mT, so the degenerate case is rare, and "distinct almost everywhere" is the right summary. |
| Eigen-directions rotate along the perimeter with curvature and B_t/B_n | Grounded (qualitative) | This follows once the fields vary with arc length s. |
| "The sheath stress is one of the candidates for replacing the hard conductive-floor reaction" | **Contradicts the repo** | See §B: the stress is orders of magnitude too small at lab plasma densities. |

## Contradictions with the repo

- The sheath cannot replace the floor reaction. Lift for 88 kg still needs ~10–17 kW, against the 520 W claim ([lift_and_equilibrium_systems.md §1a](lift_and_equilibrium_systems.md)).
- Nothing here modifies inertia. Grok says so too.

## Items [to verify]

- The exact garbled entries of Grok's 2×2 matrix (msg 10). The PDF capture is unreadable there, and a screenshot of the original would settle it [Channing to supply].

## Open questions for Channing

1. Which "plasma like sheath" discussion did you mean in msg 3? Its share link is [Channing to supply].
2. Is the double-ellipse node meant to carry its own plasma (a powered sheath) or rely on ambient plasma (ionosphere or space)? This changes n and Te by orders of magnitude.
