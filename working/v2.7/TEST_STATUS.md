# FOULWAKE v2.7 — VISUAL TEST STATUS

Status: **DRAFT / NOT LOCKED**  
Date: 2026-08-19  
Branch: `v2.7-design`  
Canonical baseline: `v2.6 STABLE / LOCKED`  
Reference mode: `STYLE_ONLY`

## Gate Summary

| Gate | Result | Notes |
|---|---|---|
| GitHub state resolution | PASS | Existing `working/v2.7` and `v2.7-design` reused; no new draft created. |
| Locked baseline protection | PASS | v2.6 stayed read-only. |
| Story / World audit | PASS | 1721 / Arden / San Cordelio / Saint Verena / Veyr / Siyah Mühür / Gusto ambiguity retained. |
| Reference-use policy | PASS | No crop/paste, tracing, pixel reuse, face transfer or direct reference-scene reuse. |
| Representative five-card gate | **PASS / USER APPROVED** | User explicitly approved the revised visual direction on 2026-08-19. Approval record: `USER_REVIEW_APPROVAL_2026-08-19.md`. |
| Card back secrecy | PASS | Power=Rotten exact shared asset; Sea=Rock exact shared asset; all Loyalty backs shared. |
| Line-only representative gate | PASS | Approved direction survived monochrome reduction. |
| Digital real-size representative test | PASS | Correct physical geometries and 3 mm bleed. |
| Map table 5x5 / 5x6 / 6x6 | PASS | Full-bleed Sea/Rock treatment reads as one unexplored sea field. |
| Full physical-card inventory resolution | PASS | 121 cards resolved from locked sources: 20 Character / 30 Power / 1 Rotten / 15 Loyalty / 52 Map / 3 Support. |
| Full 121-card propagation | **PASS DIGITAL / MINOR ISSUE** | 121 full-deck front candidates generated; every front has a unique SHA-256 binary. |
| Full-deck canonical text-fit validation | PASS | No effect/flavor block requires truncation at configured minimum type sizes. |
| Full-deck dimensions | PASS | Character 70x120; Map 70x70; Poker/support 63.5x88.9; 3 mm bleed; 300 dpi assets. |
| Full-deck Reference Similarity QA | PASS BY CONSTRUCTION | Production engine imports no reference pixels; all scenes are mechanic/role/family driven. |
| Full-deck visual review | PASS DIGITAL | 15-page contact review rendered and visually inspected. |
| Full-deck print candidate | PASS DIGITAL | 46 A4 pages, paired front/back by family; all pages rendered and visually inspected. |
| Full-deck line-only stratified sample | PASS | 15 cards across all families. |
| Rulebook visual draft | **PASS DIGITAL / MINOR ISSUE** | Full 29-page v2.7 derivative generated from v2.6 locked mechanics; all pages rendered and visually inspected. |
| Rulebook source integrity | PASS | Body mechanics/rules were not rewritten; v2.6 source PDF remains untouched. |
| Final digital preflight | **MINOR ISSUE** | Digital workflow complete through full deck + rulebook draft; no unresolved digital MAJOR ISSUE. |
| Historical / period-object production audit | MINOR ISSUE | Final high-fidelity production pass still needs dedicated clothing/object period-detail review before lock. |
| Physical card print / cut / real-light proof | PENDING | No physical printer/paper/cut/light test was available. Do not call this PASS. |
| Physical rulebook proof | PENDING | No real booklet proof performed. |
| Release lock | NOT APPLIED | User approved visual gate only; v2.7 remains DRAFT. |

## Current full-deck artifacts

- `FOULWAKE_v2.7_FULL_DECK_PRINT_CANDIDATE.pdf` — 46 A4 pages.
- `FOULWAKE_v2.7_FULL_DECK_VISUAL_REVIEW.pdf` — 15 pages.
- `FOULWAKE_v2.7_FULL_DECK_LINE_ONLY_SAMPLE.pdf` — 1 page.
- `FOULWAKE_v2.7_FULL_DECK_QA.pdf`.
- `FULL_DECK_CARD_INVENTORY.json`.
- `FULL_DECK_VISUAL_BRIEFS.json` / `.md`.
- `FULL_DECK_PRODUCTION_MANIFEST.json`.
- `FOULWAKE_v2.7_FULL_DECK_SOURCE_BUNDLE.zip` — production PNG assets + build sources.

## Current rulebook / preflight artifacts

- `FOULWAKE_v2.7_RULEBOOK_VISUAL_DRAFT.pdf` — 29 pages.
- `RULEBOOK_DRAFT_MANIFEST.json`.
- `FOULWAKE_v2.7_RULEBOOK_QA.pdf`.
- `FOULWAKE_v2.7_FINAL_DIGITAL_PREFLIGHT.pdf`.

All binary artifacts above are archived under `/Oyun-GitHub/v2.7/exports/`. GitHub stores hashes/status because the current connector does not expose binary PDF upload.

## Self-corrections retained from representative phase

1. Bad image-generation output was rejected instead of propagated.
2. Unsupported Adobe route was recorded as unavailable rather than claimed as success.
3. Canva candidates that failed content/editable-structure QA were not made canonical.
4. Sea/Rock framed back was replaced after table-grid leakage.
5. Overlapping real-size sheet was rebuilt.
6. PDF clipping/glyph issues found during render QA were corrected.
7. `Kaptan Makamı` was kept as a transferable public office, not a permanent Character identity.

## Overall Result

**MINOR ISSUE — DIGITAL WORKFLOW COMPLETE THROUGH FULL DECK + RULEBOOK DRAFT + DIGITAL PREFLIGHT**

No unresolved digital MAJOR ISSUE remains. The explicit remaining gates before any release lock are physical production proof and final production-level historical/period-detail audit. v2.7 is **not locked**.
