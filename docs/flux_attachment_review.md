# Flux-quanta binding (flux attachment): how composite fermions are built (2026-10-25)

*License CC0. Request (Channing, 2026-10-25): "Let’s look at the flux quanta binding". Companion to [fractional_fermi_sea_review.md](fractional_fermi_sea_review.md); Channing chose the composite-fermion meaning (a) there. Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations checked by web search on 2026-10-25 unless marked [to verify]. No figures reproduced. Sim: [../sims/flux_attachment_jain_sequence_sim.py](../sims/flux_attachment_jain_sequence_sim.py) (textbook illustration).*

## 1. The flux quantum: h/e, not h/2e

| Claim | Label | Note |
|---|---|---|
| φ0 = h/e ≈ 4.136×10⁻¹⁵ Wb. An electron going around this much flux picks up an Aharonov–Bohm phase of exactly 2π, so the flux is "invisible" to it | **Grounded** | Charge e carrier, AB phase = 2π·Φ/(h/e) |
| In superconductors the flux quantum is h/2e ≈ 2.068×10⁻¹⁵ Wb because the carriers are Cooper pairs of charge 2e | **Grounded** | Seen in 1961 flux-quantisation experiments (Deaver–Fairbank; Doll–Näbauer) [to verify refs] |
| Composite fermions use h/e because the bound objects are single electrons. ν counts electrons per h/e flux quantum, so ν = 1/2 means two h/e quanta per electron | **Grounded** | |

## 2. Vortex attachment in the Laughlin wavefunction

| Claim | Label | Source |
|---|---|---|
| Ψ_1/m = Π_{i<j}(z_i − z_j)^m exp(−Σ\|z_i\|²/4ℓ²), with m odd | **Grounded** | R. B. Laughlin, *PRL* 50, 1395 (1983) |
| Each factor (z_i − z_j) is a zero with 2π phase winding as electron i circles j, i.e. a vortex. Writing Ψ_1/3 = Π(z_i−z_j)² × Π(z_i−z_j) reads as "two vortices bound to each electron" × filled ν=1 (Slater) | **Grounded** (standard reading, Jain) | |
| The high-order zero keeps electrons apart (vanishing as r^m), which is how the state lowers the Coulomb energy: correlation "built into" the wavefunction | **Grounded** | |

## 3. Chern–Simons flux attachment and mean field

| Claim | Label | Source |
|---|---|---|
| A singular gauge transformation attaches 2p flux quanta to each electron through a Chern–Simons gauge field; this is exact before approximation | **Grounded** | A. Lopez, E. Fradkin, "Fractional quantum Hall effect and Chern–Simons gauge theories", *PRB* 44, 5246 (1991); B. I. Halperin, P. A. Lee, N. Read, "Theory of the half-filled Landau level", *PRB* 47, 7312 (1993) |
| Mean field: B_eff = B − 2p·φ0·n, i.e. B_eff/B = 1 − 2pν | **Grounded** (as mean field; fluctuations give the CF mass and the non-Fermi-liquid corrections) | HLR 1993 |
| Jain's construction: FQH of electrons = integer QH of composite fermions | **Grounded** | J. K. Jain, "Composite-fermion approach for the fractional quantum Hall effect", *PRL* 63, 199 (1989); also *PRB* 40, 8079 (1989) |

## 4. The Jain sequences

- With 2 flux quanta and p filled CF Landau levels: ν = p/(2p ± 1) → 1/3, 2/5, 3/7 … (B_eff parallel) and 2/3, 3/5, 4/7 … (antiparallel). They pile up symmetrically toward ν = 1/2 as p → ∞, where B_eff = 0 and the CF Fermi sea forms. **Grounded.**
- With 4 flux quanta: ν = p/(4p ± 1) → 1/5, 2/9, … and 2/7, 3/11 …, converging on a 4-flux CF Fermi sea at ν = 1/4. **Grounded** (seen in transport; e.g. Pan et al. [to verify ref]).
- The sim prints 1/3, 2/5, 2/3, 3/7, 3/5 for |p| ≤ 3 and plots both families with B_eff/B and p: `/workspace/flux_attachment_plot.png` (box only, not committed).

## 5. Fractional charge and anyonic statistics

| Claim | Label | Source |
|---|---|---|
| Quasiparticles at ν = 1/3 carry e/3 (shot noise at a QPC) | **Grounded** | R. de-Picciotto, M. Reznikov, M. Heiblum et al., "Direct observation of a fractional charge", *Nature* 389, 162 (1997); L. Saminadayar, D. C. Glattli, Y. Jin, B. Etienne, *PRL* 79, 2526 (1997) |
| Exchange phase π/3 from an anyon collider | **Grounded** | H. Bartolomei, …, G. Fève, "Fractional statistics in anyon collisions", *Science* 368, 173 (2020) |
| Braiding phase in a Fabry–Pérot interferometer | **Grounded** | J. Nakamura, S. Liang, G. C. Gardner, M. J. Manfra, "Direct observation of anyonic braiding statistics", *Nature Physics* 16, 931 (2020) [volume/page to verify] |
| Flux-attachment picture: a quasihole is a missing fraction of an electron bound to one extra vortex; charge e/m follows | **Grounded** (Laughlin 1983) | |

## 6. Zero-field flux attachment in moiré materials

In twisted MoTe2 and rhombohedral pentalayer graphene, a nearly flat Chern band with fairly uniform Berry curvature acts like a Landau level. Its Berry flux, 2π per moiré cell (Chern number 1), plays the role of the applied field. Flux attachment then works "on top of" band topology, which gives FQAH states and a likely CFL at half filling (see [fractional_fermi_sea_review.md §2](fractional_fermi_sea_review.md)). **Grounded** as observation; that the analogy holds in detail ("ideal quantum geometry") is **Plausible-untested** (Dong et al., *PRL* 131, 136502, 2023). No real magnetic flux tubes are present.

## 7. RGRF links (honest)

| Link | Label | Note |
|---|---|---|
| "Flux-tube binding" here vs plasma flux tubes ([marklund_convection_review.md](marklund_convection_review.md)), Io–Jupiter tubes (L2 in REBUILD_INDEX), Halbach/oloid fields | **Symbolic** | CF flux is a quantum phase-winding (statistical gauge flux) in a 2D sheet; it carries no field energy you could tap. Plasma flux tubes are classical MHD. |
| Vortex-bound particles vs Channing's vortex chamber / vortex threads | **Symbolic** | Shared word "vortex"; a wavefunction zero is not a fluid vortex. |
| A Chern-band analogue built from classical magnets or metamaterials (topological photonic/acoustic bands) | **Speculative** for RGRF use | Topological bands exist in classical metamaterials, but flux attachment needs strongly interacting quantum particles. |
| Energy, propulsion or levitation from flux attachment | **Not supported** | |

## 8. Gaps
- Deaver–Fairbank and Doll–Näbauer 1961 refs; 4-flux CF sequence reference (Pan et al.); Nakamura 2020 volume/page [to verify].
