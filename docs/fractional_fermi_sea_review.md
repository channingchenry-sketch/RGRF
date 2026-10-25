# Fractional Fermi seas: composite-fermion Fermi sea, zero-field composite Fermi liquids, FL* and the 2026 Innsbruck "fractional Fermi seas" (2026-10-25)

*License CC0. Request (Channing, 2026-10-25): "Can we look at the fractional fermi sea?" Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations were checked by web search on 2026-10-25 unless marked [to verify]. No figures are reproduced from any paper. Sim: [../sims/composite_fermion_geometric_resonance_sim.py](../sims/composite_fermion_geometric_resonance_sim.py) (textbook illustration).*

**Earlier archive thread:** Channing asked "Can we explore fractional fermi sea?" on 2026-10-17 (share fe20a050). See [fractional_fermi_sea_mandela_mycelium_review.md §A](fractional_fermi_sea_mandela_mycelium_review.md) and [grok_archive/2026-10-17_fractional_fermi_sea.md](grok_archive/2026-10-17_fractional_fermi_sea.md). That thread covered the Innsbruck cold-atom result (§2c below). This review adds the quantum-Hall meaning of the phrase and keeps the different meanings apart.

## 0. Four things that share the name (do not mix them up)

| Meaning | System | What is "fractional" | Label |
|---|---|---|---|
| (a) Composite-fermion Fermi sea (composite Fermi liquid, CFL) | 2D electrons at Landau-level filling ν = 1/2, high B | The particles: electrons bound to 2 flux quanta. The Fermi sea is made of emergent particles, not electrons | **Grounded** |
| (b) Zero-field / anomalous CFL | Twisted MoTe2 and rhombohedral pentalayer graphene at moiré filling 1/2, B = 0 | Same idea, but a Chern band replaces the Landau level | **Grounded** (signatures); full identification still being tested: **Plausible-untested** |
| (c) "Fractional Fermi seas" (literal phrase, 2026) | Excited 1D Cs Bose gas (Innsbruck) | The occupation: uniform plateaus of 1/2 and 1/4 in momentum space (Haldane exclusion-type, α = 2, 4) | **Grounded** (preprint) |
| (d) Fractionalized Fermi liquid, FL* | Kondo lattices / doped Mott systems (theory) | The Fermi surface volume violates Luttinger's count because of a coexisting spin liquid | **Grounded** as theory; material cases debated |

## 1. Composite-fermion Fermi sea at ν = 1/2

| Claim | Label | Source |
|---|---|---|
| Electrons plus an even number of flux quanta form composite fermions (CFs); the FQH states ν = p/(2p±1) are integer QH states of CFs | **Grounded** | J. K. Jain, *Phys. Rev. Lett.* 63, 199 (1989) |
| At ν = 1/2 the attached flux cancels the external field on average, B_eff = B − 2φ0 n = 0, so CFs form a Fermi sea with k_F = √(4πn) (spin-polarized); Chern–Simons theory | **Grounded** | B. I. Halperin, P. A. Lee, N. Read, *Phys. Rev. B* 47, 7312 (1993) |
| Surface acoustic waves showed a Fermi surface at ν = 1/2 | **Grounded** | R. L. Willett et al., "Experimental demonstration of a Fermi surface at one-half filling of the lowest Landau level", *PRL* 71, 3846 (1993) |
| Antidot/commensurability experiments: CF cyclotron orbits match an imposed lattice | **Grounded** | W. Kang, H. L. Stormer et al., *PRL* 71, 3850 (1993) [to verify]; Smet et al. 1990s [to verify] |
| Modern "geometric resonance" data (Princeton, Shayegan group) map the CF Fermi wave vector; minima are asymmetric about ν = 1/2, consistent with k_F set by the minority carriers | **Grounded** | D. Kamburov, Y. Liu, M. A. Mueed, M. Shayegan et al., "What Determines the Fermi Wave Vector of Composite Fermions?", *PRL* 113, 196801 (2014); hole-flux CF commensurability, *PRL* 109, 236401 (2012) |
| Particle-hole (PH) symmetry problem: HLR is not manifestly PH-symmetric. Son proposed the CF is a massless Dirac fermion with Berry phase π | **Grounded** (proposal widely accepted as consistent; HLR and Dirac pictures argued to agree at long wavelengths) | D. T. Son, "Is the Composite Fermion a Dirac Particle?", *Phys. Rev. X* 5, 031027 (2015); follow-ups by Wang & Senthil, Metlitski & Vishwanath, and others [to verify exact refs] |

## 2. Recent versions

**2a/2b. Zero-field CFLs (2023–2026).**

| Claim | Label | Source |
|---|---|---|
| FQAH signatures in twisted MoTe2 at ν = −2/3, −3/5 (optical, Streda) | **Grounded** | J. Cai et al. (X. Xu group), *Nature* 622, 63 (2023) |
| Thermodynamic evidence for integer and fractional Chern insulators in tMoTe2 | **Grounded** | Y. Zeng et al. (Mak/Shan group), *Nature* (2023), doi:10.1038/s41586-023-06452-3 |
| Transport: quantized fractional anomalous Hall plateaus; near ν = −1/2, R_xy varies linearly like a CFL | **Grounded** | H. Park et al. (X. Xu group), "Observation of fractionally quantized anomalous Hall effect", *Nature* (2023), doi:10.1038/s41586-023-06536-0 |
| Theory: a CFL at zero field covers much of the tMoTe2 phase diagram near 3.6° | **Grounded** (numerics) | J. Dong, J. Wang, P. Ledwith, A. Vishwanath, D. Parker, *PRL* 131, 136502 (2023) |
| Optical (trion) signatures of a zero-field CFL near ν = −1/2 | **Grounded** | "Trion sensing of a zero-field composite Fermi liquid", *Nature* (2024), doi:10.1038/s41586-024-08134-0 (X. Xu group) [author list to verify] |
| Rhombohedral pentalayer graphene/hBN: FQAH at 2/3 … 2/5, R_xy = 2h/e² at ν = 1/2 like a CFL | **Grounded** | Z. Lu, …, L. Fu, L. Ju, *Nature* 626, 759 (2024) |
| Extended QAH state below 40 mK; displacement-field transitions to "the likely composite Fermi liquid" | **Grounded** (the authors' own hedge) | Z. Lu et al., *Nature* (Jan 2025), doi:10.1038/s41586-024-08470-1 |
| A direct zero-field geometric-resonance measurement of the CF Fermi surface in these moiré systems | **[to verify]**: not found in this search; it would be the natural next test | — |

**2c. The literal phrase "fractional Fermi seas" (2026).** Y. Zeng, A. Bastianello, …, H.-C. Nägerl, M. Landini, "Realization of fractional Fermi seas", arXiv:2602.17657 (Feb 2026; a preprint as of this check). They prepare excited 1D Cs Bose gases by interaction-ramp cycles, find momentum occupations with plateaus for α = 2 and 4, and see Friedel oscillations in first-order correlations. They call the statistics "superfermionic". The companion theory paper is *PRL* 136, 230402 (9 June 2026), doi:10.1103/j3s5-gjpf. **Grounded.** This is not a quantum-Hall effect. Same name, different physics.

**2d. FL\*.** T. Senthil, S. Sachdev, M. Vojta, "Fractionalized Fermi liquids", *PRL* 90, 216403 (2003). A Fermi liquid whose Fermi-surface volume breaks the usual Luttinger count, together with a deconfined spin-liquid gauge sector. **Grounded** as theory. It is proposed for heavy fermions and the cuprate pseudogap; material evidence is **Plausible-untested**/debated. It is unrelated to flux attachment.

## 3. Plain-language picture

1. In a strong field, electrons in a flat 2D sheet fill Landau levels. ν counts electrons per flux quantum. At ν = 1/2 there are two flux quanta per electron.
2. Interactions make each electron "grab" two flux quanta (vortices of the many-body wavefunction). The bound object is a composite fermion.
3. Those two quanta cancel the applied field on average. The composite fermions behave as if they are in zero field (B_eff = 0), so they fill a Fermi sea like ordinary electrons in a metal, but made of emergent particles.
4. Move slightly away from ν = 1/2 and they feel a small B_eff. They then circle in orbits that can be large; when an orbit fits a patterned lattice, resistance dips ("geometric resonance").
5. In twisted MoTe2 and pentalayer graphene the band's own Berry curvature plays the role of the field, so something similar seems to happen at zero applied field. **Grounded** (1–4); **Plausible-untested** (5, details).

## 4. Sim (textbook illustration)

`sims/composite_fermion_geometric_resonance_sim.py`, GaAs n = 1.5×10¹¹ cm⁻², modulation period a = 200 nm. B(ν = 1/2) = 12.41 T, k_F* = 1.37×10⁸ m⁻¹. Predicted minima at |B_eff| = 2ħk_F*/(e a (i + 1/4)): 0.723, 0.402 and 0.278 T for i = 1, 2, 3. The real data's asymmetry (Kamburov 2014) is not modelled. **Grounded** formula; the parameters are illustrative. The plot is saved on the box as `/workspace/fractional_fermi_sea_plot.png` and is not committed.

## 5. Connections to RGRF threads (honest labels)

| Link | Label | Note |
|---|---|---|
| "Geometric resonance" is the literal name for CF commensurability experiments (Kamburov 2014 uses "geometrical resonance") | **Grounded** (terminology); the link to the RGRF name is **Symbolic** | Here the term means a cyclotron orbit matching a fabricated lattice period. It is a measurement tool, not an energy source. A clean, testable sense of "geometric resonance" that RGRF can cite. |
| Flux attachment vs Channing's vortex and flux-tube threads ([marklund_convection_review.md](marklund_convection_review.md), [oloid_spine_lorentz_drive.md](oloid_spine_lorentz_drive.md), Halbach docs) | **Symbolic** | CF "vortices" are zeros of a quantum wavefunction carrying h/e flux in a 2D sheet at mK and tesla. Plasma flux tubes and Halbach fields are classical. There is shared vocabulary only, no mechanism. |
| Topology: Chern numbers, Berry phase π (Son), anyons | **Grounded** in physics; mapping to oloid/jitterbug geometry is **Speculative** | The topology is band/wavefunction topology, not the shape of a device. |
| Use for energy, propulsion or levitation | **Not supported** | These states need ~10 mK–1 K, clean 2D crystals and (for GaAs) ~10 T. They do no net work and give no lift. |
| Cold-atom FFS (§2c) and quantum sensing | **Plausible-untested** | This is the authors' own outlook, not an RGRF result. |

## 6. Gaps

- Kang/Stormer 1993 and Smet references; trion-sensing author list; the Wang–Senthil and Metlitski–Vishwanath references [to verify].
- The diagrams and "project memory" file from the 2026-10-17 thread [Channing to supply] (already H315).
- Meaning for RGRF use: Channing chose (a), the composite-fermion Fermi sea (2026-10-25). Deeper flux-attachment section: [flux_attachment_review.md](flux_attachment_review.md).

*Credit: Jain; Halperin, Lee and Read; Willett; Stormer; Shayegan and the Princeton group; Son; Senthil, Sachdev and Vojta; the Xu, Mak/Shan, Ju/Fu, Vishwanath and Nägerl groups. Open and regenerative: everything here is CC0.*
