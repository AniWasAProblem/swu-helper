# Wicket Ewok Swarm (v6) — analysis and pilot guide

Decklist: `ewoks-v6.json` (leader `HMW_014` Wicket, base `HMW_023` Bright Tree Village).

v6 is a ground combat aggro deck: it floods the board with cheap 3-power Ewoks that can't be attacked the turn they land, draws off Wicket every round, and wins on turns 6–8 by attacking. It replaces v5's chip-damage plan; v5's Sentinels and most of its burn are gone. Nothing here has been playtested; the percentages are calculated, and the hand-size and sideboard advice are estimates.

Rule references are to `rules/SWU_Rules_v9_0.pdf` (v9.0).

## What changed from v5

v6 is the `ewoks-prebuilt` list with six cards swapped, not an edit of v5.

- **Kept from v5:** Red Squadron Y-Wing, Nightfall, and the 10-card sideboard.
- **Gone from v5:** Cloud-Rider Veteran, Stormchaser, Warrior of Clan Kryze, Stalwart Fleet Trooper, V-19 Skirmisher, Relentless Hunters, Run Amok, Turning the Tide, and the main-deck Collateral Damage, Aggressive Negotiations and Defenders of the Forest.
- **New:** Teebo and Chief Chirpa at three copies, Ewok Warrior, Village Tender, Benthic, Clan Wren Loyalist, Lifetree Caravan, Reckless Sacrifice, Beast Lair, Luminara.

## Analysis

1. **Game-stage plan**
   - **Early (turns 1–3):** 31 units cost 2 or less, so you have a turn-1 play 99.8% of the time and a 1-drop 85% of the time. Wicket deploys turn 3.
   - **Mid (turns 4–6):** two or three cards a turn. Chief Chirpa grows, Clan Wren Loyalist refills, Ewok Archers and Reckless Sacrifice remove blockers.
   - **Late (turn 7+):** two Luminara are the only cards above 3 cost. Without her the deck is top-decking cheap units.
2. **Curve:** 13 / 26 / 9 / 0 / 0 / 0 / 2 at costs 1–7, average 2.12. It fits the plan. Nothing costs 4–6, so Lifetree Caravan's extra resource only matters for double-spending or for Luminara.
3. **Leader and base:** 40 of 42 units cost 3 or less, so deployed Wicket's draw and Leia's heal are almost always live. The Endor base powers 9 cards (Troublemaker, Adamant Ewoks, Nightfall).
4. **Weaknesses**
   - **No Sentinel:** you can only race. Leia and Village Tender heal a little.
   - **Thin space:** three Y-Wings, and nothing that blocks in space.
   - **Sweepers:** most units have 3 HP or less; recovery is Wicket's draw and Loyalist.
   - **Sentinel walls:** 5 Saboteurs, and the two Wicket units can't attack bases.
   - **Duplicate uniques:** 18 slots are unique cards. A second copy in play is defeated (1.16.b, p. 11), and only Reckless Sacrifice and Beast Lair turn spares into value.
5. **Matchups:** favourable against ramp; slightly favourable against midrange; even against aggro and leader-combo; slightly unfavourable against space; unfavourable against control.

## How to pilot it

### Mulligan and resources

- **Keep** any six with two units costing 2 or less. Don't mulligan looking for Teebo or Chirpa; the mulligan replaces the whole hand and you must keep the new one (p. 22).
- **Resource first:** Luminara in the opening turns, a second Beast Lair, and spare copies of uniques you already have in play.
- **Keep one spare unique in hand** if you hold Reckless Sacrifice or have Beast Lair out. It is the card you discard.
- **Stop at 5 resources.** Go to 7 only with Luminara in hand.

### Turn by turn

- **Turn 1:** two 1-drops if you have them, Teebo first. Otherwise Adamant Ewoks (1 to the base) or Y-Wing (it starts chipping on turn 2). Play Leia before the other 1-drop only if your base is already damaged.
- **Turn 2:** a 2-drop plus a 1-drop. Chirpa is best once two Ewoks are out. Beast Lair only if you have a card you are happy to discard every round.
- **Turn 3:** first attack a more expensive unit with a small one and exhaust Wicket to draw. Then deploy him, since he can deploy exhausted and enters ready (3.4.4, p. 15), and attack with him for a second draw.
- **Turns 4–6:** empty your hand every turn and attack with everything. Loyalist and Wicket refill it.
- **Turn 7+:** Luminara, then cheap units for extra attacks. Close with Nightfall on your biggest ready unit.

### When not to deploy Wicket on turn 3

- **Deploy immediately** if the opponent has no units, because the leader side draws nothing then.
- **Hold him** if their board would kill a 2/5 for free and they keep playing expensive units, because the leader side keeps drawing safely.
- **With Teebo out, deploy freely.** Wicket is an Ewok, and Hidden covers the phase a unit is deployed (7.5.18, p. 34), so he can't be attacked that turn.
- If he is defeated he flips back exhausted and can't redeploy (3.4.5, p. 16), but his leader-side draw works again from the next round.

### Card-specific lines

- **Wicket's leader-side draw** is once per round. Take it on the first eligible attack. Beast tokens cost 0 (3.7, p. 18), so a Beast qualifies against any unit, and a 1-drop qualifies against anything costing 2 or more.
- **Hidden** only stops attacks, and only in the phase the unit was played. It does not stop damage from abilities or events.
- **Teebo:** he gives Hidden to every other Ewok, but he has 1 HP and dies to any ping. Don't rely on him surviving a round.
- **Chief Chirpa:** +1 power per other Ewok unit, including deployed Wicket. Beasts, Leia, Benthic, Loyalist and Y-Wing don't count.
- **Logray:** every time one of your cheap units takes damage, you ping. Attack into units with Logray out; damaged Beasts trigger it too.
- **Leia:** she heals only when you *play* a unit, so Beast tokens don't count. She does nothing while your base is undamaged.
- **Wicket the unit:** it can't attack bases. Use it to snipe behind Sentinels and to attack up for draws.
- **Adamant Ewoks:** the Endor base means the ping always works, even on an empty board.
- **Benthic:** the attack ping is ground-only. His 1 base damage on defeat makes him a fine unit to trade away.
- **Ewok Archers:** Ambush needs another unit costing 3 or less. Attacking a 4-cost or bigger unit with it also takes Wicket's leader-side draw.
- **Clan Wren Loyalist:** play it with an Ewok out, when about 28 cards in the deck are hits. On an empty board it only finds Benthic or another Loyalist. You may take nothing (8.26.1, p. 45).
- **Lifetree Caravan:** it counts itself, tokens and Wicket toward the three units. Skip it against sweeper decks if it would be your third unit committed.
- **Reckless Sacrifice:** the target must cost more than the unit you discard. Discard a 1-drop to hit anything costing 2 or more; discarding Luminara hits almost nothing. It can hit space units and deployed leaders.
- **Beast Lair:** it is Fortify, so it plays onto an empty board (7.5.21, pp. 34–35). The Beast is created at the start of the action phase and enters exhausted, so it attacks the following round. It trades a card for a 3/3, so stop feeding it when your hand is short.
- **Y-Wing:** the 3 indirect damage is unpreventable and the opponent chooses the split (8.35, p. 47). Attack the base unless a space unit must die.
- **Nightfall:** you need a ready unit for the attack half. Best targets are a large Chirpa on an open board, Troublemaker past a Sentinel, or Y-Wing for a second 3 indirect.
- **Luminara:** she enters exhausted, so on the turn she lands her trigger sends a different ready unit in at +2. After that every unit you play is also an attack.

### Initiative

Taking the initiative ends your actions for the round (p. 9), so take it only when you have nothing better left. It is worth more here than in most decks: units played this round stop being Hidden next round, and acting first lets them attack before they can be attacked.

### Playing around sweepers

Once you have about four units out against a control deck, stop adding more and hold two units in hand. Beast Lair keeps adding bodies without spending cards from the board, and Y-Wing keeps the clock going. Held units are also Reckless Sacrifice fodder.

### Sideboard starting points

| Against | In | Out |
|---|---|---|
| Fast aggro | 1 Collateral Damage, 1 Defenders of the Forest | 2 Luminara |
| Midrange / Sentinel walls | 2 Han Solo | 2 Village Tender |
| Control | 2 Han Solo, 1 Aggressive Negotiations | 3 Lifetree Caravan |
| Shields / unit upgrades | 3 Kaydel Connix | 3 Village Tender |
| Space | 2 Wild Space Wanderer, 1 Collateral Damage | 2 Luminara, 1 Beast Lair |
| Fortify bases | 2 Wild Space Wanderer | 2 Village Tender |

Kaydel has Plot: if you bring her in, resource her early and play her from your resources when Wicket deploys.
