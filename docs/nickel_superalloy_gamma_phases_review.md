# Nickel superalloys, γ′/γ″/δ, niobium and side topics: review of Grok share `28a95833` (2026-10-17)

*License: CC0-1.0. Labels: **Grounded** (established physics or a checked source), **Plausible-untested**, **Speculative**, **Symbolic**. Numbers Grok gave without a rerun are **Grok-reported**. Unchecked items are [to verify]; gaps are [Channing to supply]. Channing's words are quoted verbatim.*

- **Archive:** [grok_archive/2026-10-17_nickel_superalloys_gamma_prime_phase.md](grok_archive/2026-10-17_nickel_superalloys_gamma_prime_phase.md). 38 messages; **messages 23–38 are withheld** from the public archive (a personal visualisation and reflection side-thread) and kept privately for Channing.
- **Claim checks:** [sims/grok_s81_85_claim_checks.py](../sims/grok_s81_85_claim_checks.py), section C (K-40).
- **Related docs:** [nickel_copper_magnetostriction_review.md](nickel_copper_magnetostriction_review.md) (Ni and Cu magnetic and elastic properties, not repeated here); [materials_electronics.md](materials_electronics.md) (plasma surface treatment of composites).

## 0. Summary

This is a materials-science thread and Grok is mostly accurate. Almost everything in msgs 1–22 is **Grounded** textbook metallurgy, chemistry or nuclear data. Corrections are minor (§2). No φ, no device claims, no sims.

## 1. Claims and labels (msgs 1–22)

| Msgs | Claim (Grok) | Check | Label |
|---|---|---|---|
| 1–2 | γ′ = Ni₃(Al,Ti), ordered L1₂, coherent with the FCC γ matrix; strengthening peaks at intermediate particle sizes (~20–100 nm); anomalous yield-strength rise with temperature | Standard (Reed, *The Superalloys*, CUP 2006 [to verify page]) | Grounded |
| 3–4 | γ″ = Ni₃Nb, body-centred tetragonal D0₂₂, a ≈ 0.362 nm, c ≈ 0.74 nm, disc-shaped, three variants; metastable, converts to orthorhombic δ (D0a) above ~650–700 °C; IN718 usable to ~650 °C | Matches the standard IN718 literature | Grounded |
| 4 | Plasma polymerisation: cross-linked random networks, Yasuda's CAP (competitive ablation and polymerisation) and RSGP (rapid step-growth polymerisation) models, hydrophobic recovery | Correct attribution to H. Yasuda | Grounded |
| 4 | Acoustic radiation force via the Gor'kov potential; acoustophoresis | Correct (L. P. Gor'kov 1962) | Grounded |
| 4 | Dielectric barrier discharges for surface activation | Correct | Grounded |
| 6 | δ forms appreciably in < 100 h between ~750 and 950 °C, fastest ~850–900 °C, dissolves above ~1000–1030 °C | Consistent with published IN718 TTT diagrams | Grounded; activation energies (157–272, 197–212 kJ/mol) Grok-reported [to verify] |
| 6 | γ″ → δ by a stacking-sequence change (shear on {111}) | Standard mechanism | Grounded |
| 8 | Nb: BCC a ≈ 0.330 nm, 8.57 g/cm³, mp 2477 °C, bp ≈ 4744 °C, Tc 9.25 K, Brazil the dominant producer | All correct | Grounded |
| 8 | "Niobium is … typically 3–6 wt% in alloys such as Inconel 718, 625, and 706" | Loose: 718 has 4.75–5.5 %, 625 has 3.15–4.15 % (Nb + Ta), 706 has only ~2.5–3.3 % | Grounded with a minor correction |
| 10 | NbC/NbN, δ plates and "agglomeration": δ grows as plates/needles on grain boundaries, clustering in Nb-rich interdendritic regions | Channing asked (msg 9): "is the delta transform have agglomeration or am I visualizing that wrong". Grok's answer is right: it is directional plate growth in Nb-segregated regions, not particle agglomeration | Grounded |
| 12 | Austenite vs martensite: Ni superalloys stay FCC austenite and do not form martensite in service; C ≈ 0.02–0.08 wt% | Correct | Grounded |
| 14 | Densities: Ni 8.90; 718 ≈ 8.19–8.22; 625 ≈ 8.44; 600 ≈ 8.47 g/cm³ | Correct (Special Metals data sheets) | Grounded |
| 14 | Liquid 718 ≈ 7.4–7.5 g/cm³ at the liquidus; viscosity ~5–15 mPa·s; pure Ni 4–5 mPa·s | Pure Ni figure is right; 718 values Grok-reported | Plausible / [to verify] |
| 16 | Nb segregation ratio 4–5.5; final liquid > 15 wt% Nb; freckle defects in large ingots | Consistent with solidification literature | Grounded; numbers [to verify] |
| 16 | Surface tension ~1.47 N/m for 718, 1.51–1.55 N/m for neighbours; pure Ni ~1.7–1.8 N/m | Pure Ni right (~1.78 N/m); alloy figures Grok-reported | [to verify] |
| 18 | MnO₂ ≈ 5.03 g/cm³, decomposes ~535 °C, α (hollandite 2×2 tunnels), β (pyrolusite), δ (birnessite) polymorphs | Correct | Grounded |
| 20 | K-40: 0.0117 %, T½ 1.25 × 10⁹ yr, 89 % β⁻ to Ca-40, 10.7 % EC to Ar-40 with the 1.461 MeV γ, ~31 Bq per g K | Rerun: 31.7 Bq/g (section C) ✓ | Grounded |
| 20 | K-40 is "the largest single contributor to the internal radiation dose in the human body" | **Overstated.** By UNSCEAR figures, inhaled radon progeny give the largest internal dose (~1.3 mSv/yr world average). K-40 is the largest *ingested* source (~0.17 mSv/yr) | Correction |
| 22 | Displacement reactions: Zn + CuSO₄, Mg + 2HCl, Fe + Cu²⁺ (copper cementation) | Correct | Grounded |

## 2. Corrections

1. **Nb content (msg 8).** Not "3–6 wt%" across 718/625/706: 706 is ~2.5–3.3 %.
2. **K-40 dose (msg 20).** Radon progeny, not K-40, are the largest internal dose; K-40 is the largest ingested internal emitter.
3. Grok's own statements on γ″ temperature limits are consistent across msgs 4 and 6; no contradiction found.

## 3. One technical question from the withheld section

Most of msgs 23–38 are personal and stay private. One clause from Channing's msg 33 is a physics question and is quoted here on its own:

> "can we do a thought experiment where hydrogen has another state putting it closer to helium type properties maybe there's a dark energy correlation"

- **Metallic hydrogen, a different state of hydrogen:** predicted by E. Wigner and H. B. Huntington (1935) — Grounded as a prediction. Lab claims: Dias & Silvera (*Science* 2017) are contested; Loubeyre et al. (*Nature* 2020, IR-reflectivity transition near 425 GPa) [to verify]. Label: Grounded (theory) / Plausible (experiments).
- **"Closer to helium type properties":** no known state of hydrogen behaves like helium. Speculative.
- **A dark-energy link:** **not supported.** Dark energy appears in cosmology as a uniform energy density (~6 × 10⁻¹⁰ J/m³); no hydrogen phase is known to couple to it. Speculative.

## 4. Contradictions with the repo

None. The thread makes no device, power or φ claims. Grok's suggestions to use superalloys for "conductive floors, resonant structures" (msg 2) are design ideas only: Plausible-untested.

## 5. Open items

- Sources for the 718 liquid viscosity, surface tension and activation-energy figures [to verify].
- Whether Channing wants the hydrogen thought experiment developed publicly as a physics question [Channing to supply].
- Full share URL [Channing to supply].
