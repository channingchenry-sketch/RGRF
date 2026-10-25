# BCAAs (leucine, isoleucine, valine) and electrolytes: a general science review (2026-10-25)

> **General information, not medical advice.** This is a literature summary. It contains nothing about any individual's health or supplement use. Talk to a clinician before changing diet, supplements or fluids, especially with kidney, liver, heart or metabolic conditions.

*License CC0. Requests (Channing, 2026-10-25): "a slight turn can we look at BCAA?" and "We talked about electrolytes at the same time if that's helpful". Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations were checked by web search on 2026-10-25; anything else is [to verify]. Sim: [../sims/bcaa_leucine_mps_sim.py](../sims/bcaa_leucine_mps_sim.py) (toy illustration).*

## 0. Archive
- **Nervous-system share `4bbcf241`** (local capture, line 1521). Channing: "Can we explore the nervous system, and re visit branch chain amino acids, peptides? Also, protein chains and what they …" (capture truncated). Grok's answer (lines 1560–1600) covered BCAAs as neurotransmitter precursors, leucine–mTORC1, and "BCAAs alone often underperform vs. complete proteins/EAA blends". Related repo docs: [wick_phi4_vortex_adaptogens_review.md](wick_phi4_vortex_adaptogens_review.md).
- **The original BCAA conversation** (the one that also touched electrolytes) is in share `641f0996`. Those turns were withheld from the repo earlier and live only in `/workspace/private`. They are not quoted or summarised here.
- "BCAA" appears nowhere in the archive with any other meaning.

## 1. BCAAs

| Claim | Label | Source / note |
|---|---|---|
| Leucine, isoleucine and valine have branched aliphatic side chains. All three are essential (diet-derived). Proteins use the L-enantiomers | **Grounded** | textbook |
| Unlike most amino acids, BCAAs are first catabolised mainly in skeletal muscle (BCAT, transamination to branched-chain keto acids), then by BCKDH (oxidative decarboxylation). The liver has low BCAT activity | **Grounded** | e.g. Neinast, Murashige & Arany, *Annu. Rev. Physiol.* 81, 139 (2019) [to verify] |
| Leucine signals to mTORC1 through Sestrin2. Leucine binding releases Sestrin2 from GATOR2 (K_d ~20 µM, matching the half-max for mTORC1) | **Grounded** | R. L. Wolfson, …, D. M. Sabatini, *Science* 351, 43 (2016); structure: Saxton et al., *Science* 351, 53 (2016) |
| BCAAs alone produce a limited anabolic response: the other EAAs must come from protein breakdown | **Grounded** (argument) | R. R. Wolfe, "Branched-chain amino acids and muscle protein synthesis in humans: myth or reality?", *JISSN* 14, 30 (2017) [article no. to verify] |
| 5.6 g BCAA after resistance exercise raised myofibrillar MPS by 22 % vs placebo, about half a whey response | **Grounded** (n = 10, young trained men) | S. R. Jackman et al., *Front. Physiol.* 8, 390 (2017) |
| Reduced soreness (DOMS) and damage markers with BCAA | **Plausible-untested**: small, mixed trials, modest effects | meta-analyses [to verify] |
| Central-fatigue hypothesis: BCAAs compete with free tryptophan at the blood–brain-barrier carrier, which could lower 5-HT | **Plausible-untested**: mechanism plausible, performance evidence mixed | E. Blomstrand, *J. Nutr.* 136, 544S (2006) [to verify]; critique: Fernstrom & Fernstrom, *J. Nutr.* (2006) [to verify] |
| Raised circulating BCAAs associate with insulin resistance and predict type 2 diabetes. Causality is debated: possibly impaired BCAA catabolism rather than intake | **Grounded** (association) | C. B. Newgard et al., *Cell Metab.* 9, 311 (2009); T. J. Wang et al., *Nat. Med.* 17, 448 (2011) (top-quartile three-amino-acid score, >5-fold risk) |
| Maple syrup urine disease: inherited BCKDH deficiency causes toxic leucine/keto-acid build-up, managed with a BCAA-restricted diet and newborn screening | **Grounded** | |
| Hepatic encephalopathy / cirrhosis: BCAA supplementation is used to improve nutrition and possibly encephalopathy symptoms (Cochrane review) | **Grounded** with moderate-quality evidence | Gluud et al., Cochrane 2017 [to verify] |
| Safety: usual dietary-supplement doses are generally tolerated in healthy adults. Concerns in MSDD, ALS (an earlier trial signal) and metabolic disease [to verify]. Not for self-treatment | **Plausible-untested** | |

## 2. Electrolytes

| Claim | Label | Note |
|---|---|---|
| Na⁺ (extracellular volume, action potentials), K⁺ (resting potential, cardiac rhythm), Cl⁻ (charge and acid–base balance), Mg²⁺ (ATP–Mg cofactor, >300 enzymes), Ca²⁺ (contraction, signalling, bone) | **Grounded** | textbook physiology |
| Sweat sodium varies widely, roughly 10–90 mmol/L (~0.2–2 g/L), with large individual and acclimatisation differences | **Grounded** (range) [exact range to verify, e.g. Baker 2017 *Sports Med*] | |
| The Na⁺/K⁺-ATPase moves 3 Na⁺ out and 2 K⁺ in per ATP. It makes the gradients and can use a large share of resting energy (Skou, Nobel 1997) | **Grounded** | |
| Amino-acid uptake couples to ion gradients. SLC38 (SNAT2 etc.) and SLC1 (ASCT2 = SLC1A5) are Na⁺-coupled. **LAT1 (SLC7A5), the main leucine/BCAA carrier, is Na⁺-independent**: it exchanges leucine for intracellular glutamine, which Na⁺-coupled SNATs/ASCT2 load. So the sodium gradient powers leucine entry indirectly | **Grounded** | LAT1 is Na⁺- and pH-independent (Yan et al., *Cell Discov.* 7, 16 (2021) [vol./no. to verify]); tertiary active transport, Nicklin et al., *Cell* 136, 521 (2009) [to verify] |
| Exercise-associated hyponatremia comes mainly from drinking more hypotonic fluid than is lost (plus non-osmotic AVP). The advice is to drink to thirst; symptomatic cases are treated with hypertonic saline | **Grounded** | T. Hew-Butler et al., *Clin. J. Sport Med.* 25, 303 (2015) |
| Excess potassium or magnesium supplements are dangerous with kidney impairment | **Grounded** (general caution) | |

## 3. RGRF links (honest)

| Link | Label |
|---|---|
| Electrolytes as ionic conductors: body fluids are electrolytes in the electrochemical sense (ion transport, Debye screening ~0.8 nm at 150 mM). That ties them to the electrochemistry, cathode/anode and plasma threads ([muon_cathode_acoustic_water_review.md](muon_cathode_acoustic_water_review.md)) | Physics **Grounded**; "the body as a plasma/battery" framing **Symbolic** |
| Membrane gradients as a "leaky boundary" with gated channels (Hodgkin–Huxley; see [leaky_bound_state_family.md](leaky_bound_state_family.md)) | **Grounded** biology; the cross-scale analogy is **Symbolic** |
| Chirality: life uses L-amino acids; the origin of homochirality is open | **Grounded** fact / **Speculative** origin theories |
| Branched geometry and hydrophobic packing in protein cores (leucine zippers) | **Grounded** |
| Microbiome BCAA production (gut bacteria contribute to circulating BCAAs; Pedersen et al., *Nature* 535, 376 (2016) [to verify]) and fungal BCAA biosynthesis | **Grounded** (biosynthesis) / **Plausible-untested** (host effect size) |
| Links to the mycelium or quantum-biology threads (coherence, "docking" signals) | **Speculative / Symbolic** |

## 4. Sim (toy illustration)

A Hill-type leucine "signal" (half-max ~1 g, assumed) times a substrate limit. BCAA-only is capped at about +30 % (Wolfe's argued ceiling); complete protein is not capped. At 2.5 g leucine the model gives +86 % for complete protein vs +30 % for BCAA-only. Jackman's measured +22 % (5.6 g BCAA) is plotted for reference. Shape only, not a dosing guide. Plot: `/workspace/bcaa_plot.png` (box only).

## 5. Gaps
- [to verify]: Neinast 2019; Wolfe 2017 article number; DOMS meta-analyses; Blomstrand 2006 and the Fernstrom critique; Cochrane HE review; the sweat-sodium range source; Nicklin 2009; Pedersen 2016; the ALS signal; LAT1 paper vol./no.
- Which angle Channing wants next (neuro, metabolic, exercise, or electrochemical) [Channing to supply].
