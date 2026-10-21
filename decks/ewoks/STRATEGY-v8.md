# Wicket Ewok Swarm (v8) — analysis and pilot guide

Decklist: `ewoks-v8.json` (leader `HMW_014` Wicket, base `HMW_023` Bright Tree Village).

v8 is v6 rebuilt around a second list of missing cards. Like v7, it is a ground aggro deck with a chip-damage backup: cheap Ewoks that can't be attacked the turn they land, a Wicket draw every round, and Cloud-Rider Veteran and Red Squadron Y-Wing damaging the base past blockers. It aims to win on turns 6–8. It has not been playtested. The percentages are calculated. Most of the piloting advice comes from the v7 games (see `STRATEGY-v7.md`), because the two lists share 43 of 50 cards.

Rule references are to `rules/SWU_Rules_v9_0.pdf` (v9.0).

## What changed from v6

Twelve slots changed. The seven missing copies were each swapped for a card at a similar cost doing a similar job. Two more changes came from the v7 games: Lifetree Caravan was cut for V-19 Skirmisher, and two Village Tender for Turning the Tide.

| Out | In | Why |
|---|---|---|
| 2 Chief Chirpa | 2 Champions of Endor | 2-cost Ewok for a 2-cost Ewok. Keeps the Ewok count for Teebo and Loyalist. |
| 2 Beast Lair, 1 Reckless Sacrifice | 3 Cloud-Rider Veteran | Beast Lair was the grind engine that ignores sweepers. Cloud-Rider is the pressure that ignores Sentinels, and was the best attacker in the v7 games. |
| 2 Luminara Unduli | 2 Relentless Hunters | The only cards above 3 cost. Saboteur replaces Luminara as the answer to Sentinel walls. |
| 3 Lifetree Caravan | 3 V-19 Skirmisher | Not a missing card. The v7 games found Caravan never worth playing, and space was the worst matchup. V-19 is a 3/3 space unit that gains Sentinel while you control 3 or more units. |
| 2 Village Tender | 2 Turning the Tide | Not a missing card. Tender was the weakest slot, and the deck had one answer to a large unit. Turning the Tide deals 1 damage per friendly unit to any unit, ground or space. |

Sideboard: unchanged from v6.

**Compared with v7:** −1 Champions of Endor, −1 Defenders of the Forest, −3 Lifetree Caravan and −2 Village Tender; +1 Teebo, +1 Logray, +3 V-19 Skirmisher and +2 Turning the Tide.

## Analysis

1. **Game-stage plan**
   - **Early (turns 1–3):** 32 units cost 2 or less, so you have a turn-1 play 99.9% of the time and a 1-drop 79% of the time. Teebo is in the opening six 32% of the time (23% in v7). Wicket deploys turn 3.
   - **Mid (turns 4–6):** two or three cards a turn. Clan Wren Loyalist refills; Ewok Archers, Logray, Reckless Sacrifice and Turning the Tide clear blockers; Cloud-Rider and Y-Wing chip the base every round.
   - **Late (turn 7+):** almost nothing. Two Relentless Hunters are the only cards above 3 cost. Nightfall is the finisher. Losing Luminara and Beast Lair cost v6's late-game plan, and nothing here replaces it.
2. **Curve:** 11 / 26 / 11 / 2 at costs 1–4, average 2.08. It fits the plan. With nothing above 4, stopping at 4–5 resources is right. Turning the Tide moved two slots from 1 to 3; V-19 replaced Caravan at the same cost.
3. **Leader and base:** 41 of 43 units cost 3 or less, so deployed Wicket's on-attack draw and Leia's heal are almost always live. Plenty of 1-drops can attack a 2-cost unit for the leader-side draw. The Endor base powers 9 cards (Troublemaker, Adamant Ewoks, Nightfall). The base has no ability and no Epic Action. It is there for its planet.
4. **Weaknesses**
   - **Almost no Sentinel:** V-19 guards the space arena only (7.5.11, p. 32), and only while you control 3 or more units. On the ground you can only race. Leia and Village Tender heal a little.
   - **Space is better but not solved:** six space units (3 Y-Wing, 3 V-19). V-19 can block a pilot-stacked ship, but at 3 HP it dies doing it. Reckless Sacrifice and Turning the Tide are the only cards that remove one, and Turning the Tide needs four or five units out to kill it.
   - **Sweepers:** most units have 3 HP or less. Without Beast Lair, the only recovery is Wicket's draw and Loyalist. Turning the Tide is weak right after a sweeper, because it counts your units.
   - **No late game:** if the game reaches turn 8 or 9 on an even board, the opponent's cards are better than yours.
   - **Thin tribal payoff:** 24 Ewoks but only one Chief Chirpa. The payoff is now Teebo's Hidden (three copies) and Loyalist's search.
   - **Duplicate uniques:** 14 slots are unique (Wicket, Leia, Teebo, Chirpa, Logray, Benthic). A second copy in play is defeated (1.16.b, p. 11). Spares should be resourced or fed to Reckless Sacrifice, because Beast Lair is no longer there to use them.
5. **Matchups**
   - **Fast aggro: even.** Hidden plus three Logray punish decks that attack your units. You lose a race to anything faster. Sideboard in Collateral Damage and Defenders of the Forest.
   - **Midrange: even.** Cloud-Rider and Hunters get past Sentinels like Tarfful and Koska. Hold Wicket and attack up for the leader-side draw. Their cards outclass yours after turn 8.
   - **Control / sweepers: slightly unfavourable.** Losing Beast Lair hurts most here. Play only about four units at a time, hold two, and let Cloud-Rider and Y-Wing keep the clock going.
   - **Ramp / big units: favourable.** You are well ahead by turn 5. Reckless Sacrifice with a 1-drop deals 5 to their first big threat, Turning the Tide handles the second, and Archers or 1-drops attacking up draw cards.
   - **Space: slightly unfavourable** (unfavourable in v7). V-19 gives you a space blocker by turn 2–3 and makes the opponent attack it before your Y-Wings. Turning the Tide can kill a pilot-stacked ship from a wide board. Sideboard in Wild Space Wanderer and Collateral Damage. A pilot-stacked ship can still out-race what V-19 absorbs.
   - **Leader-combo / Force: even.** You can kill a deployed leader with a 1-drop discarded to Reckless Sacrifice, through Hunters' Saboteur, or with Turning the Tide. Otherwise race it.

## How to pilot it

v7's piloting section (`STRATEGY-v7.md`) applies unchanged except for the points below.

- **Teebo:** with three copies you will see him most games. Play him first on turn 1 or 2 so every later Ewok lands with Hidden. With him out, deploying Wicket on turn 3 is safe (7.5.18, p. 34). He still has 1 HP, so don't commit your whole hand on the assumption he survives.
- **Logray:** three copies means a second one is a dead draw once one is in play. Resource the spare, or discard it to Reckless Sacrifice (it hits anything costing 3 or more).
- **Defenders of the Forest** is sideboard-only now. Don't hold 5 resources for it in game 1.
- **Resources:** stop at 4 unless you hold Relentless Hunters, then 5. Resource spare uniques first, then Village Tender, then V-19 against decks with no space units. Never resource your last Nightfall.
- **V-19 Skirmisher:** it counts itself toward the three units, so it is a Sentinel once two other units are out. Play it before the Y-Wings against space decks, so it is already guarding when they land. Against decks with no space units it is a 3-power base attacker that can't be blocked on the ground.
- **Reckless Sacrifice (2 copies):** keep one spare cheap unit in hand while you hold it. A discarded 1-drop hits anything costing 2 or more, but never a 1-cost unit.
- **Turning the Tide:** it counts friendly units in both arenas, so it deals 4–6 by turn 4–5. Save it for a unit you can't remove in combat: a big ship, a Sentinel wall, or a deployed leader. Don't fire it right after a sweeper. Shields soak it, since it is one instance of damage.
- **Chief Chirpa (1 copy):** a bonus. Play him late, once three or more Ewoks are out.

### Sideboard starting points

| Against | In | Out |
|---|---|---|
| Fast aggro | 1 Collateral Damage, 1 Defenders of the Forest | 2 Relentless Hunters |
| Midrange / Sentinel walls | 2 Han Solo | 1 Village Tender, 1 Ewok Warrior |
| Control | 2 Han Solo, 1 Aggressive Negotiations | 1 Village Tender, 2 Turning the Tide |
| Shields / unit upgrades | 3 Kaydel Connix | 1 Village Tender, 2 Turning the Tide |
| Space | 2 Wild Space Wanderer, 1 Collateral Damage | 2 Relentless Hunters, 1 Village Tender |
| Fortify bases | 2 Wild Space Wanderer | 1 Village Tender, 1 Ewok Warrior |

Kaydel has Plot: if you bring her in, resource her early and play her from your resources when Wicket deploys.

### Open list changes

None. Both changes suggested by the v7 games (V-19 for Lifetree Caravan, Turning the Tide for Village Tender) are applied.
