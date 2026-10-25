# Review: vanadium revisited — redox flow storage, the VO₂ gate, alloys, superconductors, V-51 and biology

- **Request (Channing, verbatim):** "Can we look at Vanadium again?"
- **Sim:** [sims/vanadium_flow_battery_vo2_sim.py](../sims/vanadium_flow_battery_vo2_sim.py) ([output](../sims/vanadium_flow_battery_vo2_sim_output.txt)). It is a textbook illustration; there is no over-unity.
- **Labels:** **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. License CC0.

## 1. What "again" points to (archive search 2026-10-25)

I ran `rg -i 'vanad|VO2|V2O5|redox flow|VRFB|V3Si|V3Ga'` over docs/, grok_archive, the /workspace share txt files and the text of all 260 browser PDFs.

1. **The main earlier thread:** [helium_octave_table.md §Vanadium: oxidation states & charge separation](helium_octave_table.md#vanadium-oxidation-states--charge-separation). It was added on 2026-10-12 (commit a7b2e91) from Grok & Channing chat **screenshots**, and it is marked "*Shallow dive, to expand.*"
   - It covered the four aqueous oxidation states, the VRFB (Skyllas-Kazacos), VO₂'s transition at ~68 °C (Morin 1959), tunicates, haloperoxidases and V-nitrogenase.
   - It framed the flow battery as "a charge-separation device with a membrane as its selective leaky boundary" (R7), VO₂ as a "thermally switched gate", and a bench two-tank vanadyl-sulfate cell.
   - **Channing's own words on vanadium were not captured;** the screenshots were transcribed as structure only. [Channing to supply the original question, if remembered.]
   - **"Again" most likely means this shallow dive, now expanded.**
2. **Vanadium in the octave table:** 23 V in the "Argon Octave" ([helium_octave_table.md](helium_octave_table.md) l. 27). **Symbolic.**
3. **Carnotite:** K₂(UO₂)₂(VO₄)₂·3H₂O, a potassium uranyl vanadate, came up incidentally in share `055440d2` ([grok_archive/2026-10-17_mhd_force_balance_poynting_flux_uranates.md](grok_archive/2026-10-17_mhd_force_balance_poynting_flux_uranates.md) l. 225). Channing asked (l. 19): "…Then, can we investigate sodium and potassium uranates?" The mineral is a vanadium and uranium ore and is radioactive. The context there is chemistry only.
4. **The R7 charge-separation link:** [living_habitat_life_support.md](living_habitat_life_support.md) l. 181 (NH₄⁺ charge separation, which points to the vanadium note).

There were no hits for VRFB sizing, V₃Si/V₃Ga, alloys, V-51 or VO₂ skins. Those are new in this review.

## 2. Grounded core

| Topic | Content | Label / source |
|---|---|---|
| Oxidation states | V²⁺ (violet), V³⁺ (green), VO²⁺ (V(IV), blue), VO₂⁺ (V(V), yellow). Electron configuration [Ar]3d³4s². | **Grounded** |
| VRFB | Maria Skyllas-Kazacos and co-workers, UNSW, from 1984–86 (Sum & Skyllas-Kazacos, *J. Power Sources* 15, 179 (1985); Skyllas-Kazacos et al., *J. Electrochem. Soc.* 133, 1057 (1986) [to verify]). Negative side V²⁺/V³⁺ (−0.26 V); positive side VO²⁺/VO₂⁺ (+1.00 V); **E° ≈ 1.26 V**, with an OCV of about 1.4 V at 50 % SOC in sulfuric acid. | **Grounded** |
| Energy density | About 15–35 Wh/L of electrolyte (1.6–2 M V; mixed-acid electrolytes reach the upper end). Model value here: **20 Wh/L ≈ 15 Wh/kg**. | **Grounded** |
| Energy decoupled from power | Tank volume sets the energy and stack area sets the power. More than 10,000 cycles; the electrolyte does not wear out. | **Grounded** |
| Crossover | Both sides are the same element, so ion crossover only self-discharges the cell (a coulombic loss). It does not contaminate either side, and remixing and rebalancing recovers it. | **Grounded** |
| Round-trip efficiency | Typically **70–80 %** in DC (pump and power-conversion losses included at the low end) | **Grounded** [to verify for a specific system] |
| Large installations | Dalian Rongke, about 100 MW / 400 MWh (2022) | **Grounded** [to verify] |
| VO₂ | Insulator–metal transition at **~68 °C (341 K)**, F. J. Morin, PRL 3, 34 (1959). Monoclinic M1 (V–V dimerised) changes to rutile R. The mechanism is a mix of Mott correlation and Peierls dimerisation, still debated. Resistance changes by about 10³–10⁵ in films, with a few K of hysteresis. The near-IR becomes opaque and reflective in the metal phase, while visible light changes little. W doping lowers Tc by about 20–25 K per at. %. | **Grounded** |
| VO₂ uses | Thermochromic smart windows; adaptive radiative-cooling or emissivity skins (e.g. tunable emitters for spacecraft thermal control) | **Grounded** in lab prototypes; flight use is [to verify] |
| Steels | 0.05–0.15 % V in HSLA steels forms V(C,N) precipitates that refine grain and strengthen; used in rebar, pipelines and tools | **Grounded** |
| Ti-6Al-4V | The aerospace and biomedical workhorse alloy. V stabilises the β phase; yield strength about 880 MPa. | **Grounded** |
| Superconductors | V metal Tc ≈ **5.4 K**, one of the few elemental type-II superconductors (Nb, V, Tc). A15 compounds: **V₃Si** Tc ≈ 17 K (Hardy & Hulm 1953), **V₃Ga** ≈ 15 K. V₃Ga tapes were used in early high-field magnets. | **Grounded** |
| V-51 | **99.75 %** abundance, spin **I = 7/2**, high receptivity (about 0.38 relative to ¹H), with a broad chemical-shift range. Widely used to study vanadate biochemistry and catalysts. (V-50, 0.25 %, is very long-lived and only weakly radioactive.) | **Grounded** |
| Biology | Tunicate vanadocytes (up to ~350 mM, vanabins; Michibata); V-haloperoxidases (Vilter 1984); V-nitrogenase (Robson et al., *Nature* 322, 388 (1986)) | **Grounded** (as in the earlier note) |

## 3. RGRF links (labelled)

- **VRFB as ground or dock buffer storage, on the leaky-bound-state ledger** ([leaky_bound_state_family.md](leaky_bound_state_family.md)): stored energy is E = P·τ, and the membrane is a selective, slightly leaky boundary. Self-discharge by crossover is the "Γ" leak. **Grounded** as a ledger and **Plausible** as an RGRF dock or greenhouse buffer.
  - **Not a flight battery.** At 15 Wh/kg it is about 10× worse than Li-ion (§5).
- **VO₂ as a thermally gated boundary or skin:** an insulator-to-metal IR gate at 68 °C, i.e. a passive "opens with heat" switch for heat-reuse loops or a cabin skin. It fits the leaky-boundary gate row. **Plausible-untested** for RGRF.
- **V-51 nuclear spin and the NV review** ([nv_center_spin_degrees_of_freedom_review.md](nv_center_spin_degrees_of_freedom_review.md)): ⁵¹V is an I = 7/2 nuclear-spin degree of freedom. NV-NMR (nanoscale NMR with dynamical decoupling) can in principle detect it. **Grounded** in kind; NV detection of ⁵¹V specifically is [to verify].
- **Stator and Halbach** ([stator_review.md](stator_review.md)): Ti-6Al-4V rotor sleeves and retaining hubs are **Grounded** practice (non-magnetic and strong). Vanadium–iron–cobalt alloy (Hiperco 50, about 2 % V, saturation about 2.4 T) is a **Grounded** high-flux stator lamination option for aerospace motors, at higher cost. V in HSLA structural steel is also Grounded.
- **Superconducting coils:** V₃Ga and V₃Si are historically **Grounded** but cryogenic, and largely replaced by Nb₃Sn and HTS. For RGRF coils this is **Speculative** (needs 4 K).
- **Octave, spiral-table and colour symbolism:** vanadium's four colours (violet → green → blue → yellow) span the RGRF colour map. Green V³⁺ sits mid-sequence ("green = balanced centre", [em_geometry_map.md](em_geometry_map.md)). **Symbolic.** The colours come from d-electron ligand-field transitions, not octave position.
- **Charge separation (R7)** ([em_topological_gravity_review.md](em_topological_gravity_review.md)): the flow battery is the cleanest Grounded example of the pump + gate pattern in chemical form.

## 4. Supply, toxicity and sustainability (regenerative framing)

- **Supply (Grounded [to verify current shares]):** mostly a by-product of vanadiferous titanomagnetite and steel slag. China, Russia and South Africa dominate, plus Brazil. Also recovered from petroleum fly ash and spent catalysts.
- **Regenerative angle (Plausible):** VRFB electrolyte is reusable almost indefinitely and can be leased and recycled. Recovering vanadium from slag and fly ash turns waste into storage.
- **Toxicity (Grounded):**
  - **V₂O₅ is toxic.** IARC Group 2B (possibly carcinogenic, 2006 [to verify]). It irritates the respiratory tract, and dusts need a respirator.
  - Vanadyl and vanadate salts are harmful if ingested.
  - VRFB electrolyte is strongly acidic (about 2–4 M H₂SO₄).
  - Gloves, goggles and ventilation are needed; spills need containment.
  - Bench cells should use small volumes and a neutralisation kit.
- **Bioaccumulation (tunicates)** is a reminder to keep vanadium waste out of waterways.

## 5. Sim results (textbook illustration)

`sims/vanadium_flow_battery_vo2_sim.py`:

**(a) VRFB open-circuit voltage.** The Nernst form, with the proton term included (about 4 M H⁺ assumed), gives OCV = 1.26 V + (2RT/F)·ln(SOC/(1−SOC)):

| SOC | OCV |
|---|---|
| 50 % | 1.331 V (1.260 V with protons ignored) |
| 10 % | 1.218 V |
| 90 % | 1.444 V |

**Tank ledger** at 1.6 M V, 15–85 % usable SOC, both tanks counted: **20.3 Wh/L ≈ 15.0 Wh/kg** of electrolyte. Round-trip efficiency is 75–80 % [to verify]. Charge energy in always exceeds energy out, so there is no over-unity.

| Load | Energy out | Electrolyte | Recharge input | Loss | τ |
|---|---|---|---|---|---|
| Bench 520 W, 4 h* | 2.08 kWh | 103 L / 139 kg | 2.60–2.77 kWh | 0.52–0.69 kWh | 4 h |
| Hover 10 kW, 15 min** | 2.50 kWh | 123 L / 167 kg | 3.12–3.33 kWh | 0.63–0.83 kWh | 15 min |
| Hover 17 kW, 15 min** | 4.25 kWh | 210 L / 283 kg | 5.31–5.67 kWh | 1.06–1.42 kWh | 15 min |
| Hover 17 kW, 1 h** | 17.0 kWh | 839 L / 1133 kg | 21.3–22.7 kWh | 4.3–5.7 kWh | 1 h |

\* 520 W is the original POL input claim, which the RGRF lift ledger marked **Contradicted** ([pol_simulation_engine_skills_meitner_review.md](pol_simulation_engine_skills_meitner_review.md)). It is used here only as a bench-load figure.
\** About 10–17 kW is RGRF's first-principles eddy-current hover estimate (the same doc and [macroscopic_atom_topology_frequency_review.md](macroscopic_atom_topology_frequency_review.md)).

**Conclusion (Grounded):** a VRFB can sensibly power a bench or a docking station, but on board a POL-class craft the electrolyte would outweigh the rider. Li-ion (about 150–250 Wh/kg) remains the flight option.

**(b) VO₂ hysteresis (illustrative):** heating transition at 68 °C, cooling at 62 °C; 2.5 µm IR transmittance falls from 60 % to 5 %; resistance drops by about 10⁴.

Plot: `/workspace/vanadium_plot.png`, kept on the box and not committed.

## 6. Gaps, [to verify] and an open question

- The early VRFB papers (Sum & Skyllas-Kazacos 1985; *J. Electrochem. Soc.* 1986); a specific system's round-trip efficiency; the Dalian Rongke figures; VO₂ in flight thermal-control hardware; the IARC 2B classification for V₂O₅; current supply shares; NV-NMR detection of ⁵¹V.
- Channing's original vanadium question from the 2026-10-12 screenshots was not captured [Channing to supply].
- **Open question for Channing:** which vanadium angle did you mean to pick back up?
  - (a) a flow-battery buffer for the dock or bench;
  - (b) a VO₂ heat-gated skin or window for the craft;
  - (c) V in the motor or structure (Ti-6Al-4V, V-Fe-Co laminations);
  - (d) the biology (tunicates, V-nitrogenase);
  - (e) something from the charge-separation (R7) thread?
