# swu-helper

Reference data and deck lists for **Star Wars: Unlimited** (SWU), focused on the Premier format. There is no application code here yet — just data assets used as a source of truth for analysis, brewing, and lookups.

## Contents

### Card data

One file per set, dumped from [swu-db](https://swu-db.com):

| File | Set | Printings |
| --- | --- | --- |
| `JTL_Cards.json` | Jump to Lightspeed | 1122 |
| `LAW_Cards.json` | A Lawless Time | 901 |
| `LOF_Cards.json` | Legends of the Force | 1160 |
| `SEC_Cards.json` | Secrets of Power | 1151 |

Each file is shaped as `{ "total_cards": <int>, "data": [ <card>, ... ] }`. **`total_cards` counts printings, not distinct cards** — every variant (`Normal`, `Foil`, `Hyperspace`, `Prestige`, `Showcase`, …) is a separate entry. To get unique cards, group by `(Set, Name, Subtitle)`, not by `Number`.

Common per-card fields: `Set`, `Number`, `Name`, `Type` (`Unit` / `Leader` / `Base` / `Event` / `Upgrade`), `Rarity`, `Aspects`, `Arenas`, `Cost`, `Power`, `HP`, `Keywords`, `Traits`, `FrontText`, `FrontArt`, plus pricing. Numeric fields are stored as strings. See `CLAUDE.md` for the full field-by-field breakdown, including conditional fields and gotchas (e.g. duplicate `Aspects` entries are intentional double-aspect requirements).

### Rules

- `SWU_Rules_v7_0.pdf` — official comprehensive rules, v7.0. Cite by page number when an interaction depends on a specific rule.

### Decks

Decks are stored as JSON with a flat shape:

```json
{
  "metadata": { "name": "...", "author": "..." },
  "leader":   { "id": "SEC_004", "count": 1 },
  "base":     { "id": "JTL_024", "count": 1 },
  "deck":     [ { "id": "LOF_111", "count": 3 }, ... ],
  "sideboard":[ { "id": "JTL_096", "count": 2 }, ... ]
}
```

`id` is `<SET>_<Number>` and resolves against the corresponding `*_Cards.json` file (matching against the `Normal` variant for that `(Set, Number)`).

Current decklists:

- `qui-gon-red.json` — Qui-Gon leader, draw/wipe build.
- `Sobeksobek_Seoul_PQ_Winner.json` — Seoul PQ-winning list.

## Working with the data

No build system, no installed dependencies. Use `python3 -c "import json; ..."` for ad-hoc inspection. Card images are served from `cdn.swu-db.com` and are not cached locally.

## Notes for Claude Code

`CLAUDE.md` contains the deck-analysis persona and the full data-shape reference Claude should follow when asked to analyze a list. If you're a human reading this, the highlights are:

- Group by `(Set, Name, Subtitle)` to dedupe variants.
- Leader **deploy** does not spend resources — the resource count is a threshold, not a payment.
- "When Played: If…" conditions check at play time, so they fail on turn 1 plays that require another unit on the board.
