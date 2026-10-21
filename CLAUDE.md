# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Reference data for Star Wars: Unlimited (SWU). There is no application code, build system, or test suite — just data assets:

- `cards/{SET}_Cards.json` — card dumps from swu-db, one file per set. Set codes: `ASH` = **Ashes of the Empire**, `HMW` = **Homeworlds**, `IBH` = **Intro Battle: Hoth**, `JTL` = **Jump to Lightspeed**, `LAW` = **A Lawless Time**, `LOF` = **Legends of the Force**, `SEC` = **Secrets of Power**. See "Homeworlds (`HMW`) specifics" below for where the `HMW` dump differs from the older ones; `IBH` is a small two-deck product whose dump is laid out differently — see "Counts" below.
- `rules/SWU_Rules_v9_0.pdf` — the official comprehensive rules, **v9.0 (10/9/26) — the current version; cite this one**.

- `swudb_collection.csv` — the user's card collection (export from swu-db), columns `Set,CardNumber,Count,IsFoil,Stamp`. See "The user's collection" below.

Any tooling (deck builders, lookups, analysis scripts) is not yet present; if asked to build something, treat these files as the source of truth and place new code in the repository root, not inside the data directories below.

## Directory layout

```
swu-helper/
├── CLAUDE.md
├── README.md
├── cards/              # card databases — one {SET}_Cards.json per set
├── rules/              # comprehensive rules PDF(s)
└── decks/              # one subdirectory per deck being worked on
    └── <deck-name>/    # that deck's decklist file(s) and anything else specific to it
```

- **`cards/`** — card dumps only. A new set's dump goes here as `{SET}_Cards.json`. Elsewhere in this file a bare `{SET}_Cards.json` name means `cards/{SET}_Cards.json`.
- **`rules/`** — the rules PDF only. A new rules version goes here; a bare `SWU_Rules_v9_0.pdf` means `rules/SWU_Rules_v9_0.pdf`.
- **`decks/`** — never put deck files directly in `decks/`. Each deck gets its own subdirectory (`decks/<deck-name>/`), and every file for that deck — decklist JSON, later revisions, notes — lives inside it. When starting a new deck, create its subdirectory first; when revising an existing deck, work inside its existing subdirectory rather than creating a new one. Each strategy doc (`STRATEGY-vN.md`) must be complete on its own, written for a new player who has only that file. Don't describe it as changes from an earlier version ("vN is vN-1 with…"), and don't send the reader to earlier docs for analysis or piloting advice. Carry forward everything that still applies, rewritten for the current list, and drop anything about cards no longer in the deck. A deck `id` of `<SET>_<Number>` resolves against `cards/<SET>_Cards.json`.

## Card JSON shape

Each file is `{ "total_cards": <int>, "data": [ <card>, ... ] }`. `total_cards` counts **printings**, not distinct cards — every variant gets its own entry, so unique-card counts are much smaller than `total_cards` suggests.

A single logical card appears once per `VariantType`. Observed values: `Normal`, `Foil`, `Hyperspace`, `Hyperspace Foil`, `Prestige`, `Prestige Foil`, `Prestige Serialized`, `Showcase`. `ASH` and `HMW` have no plain `Foil` variant, and `HMW` names its serialized printing `Serialized` (not `Prestige Serialized`). To deduplicate, group by `(Set, Name, Subtitle)` — *not* by `Number`, since each variant has a different `Number`.

### Per-card fields

Always present: `Set`, `Number`, `Name`, `Type`, `Rarity`, `DoubleSided`, `Unique`, `Artist`, `VariantType`, `FrontArt`, plus pricing fields (`MarketPrice`, `FoilPrice`, optionally `LowPrice` / `LowFoilPrice`). Numeric fields (`Cost`, `Power`, `HP`, `Number`) are stored as **strings**.

Conditional fields:
- `Type` ∈ {`Unit`, `Leader`, `Base`, `Event`, `Upgrade`}. `HMW` adds `Token Unit` and `Token Upgrade`.
- `Aspects` — list of {`Aggression`, `Command`, `Cunning`, `Heroism`, `Vigilance`, `Villainy`}. **Duplicates are meaningful**: `["Command", "Command"]` means the card has a double aspect requirement, not a data bug. Absent on most `Base` cards' off-aspect variants? No — Bases also carry an aspect. `Aspects` may be missing on a small number of cards (treat as empty).
- `Arenas` ∈ {`Ground`, `Space`} — present on `Unit` and `Leader`, absent on `Event`/`Upgrade`/`Base`.
- `Power` / `HP` — `Unit` and `Leader` only; `Base` has only `HP`.
- `Cost` — absent on `Base`.
- `Subtitle` — present on `Leader` and many `Base` cards (the location name).
- `DoubleSided: true` implies `BackArt` and `BackText` are present (`Leader` cards always; some others).
- `EpicAction` — leader epic-action text, separate from `FrontText`.
- `Keywords` — parsed list of keyword abilities (`Overwhelm`, `Saboteur`, `Sentinel`, …); the same keywords also appear inline in `FrontText` with reminder text.
- `Traits` — uppercase strings like `IMPERIAL`, `VEHICLE`, `FORCE`. Used for card-text references ("friendly Force unit").

### Token cards are NOT in the dumps (except `HMW`)

The `ASH`/`IBH`/`JTL`/`LAW`/`LOF`/`SEC` files contain only deck cards — **token units/upgrades have no entry**. `HMW_Cards.json` is the exception: it carries entries for its own three tokens (Beast, Shield, Weakness — see the Homeworlds section), but still not for tokens from other sets. Known token stats (from the comprehensive rules): **Spy token** = 0 power / 2 HP ground unit, OFFICIAL trait, no aspect icons, **Raid 2** (so it attacks as a 2-power unit). **Battle Droid token** = 1/1 ground unit, SEPARATIST/DROID/TROOPER, Villainy. **Clone Trooper token** = 2/2 ground unit, REPUBLIC/CLONE/TROOPER, Heroism. **Experience token** = upgrade, +1/+1. **Shield token** = upgrade, +0/+0, prevents the next instance of damage. **Force token** = no stats (base-zone token). Added in rules v9.0 (3.7.16–17, p. 18): **Weakness token** = upgrade, CONDITION trait, -1/-1, stacks per token. **Beast token** = 3/3 **ground** unit, CREATURE trait, no aspect icons. When a deck references a token, look up its profile from the rules, not the JSON.

### Counts (printings, not unique cards)

`ASH`: 925 (264 distinct) · `HMW`: 954 (275 distinct by `(Set, Name, Subtitle)`: 272 deck cards + 3 tokens) · `IBH`: 104 (51 distinct) · `JTL`: 1122 · `LAW`: 901 · `LOF`: 1160 · `SEC`: 1151. If a task talks about "how many cards in set X," confirm whether the user means printings or distinct cards.

- **`ASH`** (Ashes of the Empire) — a full-size set: 179 Units, 34 Events, 25 Upgrades, 18 Leaders, 8 Bases. Variants are `Normal`, `Hyperspace`, `Hyperspace Foil`, `Prestige`, `Prestige Foil`, `Prestige Serialized`, `Showcase` (no plain `Foil`), and `VariantType == "Normal"` gives exactly one row per card. Like `HMW` it carries `cid` and `tcgplayerId`. No token entries.
- **`IBH`** (Intro Battle: Hoth) — two preconstructed decks (leaders Leia Organa and Darth Vader, bases Echo Caverns and Forward Command Post). Every entry is `VariantType: "Normal"` and `Rarity: "Special"`, but **each physical copy in a decklist has its own entry and `Number`** (Blizzard Force AT-ST is `70`, `89`, and `103`), so filtering on `Normal` does *not* dedupe — group by `(Set, Name, Subtitle)`. `Number` is unpadded here (`"2"`, not `"002"`). No `cid`/`tcgplayerId`, no token entries.

## Homeworlds (`HMW`) specifics

`HMW_Cards.json` — 954 printings. Distinct cards: 180 Units, 31 Events, 27 Upgrades, 18 Leaders, 16 Bases, plus 3 tokens. Themed around four planets: **Endor, Kashyyyk, Naboo, Tatooine**.

- **Extra fields.** Every entry has `cid`; all have `tcgplayerId` except Bases and tokens. `ASH` has both too; neither exists in the `IBH`/`JTL`/`LAW`/`LOF`/`SEC` dumps. `Traits` is present on every entry, including Bases.
- **Variants.** `Normal`, `Hyperspace`, `Hyperspace Foil`, `Prestige`, `Prestige Foil`, `Serialized`, `Showcase`. Filter on `VariantType == "Normal"` for one row per card — except the Beast token, which has three `Normal` printings (`T03`–`T05`, different art), so still dedupe by name.
- **Tokens are in the file**, with `Number` values `T01`–`T10` — so `Number` is not always numeric in this set; don't `int()` it blindly. Deck cards run `001`–`944`.
  - **Beast token** (`Token Unit`) = 3/3, CREATURE trait, `Aspects: []`, no text. The entry has **no `Arenas` field** — it is a ground unit per rules 3.7.17.
  - **Weakness token** (`Token Upgrade`) = -1/-1, CONDITION trait, no text. Given to *enemy* units as a debuff; the most-referenced token in the set.
  - **Shield token** (`Token Upgrade`) = +0/+0, ARMOR trait, usual damage-prevention text.
  - Token upgrades have no `Aspects` key; all tokens have `Cost: "0"`.
- **Bases.** All 16 are Common, 30 HP, single-aspect (four each in Vigilance, Command, Aggression, Cunning — no Heroism/Villainy bases), with empty `FrontText` and no Epic Action. Their only distinguishing feature is a **planet trait** in `Traits` (`ENDOR`, `KASHYYYK`, `NABOO`, `TATOOINE`) and the matching `Subtitle`. Each aspect has one base per planet.
- **Planet-base payoffs.** Cards check the base's planet — *"If you control an Endor base…"*, *"While you control … a Naboo base…"*. Base choice is therefore a deckbuilding decision beyond aspect: in deck analysis, check that the chosen base's planet actually turns on the deck's payoff cards. 17 cards do this; some accept a tribal alternative instead (*"another Ewok unit or an Endor base"* — likewise Gungan/Naboo, Wookiee/Kashyyyk, Tusken/Tatooine).
- **Fortify** (new keyword, upgrades only): *"Attach this to your base, not a unit."* 15 upgrades have it, 14 of them FORTIFICATION-trait; they give the base an ability or a defeat-this-upgrade action. They don't sit on a unit, so unit removal doesn't strip them — but upgrade removal does. Rules 7.5.21 (pp. 34–35): Fortify = the attachment restriction "Attach to your base"; your own base only, never a unit or an enemy base; ignores unit-based play restrictions, so it is playable onto an empty board.
- **Other keywords present:** Raid, Restore, Overwhelm, Sentinel, Grit, Hidden, Ambush, Shielded, Saboteur. **Hidden** = *"This unit can't be attacked if it was played this phase."*
- **Three-aspect cards.** Six units (Darth Vader, Hunter, Ima-Gun Di, Mae, Third Sister, Yoda) list three *different* aspects — two colours plus Heroism/Villainy. This is not the duplicate-aspect case; a leader + base supplies at most three aspect icons, so these fit penalty-free in only one exact combination.
- **Aspectless cards.** Five deck cards have `Aspects: []` (Friendly Eopie, Offworld Jawa, Wild Space Wanderer, Landing Pad, Growth) — playable in any deck with no penalty.
- **Grand Moff Tarkin // The Death Star** (`HMW_004`) is the one leader whose `Name` and `Subtitle` both contain `" // "` (front // deployed side). Match on the full string or a prefix when looking it up. It deploys at 9 resources as a Space-arena unit.

## Rules v9.0: changes from v8.0

Every addition/change in v9.0 (red text in the PDF, cross-checked against a full text diff of v8.0). Page numbers are v9.0 pages.

**New keyword and tokens (Homeworlds support)**
- **Fortify** — 7.5.21 (pp. 34–35), with a pointer at 3.6.1.a (p. 16). Same effect as the attachment restriction "Attach to your base." Fortify upgrades attach only to *your* base — not units, not enemy bases — and ignore unit-based restrictions on playing upgrades (such as needing an eligible unit in play). They may grant abilities to the base, and can be defeated by any ability that defeats upgrades.
- **Weakness token** — 3.7.16 (p. 18). Token upgrade, Condition trait, attached unit gets -1 power and -1 HP. Multiple Weakness tokens stack.
- **Beast token** — 3.7.17 (p. 18). Token unit: ground, Creature trait, no aspect icons, 3 power / 3 HP.

**New rules**
- **Exchange control** — 1.5 "take control" entries, new (e) (p. 5). The player chooses one card they control and one an opponent controls, and each takes control of the other's card. If either side has no eligible card, **no exchange happens at all**. (Later entries re-lettered f, g.)
- **Excess damage destination** — 1.9.11.a (p. 8). If an effect doesn't say where excess damage goes, it is dealt to the same unit/base taking the rest. If it does say, the target takes only enough to defeat it and the excess goes where indicated.
- **Simultaneous choices** — 7.1.4.a (p. 29). Choices about **hidden** information (each player discards a card) are made independently, then resolved simultaneously. Choices about **open** information (each player defeats a friendly unit) are made **sequentially**, then resolved simultaneously — so the later chooser sees the earlier choice.
- **"When Played" used by another ability** — 7.6.13.d (p. 36). "This unit/upgrade" refers to the card the When Played ability is printed on, not the card using it.
- **"When Defeated" used by another ability** — next entry, also (d) (p. 36). Same referent rule. If the source unit was defeated in the current action, Last Known Information is used; if it was defeated earlier, use its **printed** attributes and treat any condition about *how* it was defeated as false.
- **"Replace" an ability** — 8.14.4 (p. 42). The card loses the replaced ability and gains the new one for the stated duration.

**Changed rules**
- **Modifier order** — 8.15.2 (p. 42). Now "additive modifiers, then subtractive modifiers, then multiplicative modifiers." v8.0 only said increases before decreases; multiplicative modifiers are new and apply last.
- **Search / fail-to-find** — 8.26.1 (p. 45). You may choose to find nothing **only if the search specifies an attribute** of the card to find. v8.0 allowed this on any search.
- **Upgrade with no eligible unit** — 6.2 step 5.b (p. 25). The upgrade doesn't enter play and goes to the discard pile (cost already paid).
- **Upgrades falling off** — the 1.5 "defeated" entry (d) (p. 5) now says an upgrade is defeated *simultaneously* when its unit leaves play. The matching game-state check in 1.16 ("If an upgrade is no longer attached to a unit, that upgrade is defeated") was **deleted**, and the checks after it re-lettered (p. 11) — consistent with Fortify upgrades sitting on bases.
- **Leaders can't move or change control** — 3.4.6 (p. 16). Now covers leader *upgrades* as well as leader units, and being defeated instead is explicitly a replacement effect.
- **Non-leader units made into leader units** — 3.4.7 (p. 16). Broadened from "some upgrades" to any ability. Such a unit counts as a leader unit for "leader"/"non-leader" text but does not follow 3.4.1–3.4.6: it gives no aspect icons, it **can** change control or move to an out-of-play zone, and it goes to the discard pile when defeated.
- **Tokens leaving play** — 3.7.3 (p. 18). Being set aside instead is now explicitly a replacement effect, and still counts as leaving play — so "If you do" clauses still pay off (the example: bouncing a token with Anakin Skywalker, LAW #88, still heals 2).
- **Replacement effects** — replacement-effects entry (f) in 7.7 (p. 38). A replacement effect can't replace itself *or replace the same initial condition multiple times*. Example now uses Ty Yorrick (HMW #185): Open Fire for 4 deals 5, not more.
- **"For each" / "for every"** — 8.34 (p. 47). Heading and text now cover both phrasings. Procedure spelled out: determine how many times the effect applies, choose how each instance applies, then resolve all simultaneously.

**Wording only (no gameplay change)**
- "Leader side", "Leader Unit", "Leader Upgrade" are now lowercase throughout.
- Raid's bonus is lost when the attack *ends* (p. 32); punctuation fix in Saboteur (p. 32); grammar fixes in 6.3 combat damage (p. 26).
- The lasting-effect examples no longer name Surprise Strike / Wolffe.
- Contents page numbers updated: 1.8 Cost p. 7, 1.16 Game State p. 11, 7.6 Triggered Abilities p. 35, 7.7 Effects p. 37.

## The user's collection

`swudb_collection.csv` lists every card the user owns. When building or revising a deck, only use cards they own in the needed quantity. Check with `python3 check_owned.py decks/<deck>/<file>.json`.

- **Premier-legal sets are only `ASH`, `HMW`, `JTL`, `LAW`, `LOF`, `SEC`.** The CSV also contains non-legal sets (`SOR`, `SHD`, `TWI`, `IBH`, promo codes like `SECP`, `TWIOP`); ignore them for Premier decks.
- **One row per printing.** `CardNumber` is the variant's `Number` (Normal, Hyperspace, foil, etc. each have their own). To get how many copies of a card are owned, map each row to `(Set, Name, Subtitle)` via `cards/{SET}_Cards.json` and sum `Count` across printings.
- A few `CardNumber` values have a letter suffix (`SEC 571m`). Strip it and count the row as that printing.

## Working with this data

- Use `python3 -c "import json; ..."` for ad-hoc inspection — no dependencies are installed.
- Card images live on `cdn.swu-db.com`; do not assume offline availability.
- Run commands from the repository root and use the directory-qualified paths (`cards/HMW_Cards.json`, `rules/SWU_Rules_v9_0.pdf`, `decks/<deck-name>/...`).
- When citing rules, reference rule numbers and page numbers from `rules/SWU_Rules_v9_0.pdf` (v9.0; 56 pages — use the `Read` tool with a `pages` range, or `pdftotext -layout` for searching). Page numbers shifted by one in places between v8.0 and v9.0, so don't reuse v8.0 page cites.

## Key rules reminders (common analysis pitfalls)

Cite the v9.0 rules (`rules/SWU_Rules_v9_0.pdf`) when an interaction hinges on these. Nothing in this section changed in v9.0.

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
