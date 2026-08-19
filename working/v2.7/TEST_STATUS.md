# FOULWAKE v2.7 — VISUAL TEST STATUS

Status: DRAFT / NOT LOCKED
Date: 2026-08-19
Branch: `v2.7-design`
Canonical baseline: `v2.6 STABLE / LOCKED`

## Gate Summary

| Gate | Result | Notes |
|---|---|---|
| GitHub state resolution | PASS | Existing `working/v2.7` and `v2.7-design` reused; no v2.8 workspace created. |
| Story / World audit | PASS | 1721, Arden, San Cordelio, Saint Verena, Veyr, Siyah Mühür and Gusto ambiguity checked. |
| Design system board | PASS | Application-independent rules encoded and review PDF generated. |
| Canva candidate | FAIL as canonical candidate | Canva design `DAHSvmAWxYk` was generated but content/structure QA did not match the required FOULWAKE board. It is experimental only and not source-of-truth. |
| Representative five-card visual gate | MINOR ISSUE | Exact mechanics used; prototype illustration crops are not final production-resolution art and title banner is still more geometric/clean than the target hand-ink feeling. |
| Line-only test | PASS | Main scene/hierarchy remain readable after color removal. |
| 2–3 second hierarchy test | PASS | Title and primary mechanics occupy consistent predictable zones. |
| Power / Rotten Provisions back secrecy | PASS | Exact same binary back asset is reused. |
| Sea / Rock back secrecy | PASS | Exact same binary back asset is reused. |
| Back text / FOULWAKE leakage | PASS | Back assets contain no text or FOULWAKE mark. |
| Real-size print test | MINOR ISSUE | 100% digital print sheet generated and rendered; no physical printer/real-light paper test was possible in this environment. |
| 5x5 map table test | PASS | Digital rendered table simulation completed. |
| 5x6 map table test | PASS | Digital rendered table simulation completed. |
| 6x6 map table test | PASS | Digital rendered table simulation completed. |
| PDF open/render/preflight | PASS | All review PDFs open and render; Turkish glyph issue discovered during QA and corrected by embedding DejaVu fonts. |
| Full 121-card propagation | BLOCKED | Must remain blocked until user review gate is accepted. |
| Rulebook visual redesign | BLOCKED | Deferred until the card visual gate is accepted. |

## Representative Five-Card Set

1. `KAR-01 Uzakgören`
2. `GUC-01A Can Simidi`
3. `ERZ-01 Çürümüş Erzak`
4. `HAR-AD-30 Bir Bulutun Kişisel Meselesi`
5. `SET-KP-01 Kaptan Makamı`

## Important Findings

### 1. Canva generation cannot be trusted without content QA
The first generated board introduced unrelated generic copy and omitted required FOULWAKE constraints. It was therefore rejected as canonical output. The process correctly fell back to controlled review PDFs instead of propagating a bad design.

### 2. Prototype art is good enough for layout testing, not final print art
The current representative illustrations are suitable for hierarchy, humor, composition and table-language review, but their source resolution is prototype-level. Final production art must be regenerated/rebuilt at proper output resolution before final preflight.

### 3. Back secrecy logic works at asset level
`Power` and `Çürümüş Erzak` use the same back asset. `Sea` and `Rock` use the same back asset. This prevents the visual system itself from leaking those hidden distinctions.

### 4. Physical print remains an external gate
The digital file contains real-size card geometry, bleed and trim guidance. A physical 100% print under real lighting still needs to be performed before final lock.

## Overall Result

**MINOR ISSUE — USER REVIEW GATE**

No MAJOR ISSUE or FAIL remains in the digital review set, but the design must not propagate to all 121 cards yet. The next safe action is user review of the generated board, representative card set, backs, print sheet, table simulations and QA report.
