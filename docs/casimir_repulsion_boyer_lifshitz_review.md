# Review: Casimir repulsion — Lifshitz fluid route, Boyer configuration, topological and birefringent cases (share #107)

- **Archive:** [grok_archive/2026-10-22_casimir_repulsion_discussion.md](grok_archive/2026-10-22_casimir_repulsion_discussion.md) (share `c708d7f9`, 16 messages: 8 Channing, 8 Grok).
- **Related:** [shifting_phase_order_review.md §E](shifting_phase_order_review.md#e-boyer-repulsive-casimir-as-a-parallel-to-shifting-phase-order-2026-10-15) (Boyer π-shift parallel; Grok's msg 6 here is the source of the 2026-10-15 paste archived there, essentially verbatim), the **L4f Casimir checkpoint** row in [REBUILD_INDEX.md](REBUILD_INDEX.md) (plates, Casimir–Polder, zeta; 9×7 matrix still Missing), [shifting_phase_order_review.md §F](shifting_phase_order_review.md#f-floquet-periodically-driven-topological-phases-2026-10-15) (Floquet topology), [supercooled_electrons_rotation_review.md](supercooled_electrons_rotation_review.md) (#98: rotating-wall columns, vortex beams, rotation-induced fields — msg 12 here repeats that material), [tesla_davinci_threads.md §3b](tesla_davinci_threads.md#3b-electricmagnetic-as-a-complementary-pair) (E↔B duality).
- **Labels:** Grounded; Plausible-untested; Speculative; Symbolic. "Grok-reported" = not rerun here.

## 1. Casimir basics (msg 2)
| Claim | Label | Note |
|---|---|---|
| P = −π²ħc/(240 d⁴) | **Grounded** (computed) | 1.3×10⁵ Pa at 10 nm, 13 Pa at 100 nm, 1.3 mPa at 1 µm. |
| Significant only ~1–100 nm | **Grounded** | Measurable to a few µm with care (Lamoreaux 1997). |
| MEMS stiction is the main practical relevance | **Grounded** | Chan et al., Science 291, 1941 (2001). |

## 2. Lifshitz repulsion (msgs 2, 4)
| Claim | Label | Note |
|---|---|---|
| Repulsion when the medium's ε(iξ) lies between the two bodies': ε1 > ε3 > ε2 (or reverse) | **Grounded** | Dzyaloshinskii, Lifshitz & Pitaevskii, Adv. Phys. 10, 165 (1961). Munday et al. write ε1 > ε3 > ε2 with 3 = the fluid; the parent's form ε1 < ε3 < ε2 is the same condition with bodies relabelled. What matters is only that the medium is intermediate over the dominant imaginary frequencies. |
| Munday, Capasso & Parsegian 2009: Au sphere / silica plate in bromobenzene, repulsive | **Grounded** | Nature 457, 170 (2009). Au > bromobenzene > silica ordering correct. "Tens of pN up to ~40 nm" is **Grok-reported**; the paper reports repulsion measured from ~20 nm out to ~100 nm with sub-100 pN forces [to verify exact range]. |
| Earlier He films on fluorides | **Grounded** | Sabisky & Anderson, PRA 7, 790 (1973). |
| Quantum levitation of Au nanoplates over Teflon in ethanol | **Grounded** | Zhao et al., Science 364, 984 (2019). |
| Salt/ionic screening can turn repulsion to attraction at larger gaps | **Plausible** | Zero-frequency term screening; [to verify specific paper]. |
| The fluid "is pulled in" | **Grounded** (heuristic) | |

## 3. Boyer configuration (msgs 2, 4, 6)
| Claim | Label | Note |
|---|---|---|
| Perfect conductor vs perfectly permeable plate repel; U = +(7/8)π²ħc/(720a³), P = (7/8)π²ħc/(240a⁴) | **Grounded** (checked) | Boyer, PRA 9, 2078 (1974). Pressure = −dU/da consistent. |
| 7/8 from e^{x}−1 → e^{x}+1 in the mode integral | **Grounded** (computed) | ∫x³/(eˣ+1) / ∫x³/(eˣ−1) = 0.8750. |
| Round-trip π shift (r_ε r̄_μ = −1); Fermi–Dirac-like vs Bose–Einstein-like | **Grounded** | Shajesh, Brevik, Cavero-Peláez & Parashar, PRD 95, 085011 (2017); Brevik, Parashar & Shajesh, PRA 98, 032509 (2018). |
| No unambiguous vacuum Boyer-type repulsion measured; thin magnetic layers, μ(0) ≳ ε(0) | **Grounded** / Grok-reported thresholds | Kenneth et al., PRL 89, 033001 (2002); Iannuzzi & Capasso, PRL 91, 029101 (2003); Rosa, Dalvit & Milonni, PRL 100, 183602 (2008). |
| Ideal Boyer case "unstable or requires special geometry" (table) | **Clarified** | For parallel plates the repulsive force is along the gap; lateral instability applies to finite bodies. |
| Boyer π-shift ↔ shifting phase order | **Symbolic** (conceptual parallel, as Channing marked in msg 7) | Consistent with §E. |

## 4. Vacuum geometry, nonequilibrium, chiral (msg 2)
| Claim | Label | Note |
|---|---|---|
| Elongated particle over a plate with a hole repels in vacuum; unstable | **Grounded** | Levin et al., PRL 105, 090403 (2010). |
| Chiral intermediate medium (Wilczek) → oscillatory/tunable force | **Grounded** (theory) | Jiang & Wilczek, PRB 99, 125403 (2019). |
| 2024–2026 quantum-geometry bounds, twisted MoTe₂ | **Grok-reported** [to verify] | |

## 5. Topological transitions (msg 10)
| Claim | Label | Note |
|---|---|---|
| Chern number C = (1/2π)∫F d²k; σxy = Ce²/h; gap closes at transition; bulk–boundary | **Grounded** | |
| Chern-insulator Casimir force ∝ C1·C2, sign switches, quantized | **Grounded** (theory) | Rodriguez-Lopez & Grushin, PRL 112, 056804 (2014); TI axion repulsion: Grushin & Cortijo, PRL 106, 020403 (2011). |
| 2026 Nature critical-topology imaging; α-Bi₄Br₄ room-T edges | **Grok-reported** [to verify] | |

## 6. Rotating charged systems (msg 12)
Same content as the #98 review: rotating-wall columns, vortex/Landau beams (0, Larmor, cyclotron rates; Schattschneider et al., Nat. Commun. 5, 4586 (2014)) **Grounded**; London moment **Grounded**. The metal field "E ≈ −K(M/e)ω²r" is **Grok-reported** — the basic Stewart–Tolman-type result is E = (mₑ/e)ω²r for conduction electrons [to verify the ion-mass K form]. The link to Boyer/Chern is **Symbolic**.

## 7. Birefringence and Casimir torque (msgs 14, 16)
| Claim | Label | Note |
|---|---|---|
| Casimir–Lifshitz torque between birefringent media, sin 2θ | **Grounded** | Barash, Izv. Vyssh. Uchebn. Zaved. Radiofiz. 21, 1637 (1978); Somers, Garrett, Palm & Munday, Nature 564, 386 (2018): crystals vs 5CB nematic through Al₂O₃ spacer. |
| Orientation-dependent repulsion between identical birefringent slabs | **Plausible** (theory) [to verify citation] | |
| Torque magnitude "nN·m/m² at 10–20 nm" | **Grok-reported** | Same order as the paper's ~nN·m/m² [to verify]. |
| Prior "birefringence" thread not found | **Open** | Channing recalls a torque-related screenshot [Channing to supply]. |

## Key findings
1. Lifshitz repulsion condition and Boyer 7/8 result both check out (7/8 computed).
2. Grok's msg 6 is the source of the §E paste — now archived in context.
3. No vacuum Boyer repulsion has been measured; all demonstrated repulsion needs a fluid.

## Open questions for Channing
- The torque screenshot you remember: is it the Somers et al. 2018 schematic?
- Should the L4f 9×7 matrix be rebuilt from this thread?
