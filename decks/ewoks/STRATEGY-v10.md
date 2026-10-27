# Wicket Ewok Swarm (v10) — analysis and pilot guide

Decklist: `ewoks-v10.json`. Rule references are to `rules/SWU_Rules_v9_0.pdf` (v9.0).

This is ground aggro with a chip-damage backup. It floods the board with cheap Ewoks. Wicket draws a card every round. Cloud-Rider Veteran and Red Squadron Y-Wing damage the opponent's base every round, whatever blocks them. The deck aims to win on turns 6–8 and stops resourcing at 4–5.

The deck is built to survive pings and sweepers. The best decks punish small units with repeatable 1–2 damage pings and sweepers: Luke Skywalker's leader action, Red Five, The Legacy Run, Pre Vizsla. So the core Ewoks have 4 or 5 HP, not 2 or 3. The deck also carries a small space package that can stop or kill a big ship: Outland Protector to chump-block, and Dorsal Turret to kill.

The percentages are calculated. The piloting advice comes from eleven games with earlier versions of this list, which share most of their cards with it (see "Games played" at the end). This exact list has not been played yet.

## Decklist

**Leader: Wicket, Few Greater Battles to Fight** (`HMW_014`; Aggression / Heroism)
- **Leader side:** when a friendly unit attacks a unit that costs more than it, you may exhaust Wicket to draw a card.
- **Epic Action:** deploy him once you control 4 or more resources. Deploying doesn't spend resources; it is a threshold.
- **Unit side:** 2/5 ground. *On Attack:* if you control a unit that costs 3 or less, draw a card.

**Base: Bright Tree Village** (`HMW_023`; Command, 30 HP). It has no ability. It is here for its Endor planet trait, which turns on Village Troublemaker, Adamant Ewoks and Nightfall.

**Main deck (50)**

| Cost | Card | # | Type | Stats | What it does |
|---|---|---|---|---|---|
| 1 | Teebo, Striped Hunter | 3 | Ewok unit | 3/1 | Hidden; other friendly Ewoks gain Hidden. Unique. |
| 1 | Village Troublemaker | 3 | Ewok unit | 2/2 | With an Endor base: Hidden and Saboteur. |
| 1 | Wicket, Yub Nub! | 2 | Ewok unit | 3/3 | Saboteur; can't attack bases. Unique. |
| 1 | Leia Organa, These are My Friends | 2 | Unit | 2/3 | Heal 1 from your base when you play another unit costing 3 or less. Unique. |
| 1 | Village Tender | 1 | Ewok unit | 1/3 | Hidden, Restore 1. |
| 1 | Outland Protector | 2 | Space unit | 1/2 | Sentinel. |
| 1 | Dorsal Turret | 2 | Upgrade | — | Attach to a Vehicle. It gains: "When this unit deals combat damage to a unit while attacking: Defeat that unit." |
| 2 | Adamant Ewoks | 3 | Ewok unit | 3/2 | When Played (with an Endor base): 1 damage to a base and 1 to an enemy unit. |
| 2 | Logray, Bright Tree Shaman | 3 | Ewok unit | 1/5 | When another friendly unit costing 3 or less is dealt damage, ping an enemy unit for 1. Unique. |
| 2 | Ewok Brigade | 3 | Ewok unit | 2/4 | No ability. |
| 2 | Champions of Endor | 2 | Ewok unit | 3/3 | No ability. |
| 2 | Chief Chirpa, Defiant Elder | 1 | Ewok unit | 1/5 | +1/+0 per other friendly Ewok. Unique. |
| 2 | Benthic "Two Tubes" | 2 | Unit | 3/2 | On Attack: 1 to an enemy ground unit. When Defeated: 1 to a base. Unique. |
| 2 | Cloud-Rider Veteran | 3 | Unit | 1/4 | On Attack: 2 damage to a base. |
| 2 | Red Squadron Y-Wing | 3 | Space unit | 1/3 | On Attack: 3 indirect damage to the defending player. |
| 2 | Reckless Sacrifice | 2 | Event | — | Discard a unit from hand; deal 5 to a unit that costs more than it. |
| 2 | Nightfall | 3 | Event | — | 1 damage to an enemy unit; with an Endor base, attack with a unit at +2/+0. |
| 3 | V-19 Skirmisher | 3 | Space unit | 3/3 | Sentinel while you control 3 or more units. |
| 3 | Ewok Archers | 3 | Ewok unit | 2/5 | Ambush while you control another unit that costs 3 or less. |
| 3 | Turning the Tide | 2 | Event | — | 1 damage to a unit for each friendly unit. |
| 4 | Relentless Hunters | 2 | Unit | 5/4 | Saboteur. |

Teebo, the Wicket unit, Leia, Logray, Chirpa and Benthic are unique: 13 slots in total. If a second copy of one enters play, you must defeat one of the two (1.16.b, p. 11). Resource the spares, or discard them to Reckless Sacrifice.

**Sideboard (10):** 3 Aggressive Negotiations, 2 Kaydel Connix, 2 Han Solo (It'll Work), 2 Shoot Down, 1 Collateral Damage. See "Sideboard" below.

## Analysis

### 1. Game-stage plan

- **Early (turns 1–3):**
  - **Turn-1 plays:** 33 units cost 2 or less, so you almost always have one (99.9%). You have a 1-cost unit 85% of the time, and Teebo is in the opening six 32% of the time.
  - **Turn 3:** Wicket deploys, when you reach 4 resources.
  - **Space:** Outland Protector, Y-Wing and V-19 give you a space unit from turn 1–2. Against space decks, having one early matters (see "Weaknesses").
- **Mid (turns 4–6):** you play two or three cards a turn.
  - **Clear blockers:** Logray, Ewok Archers' Ambush, Reckless Sacrifice, Turning the Tide and Nightfall.
  - **Kill a big ship:** Dorsal Turret on a ready Y-Wing or V-19.
  - **Chip the base:** Cloud-Rider and Y-Wing, every round. Adamant Ewoks deals 1 to the base when it is played.
  - **Survive pings:** Ewok Brigade (4 HP), Archers, Logray and Chirpa (5 HP), and Cloud-Rider (4 HP) all survive a 1–3 damage ping. Logray turns each ping on a cheap friendly unit into one of yours.
- **Late (turn 7+):**
  - **Finishers:** Nightfall (+2 power and an extra attack), Relentless Hunters, and the Saboteurs for getting past Sentinels.
  - **Odds:** you see at least one Nightfall by turn 6 69% of the time, without counting Wicket's draws.
  - **Risk:** there are no big units, and the hand is usually only 2–4 cards by now. If the board is even on turns 8–9, the opponent's cards are better than yours. This is a deck that has to win before turn 9.

### 2. Cost curve

15 / 25 / 8 / 2 cards at costs 1–4, average 1.94. That is a low, dense aggro curve, and with nothing above 4, stopping at 4–5 resources is right. At 4 resources you can cast a 2-drop and two 1-drops, or a 3-drop and a 1-drop, every round. The 3-cost slot is V-19, Ewok Archers and Turning the Tide. Most 3-cost cards that didn't affect the board have been cut: in the games played, they ended up resourced instead of cast.

### 3. Leader and base

- **Leader side:**
  - **Trigger:** Wicket draws whenever a cheaper unit attacks a more expensive one, once per round, because you exhaust him to do it.
  - **Who qualifies:** a 1-drop qualifies against anything costing 2 or more. A Dorsal Turret Y-Wing (cost 2) attacking a 4-cost piloted ship also qualifies, and you draw.
  - **Pumps don't change cost:** Nightfall raises power, not printed cost.
- **Deploy (4 resources, turn 3):**
  - **Draw condition:** the deployed 2/5 draws on every attack while you control a unit costing 3 or less. 39 of 41 units qualify, so it is almost always live.
  - **Ready on deploy:** he deploys ready, even from exhausted (3.4.4, p. 15), so you can use the leader-side draw first, then deploy and attack for a second draw.
  - **Toughness:** 5 HP survives most pings, but not two -3/-3 effects (Anakin Skywalker, Champion of Mortis) or a 5-power attacker after a ping.
- **Base:** 30 HP and no ability. The Endor trait powers 9 cards (3 Troublemaker, 3 Adamant Ewoks, 3 Nightfall). Leia and Village Tender are the only healing.

### 4. Weaknesses

- **Big ships:**
  - **Removal:** only Dorsal Turret kills a ship with more than 5 HP, such as a Luke-piloted fighter (7/9), Chimaera (6/6) or Nightbrother (6/7). You have only 2 Turrets, and each needs a Vehicle that has survived a round.
  - **Blocking:** Outland Protector and V-19 buy time. They don't kill anything.
  - **By turn 5:** you see a Protector or a Turret 74% of the time.
- **Sweepers that scale:**
  - **What gets through:** the 4- and 5-HP units shrug off pings. A real board wipe still kills everything: Pre Vizsla defeats up to 6 total HP, and The Legacy Run deals 6 divided.
  - **Still small:** Teebo (1 HP), Troublemaker (2), Adamant Ewoks (2), Benthic (2) and the Wicket unit (3) die to anything.
  - **Recovery:** Wicket's draw is the only refill.
- **Almost no ground Sentinel:** you can only race on the ground.
- **No late game on an even board:** see the game-stage plan.
- **Blank cards against decks with no ground units:**
  - **Need enemy ground units:** the Wicket unit (it can't attack bases), Benthic's ping and Archers' Ambush.
  - **Need the opponent to damage your units:** Logray.
  - **Needs expensive enemy units:** Wicket's leader-side draw.
- **Shields:** Turning the Tide and Reckless Sacrifice are one instance of damage each, so a Shield soaks all of it. Dorsal Turret's defeat needs combat damage to land, so a Shield stops that too. The answers are the Saboteurs (Troublemaker, Hunters, Wicket the unit), which defeat the Shield first, and Kaydel from the sideboard.

### 5. Matchups

- **Fast aggro: even.**
  - **Why it's even:** the 4–5 HP units trade well with 2- and 3-drops, Logray punishes decks that attack your units, and Leia heals.
  - **Racing:** you lose a pure race to anything faster.
- **Midrange (Tarfful, Sentinel walls): even.** These games go long and grind your units down.
  - **Get past Sentinels:** Cloud-Rider's base damage, plus Saboteur on Troublemaker and Hunters.
  - **Wicket:** hold him on the leader side and attack up each round for the draw.
  - **Clock:** their cards outclass yours after turn 8.
- **Ping / sweeper control (Maul, Old Master): unfavourable.** See "Against Maul" below.
  - **How they win:** Maul plays a unit for 1 less and defeats it right away, so The Legacy Run's 6 divided damage lands for 4 resources. Chimaera, Anakin, Pre Vizsla and a Maul that replays units follow from turn 5.
  - **What carries it:** the 4–5 HP units mean each sweep kills fewer of yours. Saboteurs get past Imperial Armored Commando and Jod Na Nawood. Adamant Ewoks, Nightfall and Y-Wing deal damage that a sweep can't undo.
- **Ramp / big units: favourable.**
  - **Removal:** Reckless Sacrifice (discard a 1-drop) deals 5 to their first big threat. Dorsal Turret kills a big ship. Turning the Tide or a Nightfall attack handles the next one.
  - **Draws:** cheap units attacking up draw cards.
- **Space / pilots (Luke Skywalker, Wedge Antilles): slightly unfavourable.** See "Against Luke Skywalker" below.
  - **Blocking:** Outland Protector blocks a 7-power pilot ship for 1 resource, and V-19 blocks as well.
  - **Removal:** Dorsal Turret kills the ship. Turning the Tide kills an unpiloted 4-HP fighter.
  - **Air Superiority:** it only works if they control more space units than you, so play your ships early.
  - **Sideboard:** bring in Shoot Down.
- **Leader-combo / Force: even.** You can kill a deployed leader with Reckless Sacrifice (discarding a 1-drop), Hunters' Saboteur, Turning the Tide, a Dorsal Turret ship (space leaders) or a Nightfall attack. Otherwise race it.

## How to pilot it

### Mulligan

- **Keep** any six with two cheap units that can damage a base or hold a board. Village Tender, Logray and the Wicket unit don't count toward the two.
- **Don't mulligan for Teebo.** A mulligan replaces the whole hand and you must keep the new six (p. 22).

### Resources

- **Setup:** you see the opponent's leader and base before you choose your two setup resources. Use that.
  - **Against Luke, Wedge or Maul:** never resource Reckless Sacrifice, Dorsal Turret or Outland Protector at setup.
  - **Against a space deck:** don't resource your Y-Wings either.
- **How many:** stop at 4. Go to 5 only if you hold Relentless Hunters or need to cast a 3-drop and a 2-drop in the same round. With nothing above 4, more resources just empty your hand faster.
- **What to resource first:**
  1. Spare copies of uniques you already have in play.
  2. Village Tender.
  3. Outland Protector, Dorsal Turret and V-19, against decks with no space units.
  4. The Wicket unit, Logray and Ewok Archers, against decks with no ground units.
- **Never resource your last Nightfall.** It is a finisher. Resourcing all three lost one game by 2 damage.
- **Never resource your last Reckless Sacrifice against a deck with big units.** It is one of only three answers to a 6+ HP threat.

### Turn by turn

- **Turn 1:** two 1-drops if you have them, Teebo first.
  - **Against a space deck:** play Outland Protector or Y-Wing, so your ships are already out when theirs arrive.
  - **No 1-drops:** play Cloud-Rider Veteran or Y-Wing, which start chipping on turn 2, or Adamant Ewoks (1 to the base).
  - **Leia:** play her before the other 1-drop only if your base is already damaged.
  - **No attacks:** units enter play exhausted, so nobody can attack on turn 1.
- **Turn 2:** a 2-drop plus a 1-drop.
  - **Default body:** Ewok Brigade against decks that ping. Champions of Endor otherwise.
  - **Chirpa:** best once two Ewoks are out.
  - **Against space decks:** V-19 and Archers are 3-drops. Play V-19 early, so it is already guarding when their ships attack.
- **Turn 3:** attack a more expensive unit with a small one and exhaust Wicket to draw. Then deploy him and attack with him for a second draw.
- **Turns 4–6:** play most of your hand and attack with everything. Cloud-Rider and Y-Wing attack every round. Against a sweeper deck, keep two units in hand (see "Playing around sweepers").
- **Turn 7+:** count damage. Close with Nightfall on Cloud-Rider, Y-Wing, Hunters or a Saboteur.

### When not to deploy Wicket on turn 3

- **Deploy at once** if the opponent has no units, or only 1-cost ground units (pilot decks). The leader side draws nothing then.
- **Hold him** if their board would kill a 2/5 for free and they keep playing expensive units, because the leader side keeps drawing safely. Do this against midrange: in one game he was deployed into Obi-Wan and a Beast, drew one card and died to the next action.
- **Against Maul**, he can't dodge Anakin's -3/-3 (twice) or The Legacy Run. Deploy him when he can attack straight away, so he draws at least once.
- **With Teebo out, deploy freely.** Wicket is an Ewok, and Hidden covers the phase a unit is deployed (7.5.18, p. 34), so he can't be attacked that turn. Hidden doesn't stop pings or events.
- **If he is defeated,** he flips back exhausted and can't redeploy (3.4.5, p. 16). His leader-side draw works again from the next round.

### Card-specific lines

- **Hidden** only stops attacks, and only in the phase the unit was played. It doesn't stop damage from abilities or events, which is how the ping decks kill Ewoks.
- **Teebo:** play him first on turn 1 or 2 so every later Ewok lands with Hidden. He has 1 HP and dies to any ping, so don't commit your whole hand on the assumption he survives. A second copy is dead while one is in play.
- **Village Troublemaker:** with your Endor base it always has Hidden and Saboteur. It is the cheapest way past a Sentinel, and a strong Nightfall target.
- **Wicket the unit:** it can't attack bases. Use it to snipe behind Sentinels (Saboteur) and to attack up for draws.
- **Leia:** she heals when you play another unit costing 3 or less. She does nothing while your base is undamaged.
- **Outland Protector:**
  - **What it does:** a 1-cost space Sentinel (7.5.11, p. 32). Its job is to soak one hit from a pilot ship or a big capital ship.
  - **Why the block holds:** the enemy ship's On Attack ability can kill it before combat damage, and the attack still deals nothing, because the defender has left play (6.3 step 4.c, p. 26). The only exception is an attacker with Overwhelm.
  - **Other uses:** it protects your Y-Wings, counts toward Turning the Tide and Archers' Ambush, and keeps Wicket's deployed draw live.
- **Dorsal Turret:**
  - **Targets:** put it on a ready Y-Wing or V-19 and attack the biggest enemy ship. Any combat damage defeats it: a Luke-piloted fighter, Chimaera, Nightbrother. The defeat is not damage, so HP doesn't matter. Your ship usually dies too, which is a good trade.
  - **Shields:** a Shield prevents the combat damage, so the defeat never triggers. Remove the Shield first.
  - **The Legacy Run:** don't use it on The Legacy Run while you have units in play, because its When Defeated deals 6 damage divided among your units.
  - **Timing:** a ship played this round is exhausted. Keep the Turret in hand until a ship has survived a round, then play it and attack in the same action. A Nightfall attack with a Turret ship also works.
  - **No Vehicle:** an upgrade with no eligible unit goes to the discard pile (6.2 step 5.b, p. 25), so don't play it without one.
- **Adamant Ewoks:** the Endor base means the ping always works, even on an empty board. It has been one of the best cards in the games played, because its damage lands when it is played and can't be answered first.
- **Logray:** every time one of your cheap units takes damage, you ping. That includes damage from The Legacy Run, Luke's ping and Red Five, so the more your units survive, the more you ping. He is strong against decks that damage your units (five pings in one game) and blank against decks that only attack your base.
- **Ewok Brigade:** a plain 2/4 Ewok. It survives Luke's ping plus Red Five's 2, and on a 4-HP board The Legacy Run's 6 divided damage kills at most one unit. Against decks that don't ping, Champions of Endor (3/3) hits harder.
- **Ewok Archers:**
  - **Ambush:** with another unit costing 3 or less out, it can attack an enemy unit the turn it is played (7.5.5, p. 31). It is still exhausted afterwards, and it can't Ambush a base.
  - **Best use:** kill 2-HP ground units, or finish a damaged one.
  - **Toughness:** at 5 HP it survives every ping and Legacy Run's split.
- **Chief Chirpa:** +1 power per other Ewok unit, including deployed Wicket. Leia, Benthic, Cloud-Rider, Y-Wing, V-19, Protector and Hunters don't count. There are 24 Ewoks but only one Chirpa, so play him once three or more Ewoks are out.
- **Benthic:** the attack ping hits ground units only. His 1 base damage on defeat makes him a fine unit to trade away.
- **Champions of Endor:** a plain 3/3 Ewok. It trades with most 2- and 3-drops and gets Hidden from Teebo.
- **Cloud-Rider Veteran:**
  - **Base damage:** the 2 base damage happens whatever it attacks, so a Sentinel doesn't stop it.
  - **Attacking up:** attacking a unit that costs 3 or more gets the base damage and Wicket's leader-side draw.
  - **Best attacker:** it was the best attacker in the games played.
  - **Weak spots:** ping decks target it first. Its 4 HP survives one ping, but not an Air Superiority (4 damage).
- **Red Squadron Y-Wing:**
  - **Indirect damage:** the opponent splits the 3 indirect damage between their base and units, and it can't be prevented (8.35, p. 47).
  - **What to attack:** attack the base unless a space unit must die. Attacking the base deals up to 4 a turn (1 combat plus 3 indirect), but expect less: opponents often put the damage on units, and a 1-cost space Sentinel or an Ambush ship stops it.
  - **Turret carrier:** it is also the cheapest Dorsal Turret carrier.
- **V-19 Skirmisher:**
  - **Sentinel:** it counts itself toward the three units, so it becomes a Sentinel once two other units are out (7.5.11, p. 32).
  - **Against decks with no space units:** it is a 3-power base attacker that can't be blocked on the ground.
  - **Toughness:** at 3 HP it dies to a pilot ship's On Attack, so it buys one turn at most.
- **Reckless Sacrifice:**
  - **Targeting:** the target must cost more than the unit you discard. A discarded 1-drop hits anything costing 2 or more. Discarding Hunters only hits units costing 5 or more. It never hits a 1-cost unit, so it can't touch 1-cost ships carrying pilots.
  - **Reach:** it can hit space units and deployed leaders.
  - **Fuel:** keep one spare cheap unit in hand while you hold it. A spare unique 1-drop is the best discard.
- **Turning the Tide:**
  - **Damage:** it counts friendly units in both arenas, so it deals 4–6 by turns 4–5.
  - **Targets:** save it for a unit you can't remove in combat, such as an unpiloted ship, a Sentinel or a deployed leader.
  - **Shields:** it is one instance of damage, so a Shield soaks all of it.
- **Relentless Hunters:** the Saboteur that can attack bases. Play it the first round you can, or resource it. Holding it for later wasted it in two games.
- **Nightfall:** you need a ready unit for the attack half. Best targets are Cloud-Rider (5 to the base in total), Hunters or Troublemaker past a Sentinel, Y-Wing for a second 3 indirect, or a Dorsal Turret ship into a big ship.

### Initiative

Taking the initiative ends your actions for the round (p. 9), so take it only when you have nothing better left. It is worth more here than in most decks. Units played this round stop being Hidden next round, and acting first lets them attack before they can be attacked.

An opponent who claims it every round will remove your best attacker with their first action each round. Against that, lean on damage that lands when a card is played (Adamant Ewoks, Nightfall), and attack first with the unit most likely to be removed.

### Playing around sweepers

- **Against a deck with The Legacy Run, Pre Vizsla or a similar sweeper:** keep three or four units out, mostly 4–5 HP, and hold two units in hand.
- **What the held units do:** they rebuild the board after the sweep, and they are Reckless Sacrifice fodder.
- **What keeps pressure on:** Cloud-Rider and Y-Wing keep the clock going on their own.

### Playing around bounce and exhaust

Against decks that return or exhaust your units (Razor Crest, Death Space Skirmisher, Jod Na Nawood), attack with your biggest ready unit before you play cards. A unit that has already attacked loses nothing that round if it is bounced or exhausted.

## Sideboard

| Card | # | What it is for |
|---|---|---|
| Aggressive Negotiations | 3 | 3-cost event: attack with a unit; it gets +1/+0 for each card in your hand. A finisher for matchups where your hand stays full. |
| Kaydel Connix, For Our Survival | 2 | 3-cost 3/2. When Played: defeat all non-unique upgrades on a unit, including Shield tokens. Plot: resource her early and play her from resources when Wicket deploys. |
| Han Solo, It'll Work | 2 | 4-cost 3/7 Saboteur. When Played: deals 3 to himself and gives 3 Advantage tokens to a unit. At 7 HP he survives sweepers. |
| Shoot Down | 2 | 2-cost event: 3 damage to a space unit; if it is defeated, you may deal 2 to a base. Kills Green Leader, X-Wings, Y-Wings, Onyx Squadron Brute, or a damaged Red Five. |
| Collateral Damage | 1 | 3-cost event: 2 damage to a unit, then 2 to a base or another unit in the same arena. |

| Against | In | Out |
|---|---|---|
| Hand reaching 5+ in game 1 | 3 Aggressive Negotiations | See "When to bring in Aggressive Negotiations" below |
| Fast aggro | 1 Collateral Damage | 1 Dorsal Turret |
| Midrange / Sentinel walls | 2 Han Solo | 1 Village Tender, 1 Leia Organa |
| Ping / sweeper control (Maul) | 2 Han Solo | 2 Teebo |
| Shields / unit upgrades | 2 Kaydel Connix | 1 Village Tender, 1 Leia Organa |
| Space / pilots (Luke, Wedge) | 2 Shoot Down | 1 Village Tender, 1 Wicket, Yub Nub! |

Against Maul, Teebo is the worst card. His 1 HP dies to every split of The Legacy Run, and Hidden does nothing against it.

There is no answer to Fortify upgrades in this sideboard. Against a Fortify base, ignore the upgrades and race.

### When to bring in Aggressive Negotiations

- **The test:** in game 1, count your hand at the start of each of your action phases from round 4 onward. If it reaches 5 or more cards, consider bringing in all 3 Aggressive Negotiations for game 2. Before round 4, a hand of 5 is normal and tells you nothing.
- **Why 5:** the card counts the cards still in hand when it resolves, and it has already left your hand by then. A hand of 5 makes it +4, a real finisher. With a hand of 2–4, which is normal against ping and sweeper decks, it is +1 to +3 for 3 resources and not worth a slot.
- **Which opponents:** a full hand usually means the opponent isn't killing your units every round, so your cheap cards are piling up. That points to slow midrange, control without pings, or ramp.
- **What to take out:** the cards that matchup doesn't need:
  - **No big ships:** take out 2 Dorsal Turret and 1 Village Tender.
  - **They do have big ships:** keep the Turrets and take out 1 Village Tender, 1 Leia Organa and 1 Champions of Endor.
- **How to play it:**
  - **Timing:** cast it before your other cards that round, while your hand is biggest.
  - **Ready attacker:** it is an attack, not an extra attack, so it needs a ready unit.
  - **Best targets:** deployed Wicket (his On Attack also draws a card), Cloud-Rider (+2 to the base), Y-Wing (+3 indirect), or a Saboteur against a Sentinel wall.
  - **Resources:** once it is in the deck, a big hand has value, so don't resource a card just because your hand is full.

## Games played

All games were on the SWUSim simulator, with earlier versions of this list. Those versions had the same leader, base and core Ewok package. In the first three games the opponent was the built-in bot, which never attacked units. In the rest, both seats were played by Claude.

| Game | Opponent | Result |
|---|---|---|
| 109 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 5 |
| 110 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 4 |
| 113 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 4 |
| 117 | Wedge Antilles pilots, 26 HP base | Lost, round 4, opponent on 10 |
| 118 | Tarfful midrange, 30 HP base | Lost, round 9, opponent on 2 |
| 129 | Maul, Old Master / Dune Sea (30 HP) | Lost, round 9, opponent on 16 |
| 130 | Maul, Old Master / Dune Sea (30 HP) | Lost, round 9, opponent on 24 |
| 131 | Luke Skywalker, Hero of Yavin / Data Vault (33 HP) | Lost, round 6, opponent on 8 |
| 132 | Luke Skywalker, Hero of Yavin / Data Vault (33 HP) | Lost, round 7, opponent on 6 |

The four most recent games (129–132) shaped the current list:
- **Abilities killed 22 units.** Every one of them had 3 HP or less, so the current list has more 4–5 HP Ewoks.
- **Nothing could kill the biggest ship.** It was a Luke-piloted 7/9 in game 132, plus Chimaera and Nightbrother against Maul.
- **Hands stayed small.** The hand held only 2–4 cards every round, so cards that scale with hand size or need setup were weak.
- **3-cost cards with no board effect went unplayed.** They were resourced instead of cast.

### Against Maul, Old Master

- **Their engine:** Maul's leader action plays a unit for 1 less and defeats it at once. The Legacy Run then deals 6 damage divided among your units for 4 resources. They did this twice a game, and Maul's deploy replays a unit defeated that phase.
- **What follows:** Anakin Skywalker (two -3/-3s), Chimaera (defeats a unit, heals their base), Nightbrother (replays a unit from discard) and Pre Vizsla (defeats units totalling 6 HP) from turn 5.
- **Their Sentinels:** Imperial Armored Commando (Shielded) and Jod Na Nawood (who can also exhaust an arena) block the ground.
- **The clock:** Maul deploys at 7 resources and Pre Vizsla costs 8, so they need to be dead by about round 7. In both games they had taken under 10 damage by round 6, which is too slow.
- **How to play it:**
  - **Spread the board:** play 4–5 HP units and never put more than four units out, so one Legacy Run can't wipe you.
  - **Get past Sentinels:** Troublemaker and Hunters (Saboteur) get through Commando's Shield and the Sentinels.
  - **Don't kill The Legacy Run with your own units out.** Kill it when your board is empty, so its 6 damage has nothing to hit (game 129).
  - **Space:** their Onyx Squadron Brute hits your base for 2 each round unopposed, so contest space early with Protector, Y-Wing or V-19.

### Against Luke Skywalker, Hero of Yavin

- **Their engine:**
  - **Pings:** after a Fighter attacks, Luke's leader action pings 1, and Red Five deals 2 to a damaged unit. Together they kill anything with 3 HP or less every round. Hotshot Maneuver, Air Superiority, Green Leader and Resistance Blue Squadron add more.
  - **Pilot ship:** at 6 resources Luke deploys as a pilot. A Resistance Blue Squadron carrying him was a 7/9 that dealt 3 to a unit on every attack and hit the base for 7. The Luke upgrade can't be defeated by enemy card abilities, but the ship under it can.
- **Both games were close** (opponent on 8 and 6), so a few points of blocking or removal swings the matchup.
- **How to play it:**
  - **Before Luke deploys:** get a space unit out early so Air Superiority stays off.
  - **Your 4–5 HP units:** play them so the ping-plus-Red-Five combo needs two turns per kill.
  - **Turning the Tide:** save it for Red Five before Luke boards it. Red Five has 4 HP.
  - **After Luke deploys:** chump the pilot ship with Outland Protector or V-19. Kill it with a Dorsal Turret Y-Wing or V-19, or with Reckless Sacrifice plus Turning the Tide.
  - **Setup resources:** keep your space cards in hand. In game 131, V-19 and Reckless Sacrifice were resourced at setup, and the Y-Wing and Cloud-Rider later.

### Against Wedge Antilles pilots

- **It is a pure race,** and a well-piloted Wedge deck wins it. Pilots stacked on a 1-cost ship hit for 6 to 8 a round from round 2.
- **Removing the ship:**
  - Reckless Sacrifice can't hit it, because it costs 1.
  - Dorsal Turret kills it whatever its HP.
  - Turning the Tide from a wide board can kill it.
  - Outland Protector and V-19 with Sentinel absorb hits.
- **Wicket:** their ground units all cost 1, so deploy him on round 3. Resource the Wicket unit and Logray.
- **Attack before playing cards,** because Razor Crest bounces and Death Space Skirmisher exhausts.

### Against Tarfful midrange

- **Their plan:** they kill your units for seven rounds and then turn on your base. Bo-Katan Kryze at 9 resources gives every unit you control -3/-3, so the game must end by round 8.
- **Wicket:** hold him and take the leader-side draw each round by attacking up. All of their units cost 3 or more.
- **Your best attacker:** Cloud-Rider Veteran, because Tarfful and Koska Reeves are Sentinels and its base damage ignores them. The Saboteurs also get through.
- **Nightfall:** save it for the last 6 damage. Game 118 was lost with the opponent on 2.

### What to check in the next games

- **Dorsal Turret:** how often it is in hand with a ready Vehicle to put it on. If it is usually stranded, swap it for Shoot Down.
- **Ewok Brigade vs. Champions:** whether the 2/4 bodies actually survive the sweeps, or whether the lost power makes the clock too slow.
- **The Maul clock:** how much damage is on their base by round 6. If it is still under 15, the Maul matchup needs a faster plan, not a tougher one.
- **Hand size in game 1:** the largest hand you hold at the start of an action phase from round 4 on, and against which decks. That decides when Aggressive Negotiations comes in.
