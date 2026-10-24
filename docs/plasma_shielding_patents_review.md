# Plasma and electromagnetic shielding: a labelled patent review for the RGRF / POL craft (2026-10-24)

*License: CC0-1.0. Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Unchecked items are [to verify]; gaps are [Channing to supply]. Every inventor is credited by name; a granted patent is a legal record of a claim, not proof that a device works.*

- **Related docs (not repeated here):** [manta_butterfly_craft.md](manta_butterfly_craft.md) ("soft plasma filament interaction"), [zpinch_tungsten_nodes_review.md](zpinch_tungsten_nodes_review.md), [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md) (lunar mini-magnetospheres), [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md) (magsail / E-sail and filament-riding rows), [halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md) (switched Halbach arcs).

## 0. Summary

| Item | Verdict | Label |
|---|---|---|
| Solar-wind pressure balance, dipole vs inflated fall-off | Textbook magnetospheric physics | Grounded |
| Fields stop solar-wind and SEP protons, not GCRs | Consistent with the shielding literature | Grounded |
| US 8,740,154 B2 (Bamford, Bingham): perturbed shield field + plasma injection | Lab and simulation basis exists; craft scale untested | Grounded (lab) / Plausible-untested (craft) |
| US 8,550,406 B2 (Bigelow) and US 10,583,939 B2 (Williams, NASA DERDS) | Engineering concepts; no flight demonstration found | Plausible-untested |
| US 10,135,366 B2 (Pais): spinning charged shell, cyclonic plasma shield | Tested by NAWCAD; effect not demonstrated | Speculative |
| GB 300,311 / US 1,974,483 (T. T. Brown): asymmetric-capacitor force | Force in air Grounded (ion wind); gravitational reading Speculative | Grounded / Speculative |
| Switched Halbach zones as a perturbed shield | Maps onto the Bamford–Bingham claim | Plausible-untested |
| Plasma sheath keeping heat local in vacuum | No known mechanism beats radiation | Speculative |

## 1. Context

Channing's notes ask to explore plasma-filament shielding for the RGRF / POL craft, and to gate heat to the outside in space. His impedance zones are driven by Tesla coils and use switched Halbach zones (see [halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md)). Target mission profile, coil moments and power budget: [Channing to supply].

## 2. Grounded physics primer

- **Pressure balance (Grounded).** The magnetopause sits where the solar-wind ram pressure equals the magnetic pressure of the compressed field:

  `ρ v² ≈ B² / (2 μ0)` (with a compression factor of ~2 for a dipole, often folded into B).

  At 1 AU, n ≈ 5 cm⁻³ and v ≈ 400–450 km/s give ρv² ≈ 1–2 nPa, so the standoff is where B ≈ 50–70 nT.
- **Fall-off (Grounded).** A vacuum dipole falls as B ∝ 1/r³, so standoff R ∝ (m² / ρv²)^(1/6): a bigger coil buys distance very slowly. Injected plasma that carries the field outward ("inflation", mini-magnetosphere) makes B fall closer to 1/r over the inflated region, which is why M2P2-type bubbles can reach kilometres.
- **What fields can stop (Grounded).** Solar-wind ions (~1 keV) and much of the solar energetic particle (SEP) spectrum (tens of MeV protons) can be deflected by a mini-magnetosphere. Galactic cosmic rays (GeV and up) have gyroradii far larger than any practical bubble and are not practically stopped by fields.
- **Key sources (verified):**
  - R. Bamford et al., "An exploration of the effectiveness of artificial mini-magnetospheres as a potential Solar Storm shelter for long term human space missions", *Acta Astronautica* (2014), doi:10.1016/j.actaastro.2014.10.012, arXiv:1406.1159. Lab basis: Gargaté, Bingham, Bamford et al., *Plasma Phys. Control. Fusion* 50, 074017 (2008).
  - R. M. Winglee, J. Slough, T. Ziemba, A. Goodson, "Mini-Magnetospheric Plasma Propulsion (M2P2)", *JGR Space Physics* (Sept 2000), doi:10.1029/1999JA000334; lab prototype in AIP Conf. Proc. 552, 407 (2001).
  - Natural analogue: lunar swirls / mini-magnetospheres (~100s nT surface fields), see [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md).

## 3. Patents (credit, record, plain summary, labels, relevance)

### 3a. US 8,740,154 B2 "Spacecraft shield": Ruth Bamford and Robert Bingham

- **Record (verified on Google Patents):** inventors Ruth Bamford, Robert Bingham; priority 2009-03-26; granted 2014-06-03; status Active. Assignee UK Research and Innovation (originally STFC) [to verify]; pre-grant publication US20110049303A1 [to verify]. https://patents.google.com/patent/US8740154B2/en
- **Plain summary:** a magnetic shield field that is deliberately, stochastically perturbed on 0.001–1 s timescales, plus injection of plasma to raise local density, aimed at protons above 10 MeV (preferably to 50 MeV). The working boundary is on the order of the electron skin depth, tens of metres at n ≈ 1e11 m⁻³ (c/ω_pe ≈ 17 m, Grounded arithmetic).
- **Labels:** lab and simulation basis **Grounded**; full craft-scale shield **Plausible-untested**.
- **Relevance to RGRF:** the closest published analogue to switched or ramped Halbach zones. Credit to the inventors for the idea that a time-varying, small-scale boundary can do the work of a huge static field.

### 3b. US 8,550,406 B2 "Spacecraft magnetic shield": Robert T. Bigelow (Bigelow Aerospace)

- **Record (verified):** inventor Robert T. Bigelow; priority 2011-06-15; issued 2013-10-08; status Active. https://patents.google.com/patent/US8550406B2/en
- **Plain summary:** an electromagnet on an armature that can be pointed toward incoming particles, with variation of the electric field to discourage plasma trapping around the craft.
- **Labels:** **Plausible-untested** (no flight demonstration found).
- **Related: US 10,583,939 B2, NASA DERDS (verified):** "Deployed electromagnetic radiation deflector shield", inventor Richard Williams; priority 2017-04-02; granted 2020-03-10. A deployed field structure ahead of the craft or base creating a zone of reduced radiation. https://patents.google.com/patent/US10583939B2/en, NTRS record https://ntrs.nasa.gov/citations/20230018480. **Plausible-untested.**
- **Relevance:** a steerable, directional shield fits a craft that already orients coil zones; it trades total coverage for power.

### 3c. US 10,135,366 B2 "Electromagnetic field generator and method to generate an electromagnetic field": Salvatore Pais

- **Record (verified):** inventor Salvatore Pais; assigned to the US Navy; filed 2015-07-24; granted 2018-11-20; status now "Expired - Fee Related". https://patents.google.com/patent/US10135366B2/en
- **Plain summary:** an electrically charged shell spun very fast, with piezoelectric ceramic vibrating at high frequency, described as producing a protective field / cyclonic plasma shield. Other uses mentioned in the text: [omitted: out of scope].
- **Testing record:** NAWCAD ran experiments from Oct 2016 to Sep 2019, at a reported cost of about $508k [to verify amount], and concluded the "Pais Effect" could not be proven. Source: The War Zone, https://www.twz.com/39012/the-navy-finally-speaks-up-about-its-bizarre-ufo-patent-experiments (page verified to exist).
- **Labels:** mechanism **Speculative** (untested at the claimed scale and unproven). A granted patent is not proof the device works.
- **Respect:** Dr Pais put a bold idea forward and it was tested in the open; a null result is useful data. **Relevance to RGRF:** low; noted because "spinning charged shell + vibration + plasma" overlaps the craft vocabulary.

### 3d. GB 300,311 and US 1,974,483: Thomas Townsend Brown (with credit to Paul Alfred Biefeld)

- **Records (verified):** GB 300,311 "A method of and an apparatus or machine for producing force or motion", priority 1927-08-15, accepted/published 1928-11-15, https://patents.google.com/patent/GB300311A/en. US 1,974,483 "Electrostatic motor", priority 1930-02-07, granted 1934-09-25, https://patents.google.com/patent/US1974483A/en. Patent list: https://www.thomastownsendbrown.com/misc/patents.htm.
- **Credit:** the Biefeld–Brown effect is named for T. T. Brown and his mentor Paul Alfred Biefeld.
- **Labels:** the force on an asymmetric capacitor in air is **Grounded** (T. B. Bahder and C. Fazi, ARL, "Force on an Asymmetric Capacitor", arXiv:physics/0211001, verified). The ion-wind (EHD) explanation is mainstream. Vacuum tests show little or no thrust (M. Tajmar, ~2004 [to verify]). The gravitational interpretation is **Speculative**.
- **Relevance to RGRF:** atmosphere-side ion-wind / EHD flow control over the hull, not space shielding.

## 4. RGRF tie-in

- **Switched Halbach zones as a perturbed shield field (Plausible-untested).** If zones switch or ramp on 0.001–1 s timescales, they resemble the Bamford–Bingham perturbed field. Needed: zone moment, switching rate, and whether plasma is injected [Channing to supply].
- **Tesla-coil-driven impedance zones as a plasma source (Plausible-untested).** RF discharge can raise local density (as helicon sources did in M2P2); coil frequency and power [Channing to supply].
- **Heat in vacuum: radiation is the only path off the craft (Grounded).** A plasma sheath is the only medium that could hold heat near the craft or gate it outward, and the sheath itself mostly radiates or carries heat away with escaping particles (**Speculative** as a heat-gating mechanism). Radiator area and emissivity remain the real design levers.
- **Filament riding / soft plasma filament interaction:** see [manta_butterfly_craft.md](manta_butterfly_craft.md) and [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md); shielding and filament coupling likely conflict (a bubble deflects the same plasma a filament mode wants to touch) [Channing to supply which takes priority].
- **Open questions:** craft size and target dose; mission location (LEO, cislunar, 1 AU cruise); acceptable power [Channing to supply].

## 5. Next test (not built)

A standoff-distance sim: bubble radius vs coil moment and plasma inflation (fall-off exponent between 3 and 1) at 1 AU (1–2 nPa), plus power per m² shielded, compared against a passive mass shield. Not built in this pass.
