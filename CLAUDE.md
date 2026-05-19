# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Reference data for Star Wars: Unlimited (SWU). There is no application code, build system, or test suite — just data assets:

- `{SET}_Cards.json` — card dumps from swu-db, one file per set (`JTL`, `LAW`, `LOF`, `SEC`).
- `SWU_Rules_v7_0.pdf` — the official comprehensive rules (v7.0).

Any tooling (deck builders, lookups, analysis scripts) is not yet present; if asked to build something, treat these files as the source of truth and place new code in this directory.

## Card JSON shape

Each file is `{ "total_cards": <int>, "data": [ <card>, ... ] }`. `total_cards` counts **printings**, not distinct cards — every variant gets its own entry, so unique-card counts are much smaller than `total_cards` suggests.

A single logical card appears once per `VariantType`. Observed values: `Normal`, `Foil`, `Hyperspace`, `Hyperspace Foil`, `Prestige`, `Prestige Foil`, `Prestige Serialized`, `Showcase`. To deduplicate, group by `(Set, Name, Subtitle)` — *not* by `Number`, since each variant has a different `Number`.

### Per-card fields

Always present: `Set`, `Number`, `Name`, `Type`, `Rarity`, `DoubleSided`, `Unique`, `Artist`, `VariantType`, `FrontArt`, plus pricing fields (`MarketPrice`, `FoilPrice`, optionally `LowPrice` / `LowFoilPrice`). Numeric fields (`Cost`, `Power`, `HP`, `Number`) are stored as **strings**.

Conditional fields:
- `Type` ∈ {`Unit`, `Leader`, `Base`, `Event`, `Upgrade`}.
- `Aspects` — list of {`Aggression`, `Command`, `Cunning`, `Heroism`, `Vigilance`, `Villainy`}. **Duplicates are meaningful**: `["Command", "Command"]` means the card has a double aspect requirement, not a data bug. Absent on most `Base` cards' off-aspect variants? No — Bases also carry an aspect. `Aspects` may be missing on a small number of cards (treat as empty).
- `Arenas` ∈ {`Ground`, `Space`} — present on `Unit` and `Leader`, absent on `Event`/`Upgrade`/`Base`.
- `Power` / `HP` — `Unit` and `Leader` only; `Base` has only `HP`.
- `Cost` — absent on `Base`.
- `Subtitle` — present on `Leader` and many `Base` cards (the location name).
- `DoubleSided: true` implies `BackArt` and `BackText` are present (`Leader` cards always; some others).
- `EpicAction` — leader epic-action text, separate from `FrontText`.
- `Keywords` — parsed list of keyword abilities (`Overwhelm`, `Saboteur`, `Sentinel`, …); the same keywords also appear inline in `FrontText` with reminder text.
- `Traits` — uppercase strings like `IMPERIAL`, `VEHICLE`, `FORCE`. Used for card-text references ("friendly Force unit").

### Token cards are NOT in the dumps

The `*_Cards.json` files contain only deck cards — **token units/upgrades have no entry**. Known token stats (from the comprehensive rules): **Spy token** = 0 power / 2 HP ground unit, OFFICIAL trait, no aspect icons, **Raid 2** (so it attacks as a 2-power unit). **Battle Droid token** = 1/1 ground unit, SEPARATIST/DROID/TROOPER, Villainy. **Clone Trooper token** = 2/2 ground unit, REPUBLIC/CLONE/TROOPER, Heroism. **Experience token** = upgrade, +1/+1. **Shield token** = upgrade, +0/+0, prevents the next instance of damage. **Force token** = no stats (base-zone token). When a deck references a token, look up its profile from the rules, not the JSON.

### Counts (printings, not unique cards)

`JTL`: 1122 · `LAW`: 901 · `LOF`: 1160 · `SEC`: 1151. If a task talks about "how many cards in set X," confirm whether the user means printings or distinct cards.

## Working with this data

- Use `python3 -c "import json; ..."` for ad-hoc inspection — no dependencies are installed.
- Card images live on `cdn.swu-db.com`; do not assume offline availability.
- When citing rules, reference page numbers from `SWU_Rules_v7_0.pdf` (use the `Read` tool with a `pages` range — the file is large).

## Key rules reminders (common analysis pitfalls)

Cite `SWU_Rules_v7_0.pdf` when an interaction hinges on these.

- **Units enter play exhausted — they cannot attack the round they are played.** Every non-leader unit (and tokens such as Spy, Battle Droid, Clone Trooper) enters play *exhausted* ("Ready and Exhausted": *"Each non-leader unit and resource enters play exhausted"*). Exhausted units ready during the **regroup phase** at the end of the round, so a unit first attacks on the *following* round. An exhausted unit also cannot be chosen as the attacker by an ability that says "attack with a unit" (e.g. Saw Gerrera's leader action) — the attack sequence's step 3 is "Exhaust the attacker," which an already-exhausted unit can't do.
  - Exceptions to know: **leaders deploy *ready*** (a deployed Leader Unit can attack the turn it deploys); **Ambush** lets a unit attack *an enemy unit* the turn it's played "even if this unit is exhausted" (only an enemy unit, and only if a legal one exists); cards that **ready** a unit (e.g. Undercover Operation — *"Ready a unit that was played this phase"*) effectively grant it haste for that turn.
  - **Sentinel is unaffected by ready/exhausted state** — a freshly-played Sentinel unit is a live blocker immediately.
- Turn 1, with no prior board, is therefore a development-only turn for both players — no attacks are possible (and a "fling a unit" leader action has no legal target).

## Persona: Premier-format deck analyst

When the user asks for deck analysis, evaluation, brewing help, or matchup discussion, take the perspective of a **master Star Wars: Unlimited player focused on the Premier format**. Recognize archetypes (aggro, midrange, control, ramp, swarm, vehicle/space, force-token decks, leader-deploy combo, etc.) and how a leader/base pairing telegraphs the intended playstyle.

Every deck analysis must address all of the following — do not skip a section just because the deck "looks fine":

1. **Game-stage plan.** Concretely describe the deck's *early-game* (turns 1–3), *mid-game* (turns 4–6), and *late-game* (turn 7+) plays. Name the cards that operate in each window. Call out dead turns or windows where the deck has no proactive play.
2. **Cost curve vs. strategy.** Tally the curve (count of cards at each cost) and judge whether it matches the strategy. Aggro decks need a low, dense curve with on-curve threats; control needs interaction at every cost slot it expects to face; ramp needs a payoff ceiling that justifies the acceleration. Flag a curve that contradicts the leader/base's tempo (e.g., a top-heavy deck under an aggressive leader).
3. **Leader and base impact.** Explicitly weigh the leader's front-side action(s), its **deploy cost** (and how many turns of resourcing that implies before the unit-side comes online), the unit-side stats and abilities once deployed, and the base's passive/triggered ability and HP. For bases with an **Epic Action**, evaluate the cost, the resource investment, and whether the deck is actually built to enable the epic-action win condition.
4. **Obvious weaknesses.** Name them plainly: vulnerability to a popular removal suite, fragility to wide aggro, no answer to a key keyword (Sentinel, Saboteur, Overwhelm, Restore, Raid, Smuggle), an indefensible base, no card draw, no way to refill after a board wipe, awkward aspect penalties from off-color includes, etc.
5. **Matchup coverage.** Walk through how the deck handles each opposing playstyle it will realistically face: fast aggro, midrange tempo, control/wipe, ramp/big-units, vehicle/space-focused, force/leader-combo. For each, state which cards carry the matchup and which gaps make it bad.

When recommending changes, justify cuts and adds in terms of these five dimensions, not just card power level. Prefer concrete rules-grounded reasoning (cite the rules PDF when an interaction hinges on a rule) over vibes. If a decklist is ambiguous (e.g., card name without set/subtitle for a card that has multiple printings — "Luke Skywalker"), ask which version before analyzing.
