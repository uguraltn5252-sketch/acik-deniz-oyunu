# FOULWAKE v2.7 — DESIGN WORKFLOW

Status: **DRAFT / NOT LOCKED**  
Canonical baseline: `v2.6 STABLE / LOCKED`  
Reference mode: `STYLE_ONLY`

## Source-of-truth model

1. **GitHub ACTIVE_DRAFT** holds mechanics references, card IDs/text, story/world constraints, visual standards, test status and artifact hashes.
2. `DESIGN_SYSTEM_MASTER.md` + `REFERENCE_USE_POLICY.md` remain the application-independent visual authority.
3. Canva is preferred only when editable structure passes content/editability QA.
4. Adobe Express is secondary and used only when the requested operation is supported.
5. Otherwise the workflow uses controlled local production + PDF review artifacts and records the limitation honestly.
6. No design tool may silently alter canonical mechanics or wording.

## User Review Gate

**APPROVED — 2026-08-19.**

Record: `USER_REVIEW_APPROVAL_2026-08-19.md`.

This approval authorized full-deck propagation and rulebook visual work. It did **not** authorize a release lock. v2.7 remains DRAFT / NOT LOCKED.

## Reference-use rule

`REFERENCE = INSPIRATION, NOT SOURCE ART`

Allowed: line character, color balance, texture strength, adult-caricature level, humor level, visual hierarchy and atmosphere.

Forbidden by default: crop/paste, tracing, pixel-level reuse, cut-out character/object/background reuse, same-face transfer, direct reference-card artwork reuse and unnecessary copying of pose/composition.

## Completed production sequence

1. Resolve v2.6 locked baseline and existing v2.7 draft — PASS.
2. Story / World audit — PASS.
3. Design System + Reference Use Policy — PASS.
4. Representative card audit and five visual briefs — PASS.
5. Five original representative candidates — PASS / MINOR ISSUE.
6. Reference Similarity + Mechanic-Visual QA — PASS.
7. Card-back secrecy system — PASS.
8. Line-only / 2–3 second / real-size / table tests — PASS after self-corrections.
9. User Review Gate — **APPROVED**.
10. Full 121-card inventory resolved from locked sources — PASS.
11. Full 121-card digital propagation — **COMPLETE / PASS DIGITAL / MINOR ISSUE**.
12. Full-deck text-fit, dimensions, uniqueness and secrecy checks — PASS.
13. 15-page full-deck visual review render — PASS.
14. 46-page A4 print candidate render — PASS DIGITAL.
15. Full 29-page rulebook visual derivative — **COMPLETE / PASS DIGITAL / MINOR ISSUE**.
16. Rulebook 29-page render QA — PASS.
17. Historical / period-object audit — **PASS DIGITAL AFTER SELF-CORRECTION**.
18. Final digital preflight — **PASS DIGITAL / PHYSICAL GATE PENDING**.

## Historical self-corrections

The production audit caught and corrected two period-readability risks before the workflow was declared digitally complete:

- `GUC-01A/B Can Simidi`: modern manufactured ring-buoy cue removed; replaced with a rope loop and small wooden float/cask visual.
- `KAR-06 Dipgören`: helmet-like diver cue removed; replaced with a weighted recovery line / breath-hold-diver visual cue.

No known unresolved anachronism remains in the current schematic card candidate.

## Current production artifacts

Binary outputs are archived under `/Oyun-GitHub/v2.7/exports/`; exact hashes are in `EXPORT_MANIFEST.json`.

Key outputs:

- `FOULWAKE_v2.7_FULL_DECK_PRINT_CANDIDATE.pdf`
- `FOULWAKE_v2.7_FULL_DECK_VISUAL_REVIEW.pdf`
- `FOULWAKE_v2.7_FULL_DECK_LINE_ONLY_SAMPLE.pdf`
- `FOULWAKE_v2.7_FULL_DECK_QA.pdf`
- `FOULWAKE_v2.7_HISTORICAL_PERIOD_AUDIT.pdf`
- `FULL_DECK_CARD_INVENTORY.json`
- `FULL_DECK_VISUAL_BRIEFS.json` / `.md`
- `FULL_DECK_PRODUCTION_MANIFEST.json`
- `FOULWAKE_v2.7_FULL_DECK_SOURCE_BUNDLE.zip`
- `FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf`
- `FOULWAKE_v2.7_RULEBOOK_QA.pdf`
- `FOULWAKE_v2.7_FINAL_DIGITAL_PREFLIGHT.pdf`

## Remaining real gate before any lock

### Physical production proof — PENDING

A real 100% card print, duplex alignment, cut-tolerance, hand-readability and real-light check has not been performed in this environment. A physical rulebook proof has also not been performed.

The rulebook interior still carries a **non-blocking MINOR visual-refinement issue** because much of its typography/flow is inherited from the locked source. This is not a mechanics or digital-render failure.

## Lock rule

Do not convert v2.7 to STABLE / LOCKED unless the user explicitly instructs it with language such as `kilitle`, `stable yap` or `release et` after physical production proof is addressed.

Current next gate: **physical card/rulebook production proof**.
