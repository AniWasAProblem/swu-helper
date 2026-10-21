# Wicket Ewok Swarm (v7) — analysis and pilot guide

Decklist: `ewoks-v7.json` (leader `HMW_014` Wicket, base `HMW_023` Bright Tree Village).

v7 is a ground combat aggro deck with a chip-damage backup: it floods the board with cheap Ewoks that can't be attacked the turn they land, draws off Wicket every round, and wins on turns 6–8 by attacking while Cloud-Rider Veteran and Red Squadron Y-Wing damage the base regardless of blockers. It has no late game, so it must win before the opponent's expensive cards take over. The percentages are calculated and the sideboard advice is an estimate. The piloting advice has been revised after five simulator games (see "Games played" at the end); that is a small sample, so treat it as a starting point.

Rule references are to `rules/SWU_Rules_v9_0.pdf` (v9.0).

## What changed from v6

v7 is v6 rebuilt around the cards actually owned. Nine slots changed.

- **Out:** 2 Beast Lair, 2 Luminara Unduli, 2 Chief Chirpa, 1 Teebo, 1 Logray, 1 Reckless Sacrifice.
- **In:** 3 Champions of Endor, 3 Cloud-Rider Veteran, 2 Relentless Hunters, 1 Defenders of the Forest.
- **Sideboard:** unchanged.

## Analysis

1. **Game-stage plan**
   - **Early (turns 1–3):** 33 units cost 2 or less, so you have a turn-1 play 99.9% of the time and a 1-drop 83% of the time. Wicket deploys turn 3.
   - **Mid (turns 4–6):** two or three cards a turn. Clan Wren Loyalist refills, Ewok Archers and Reckless Sacrifice remove blockers, Cloud-Rider and Y-Wing chip the base every round.
   - **Late (turn 7+):** nothing. Two Relentless Hunters and one Defenders of the Forest are the only cards above 3 cost.
2. **Curve:** 12 / 26 / 9 / 2 / 1 at costs 1–5, average 2.08. It fits the plan. Lifetree Caravan's extra resource is for playing more cards per turn, not for bigger ones.
3. **Leader and base:** 42 of 45 units cost 3 or less, so deployed Wicket's draw and Leia's heal are almost always live. The Endor base powers 9 cards (Troublemaker, Adamant Ewoks, Nightfall).
4. **Weaknesses**
   - **No Sentinel:** you can only race. Leia and Village Tender heal a little.
   - **Thin space:** three Y-Wings, and nothing that blocks in space. No main-deck card removes a large ship, so a pilot-stacked vehicle attacks your base every round.
   - **Sweepers:** most units have 3 HP or less; recovery is Wicket's draw and Loyalist.
   - **No late game:** if the game reaches turn 8 or 9 on an even board, the opponent's cards are better than yours.
   - **Blank cards against decks with no ground units:** the Wicket unit, Logray, Hidden and Wicket's leader-side draw all need enemy ground units or enemy attacks on your units.
   - **Low power in places:** twelve units have 1 power. Six of them (Cloud-Rider, Y-Wing) do their work through abilities; the other six are support.
   - **Thin tribal payoff:** 29 Ewoks, but only one Chief Chirpa. The payoff is Teebo's Hidden and Loyalist's search.
5. **Matchups:** favourable against ramp; even against midrange, aggro and leader-combo; slightly unfavourable against control; unfavourable against space. Midrange and space were both downgraded after games 117 and 118.

## How to pilot it

### Mulligan and resources

- **Keep** any six with two cheap units that can damage a base. Village Tender, Logray and the Wicket unit don't count. Don't mulligan looking for Teebo; the mulligan replaces the whole hand and you must keep the new one (p. 22).
- **Resource first:** Lifetree Caravan, Defenders of the Forest, then spare copies of uniques you already have in play. Caravan was never worth playing in five games.
- **Never resource your last Nightfall.** It is the deck's finisher; resourcing all three lost game 118 by 2 damage.
- **Relentless Hunters:** play it the first round you can, or resource it. Holding it for later wasted it in two games.
- **Keep one spare unit in hand** if you hold Reckless Sacrifice. A spare unique 1-drop is the best card to discard.
- **Stop at 5 resources, firmly.** Four is enough if you hold no Hunters or Defenders. Cards run out before resources do: going to 7 in game 118 emptied the hand by round 7.

### Turn by turn

- **Turn 1:** two 1-drops if you have them, Teebo first. Otherwise Cloud-Rider Veteran or Y-Wing (they start chipping on turn 2), or Adamant Ewoks (1 to the base). Play Leia before the other 1-drop only if your base is already damaged.
- **Turn 2:** a 2-drop plus a 1-drop. Champions of Endor is the default body; Chirpa is best once two Ewoks are out.
- **Turn 3:** first attack a more expensive unit with a small one and exhaust Wicket to draw. Then deploy him, since he can deploy exhausted and enters ready (3.4.4, p. 15), and attack with him for a second draw.
- **Turns 4–6:** empty your hand every turn and attack with everything. Cloud-Rider and Y-Wing attack every round.
- **Turn 7+:** count damage and close with Nightfall on Cloud-Rider, Hunters or Y-Wing.

### When not to deploy Wicket on turn 3

- **Deploy immediately** if the opponent has no units, or only 1-cost ground units (pilot decks), because the leader side draws nothing then.
- **Hold him** if their board would kill a 2/5 for free and they keep playing expensive units, because the leader side keeps drawing safely. Follow this against midrange: in game 118 he was deployed into Obi-Wan and a Beast, drew one card and died to the next action.
- **With Teebo out, deploy freely.** Wicket is an Ewok, and Hidden covers the phase a unit is deployed (7.5.18, p. 34), so he can't be attacked that turn.
- If he is defeated he flips back exhausted and can't redeploy (3.4.5, p. 16), but his leader-side draw works again from the next round.

### Card-specific lines

- **Wicket's leader-side draw** is once per round. Take it on the first eligible attack. A 1-drop qualifies against anything costing 2 or more.
- **Hidden** only stops attacks, and only in the phase the unit was played. It does not stop damage from abilities or events.
- **Teebo:** he gives Hidden to every other Ewok, but he has 1 HP and dies to any ping. With two copies, don't plan around him.
- **Chief Chirpa:** +1 power per other Ewok unit, including deployed Wicket. Leia, Benthic, Loyalist, Cloud-Rider, Y-Wing and Hunters don't count. There is only one, so treat him as a bonus.
- **Logray:** every time one of your cheap units takes damage, you ping. Attack into units with Logray out. He is strong against decks that attack your units (five pings in game 118) and blank against decks that only attack your base.
- **Leia:** she heals when you play another unit costing 3 or less. She does nothing while your base is undamaged.
- **Wicket the unit:** it can't attack bases. Use it to snipe behind Sentinels and to attack up for draws. Resource it against decks with no ground units.
- **Adamant Ewoks:** the Endor base means the ping always works, even on an empty board. It has been the best card in the games played, because its damage lands when it is played and can't be answered first.
- **Benthic:** the attack ping is ground-only. His 1 base damage on defeat makes him a fine unit to trade away.
- **Champions of Endor:** a plain 3/3 Ewok. It trades with most 2- and 3-drops and gets Hidden from Teebo.
- **Cloud-Rider Veteran:** the 2 base damage happens whatever it attacks, so a Sentinel doesn't stop it. Attacking a unit that costs 3 or more gets the base damage and Wicket's leader-side draw.
- **Y-Wing:** the 3 indirect damage is unpreventable and the opponent chooses the split (8.35, p. 47). Attack the base unless a space unit must die. Expect less than 4 a turn: opponents often put the indirect damage on units, and a 1-cost space Sentinel or an Ambush ship stops it cold.
- **Ewok Archers:** Ambush needs another unit costing 3 or less. Attacking a 4-cost or bigger unit with it also takes Wicket's leader-side draw.
- **Clan Wren Loyalist:** play it with an Ewok out, when about 27 cards in the deck are hits. On an empty board it only finds Benthic or another Loyalist. You may take nothing (8.26.1, p. 45).
- **Lifetree Caravan:** it counts itself and Wicket toward the three units. Skip it against sweeper decks if it would be your third unit committed.
- **Reckless Sacrifice:** the target must cost more than the unit you discard. Discard a 1-drop to hit anything costing 2 or more; discarding Hunters only hits units costing 5 or more. It can hit space units and deployed leaders, but never a 1-cost unit, because the deck's cheapest units cost 1. That rules out 1-cost ships carrying pilots.
- **Relentless Hunters:** the Saboteur that can attack bases. Hold it for when a Sentinel is in the way.
- **Defenders of the Forest:** treat it as a removal spell. Ambush for 5 (7.5.5, p. 31), with Overwhelm sending the excess to the base; it will usually die afterwards.
- **Nightfall:** you need a ready unit for the attack half. Best targets are Cloud-Rider (5 to the base in total), Hunters or Troublemaker past a Sentinel, or Y-Wing for a second 3 indirect.

### Initiative

Taking the initiative ends your actions for the round (p. 9), so take it only when you have nothing better left. It is worth more here than in most decks: units played this round stop being Hidden next round, and acting first lets them attack before they can be attacked.

An opponent who claims it every round will remove your best attacker with their first action each round. Against that, lean on damage that lands when a card is played (Adamant Ewoks, Ewok Archers' Ambush, Nightfall) and attack with the unit most likely to be removed first.

### Playing around sweepers

Once you have about four units out against a control deck, stop adding more and hold two units in hand. Cloud-Rider and Y-Wing keep the clock going on their own. Held units are also Reckless Sacrifice fodder.

### Playing around bounce and exhaust

Against decks that return or exhaust your units (Razor Crest, Death Space Skirmisher), attack with your biggest ready unit before you play cards. A unit that has already attacked loses nothing that round if it is bounced or exhausted. This comes from two v6 games against a Wedge Antilles pilot deck, where developing first cost a 4-power Chief Chirpa attack.

### Sideboard starting points

| Against | In | Out |
|---|---|---|
| Fast aggro | 1 Collateral Damage, 1 Defenders of the Forest | 2 Lifetree Caravan |
| Midrange / Sentinel walls | 2 Han Solo | 2 Village Tender |
| Control | 2 Han Solo, 1 Aggressive Negotiations | 3 Lifetree Caravan |
| Shields / unit upgrades | 3 Kaydel Connix | 3 Village Tender |
| Space | 2 Wild Space Wanderer, 1 Collateral Damage | 2 Relentless Hunters, 1 Defenders of the Forest |
| Fortify bases | 2 Wild Space Wanderer | 2 Village Tender |

Kaydel has Plot: if you bring her in, resource her early and play her from your resources when Wicket deploys.

## Games played

All games were on the SWUSim simulator. In games 109–113 the opponent was the built-in bot, which never attacked units; in 117 and 118 the agent played both seats.

| Game | List | Opponent | Result |
|---|---|---|---|
| 109 | v6 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 5 |
| 110 | v6 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 4 |
| 113 | v7 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 4 |
| 117 | v7 | Wedge Antilles pilots, 26 HP base | Lost, round 4, opponent on 10 |
| 118 | v7 | Tarfful midrange, 30 HP base | Lost, round 9, opponent on 2 |

### Against Wedge Antilles pilots

- It is a pure race, and a well-piloted Wedge deck wins it: pilots stacked on a 1-cost ship hit for 6 to 8 a round from round 2.
- Nothing in the main deck removes that ship. Chip it with Adamant Ewoks' ping only if a second source of damage can finish it.
- Its ground units all cost 1, so deploy Wicket on round 3 and resource the Wicket unit and Logray.
- Attack before playing cards, because Razor Crest bounces and Death Space Skirmisher exhausts.

### Against Tarfful midrange

- It kills your units for seven rounds and then turns on your base. Bo-Katan Kryze at 9 resources gives every unit you control -3/-3, so the game must end by round 8.
- Hold Wicket and take the leader-side draw each round by attacking up; its units all cost 3 or more.
- Cloud-Rider Veteran is the best attacker here, because Tarfful and Koska Reeves are Sentinels and its base damage ignores them.
- Save Nightfall for the last 6 damage.

### List changes these games point to

Not yet applied to `ewoks-v7.json`.

- Cut 3 Lifetree Caravan for 3 V-19 Skirmisher, a space unit with conditional Sentinel.
- Village Tender is the next weakest slot; Turning the Tide could take two of them as an answer to a large ship.
