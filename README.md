# swu-helper

Reference data for **Star Wars: Unlimited** (SWU), focused on the Premier format. There is no application code here yet — just data assets used as a source of truth for analysis, brewing, and lookups.

## Layout

```
swu-helper/
├── CLAUDE.md
├── README.md
├── cards/              # card databases — one {SET}_Cards.json per set
├── rules/              # comprehensive rules PDF
└── decks/              # one subdirectory per deck being worked on
    └── <deck-name>/    # that deck's decklist file(s) and anything else specific to it
```

## Contents

### Card data — `cards/`

One file per set, dumped from [swu-db](https://swu-db.com):

| File (in `cards/`) | Set | Printings |
| --- | --- | --- |
| `ASH_Cards.json` | Ashes of the Empire | 925 |
| `HMW_Cards.json` | Homeworlds | 954 |
| `IBH_Cards.json` | Intro Battle: Hoth | 104 |
| `JTL_Cards.json` | Jump to Lightspeed | 1122 |
| `LAW_Cards.json` | A Lawless Time | 901 |
| `LOF_Cards.json` | Legends of the Force | 1160 |
| `SEC_Cards.json` | Secrets of Power | 1151 |

Each file is shaped as `{ "total_cards": <int>, "data": [ <card>, ... ] }`. **`total_cards` counts printings, not distinct cards** — every variant (`Normal`, `Foil`, `Hyperspace`, `Prestige`, `Showcase`, …) is a separate entry. To get unique cards, group by `(Set, Name, Subtitle)`, not by `Number`.

Common per-card fields: `Set`, `Number`, `Name`, `Type` (`Unit` / `Leader` / `Base` / `Event` / `Upgrade`; `HMW` also has `Token Unit` / `Token Upgrade`), `Rarity`, `Aspects`, `Arenas`, `Cost`, `Power`, `HP`, `Keywords`, `Traits`, `FrontText`, `FrontArt`, plus pricing. Numeric fields are stored as strings. See `CLAUDE.md` for the full field-by-field breakdown, including conditional fields and gotchas (e.g. duplicate `Aspects` entries are intentional double-aspect requirements).

Token cards are generally **not** in the dumps. `HMW_Cards.json` is the exception — it includes its own Beast, Shield, and Weakness tokens (numbered `T01`–`T10`, so `Number` is not always numeric there). `CLAUDE.md` has a section on the other ways the Homeworlds dump differs: variant names, extra `cid` / `tcgplayerId` fields, planet-trait bases, the Fortify keyword.

### Rules — `rules/`

- `rules/SWU_Rules_v9_0.pdf` — official comprehensive rules, **v9.0 (10/9/26), the current version**. Cite by rule number and page when an interaction depends on a specific rule.

v9.0 adds the Fortify keyword and the Weakness and Beast tokens, and changes several general rules (modifier order, searching, simultaneous choices, excess damage, exchanging control, leader and token replacement effects). `CLAUDE.md` lists every change from v8.0 with rule and page numbers.

### Decks — `decks/`

Each deck being worked on gets its own subdirectory, `decks/<deck-name>/`, holding that deck's decklist file(s) and anything else specific to it. Deck files do not go directly in `decks/`.

No decklists are checked in yet. The expected decklist format is JSON with a flat shape:

```json
{
  "metadata": { "name": "...", "author": "..." },
  "leader":   { "id": "SEC_004", "count": 1 },
  "base":     { "id": "JTL_024", "count": 1 },
  "deck":     [ { "id": "LOF_111", "count": 3 }, ... ],
  "sideboard":[ { "id": "JTL_096", "count": 2 }, ... ]
}
```

`id` is `<SET>_<Number>` and resolves against the corresponding `cards/<SET>_Cards.json` file. It is usually the `Normal` variant's number, though a list may point at another printing (e.g. a Showcase leader).

## Working with the data

No build system, no installed dependencies. Use `python3 -c "import json; ..."` for ad-hoc inspection. `pdftotext -layout` is handy for searching the rules PDF. Card images are served from `cdn.swu-db.com` and are not cached locally.

## Notes for Claude Code

`CLAUDE.md` contains the deck-analysis persona, the full data-shape reference, the Homeworlds notes, and the v9.0 rules changelog Claude should follow when asked to analyze a list. If you're a human reading this, the highlights are:

- Group by `(Set, Name, Subtitle)` to dedupe variants.
- Leader **deploy** does not spend resources — the resource count is a threshold, not a payment.
- "When Played: If…" conditions check at play time, so they fail on turn 1 plays that require another unit on the board.
- Units enter play exhausted and can't attack the round they're played; leaders deploy ready.
