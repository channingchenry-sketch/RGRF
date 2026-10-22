# Modular Core GitHub repo proposal: review of share #124 (`0cc69365`), the founding chat of Resona-POL-Modular-Core

*License CC0. Source: Grok conversation "Modular Core GitHub Repo Proposal" (4 messages, 3 pages), archived verbatim at [grok_archive/2026-10-22_modular_core_github_repo_proposal.md](grok_archive/2026-10-22_modular_core_github_repo_proposal.md). Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic** (φ is Symbolic unless tested). Grok's claims are **Grok-reported** unless checked here. Repo state was checked with `gh` on 2026-10-22.*

**Scope notes.**
- **Surname check:** no surname appears. The only near-hit is inside the GitHub handle `channingchenry-sketch`.
- **Omissions:** nothing out of scope was found.
- **Why this share matters:** this is the founding chat for [Resona-POL-Modular-Core](https://github.com/channingchenry-sketch/Resona-POL-Modular-Core). Channing says it was meant to be what everything linked to early on.

**Related docs.**
- RGRF already links to Modular Core from [../README.md](../README.md) (phi-spiral result) and [README.md](README.md) (simulation code). The legacy POL review is in [legal_safety_and_grounding_review.md](legal_safety_and_grounding_review.md) (520 W vs 10–16.7 kW).
- Coil physics: [tesla_meao_secondary_faraday_verdet_review.md](tesla_meao_secondary_faraday_verdet_review.md) (#123).

## 0. Keyword search: no green-lensing content
There is one hit for "green": the infographic's "earthy greens, golds" colour scheme. It is a palette, not optics. There are 0 hits for "lensing" or "lens". **No green-lensing content.**

## 1. Channing (verbatim)
- "Can I get a link to the modular core to add to the website?"
- "Let’s do steps 2 then, 1 then,3."

## 2. What Grok claimed vs what exists
| Grok's claim | Status (checked 2026-10-22) |
|---|---|
| Msg 2: "I don't see a live public link yet ... likely still in our private collaborative files" | Plausible. The repo's first commit is 2026-06-04, so it postdates this chat or was made during it |
| Step 2 "(Completed)": Canva infographic, link text "View / Edit the Modular Core Infographic" | **URL not captured in the share** [to verify]. Whether the design exists in Channing's Canva is [Channing to supply]. No infographic is in either repo |
| Step 1 "(Completed)": repo created "with a basic README" | **Confirmed.** The repo was created 2026-06-04 12:00 PDT with commit `36949c1` "Initial commit", which added only a 2-line README (title plus the description "Modular Core for POL v0.1 ... under public domain"). Who created it (Grok's connector or Channing) is [to verify] |
| "I'll populate it soon with blueprints, Python hover simulations, BOM, and limitations" | **Not done by Grok.** The only later commit is `e12546b` (2026-10-11 21:16 PDT), a first-principles rebuild: `sim/hover_dynamics.py`, `sim/height_control.py`, `legacy/grok_v0.1/` (Grok-era scripts, marked not physically valid, with PHYSICS_REVIEW.md), concept art, CC0 LICENSE, and the full README |
| Step 3: raw README embed link `https://raw.githubusercontent.com/channingchenry-sketch/Resona-POL-Modular-Core/main/README.md` | **Works** (HTTP 200; default branch `main`). It now serves the October README, not the basic one |
| "Under public domain" | **Confirmed:** CC0 1.0 LICENSE (added in `e12546b`) |

## 3. What the proposal promised vs what exists
| Promised item | Exists? | Where / note |
|---|---|---|
| CAD/STL files for phi-spiral coils | **Missing** | There are no CAD or STL files. The coil geometry exists only as parameters in the sims |
| Python simulation scripts | **Exists** | `sim/hover_dynamics.py` and `sim/height_control.py` (current); `legacy/grok_v0.1/hover_dynamics.py`, `rgrf_scaler.py`, `resonance_calc.py` (historical) |
| Resonance tuning parameters | **Partial** | `legacy/grok_v0.1/resonance_calc.py` plus run outputs (historical; see the #115 correction: the 1.335 ratio is not φ, and the 13.56 MHz lumped tuning cannot be reached). The current sim uses a 100 Hz drive and has no resonant-tuning module |
| Integration diagrams for website embedding | **Missing** | Only AI concept art (`docs/concept_art/`, labelled speculative). There are no integration or wiring diagrams |
| Website embed | **Partial** | The raw README link works. The website page itself and any Canva embed are [Channing to supply] |
| BOM (Trametes versicolor/hemp) | **Missing as a file** | Mentioned in `legacy/grok_v0.1/docs/baseline_pol_v0.1.md` [to verify contents]. There is no standalone BOM |
| Limitations (conductive floor) | **Exists** | README "Current honest status" |

## 4. Physics labels
| Claim | Label |
|---|---|
| Eddy-current lift over a conductive floor; conductive-floor requirement | Grounded (the repo sim gives ~10–16.7 kW for 88 kg, not 520 W) |
| Golden-ratio spiral coils as a performance feature | Symbolic. The repo sim found the phi spiral 8.7 % *worse* than linear spacing |
| Tesla-resonant wireless power distribution | Plausible-untested at this power. Resonance cancels reactive power, not losses |
| Mycelium composite deck | Plausible-untested |
| Docking stations, Waverider, cosmic fleet | Speculative / fiction (*Entanglements*) |

## 5. Open questions for Channing
1. Can you supply the Canva infographic URL, or confirm whether the design exists? [Channing to supply]
2. Which website page should link here, and should it point at the raw README or the repo page? [Channing to supply]
3. **Hub README:** should there be one landing page (e.g. a short section at the top of RGRF's README, or a profile README) that links RGRF and Resona-POL-Modular-Core as the "everything links here" entry point that this chat intended? (Suggestion only. The other repo was not edited.)
4. Should CAD/STL coil files and an integration diagram be added to Modular Core to close out the original promise?
