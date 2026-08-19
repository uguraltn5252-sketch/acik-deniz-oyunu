# FOULWAKE v2.7 — VISUAL TEST STATUS

Status: DRAFT / NOT LOCKED
Date: 2026-08-19
Branch: `v2.7-design`
Canonical baseline: `v2.6 STABLE / LOCKED`
Reference mode: `STYLE_ONLY`

## Gate Summary

| Gate | Result | Notes |
|---|---|---|
| GitHub state resolution | PASS | Existing `working/v2.7` and `v2.7-design` reused; no new draft was created. |
| Locked baseline protection | PASS | `v2.6 STABLE / LOCKED` was read only; no locked artifact was changed. |
| Story / World audit | PASS | 1721, Arden, San Cordelio, Saint Verena, Veyr, Siyah Mühür and Gusto ambiguity checked against the current v2.7 World Bible. |
| Reference-use policy | PASS | `REFERENCE_USE_POLICY.md` added. Default is STYLE_ONLY; crop/paste, tracing, pixel reuse and reference-character transfer are forbidden. |
| Representative visual briefs | PASS | All five representative cards received mechanic-first briefs in `REPRESENTATIVE_VISUAL_BRIEFS.md`. |
| Image-generation attempt | FAIL / REJECTED | The image-generation attempt produced an unrelated project dashboard with incorrect content, so it was rejected and not used as card art. |
| Adobe Express art attempt | FAIL / UNAVAILABLE | Direct standalone illustration generation was not available for this gate. No false success was recorded. |
| Canva revised import | FAIL AS EDITABLE SOURCE | Canva design `DAHSv3GnJGo` imported, but validation returned one page and empty rich-text content; it is experimental only and not the source of truth. |
| PDF-first fallback | PASS | Controlled local production generated the revised review set and archived it to `/Oyun-GitHub/v2.7/exports/`. |
| Representative five-card visual gate | MINOR ISSUE / USER REVIEW | Exact mechanics used; all five illustrations are newly constructed without reference pixels/crops. Art remains representative/prototype-level rather than final production illustration. |
| Reference Similarity QA | PASS | No crop/paste, tracing, pixel-level reuse, reference face transfer or reference-scene repackaging detected. |
| Line-only test | PASS | Main subject/action and card hierarchy remain readable after color removal. |
| 2–3 second hierarchy test | PASS | Title and primary mechanic zones are consistent and quickly locatable. |
| Power / Rotten Provisions back secrecy | PASS | Exact same binary back asset is reused. |
| Sea / Rock back secrecy | PASS | Exact same binary back asset is reused in the v2.7 visual draft. |
| Back text / FOULWAKE leakage | PASS | Back assets contain no text and no FOULWAKE mark. |
| 5x5 map table test | PASS AFTER SELF-CORRECTION | Initial framed back read too strongly as a card grid; it was rejected, replaced by a full-bleed continuous-sea back, then retested. |
| 5x6 map table test | PASS AFTER SELF-CORRECTION | Full-bleed identical Sea/Rock back reads as one unexplored sea field. |
| 6x6 map table test | PASS AFTER SELF-CORRECTION | Full-bleed identical Sea/Rock back reads as one unexplored sea field. |
| Digital real-size print test | PASS | 100% PDF uses real card geometry with 3 mm bleed and trim guides; the first overlapping sheet was rejected and rebuilt as two clean A4 pages. |
| Physical print | PENDING | No real printer, paper, cut tolerance or real-light test was available. Do not call this a physical-print PASS. |
| Historical / story QA | MINOR ISSUE | No lore ambiguity is resolved, but final production illustration should still receive a dedicated period-object and clothing audit before lock. |
| PDF open/render/preflight | PASS | Seven revised PDFs open and render. Visual clipping/overlap defects discovered during review were corrected and PDFs rerendered. |
| Full 121-card propagation | BLOCKED | Must remain blocked until explicit user acceptance of the visual gate. |
| Rulebook visual redesign | BLOCKED | Deferred until card visual gate approval. |

## Representative Five-Card Set

1. `KAR-01 Uzakgören`
2. `GUC-01A Can Simidi`
3. `ERZ-01 Çürümüş Erzak`
4. `HAR-AD-30 Bir Bulutun Kişisel Meselesi`
5. `SET-KP-01 Kaptan Makamı`

## Self-Corrections Performed Without User Interruption

1. Rejected the unrelated image-generation output instead of propagating it.
2. Rejected Adobe Express as a direct illustration route when the requested operation was unavailable.
3. Rejected Canva as canonical when editable/content validation failed.
4. Replaced the first Sea/Rock framed back after the table test showed an obvious card-grid effect.
5. Split the first real-size print sheet after card overlap was found during visual PDF inspection.
6. Rebuilt Design System Board and Visual QA pages after text clipping/overlap was detected during render review.
7. Reworked `Kaptan Makamı` so the visual reads as an empty transferable office rather than a permanent Captain character.

## Current Production-Art Limitation

The revised representative illustrations are original and mechanic-specific, but they are still controlled prototype artwork rather than final hand-illustrated production masters. They are sufficient for the current visual-language/layout gate. They must be upgraded before final full-deck preflight if the user approves the direction.

## Overall Result

**MINOR ISSUE — USER REVIEW GATE**

No unresolved digital MAJOR ISSUE remains in the revised review set. Full-deck propagation stays blocked until the user explicitly approves the visual direction.
