# FOULWAKE v2.7 — DESIGN SYNC STATUS

Status: DRAFT / NOT LOCKED
Branch: `v2.7-design`
Mechanical source: `v2.6 STABLE / LOCKED` (mechanical baseline `v2.5`)
Figma file: `FOULWAKE v2.7 DESIGN SYSTEM`
Figma key: `LOJtIBKKfN2KVGx8wD6rU9`

## Canonical split

- GitHub = game content, mechanics, card IDs/names/effects/counts, version history, tests, release artifacts.
- Figma = visual source of truth for card layouts, illustrations, backs, typography, color, bleed/safe area, rulebook layout and print tests.
- Mechanical/text changes are made in GitHub first, then synced to Figma.
- Pure visual changes are made in Figma first, then exported artifacts are returned to GitHub.

## Current Figma structure

Pages:
- `00 — DESIGN SYSTEM`
- `01 — CARDS`
- `02 — RULEBOOK / TESTS`

Design-system frames already present:
- `00 — DESIGN RULES`
- `01 — COLOR / TYPE / VARIABLES`
- `02 — CORE COMPONENTS`

Master components already present:
- `CARD / MASTER / Character` — 70x120 mm trim
- `CARD / MASTER / Power` — 63.5x88.9 mm trim
- `CARD / MASTER / Loyalty` — 63.5x88.9 mm trim
- `CARD / MASTER / Map` — 70x70 mm trim
- `CARD / MASTER / Support`

## Canonical physical card inventory

- 20 Character
- 30 Power
- 1 Rotten Provisions / Çürümüş Erzak
- 15 Loyalty
- 52 Map
- 3 Support
- Total: 121 physical cards

Source data is read from the v2.6 release package and its locked mechanical baseline, not invented in Figma.

## v2.7 visual rules already accepted

- No `FOULWAKE` text on cards.
- No text on card backs.
- Sea + Rock share one back in the v2.7 visual draft.
- Sea/Rock back has no compass, ship, anchor, rock, island, lighthouse, or other identifying central object.
- Island backs are identical within the Island group.
- Lighthouse backs are identical within the Lighthouse group.
- Rotten Provisions must be physically indistinguishable from Power cards and share the same back.
- Character cards: 70x120 mm.
- Map cards: 70x70 mm.
- Power/Loyalty/other hand cards: 63.5x88.9 mm.
- Default bleed: 3 mm; safe area: 4–5 mm.
- Art direction: LINE > COLOR > TEXTURE; roughly 70/20/10.
- Visual tone: adult maritime caricature; serious world, absurd people; humor must not erase tension.
- Title banner/flama treatment from the approved Captain reference may be used as a design motif, but not copied literally.

## Phase 0 discovery result

Figma scan confirmed:
- 3 pages exist.
- 5 master card components exist at real physical ratios.
- No local variables currently exist.
- No local text styles currently exist.

Therefore the next proper Figma step is Foundations before further component refinement:
1. create color variables,
2. create spacing/radius/print variables where useful,
3. create text styles,
4. bind master components to those tokens,
5. create and validate a small representative review set,
6. only then propagate the visual system to all 121 cards.

## Current blocker

The authenticated Figma account is on Starter / View and the Figma MCP monthly tool-call quota has been reached during Phase 0 library discovery.

No visual work will be silently moved to another generator while this project is under the user-requested Figma-first workflow. GitHub preparation may continue, but Figma mutations must resume only when Figma MCP access is available again.

## Next representative review set when Figma access resumes

- `KAR-01 Uzakgören` — Character front, tests character portrait hierarchy and title flama.
- `GUC-01A Can Simidi` — Power front, tests poker-card readability and stronger visual joke potential.
- `ERZ-01 Çürümüş Erzak` — must match Power physically/back-wise while front remains distinctive.
- `HAR-AD-30 Bir Bulutun Kişisel Meselesi` — Map front, tests 70x70 event readability and dark humor.
- `SET-KP-01 Kaptan Makamı` — Support card, tests Captain visual identity without making Captain a permanent character card.

After these five pass at real size, propagate the system across the full card set and rulebook.
