# FOULWAKE v2.7 — DESIGN WORKFLOW

Status: DRAFT / NOT LOCKED
Canonical baseline: `v2.6 STABLE / LOCKED`
Reference mode: `STYLE_ONLY`

## Source-of-truth model

1. **GitHub ACTIVE_DRAFT** holds mechanics references, card IDs/text, story/world constraints, the visual standard, test status and artifact hashes.
2. `DESIGN_SYSTEM_MASTER.md` + `REFERENCE_USE_POLICY.md` are the application-independent visual authority.
3. **Canva** is the preferred editable production workspace only when the imported/generated structure actually passes content/editability QA.
4. **Adobe Express** is secondary and used only when the required operation is supported.
5. If Canva/Adobe cannot produce a controlled result, the workflow falls back to local production plus review/test PDFs instead of stopping.
6. No design app may silently change canonical mechanics or wording.

## Reference-use rule

`REFERENCE = INSPIRATION, NOT SOURCE ART`

Allowed: line character, color balance, texture strength, adult-caricature level, humor level, visual hierarchy and atmosphere.

Forbidden by default: crop/paste, tracing, pixel-level reuse, cut-out character/object/background reuse, same-face transfer, direct reference-card artwork reuse, and unnecessary copying of the same pose/composition.

Every representative/final illustration must pass `REFERENCE_USE_POLICY.md` before scale.

## Change routing

### Mechanical/content change
`GitHub -> validation -> design sync -> export -> GitHub status/manifest`

### Pure visual change
`Visual production -> compare against design system + reference policy -> QA -> user review -> export/status`

## Self-correction rule

A tool finishing is not a workflow gate.

If a candidate is wrong, unsupported, clipped, grid-leaking, mechanically misleading or reference-reusing, classify it as FAIL, fix it without asking the user when safe, rerender/retest, and only then continue.

## Current production order

1. Resolve locked baseline and active draft.
2. Audit story/world constraints.
3. Resolve Design System + Reference Use Policy.
4. Audit exact representative-card mechanics.
5. Produce five mechanic-first visual briefs.
6. Produce five new original representative illustrations.
7. Run Reference Similarity QA.
8. Run Mechanic-Visual Consistency QA.
9. Test title/banner hierarchy.
10. Produce/test card-back families.
11. Run Power/Rotten and Sea/Rock secrecy tests.
12. Run line-only test.
13. Run 2–3 second hierarchy test.
14. Run digital real-size print test.
15. Run 5x5 / 5x6 / 6x6 table tests.
16. Render all review PDFs and correct clipping/overflow/layout defects.
17. Attempt Canva editable review source; reject it if structure/content QA fails.
18. Reach User Review Gate only at PASS or MINOR ISSUE.
19. Propagate to all 121 physical cards only after explicit user approval.
20. Apply the approved visual universe to the rulebook.
21. Run final production-art, physical-print and full-deck preflight before any lock request.

## Representative five-card gate

- `KAR-01 Uzakgören`
- `GUC-01A Can Simidi`
- `ERZ-01 Çürümüş Erzak`
- `HAR-AD-30 Bir Bulutun Kişisel Meselesi`
- `SET-KP-01 Kaptan Makamı`

Current revised result: **MINOR ISSUE / USER REVIEW REQUIRED**.

All five current representative illustrations are newly constructed for this gate and contain no reference crops or pixels. They remain representative/prototype production art; final illustration masters require an additional period-detail/art-fidelity pass before final lock.

## Current known tool status

- Earlier Canva generated candidate `DAHSvmAWxYk`: content QA FAIL; not canonical.
- Revised Canva import `DAHSv3GnJGo`: technical import succeeded, but page-count/rich-text validation failed intended editable structure; not canonical.
- Adobe Express direct standalone art generation: unavailable for this gate.
- PDF-first controlled review workflow: PASS.

## Required review questions at User Review Gate

- Does the new visual direction feel like FOULWAKE rather than a generic pirate game?
- Is the hand-ink/limited-color language close enough to the target to justify a production-art refinement pass?
- Is the title banner controlled rather than oversized?
- Are mechanics readable at real size?
- Does humor remain inside the world instead of replacing tension?
- Are card backs mechanically safe?
- Does the facedown map read as one sea field at table distance?
- Is `Kaptan Makamı` clearly an office/role rather than a permanent Character identity?
