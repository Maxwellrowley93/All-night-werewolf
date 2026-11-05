# All Night Werewolf

A phone-based companion app for playing Werewolf in person. One person runs the game as **Game Master (GM)**. Everyone else joins on their own phone with a 4-letter room code, sees their secret role, and submits night actions privately. The app works out what happened each night and writes a script for the GM to read aloud at Town Hall.

**Play it:** https://maxwellrowley93.github.io/All-night-werewolf/

## How to play

### 1. Set up
1. The GM opens the app, enters their name and taps **Create New Game**. The GM's screen shows the room code, who has joined, and the role setup.
2. Players open the app, enter their name and the room code, and tap **Join Game**. You can also share `…/All-night-werewolf/?room=ABCD` and the code is filled in for you.
3. The GM chooses how many of each role to include, or taps **Simple** or **Advanced** under **Quick setup** to fill in a balanced line-up for the players who have joined (see [Suggested line-ups](#suggested-line-ups)), then adjusts it if they like. The role count must match the number of players and include at least one Werewolf. The Mayor, Bard, Scapegoat and Symbiote are limited to one each.
4. The GM sets when **the Final** begins: by default when the number of players left equals the starting Werewolves + 2, adjustable with − and +.
5. The GM sets the **night timer** (5 minutes by default, or Off).
6. The GM taps **Assign Roles & Start Game**. Roles are dealt at random, Night 1 begins, and the GM's controls appear on the **Players**, **Actions** and **Town Hall** tabs.

### 2. Night
- Every player's screen looks the same: a bar showing the phase of the game (Night, Gather, Vote, Banish, Dawn), a status line such as "🐺 2 of 3 still hidden · 🏁 Final at 5 players · 9 left", and a face-down card.
- Each player taps the card to see their role and their action, then taps again to hide it. The card also hides itself after they confirm an action, if they switch apps, and at each new stage of the game.
- The card says which team the player is on: Villager team, Werewolf team, or, for the Jester, no team. When a role is revealed, the GM's script gives the team too.
- Werewolves see the rest of their pack on the card.
- Players with a night ability choose a target on the card and confirm. Abilities that can only be used once per game also have a **Not tonight** button.
- Everyone mingles, schemes and bluffs. If the night timer is on, every phone counts down to Town Hall ("⏳ 3:42 until Town Hall") and buzzes at "⏰ Time to gather!". The timer only informs: the night ends when the GM taps End Night, and the GM can tap **+1 min** to give everyone longer.
- On the **Actions** tab, the GM sees every action as it comes in, a step-by-step preview of how the night will play out, and the script that will be read.
- On the **Players** tab, the GM taps **End Night → Call Everyone to Town Hall** once everyone has acted. If anyone hasn't, the app warns the GM first. Every phone then tells its player to gather.

Nobody dies yet. When the night ends, the Seer gets their result and any Bard, Scapegoat or Symbiote effect starts. Attacks land at dawn, after the vote.

### 3. Town Hall
1. **Gather and discuss.** Every phone shows a call to gather. The **Town Hall** tab gives the GM a script to open the meeting. Lines in quotes are read aloud. Lines in `[brackets]` are notes for the GM only. The village then discusses.
2. **Vote.** The GM taps **Open the Floor to Voting**. Each player selects a player on their own phone and taps **Confirm Vote**. A dead villager's ghost has one final vote: at each Town Hall they either use it or tap **Save My Vote for Later**, and voting waits for that choice. Dead Werewolves and the Jester don't get a ghost vote, and nor does a Symbiote unless their host is a villager who is still alive. A confirmed vote can't be changed. The GM sees who has voted, but not for whom. If someone can't vote, the GM can tap **Close Voting & Reveal**.
3. **Banish.** Once all votes are in, each phone becomes a full-screen landscape blackboard showing only the name its player voted for. The GM calls each name in turn and that player holds up their phone. The GM's phone shows every vote and the tally, with Bard and Scapegoat effects already applied.
4. **Move on.** The GM eliminates whoever leads the vote and reveals their role, or runs a tiebreak vote between the tied players if it's a tie, then taps **Move On — Go to Dawn**.
5. **Dawn.** The night's attacks land and the GM reads out what happened from the script. An attack on someone who has just been voted out is wasted. Choices made before the vote still count even if the player who made them was voted out, so a banished wolf's kill still lands. Anyone who dies becomes a ghost on their phone. The GM then taps **Start Night** to begin the next round, or **Begin the Final** once it's due. If the night's deaths end the game, the GM still reads out who died first, then taps **Reveal the Result**.

### 4. The Final
The Final is the climax: no more nights, only votes. It's due at dawn once the players left reach the number set at the start, or the Werewolves equal everyone else. The GM can also tap **Begin the Final Early**.

Each round of the Final is a Town Hall (Gather, End?, Decision, Vote, Banish):
1. **Gather.** The GM reads the Final's script and the village talks.
2. **End?** The GM taps **Open the End Vote**. Each living player secretly chooses **END** or **BANISH** on their phone.
3. **Decision.** Once everyone has chosen, each phone's blackboard shows END or BANISH, and the GM calls them out. If a majority chose END, the GM taps **End the Game**. Otherwise (a tie or fewer) the GM taps **Banish Someone**.
4. **Vote and banish.** A normal vote, with ghost votes and tiebreaks as usual. Whoever is banished in the Final **doesn't reveal their role**, so from then on the wolf count shows "?". They don't get a ghost vote. The GM then taps **Next Round of the Final**.

The GM can tap **Declare Stalemate & End the Game** at any time in the Final, for example if tiebreaks keep tying.

When the Final ends, the survivors reveal who they are. Each survivor's phone has a **Reveal Who I Am** button: when the GM calls their name, they tap it and their phone fills with their team (🐺 Werewolf, 🏡 Villager and so on) to hold up. The GM then taps **Show the Result**.

### Winning
- **Villagers** win when every Werewolf is dead before the Final, or when the Final ends with no Werewolf among the survivors.
- **Werewolves** win if any Werewolf survives to the end of the Final, or at once if they ever outnumber everyone else still alive. Equal numbers start (or continue) the Final instead.
- **The Jester** wins on their own if the village votes them out at Town Hall, in the Final too.
- With two players left, the game ends automatically.

The app checks for a win after every vote and every dawn, and ends the game automatically.

When the game ends, every phone switches to the result: the winning team in big letters and its colour, then each player's own result (for example "You survived to the end" or "Your team won, but you didn't make it to the end"), then everyone's role grouped by team, with the dead marked 💀. The Symbiote wins or loses with their host, and the Jester with getting voted out. The GM can tap **Play Again with the Same Players** to start a fresh game in the same room: everyone stays in, roles are dealt again and the GM code doesn't change. Werewolves can only win at dawn, once the night's attacks have landed.

## Suggested line-ups

Every wolf kills each night, so the wolves are strong: the village needs roughly one banishment per wolf before the Final. These are what the **Simple** and **Advanced** buttons fill in. Villagers fill the remaining places. They're estimates from the pace of the game, so adjust them once you've seen a few games.

**Simple:** only the classic roles.

| Players | Werewolves | Seer | Doctor | Hunter | Final at |
|---|---|---|---|---|---|
| 5 | 1 | 1 | – | – | 3 |
| 6–8 | 1 | 1 | 1 | – | 3 |
| 9–12 | 2 | 1 | 1 | – | 4 |
| 13–14 | 2 | 1 | 1 | 1 | 4 |
| 15–17 | 3 | 1 | 2 | 1 | 5 |
| 18–20 | 3 | 2 | 2 | 1 | 5 |

**Advanced:** more wolves, balanced by more protection, plus about one chaos role per six players.

| Players | Werewolves | Village roles | Chaos and twists | Final at |
|---|---|---|---|---|
| 5–6 | 1 | Seer, Doctor | – | 3 |
| 7–8 | 1 | Seer, Doctor | Jester | 3 |
| 9–12 | 2 | Seer, Doctor, Witch, Bard | Jester, Hairy Villager | 4 |
| 13–16 | 3 | Seer, 2 Doctors, Witch, Tank, Mayor | Jester, Seductress | 5 |
| 17–20 | 4 | 2 Seers, 2 Doctors, Witch, Tank, Hunter, Mayor, Bard | Jester, Puppetmaster, Seductress, Symbiote, Scapegoat and Hairy Villager, added one at a time from 17 to 20 players | 6 |

## Roles

Each player's card gives their role one short line. The full rules are here, for the GM to explain if a question comes up.

Each player's card gives their role one short line. The full rules are here, for the GM to explain if a question comes up.

| Role | Team | What it does |
|---|---|---|
| 🐺 Werewolf | Wolves | Each night, **every werewolf makes their own kill**. Wolves can split up to kill several players, or team up on one target to get past a Doctor, a healing potion or a Tank. Werewolves can see their pack. They can target anyone, their pack included, but a kill on a Werewolf has no effect. |
| 🏡 Villager | Village | No ability. Use your wits at Town Hall. |
| 🔮 Seer | Village | Each night, inspect a player. When the night ends, before the vote, your phone shows whether they are a Werewolf. |
| ⚕️ Doctor | Village | Each night, protect a player (yourself included). The protection cancels **one** attack on them, either a wolf kill or poison. Two wolves on the same target still get through. |
| 🧙 Witch | Village | One Healing Potion (cancels one wolf attack on a player) and one Poison Potion (kills anyone). Each can be used once, and only one per night. |
| 🎯 Hunter | Village | Once per game, shoot a player at night. Nothing can stop the silver bullet. |
| 🎵 Bard | Village | Once per game, choose a player whose vote counts double at the next Town Hall. The tally counts that vote twice. |
| 🐐 Scapegoat | Village | Once per game, choose a player. At the next Town Hall, every vote against them counts against you instead. The tally applies this automatically. |
| 🃏 Jester | Themselves | Wins by getting voted out at Town Hall. |
| 💋 Seductress | Village | Each night, distract a player. Whatever action they take that night has no effect. |
| 🎭 Puppetmaster | Village | Each night, pick a player to control and a new target for them. Their action hits your chosen target instead. |
| 🔗 Symbiote | Their host's | Must bond with a player on their first night, or the app bonds them to someone at random. They learn their host's exact role, join the host's side and win if the host survives the game. If the host dies, the Symbiote dies too, but not the other way round. The host isn't told. A Symbiote never counts as a Werewolf. Only one per game. |
| ⭐ Mayor | Village | Revealed to everyone when the game starts. |
| 🛡️ Tank | Village | Survives the first night attack (they're wounded and it's announced). The second attack kills, whether it comes on a later night or the same night, so two wolves can kill an unwounded Tank in one night. A Town Hall vote still eliminates them outright. |
| 🧔 Hairy Villager | Village | A Villager, but the Werewolves see them listed as part of their pack. The wolves can still kill them. A kill on a real wolf has no effect, so finding out who the Hairy Villager is costs the pack a kill. The Seer sees them as not a Werewolf. |

### Night resolution order

Actions are worked out in this order. Steps 6 and 7 happen at dawn, after the vote, and everything else happens when the night ends:

1. **Seductress.** Actions from distracted players have no effect, and a distracted Witch keeps her potion.
2. **Puppetmaster.** Controlled players' actions are redirected to the new target.
3. **Symbiote.** The bond is formed, or made at random if the Symbiote didn't bond. It takes effect immediately, so it counts for that round's vote and attacks.
4. **Doctor and the Witch's healing potion.**
5. **Seer.**
6. **Attacks.** Each werewolf's kill (unless it now points at a Werewolf), then poison, then the Hunter's shot. Each protection cancels a single attack: a healing potion stops one wolf kill, and a Doctor's protection stops one wolf kill or poison. For example, two wolves against one Doctor means the target still dies. The Hunter's shot can't be stopped. A Tank who hasn't been hit before survives one hit that gets through, and two hits kill them.
7. **Symbiote deaths.** If the host died, the Symbiote dies too.
8. **Bard and Scapegoat.** Their effects are stored for the next Town Hall.

## If something goes wrong

- **A phone dies or a player taps the wrong name.** On the **Players** tab, the GM taps that player to open their panel. At night the GM can enter their action, with the same choices their phone shows, or clear one so it can be redone. During voting the GM can enter their vote, save a ghost's final vote, change a vote, or clear one so it can be cast again. While voting is open the GM sees whether someone has voted, not who for.
- **A vote is wrong at the reveal.** On the **Town Hall** tab, tap that player's blackboard (or tap them on the Players tab). The GM sees their vote and can change it, or switch a ghost's vote to saved. The tally and the player's blackboard update straight away. If someone has already been eliminated and the change alters the result, bring them back from their panel.
- **The GM eliminates the wrong player.** Tap that player and choose **Bring Back (Undo Elimination)**. This can't undo the end of a game.
- **The GM's phone dies.** The GM's screen shows a 4-digit **GM code**. On any other phone, open the game, enter the room code, tap **Game Master's phone died? Take over here**, enter the GM code and tap **Resume as Game Master**. The game carries on from where it was.
- **Something didn't save.** If a phone loses its connection, it says "Didn't save" and keeps the choice on screen, so the player can tap Confirm again. A night action and its "done" mark always save together.

## Good to know

- **Refreshing is safe.** Each phone remembers its game, so reloading the page or reopening the browser puts you straight back in. A player who loses their place (for example, on a new phone) can rejoin by entering the same name and room code. The GM can take over from another phone with the GM code.
- **No scrolling, full width.** Every in-game screen is laid out compactly and shrinks itself to fit the phone, including with 20 players. On screens wider than a phone, including Android Chrome's **Desktop site** mode, everything scales up to fill the width. The GM's screens also grow their text to fill the phone when there's room, and show the player list one per row or two side by side, whichever allows bigger text.
- **Leave game**, always at the very bottom of the screen, takes a phone out of the current game.
- **Roles are not cryptographically secret.** There are no logins, so anyone with a room code can read that game, including every player's role, or change or delete it. `database.rules.json` stops anyone listing every room, wiping them all at once or adding fields the game doesn't use, and it limits the size of each entry. It can't limit how many entries get added. It's built for friends playing in the same room, not for strangers online.

## Hosting your own copy

The whole app is a single file, `index.html`. There's no build step and nothing to install.

1. **Firebase:** create a free project at https://console.firebase.google.com and add a **Realtime Database**.
2. In the database **Rules**, paste in the contents of `database.rules.json` and publish them.
3. In `index.html`, set `FIREBASE_URL` to your database URL.
4. **Hosting:** any static host works. This repo uses GitHub Pages, serving `index.html` from the `main` branch.

To try it locally, open `index.html` in a browser, or serve the folder with any static server (for example, `npx serve`). It still talks to whichever Firebase database `FIREBASE_URL` points at.

## Testing on one browser

`test.html` runs a Game Master and any number of players side by side, each in its own window on the page. It uses the real game and the real database.

1. Run `python serve.py` and open http://localhost:8123/test.html. Opening the file directly won't work, and `serve.py` stops the browser keeping old copies of the files.
2. Choose how many players you want and tap **New Test Game**. The windows create the room and join it automatically.
3. Set the roles in the Game Master window and start the game. Play each phone by hand, or use **Random** on one window or **Random Choices for Everyone Waiting** on all of them.

Windows waiting for a choice have an orange border. Reloading the page returns to the same game. **New Test Game** and **Delete Test Game** remove the test room from the database.

## How it works

- Plain HTML, CSS and JavaScript in one file, with no framework or dependencies apart from Google Fonts.
- Game state is stored in the Firebase Realtime Database through its REST API, so no Firebase SDK is needed. Each phone checks the game every 2 seconds and redraws when something changes.
- Each phone remembers which game it's in using `localStorage`.
- All night logic lives in a single function, `resolveNight()`. It drives the GM's live preview, the actual end-of-night result, and the Town Hall script, so all three always agree.
