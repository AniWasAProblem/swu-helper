# Wicket Ewok Swarm (v9) — analysis and pilot guide

Decklist: `ewoks-v9.json`. Rule references are to `rules/SWU_Rules_v9_0.pdf` (v9.0).

This is ground aggro with a chip-damage backup. It floods the board with cheap Ewoks that can't be attacked the turn they land. Wicket draws a card every round. Cloud-Rider Veteran and Red Squadron Y-Wing damage the opponent's base every round, whatever blocks them. The deck aims to win on turns 6–8. It stops resourcing at 4–5, so the extra cards pile up in hand, and Aggressive Negotiations turns a full hand into a large late attack.

The percentages are calculated. The piloting advice comes from seven games with earlier versions of the list, which share most of their cards with this one (see "Games played" at the end). That is a small sample, so treat it as a starting point. This exact list has not been played yet.

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
| 2 | Adamant Ewoks | 3 | Ewok unit | 3/2 | When Played (with an Endor base): 1 damage to a base and 1 to an enemy unit. |
| 2 | Logray, Bright Tree Shaman | 3 | Ewok unit | 1/5 | When another friendly unit costing 3 or less is dealt damage, ping an enemy unit for 1. Unique. |
| 2 | Ewok Warrior | 3 | Ewok unit | 3/2 | Hidden. |
| 2 | Champions of Endor | 2 | Ewok unit | 3/3 | No ability. |
| 2 | Chief Chirpa, Defiant Elder | 1 | Ewok unit | 1/5 | +1/+0 per other friendly Ewok. Unique. |
| 2 | Benthic "Two Tubes" | 3 | Unit | 3/2 | On Attack: 1 to an enemy ground unit. When Defeated: 1 to a base. Unique. |
| 2 | Cloud-Rider Veteran | 3 | Unit | 1/4 | On Attack: 2 damage to a base. |
| 2 | Red Squadron Y-Wing | 3 | Space unit | 1/3 | On Attack: 3 indirect damage to the defending player. |
| 2 | Reckless Sacrifice | 2 | Event | — | Discard a unit from hand; deal 5 to a unit that costs more than it. |
| 2 | Nightfall | 3 | Event | — | 1 damage to an enemy unit; with an Endor base, attack with a unit at +2/+0. |
| 3 | Clan Wren Loyalist | 3 | Unit | 3/2 | When Played: search the top 5 for a card sharing a Trait with a unit you control. |
| 3 | V-19 Skirmisher | 3 | Space unit | 3/3 | Sentinel while you control 3 or more units. |
| 3 | Turning the Tide | 2 | Event | — | 1 damage to a unit for each friendly unit. |
| 3 | Aggressive Negotiations | 3 | Event | — | Attack with a unit; +1/+0 for each card in your hand. |
| 4 | Relentless Hunters | 2 | Unit | 5/4 | Saboteur. |

Teebo, the Wicket unit, Leia, Logray, Chirpa and Benthic are unique: 14 slots in total. If a second copy of one enters play, you must defeat one of the two (1.16.b, p. 11). Resource the spares, or discard them to Reckless Sacrifice.

**Sideboard (10):** 3 Kaydel Connix, 2 Wild Space Wanderer, 2 Han Solo (It'll Work), 2 Collateral Damage, 1 Defenders of the Forest. See "Sideboard" below.

## Analysis

### 1. Game-stage plan

- **Early (turns 1–3):** 32 units cost 2 or less, so you have a turn-1 play 99.9% of the time and a 1-drop 79% of the time. Teebo is in the opening six 32% of the time. Wicket deploys on turn 3, when you reach 4 resources.
- **Mid (turns 4–6):** you play two or three cards a turn.
  - **Refill:** Clan Wren Loyalist.
  - **Clear blockers:** Logray, Reckless Sacrifice, Turning the Tide and Nightfall.
  - **Chip the base:** Cloud-Rider and Y-Wing, every round.
  - **Pump an attack:** from turn 4, once you hold 4 or more cards, Aggressive Negotiations turns one attack into 5+ damage.
- **Late (turn 7+):**
  - **Finishers:** Aggressive Negotiations and Nightfall. Because you stop resourcing early and draw extra off Wicket, the hand is usually full, so each Aggressive Negotiations adds 5–7 damage.
  - **Odds:** without Wicket's draws, you see at least one Aggressive Negotiations by the start of turn 4 57% of the time, and at least one Nightfall by turn 6 69% of the time.
  - **Risk:** there are no big units. If the board is even on turns 8–9, the opponent's cards are better than yours.

### 2. Cost curve

11 / 26 / 11 / 2 cards at costs 1–4, average 2.08. It fits a low-curve aggro plan, and with nothing above 4, stopping at 4–5 resources is right. At 4–5 resources you can cast a 3-cost card and a 1–2 drop in the same round. The 3-cost slot is mostly interaction and refill: Loyalist, Turning the Tide and Aggressive Negotiations. V-19 is the only 3-cost body.

### 3. Leader and base

- **Leader side:**
  - **Trigger:** Wicket draws whenever a cheaper unit attacks a more expensive one, once per round, because you exhaust him to do it.
  - **Who qualifies:** a 1-drop qualifies against anything costing 2 or more.
  - **Pumps don't change cost:** Aggressive Negotiations and Nightfall raise power, not printed cost. A 1-drop given +5 attacking a 4-cost unit draws a card and usually kills it.
- **Deploy (4 resources, turn 3):**
  - **Draw condition:** the deployed 2/5 draws on every attack while you control a unit costing 3 or less. 38 of 40 units qualify, so it is almost always live.
  - **Ready on deploy:** he deploys ready, even from exhausted (3.4.4, p. 15), so you can use the leader-side draw first, then deploy and attack for a second draw.
  - **Best pump target:** an Aggressive Negotiations attack is still an attack, so his On Attack draw fires. Deployed Wicket swinging for about 7 and drawing a card is the best target for it.
- **Base:** 30 HP and no ability. The Endor trait powers 9 cards (3 Troublemaker, 3 Adamant Ewoks, 3 Nightfall). Leia and Village Tender are the only healing.

### 4. Weaknesses

- **Almost no Sentinel:**
  - **Ground:** you can only race.
  - **Space:** V-19 guards it, but only while you control 3 or more units (7.5.11, p. 32).
- **Space is not solved:**
  - **Blockers:** six space units (3 Y-Wing, 3 V-19). V-19 can block a pilot-stacked ship, but at 3 HP it dies doing it.
  - **Removal:** only Reckless Sacrifice and Turning the Tide remove a big ship, and Turning the Tide needs four or five units out to kill one.
- **Sweepers:**
  - **Toughness:** most units have 3 HP or less. Only Logray, Chirpa and deployed Wicket have 5.
  - **Recovery:** Wicket's draw and Loyalist are all you have.
  - **Events after a wipe:** Turning the Tide counts your units, and Aggressive Negotiations needs a ready unit. Both are weak right after a sweeper.
- **Small hand, small pump:** against decks that make you dump your hand early, Aggressive Negotiations gives +1 or +2 and is a weak 3-cost card.
- **No late game on an even board:** see the game-stage plan.
- **Blank cards against decks with no ground units:**
  - **Need enemy ground units:** the Wicket unit (it can't attack bases) and Benthic's ping.
  - **Need the opponent to attack your units:** Logray and Hidden.
  - **Needs expensive enemy units:** Wicket's leader-side draw.
- **Thin tribal payoff:** 21 Ewoks but only one Chief Chirpa. The payoffs are Teebo's Hidden and Loyalist's search.

### 5. Matchups

- **Fast aggro: even.** Hidden and Logray punish decks that attack your units, but you lose a race to anything faster. You empty your hand early, so Aggressive Negotiations is small; side some out.
- **Midrange: even.** These games go long and grind your units down.
  - **Get past Sentinels:** Cloud-Rider's base damage, Saboteur on Troublemaker and Hunters, and a full-hand Aggressive Negotiations punch through walls like Tarfful and Koska Reeves.
  - **Wicket:** hold him on the leader side and attack up each round for the draw.
  - **Clock:** their cards outclass yours after turn 8.
- **Control / sweepers: slightly unfavourable.** Play only about four units at a time and hold two in hand. Cloud-Rider and Y-Wing keep the clock going. A big Aggressive Negotiations can end a game the opponent thought they had stabilised, so keep one unit back to be ready after a wipe.
- **Ramp / big units: favourable.** You are well ahead by turn 5.
  - **Removal:** Reckless Sacrifice with a 1-drop deals 5 to their first big threat. Turning the Tide or a pumped attacker handles the second.
  - **Draws:** cheap units attacking up draw cards.
- **Space: slightly unfavourable.**
  - **Blocking:** V-19 gives you a space blocker by turn 2–3 and forces the opponent to attack it before your Y-Wings.
  - **Removal:** Turning the Tide from a wide board can kill a pilot-stacked ship, and so can a pumped Y-Wing or V-19.
  - **Racing:** a pilot-stacked ship can still out-race what V-19 absorbs.
- **Leader-combo / Force: even.** You can kill a deployed leader with Reckless Sacrifice (discarding a 1-drop), Hunters' Saboteur, Turning the Tide or a pumped attacker. Otherwise race it.

## How to pilot it

### Mulligan

- **Keep** any six with two cheap units that can damage a base. Village Tender, Logray and the Wicket unit don't count.
- **Don't mulligan for Teebo.** A mulligan replaces the whole hand and you must keep the new six (p. 22).

### Resources

- **How many:** stop at 4. Go to 5 only if you hold Relentless Hunters. Cards run out before resources do: going to 7 in one game emptied the hand by round 7.
- **Hand size:** a big hand now has value because it powers Aggressive Negotiations. Don't resource a card just because your hand is full.
- **What to resource first:**
  1. Spare copies of uniques you already have in play.
  2. Village Tender.
  3. V-19, against decks with no space units.
  4. The Wicket unit and Logray, against decks with no ground units.
  5. Aggressive Negotiations, against fast aggro.
- **Never resource your last Nightfall.** It is a finisher. Resourcing all three lost one game by 2 damage.

### Turn by turn

- **Turn 1:** two 1-drops if you have them, Teebo first.
  - **No 1-drops:** play Cloud-Rider Veteran or Y-Wing, which start chipping on turn 2, or Adamant Ewoks (1 to the base).
  - **Leia:** play her before the other 1-drop only if your base is already damaged.
  - **No attacks:** units enter play exhausted, so nobody can attack on turn 1.
- **Turn 2:** a 2-drop plus a 1-drop. Champions of Endor is the default body. Chirpa is best once two Ewoks are out. V-19 is a 3-drop: play it early against space decks so it is already guarding when their ships attack.
- **Turn 3:** attack a more expensive unit with a small one and exhaust Wicket to draw. Then deploy him and attack with him for a second draw.
- **Turns 4–6:** play most of your hand and attack with everything. Cloud-Rider and Y-Wing attack every round. Cast Aggressive Negotiations before your other cards that round, while your hand is still big.
- **Turn 7+:** count damage. Close with Aggressive Negotiations or Nightfall on Cloud-Rider, Y-Wing, Hunters or a Saboteur.

### When not to deploy Wicket on turn 3

- **Deploy at once** if the opponent has no units, or only 1-cost ground units (pilot decks). The leader side draws nothing then.
- **Hold him** if their board would kill a 2/5 for free and they keep playing expensive units, because the leader side keeps drawing safely. Do this against midrange: in one game he was deployed into Obi-Wan and a Beast, drew one card and died to the next action.
- **With Teebo out, deploy freely.** Wicket is an Ewok, and Hidden covers the phase a unit is deployed (7.5.18, p. 34), so he can't be attacked that turn.
- **If he is defeated,** he flips back exhausted and can't redeploy (3.4.5, p. 16). His leader-side draw works again from the next round.

### Card-specific lines

- **Hidden** only stops attacks, and only in the phase the unit was played. It doesn't stop damage from abilities or events.
- **Teebo:** play him first on turn 1 or 2 so every later Ewok lands with Hidden. He has 1 HP and dies to any ping, so don't commit your whole hand on the assumption he survives. A second copy is dead while one is in play.
- **Village Troublemaker:** with your Endor base it always has Hidden and Saboteur. It is the cheapest way past a Sentinel, and a strong Aggressive Negotiations or Nightfall target.
- **Wicket the unit:** it can't attack bases. Use it to snipe behind Sentinels (Saboteur) and to attack up for draws.
- **Leia:** she heals when you play another unit costing 3 or less. She does nothing while your base is undamaged.
- **Adamant Ewoks:** the Endor base means the ping always works, even on an empty board. It has been the best card in the games played, because its damage lands when it is played and can't be answered first.
- **Logray:** every time one of your cheap units takes damage, you ping. Attack into enemy units while he is out. He is strong against decks that attack your units (five pings in one game) and blank against decks that only attack your base.
- **Chief Chirpa:** +1 power per other Ewok unit, including deployed Wicket. Leia, Benthic, Loyalist, Cloud-Rider, Y-Wing, V-19 and Hunters don't count. There is only one copy, so play him late, once three or more Ewoks are out.
- **Benthic:** the attack ping hits ground units only. His 1 base damage on defeat makes him a fine unit to trade away.
- **Champions of Endor:** a plain 3/3 Ewok. It trades with most 2- and 3-drops and gets Hidden from Teebo.
- **Cloud-Rider Veteran:** the 2 base damage happens whatever it attacks, so a Sentinel doesn't stop it. Attacking a unit that costs 3 or more gets the base damage and Wicket's leader-side draw. It was the best attacker in the games played.
- **Red Squadron Y-Wing:** the opponent splits the 3 indirect damage between their base and units, and it can't be prevented (8.35, p. 47). Attack the base unless a space unit must die. Attacking the base deals up to 4 a turn (1 combat plus 3 indirect), but expect less: opponents often put the damage on units, and a 1-cost space Sentinel or an Ambush ship stops it.
- **V-19 Skirmisher:** it counts itself toward the three units, so it becomes a Sentinel once two other units are out. Against decks with no space units it is a 3-power base attacker that can't be blocked on the ground.
- **Clan Wren Loyalist:** play it with an Ewok out, so any of the 21 Ewoks is a hit. On an empty board it only finds Benthic or another Loyalist. You may take nothing, because the search names an attribute (8.26.1, p. 45). It can't find events: Aggressive Negotiations, Nightfall and the others share no trait with a unit.
- **Reckless Sacrifice:**
  - **Targeting:** the target must cost more than the unit you discard. A discarded 1-drop hits anything costing 2 or more; discarding Hunters only hits units costing 5 or more. It never hits a 1-cost unit, so it can't touch 1-cost ships carrying pilots.
  - **Reach:** it can hit space units and deployed leaders.
  - **Fuel:** keep one spare cheap unit in hand while you hold it. A spare unique 1-drop is the best discard.
- **Turning the Tide:** it counts friendly units in both arenas, so it deals 4–6 by turns 4–5. Save it for a unit you can't remove in combat: a big ship, a Sentinel wall or a deployed leader. It is one instance of damage, so a Shield soaks all of it.
- **Aggressive Negotiations:**
  - **Hand count:** it counts the cards still in hand when it resolves, and the card itself has already left. Play it before your other cards that round.
  - **Ready attacker:** it is an attack, not an extra attack, so it needs a ready unit.
  - **Best targets:** deployed Wicket (he also draws), Cloud-Rider (+2 to the base), Y-Wing (+3 indirect), or a Saboteur (Troublemaker, Hunters, Wicket the unit) against a Sentinel wall.
- **Relentless Hunters:** the Saboteur that can attack bases. Play it the first round you can, or resource it. Holding it for later wasted it in two games.
- **Nightfall:** you need a ready unit for the attack half. Best targets are Cloud-Rider (5 to the base in total), Hunters or Troublemaker past a Sentinel, or Y-Wing for a second 3 indirect.

### Initiative

Taking the initiative ends your actions for the round (p. 9), so take it only when you have nothing better left. It is worth more here than in most decks. Units played this round stop being Hidden next round, and acting first lets them attack before they can be attacked.

An opponent who claims it every round will remove your best attacker with their first action each round. Against that, lean on damage that lands when a card is played (Adamant Ewoks, Nightfall, Aggressive Negotiations), and attack first with the unit most likely to be removed.

### Playing around sweepers

Once you have about four units out against a control deck, stop adding more and hold two units in hand. Cloud-Rider and Y-Wing keep the clock going on their own. The held units are also Reckless Sacrifice fodder, and they keep the hand big for Aggressive Negotiations.

### Playing around bounce and exhaust

Against decks that return or exhaust your units (Razor Crest, Death Space Skirmisher), attack with your biggest ready unit before you play cards. A unit that has already attacked loses nothing that round if it is bounced or exhausted.

## Sideboard

| Card | # | What it is for |
|---|---|---|
| Kaydel Connix, For Our Survival | 3 | 3-cost 3/2. When Played: defeat all non-unique upgrades on a unit. Plot: resource her early and play her from resources when Wicket deploys. |
| Wild Space Wanderer | 2 | 3-cost 3/2 space unit, no aspect. When Played: defeat an upgrade on a base (Fortify). |
| Han Solo, It'll Work | 2 | 4-cost 3/7 Saboteur. When Played: deals 3 to himself and gives 3 Advantage tokens to a unit. |
| Collateral Damage | 2 | 3-cost event: 2 damage to a unit, then 2 to a base or another unit in the same arena. |
| Defenders of the Forest | 1 | 5-cost 5/3 Ewok with Ambush and Overwhelm (7.5.5, p. 31). Treat it as a removal spell that usually dies afterwards. |

| Against | In | Out |
|---|---|---|
| Fast aggro | 2 Collateral Damage, 1 Defenders of the Forest | 2 Relentless Hunters, 1 Aggressive Negotiations |
| Midrange / Sentinel walls | 2 Han Solo | 1 Village Tender, 1 Ewok Warrior |
| Control | 2 Han Solo | 1 Village Tender, 1 Turning the Tide |
| Shields / unit upgrades | 3 Kaydel Connix | 1 Village Tender, 2 Turning the Tide |
| Space | 2 Wild Space Wanderer, 1 Collateral Damage | 2 Relentless Hunters, 1 Village Tender |
| Fortify bases | 2 Wild Space Wanderer | 1 Village Tender, 1 Ewok Warrior |

Defenders of the Forest costs 5. Only bring it in when you plan to go to 5 resources, and don't hold resources open for it in game 1.

## Games played

All games were on the SWUSim simulator, with earlier versions of this list. Those versions had the same leader, base and core Ewok package, but no Aggressive Negotiations, V-19 or Turning the Tide. In the first three games the opponent was the built-in bot, which never attacked units. In the last two, both seats were played by Claude.

| Game | Opponent | Result |
|---|---|---|
| 109 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 5 |
| 110 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 4 |
| 113 | Wedge Antilles pilots, 26 HP base (bot) | Won, round 4 |
| 117 | Wedge Antilles pilots, 26 HP base | Lost, round 4, opponent on 10 |
| 118 | Tarfful midrange, 30 HP base | Lost, round 9, opponent on 2 |

After those games, the deck stopped resourcing at 4–5 and kept drawing extra cards off Wicket. The leftover cards in hand are why Aggressive Negotiations is now in the main deck.

### Against Wedge Antilles pilots

- **It is a pure race,** and a well-piloted Wedge deck wins it. Pilots stacked on a 1-cost ship hit for 6 to 8 a round from round 2.
- **Removing the ship:**
  - Reckless Sacrifice can't hit it, because it costs 1.
  - Turning the Tide from a wide board can kill it.
  - A V-19 with Sentinel absorbs some hits.
- **Wicket:** their ground units all cost 1, so deploy him on round 3. Resource the Wicket unit and Logray.
- **Attack before playing cards,** because Razor Crest bounces and Death Space Skirmisher exhausts.

### Against Tarfful midrange

- **Their plan:** they kill your units for seven rounds and then turn on your base. Bo-Katan Kryze at 9 resources gives every unit you control -3/-3, so the game must end by round 8.
- **Wicket:** hold him and take the leader-side draw each round by attacking up. All of their units cost 3 or more.
- **Your best attacker:** Cloud-Rider Veteran, because Tarfful and Koska Reeves are Sentinels and its base damage ignores them. A full-hand Aggressive Negotiations on a Saboteur also gets through.
- **Nightfall:** save it for the last 6 damage. Game 118 was lost with the opponent on 2.

### What to check in the next games

- **Hand size:** how many cards are usually in hand when you cast Aggressive Negotiations. If it's often 3 or fewer, cut one.
- **Sweeper decks:** whether the deck misses the 5-HP Ewok Archers that Aggressive Negotiations replaced.
