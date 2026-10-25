# Leaky boundary states, quantum tunneling, and pressure/density gradients (2026-10-25)

*License CC0. Requests (Channing, 2026-10-25): "Can we look at our leaky boundary state and quantum tunneling?" and "Also, pressure density gradients". Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations were checked by web search on 2026-10-25, or are carried from repo docs where they were already checked; anything else is marked [to verify]. No figures reproduced. Sim: [../sims/leaky_boundary_tunneling_sim.py](../sims/leaky_boundary_tunneling_sim.py) (textbook illustration). Companions: [flux_attachment_review.md](flux_attachment_review.md), [fractional_fermi_sea_review.md](fractional_fermi_sea_review.md).*

## 0. What "our leaky boundary state" meant (archive)

Channing's earlier words (verbatim):

| File : line | Channing |
|---|---|
| [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md) : 55 (share 10bbfe00, msg 9; archive [grok_archive/2026-10-17_it3_framework_investigation.md](grok_archive/2026-10-17_it3_framework_investigation.md) : 502) | "We kind of have a leaky bound state in our solar system with our prior discussion on the heliopause, heliopause shock, etc.. can we re explore" |
| it3_leaky_bound_states_review.md : 53 (msg 7) | "Let’s explore the bound states (almost sound like our cavity) also let’s see how closely it aligns to our cosmological path" |
| [pol_v0_1_zones.md](pol_v0_1_zones.md) : 153 (2026-10-12) | "Material choice the loops typically going around the outside much like on our craft creating a sort of control for the leaky boundary" |
| [fuller_tensegrity_vortex_node_review.md](fuller_tensegrity_vortex_node_review.md) : 27 | "Can we explore quantum tunneling and phase change states?" |
| [electrostatic_nodal_spin_dynamics_review.md](electrostatic_nodal_spin_dynamics_review.md) : 21 | "… we can wrap up here the rigorous calculations of pressure density gradient and angular momentum would currently be hard to track on a cosmic scale.. to be continued, thank you!" |
| [molecular_vibration_schrodinger_dirac_review.md](molecular_vibration_schrodinger_dirac_review.md) : 16 | "They have made progress in the neural network representation, right?(they used living neurons I believe).. pressure gradients?" |
| [fungal_biophysics_crystara_review.md](fungal_biophysics_crystara_review.md) : 9 | "… can we dive into Turgor pressure gradients,Tubular vacuolar systems,Hydrostatic pressure, …" |

The leaky-boundary thread is also covered in the 2026-10-12 re-walk, [em_topological_gravity_review.md](em_topological_gravity_review.md) §R4–R6, lines 831–900: black-hole paths, then angular momentum, then pressure gradients, then leaky boundaries, then heliosheath back pressure. That doc also covers the heliosphere as a leaky boundary ([stellarator_argon_heliosphere_review.md §4](stellarator_argon_heliosphere_review.md)) and the stress-jump balance F_net ([electrostatic_isotropic_stress_review.md](electrostatic_isotropic_stress_review.md) line 176; commit 44423b3, `sims/heliopause_pressure_balance.py`). The gravity doc's Sun section, lines 1114–1117 (hot/cold convection, pressure differentials), is Grok-side summary, not Channing verbatim.

**Candidate meanings:**
- (A) The heliosphere as a "leaky bound state": a confined region whose boundary passes particles and flux (heliopause, termination shock). This is the most direct match.
- (B) The POL/craft "controlled leaky boundary": the perimeter loop, the impedance zone and gated leakage (R6).
- (C) The cavity as an engineered bound state.

Whether "quantum tunneling" is meant as a mechanism for (A) or (B), or as a parallel, is **[Channing to supply]**.

## 1. Tunneling basics

| Claim | Label | Source |
|---|---|---|
| In a barrier with V > E the wave is evanescent, ψ ~ e^(−κx), κ = √(2m(V−E))/ħ. For a thick barrier T ≈ 16(E/V)(1−E/V)e^(−2κd); WKB gives T ~ exp(−2∫κ dx) | **Grounded** | textbook |
| Alpha decay is tunneling through the Coulomb barrier (Geiger–Nuttall law) | **Grounded** | G. Gamow, *Z. Phys.* 51, 204 (1928); R. W. Gurney, E. U. Condon, *Nature* 122, 439 (1928) |
| The scanning tunneling microscope: current ∝ e^(−2κd), about ×10 per Å | **Grounded** | G. Binnig, H. Rohrer, Ch. Gerber, E. Weibel, *PRL* 49, 57 (1982) |
| Josephson tunneling of Cooper pairs | **Grounded** | B. D. Josephson, *Phys. Lett.* 1, 251 (1962) [to verify] |
| Macroscopic quantum tunneling and energy quantisation in a superconducting circuit (1984–85) | **Grounded** | Nobel Prize in Physics 2025: J. Clarke, M. H. Devoret, J. M. Martinis (nobelprize.org press release, 7 Oct 2025) |
| Resonant tunneling through double barriers | **Grounded** | R. Tsu, L. Esaki, *APL* 22, 562 (1973); L. L. Chang, L. Esaki, R. Tsu, *APL* 24, 593 (1974) |

## 2. Leaky boundaries as physics

- **Quasi-bound (Gamow) states.** These have a complex energy E − iΓ/2. Γ is the leak rate, with lifetime τ = ħ/Γ, and they appear as Lorentzian transmission peaks. **Grounded.**
- **Leaky modes.** Leaky waveguide and cavity modes, and Fabry–Pérot resonances with finite Q, have the same mathematics. **Grounded.**
- **Optical tunneling.** Frustrated total internal reflection: an evanescent field crosses a sub-wavelength gap, which is how prism couplers and fibre couplers work. **Grounded** (textbook; e.g. Zhu et al., *Am. J. Phys.* 54, 601 (1986) [to verify]).
- **Evanescent coupling** between resonators sets the splitting and the leak rate. This is the same 2×2 algebra as [zeeman_muon_cavity_review.md](zeeman_muon_cavity_review.md). **Grounded.**

## 3. Tie-in to the flux work: edges are boundary states

| Claim | Label | Source |
|---|---|---|
| Quantum Hall edges are chiral 1D channels. The bulk is gapped, and current flows on the boundary | **Grounded** | Halperin 1982; Wen's chiral Luttinger liquid [to verify refs] |
| A quantum point contact (QPC) pinches two edges together. Quasiparticles tunnel between them, which makes the boundary "leaky" on purpose | **Grounded** | |
| That tunneling gives shot noise S = 2e*I_B(1−t), which measures e* = e/3 | **Grounded** | de-Picciotto et al., *Nature* 389, 162 (1997); Saminadayar et al., *PRL* 79, 2526 (1997) |
| Anyon colliders and interferometers use the same leaky QPCs | **Grounded** | Bartolomei et al., *Science* 368, 173 (2020); Nakamura et al., *Nat. Phys.* (2020) |
| Topological insulators: a gapped bulk with protected boundary states (2D helical edges, 3D Dirac surface). The bulk-boundary correspondence: the bulk invariant counts the boundary modes | **Grounded** | Kane & Mele 2005; Hasan & Kane, *RMP* 82, 3045 (2010) [to verify] |
| Topological boundary states resist backscattering, but they still leak when they couple across a narrow sample or to magnetic impurities | **Grounded** | |

## 4. Plasma and space: classical leakage, not tunneling

- **Magnetopause.** Pressure balance: ρ_sw v² ≈ B_mp²/2μ₀. Leakage happens through Dungey reconnection (*PRL* 6, 47, 1961), flux-transfer events and Kelvin–Helmholtz roll-up on the flanks, all gated by the IMF direction. **Grounded** (refs as in em_topological_gravity_review §R4/R6).
- **Heliopause.** Voyager 1 crossed in 2012 at ~122 au: solar-origin particles fell, galactic cosmic rays rose, and |B| changed with no change in direction (Krimigis et al. and Burlaga et al., *Science* 341, 2013, as cited in §R4). The boundary is porous: ACR leakage, GCR entry, and neutral atoms crossing by charge exchange. **Grounded.** Our earlier balance check gives 267 ± 55 fPa inside versus ~229 fPa outside (commit 44423b3). **Grounded.**
- **Why it is not tunneling.** The particles there have gyroradii of ~10³–10⁵ km and de Broglie wavelengths around 10⁻¹² m. Crossing happens by drifts, diffusion along stochastic field lines, reconnection and charge exchange, all classical. Calling the heliosphere a "leaky bound state" is **Symbolic** (a good metaphor, and Grok's framing in share 10bbfe00).

## 5. Pressure and density gradients

| Topic | Label | Note |
|---|---|---|
| Boundary pressure balance: p_th + B²/2μ₀ + ρv²(normal) is continuous across a tangential discontinuity | **Grounded** | Heliopause check above; magnetopause standoff ~10 R_E |
| Fick's law J = −D∇n; classical cross-field diffusion D⊥ ~ η⊥ n k T/B², and Bohm diffusion D_B = kT/16eB | **Grounded** | Bohm diffusion is empirical |
| Diamagnetic drift v* = −∇p × B/(q n B²): a pressure gradient in a field drives current along the boundary (the magnetopause Chapman–Ferraro current) | **Grounded** | |
| Curvature and ∇B drifts: charge-dependent, so they separate species. This gives the ring current, and is part of how energetic particles leak at boundaries | **Grounded** | |
| Rayleigh–Taylor: heavy over light, or plasma held up by field curvature (the interchange instability), σ = √(A g k) | **Grounded** | Heliopause RT/KH studies in MHD models are a pending section ([stellarator_argon_heliosphere_review.md §5](stellarator_argon_heliosphere_review.md)); specific papers [to verify] |
| Kelvin–Helmholtz at the magnetopause flanks mixes solar-wind plasma inward (a "leak" by vortex roll-up) | **Grounded** | e.g. Hasegawa et al., *Nature* 430, 755 (2004) [to verify] |
| Baroclinic vorticity: Dω/Dt ⊃ (∇ρ × ∇p)/ρ². Misaligned density and pressure gradients spin up vortices (sea breezes, shock–bubble interaction, Richtmyer–Meshkov) | **Grounded** | This is the honest source term for Channing's vortex and helium-loop threads (see the "vorticity needs shear or baroclinic torque" note in [electrostatic_nodal_spin_dynamics_review.md](electrostatic_nodal_spin_dynamics_review.md) line 49). Applying it to a heated helium loop is **Plausible-untested**; the energy comes from the stratification/heater, not from the vortex. |
| A gradient shapes a tunneling barrier: a field F tilts V(x) = φ − eFx into a triangle, and WKB gives Fowler–Nordheim emission, T ~ exp(−4√(2m)φ^(3/2)/(3ħeF)) | **Grounded** | R. H. Fowler, L. Nordheim, *Proc. R. Soc. A* 119, 173 (1928) |
| A density gradient at a QH edge splits the edge into alternating compressible and incompressible strips, which sets where the edge channels sit and how they equilibrate | **Grounded** | D. B. Chklovskii, B. I. Shklovskii, L. I. Glazman, "Electrostatics of edge channels", *PRB* 46, 4026 (1992) |
| One "pressure–density gradient" law across solar, plasma, fungal and quantum scales | **Symbolic** | The same calculus (gradients drive fluxes), but different physics at each scale |

## 6. Sim (textbook illustration)

`sims/leaky_boundary_tunneling_sim.py`, GaAs effective mass 0.067 mₑ. Exact transfer matrix:
- **Single 0.3 eV barrier.** At E = 0.1 eV and d = 5 nm, T = 9.4×10⁻³, versus a bare e^(−2κd) = 2.7×10⁻³; the gap is the prefactor. Ledger: |R + T − 1| ≤ 2×10⁻¹⁵.
- **Double barrier 4/10/4 nm.** Quasi-bound resonance at 34.1 meV with T_peak ≈ 1, Γ = 0.146 meV, so τ = ħ/Γ ≈ 4.5 ps (the leak rate). Ledger: ≤ 2×10⁻¹³. A resonant peak redistributes transmission; it does not create any.
- **QPC toy.** S = 2e*I_B(1−t) for e/3 versus e.
- **Fowler–Nordheim (gradient panel).** φ = 4.5 eV, T(5 GV/m) = 2.2×10⁻⁶; the analytic and numeric WKB agree to 4×10⁻⁵.
- **Rayleigh–Taylor.** σ for A = 0.5, λ = 0.1 m is 17.6 s⁻¹.
- **Baroclinic torque** g ∂ρ/∂x / ρ.

Plot: `/workspace/leaky_boundary_tunneling_plot.png` (box only).

## 7. RGRF links (honest)

| Link | Label |
|---|---|
| A designed "controlled leaky boundary" (POL perimeter loop, impedance zone, gated leakage R6) as a design principle: gate exchange by species, energy, timing | **Plausible-untested** as engineering; tying it to tunneling is **Symbolic** |
| The POL impedance zone acting as a tunneling barrier | **Speculative**: no quantum-coherent carriers at those scales |
| The heliosphere as a leaky bound state (Gamow-state analogy, with a leak rate set by reconnection and diffusion) | **Symbolic** |
| QH/TI edge states as the cleanest real "leaky boundary states" | **Grounded** physics; mapping them onto RGRF is **Symbolic** |
| Free energy from tunneling or boundary leakage | **Not supported.** Tunneling conserves energy (R + T = 1); gradients release only the energy already stored in them. |

## 8. Gaps
- Which meaning, (A), (B) or (C), is intended, and whether tunneling is a mechanism or a parallel [Channing to supply].
- [to verify]: Josephson 1962; Zhu et al. 1986 FTIR; Halperin 1982, Wen edge refs; Kane–Mele 2005, Hasan–Kane 2010; Hasegawa 2004; heliopause RT/KH papers.
