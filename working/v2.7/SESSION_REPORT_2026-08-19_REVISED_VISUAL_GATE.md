# FOULWAKE v2.7 — REVISED VISUAL GATE SESSION REPORT

Date: 2026-08-19
Status: DRAFT / NOT LOCKED

## Resolved Workspace

- CURRENT_LOCKED_RELEASE: `v2.6 STABLE / LOCKED`
- ACTIVE_DRAFT: `v2.7`
- ACTIVE_BRANCH: `v2.7-design`
- ACTIVE_WORKSPACE_PATH: `working/v2.7`
- REFERENCE_USE_MODE: `STYLE_ONLY`

No new draft was created. No v2.6 locked file was modified.

## New Active-Draft Controls

- `REFERENCE_USE_POLICY.md`
- `REPRESENTATIVE_VISUAL_BRIEFS.md`

The reference policy makes crop/paste, tracing, pixel reuse and direct reference-asset reuse explicit FAIL conditions unless the user specifically asks for asset reuse/editing.

## Representative Set Reworked

- `KAR-01 Uzakgören`
- `GUC-01A Can Simidi`
- `ERZ-01 Çürümüş Erzak`
- `HAR-AD-30 Bir Bulutun Kişisel Meselesi`
- `SET-KP-01 Kaptan Makamı`

All five current representative illustrations were constructed anew from mechanic-first briefs. Uploaded reference images were not embedded, cropped, traced or used as pixel sources.

## Tool / Fallback Record

1. Image-generation candidate: rejected because it produced an unrelated project dashboard with incorrect content.
2. Adobe Express: direct standalone illustration generation unavailable for this task.
3. Canva revised import: design `DAHSv3GnJGo` imported technically, but validation returned one page and empty rich text. It is not canonical.
4. Controlled local production + PDF fallback: used for the revised review set.

This follows the rule that tool completion is not workflow completion and failed candidates are not promoted.

## Self-Corrections

- Rejected unrelated generated artwork before use.
- Rebuilt Sea/Rock back after initial table render looked like a card grid; full-bleed continuous sea retested PASS at 5x5, 5x6 and 6x6.
- Rebuilt digital real-size print test after the first A4 layout overlapped cards; final test uses two clean pages.
- Rebuilt Design System Board after title/content clipping was found during render QA.
- Rebuilt Visual QA PDF after right-column clipping was found.
- Reworked Kaptan Makamı so an empty chair + separate tricorn communicates transferable office rather than a permanent Captain character.

## Revised Binary Review Artifacts

- `FOULWAKE_v2.7_DESIGN_SYSTEM_BOARD_REVISED.pdf`
  - SHA-256: `88ac72a5c0d5b8ba02cbacc81717f4b8ff36db35f5e42728a8650f6e7dba50c7`
- `FOULWAKE_v2.7_REPRESENTATIVE_CARD_TEST_REVISED.pdf`
  - SHA-256: `3aaf06349109444dd2acfaa207b10c8d9c751799acdf2a524d52c488018c23a3`
- `FOULWAKE_v2.7_CARD_BACK_TEST_REVISED.pdf`
  - SHA-256: `426d83fe206dd7acec2cdbe3d2f6b13db6d5b817730bcb48c8881c076f130c8b`
- `FOULWAKE_v2.7_LINE_ONLY_TEST_REVISED.pdf`
  - SHA-256: `2331c53b6e86e08f19f14ef2964d2dd5b7dd86b4834be2a5bd8d3c8a2a3cbb2e`
- `FOULWAKE_v2.7_PRINT_TEST_REVISED.pdf`
  - SHA-256: `35e1695a6eefa8c0d6cefa535fb484e0626520e8eb54536c40fb39227599ccdf`
- `FOULWAKE_v2.7_TABLE_TEST_REVISED.pdf`
  - SHA-256: `255fd650fa290c76aec774bd71b4901c5ccb5f67ea69d3654be8dc2fa9221783`
- `FOULWAKE_v2.7_VISUAL_QA_REVISED.pdf`
  - SHA-256: `00b3ad6eb8c1e3bc891974ff274d3e8c3ae0e9c1e865505460b930667699e696`

All revised PDFs and hash records are archived under `/Oyun-GitHub/v2.7/exports/` in the user file library. GitHub binary PDF upload is not available in the current connector, so no binary GitHub upload is claimed.

## QA Result

- Reference Similarity QA: PASS
- Mechanic-Visual Consistency: PASS
- Line-only: PASS
- 2–3 second hierarchy: PASS
- Back secrecy: PASS
- Map table: PASS after self-correction
- Digital real-size geometry: PASS
- PDF render/preflight: PASS
- Physical print: PENDING
- Historical/period-object final production audit: MINOR / PENDING
- Canva editable-source QA: FAIL / NOT CANONICAL

## Overall

**MINOR ISSUE — USER REVIEW GATE**

The revised set is safe to show for a visual-direction decision. It is not safe to propagate to all 121 cards until explicit user approval. Final production art also requires a refinement/period-detail pass before lock.
