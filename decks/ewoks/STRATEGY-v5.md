# Wicket Ewok Swarm (v5) — analysis and pilot guide

Decklist: `ewoks-v5.json` (leader `HMW_014` Wicket, base `HMW_023` Bright Tree Village).

v5 is a chip-damage aggro deck: it wins by turn 6–8 through many small attacks plus repeatable base damage, and it loses if a sweeper resets it or the game goes long. Nothing here has been playtested; the percentages are calculated, and the hand-size and sideboard advice are estimates.

Rule references are to `rules/SWU_Rules_v9_0.pdf` (v9.0).

## Analysis

1. **Game-stage plan**
   - **Early (turns 1–3):** 24 units cost 2 or less, so you have a turn-1 play 99% of the time. Wicket deploys turn 3.
   - **Mid (turns 4–6):** two cards a turn, while Cloud-Rider Veteran and Red Squadron Y-Wing chip the base every round.
   - **Late (turn 7+):** only three Relentless Hunters and two Defenders of the Forest cost more than 3.
2. **Curve:** 7 / 20 / 18 / 3 / 2, average cost 2.46. It fits the plan; the two 5-drops give spare resources somewhere to go.
3. **Leader and base:** 33 of 38 units cost 3 or less, so deployed Wicket's draw and Leia's heal are almost always live. The Endor base powers 9 cards (Troublemaker, Adamant Ewoks, Nightfall).
4. **Weaknesses**
   - **Sweepers:** recovery is only Wicket's draw and Stormchaser.
   - **Low power:** eight units have 1 power, so you kill things with pings, not combat.
   - **Sentinel is conditional or late:** Kryze needs another exhausted unit, V-19 needs three units, Stalwart costs 3.
   - **Few Saboteurs:** 7, so a Sentinel wall blocks most of your ground attacks.
   - **Ewok payoff is thin:** 15 Ewoks, and only Teebo cares.
5. **Matchups:** slightly favourable against aggro, space and ramp; even against midrange and leader-combo; slightly unfavourable against control.

## How to pilot it

### Mulligan and resources

- **Keep** any six with two units costing 2 or less, or one plus a 3-drop. Don't mulligan looking for a Sentinel or Leia; the mulligan replaces the whole hand and you must keep the new one (p. 22).
- **Resource first:** Defenders, Relentless Hunters, Aggressive Negotiations, and second copies of Leia or Logray.
- **Don't resource your only Disaster** while you hold Stormchaser. It has to be revealed from hand or already be in your discard pile.
- **Stop at 5 or 6 resources.** Go to 6 only if you hold Defenders plus cheap cards to play alongside it.

### Turn by turn

- **Turn 1:** in order of preference: Cloud-Rider Veteran or Y-Wing (they start chipping on turn 2), Adamant Ewoks (1 to the base), or Leia plus Troublemaker. Play Stormchaser only if you can show a Disaster.
- **Turn 2:** a 2-drop plus a 1-drop, or Stalwart / V-19. Ewok Archers only if you already have a cheap unit and they have something to ambush.
- **Turn 3:** first attack a more expensive unit with a small one and exhaust Wicket to draw. Then deploy him, since he can deploy exhausted and enters ready (3.4.4, p. 15), and attack with him for a second draw.
- **Turns 4–6:** two cards a turn. Cloud-Rider and Y-Wing attack every round. Make sure a Sentinel is active before you run out of actions.
- **Turn 7+:** count damage and close with Aggressive Negotiations or Nightfall on a Saboteur unit.

### When not to deploy Wicket on turn 3

- **Deploy immediately** if the opponent has no units, because the leader side draws nothing then.
- **Hold him** if their board would kill a 2/5 for free and they keep playing expensive units, because the leader side keeps drawing safely.
- If he is defeated he flips back and can't redeploy, but his leader-side draw works again.

### Card-specific lines

- **Wicket's leader-side draw** is once per round. Take it on the first eligible attack. The Beast token costs 0 (3.7, p. 18), so it qualifies against any unit.
- **Warrior of Clan Kryze:** Sentinel needs *another* exhausted unit. Units enter play exhausted, so playing anything switches it on. It is off at the start of each round until you act.
- **V-19 Skirmisher:** it counts itself toward the three units. Its Sentinel only guards the space arena (7.5.11, p. 32).
- **Logray:** every time one of your cheap units takes damage, you ping. Attack into units with Logray out, and put Run Amok's friendly damage on the Beast for an extra ping.
- **Leia:** play her before your other units. She does nothing while your base is undamaged, so she isn't urgent on turn 1.
- **Cloud-Rider Veteran:** the 2 base damage happens whatever it attacks. Attacking a unit that costs 3 or more gets the base damage and Wicket's leader-side draw.
- **Y-Wing:** the 3 indirect damage is unpreventable and the opponent chooses the split (8.35, p. 47). Attack the base unless a space unit must die.
- **Nightfall:** you need a ready unit for the attack half. The best targets are Troublemaker or Hunters (Saboteur) and Cloud-Rider (5 to the base in total).
- **Aggressive Negotiations:** play it before your other cards that turn, on a Saboteur unit. It counts the hand after it leaves.
- **Turning the Tide:** cast it before your attacks trade units away. It counts both arenas, Wicket and Beasts, and it can hit space.
- **Defenders of the Forest:** treat it as a removal spell. Ambush for 5 (7.5.5, p. 31), with Overwhelm sending the excess to the base; it will usually die afterwards.
- **Wicket the unit:** it can't attack bases. Use it to snipe behind Sentinels and to attack up for draws.

### Initiative

Taking the initiative ends your actions for the round, so take it only when you have nothing better left. It is worth more than usual here in two cases: when your Hidden units from this round need to attack before they can be attacked, and when Kryze needs you to act first next round to switch Sentinel on.

### Playing around sweepers

Once you have about four units out against a control deck, stop adding more and hold two units in hand. Cloud-Rider and Y-Wing keep the clock going on their own, and the held cards make Aggressive Negotiations bigger.

### Sideboard starting points

| Against | In | Out |
|---|---|---|
| Fast aggro | 1 Collateral Damage | 1 Aggressive Negotiations |
| Midrange | 2 Han Solo, 1 Defenders of the Forest | 3 Warrior of Clan Kryze |
| Control | 2 Han Solo, 1 Aggressive Negotiations | 3 Stalwart Fleet Trooper |
| Shields / unit upgrades | 3 Kaydel Connix | 2 Turning the Tide, 1 Collateral Damage |
| Fortify bases | 2 Wild Space Wanderer | 2 Turning the Tide |

Kaydel has Plot: if you bring her in, resource her early and play her from your resources when Wicket deploys.
