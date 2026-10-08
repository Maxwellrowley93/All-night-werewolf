# All Night Werewolf

A phone-based companion app for playing Werewolf in person. One person runs the game as **Game Master (GM)**. Everyone else joins on their own phone with a 4-letter room code, sees their secret role, and submits night actions privately. The app works out what happened each night and writes a script for the GM to read aloud at Town Hall.

**Play it:** https://maxwellrowley93.github.io/All-night-werewolf/

## How to play

### 1. Set up
1. The GM opens the app, enters their name and taps **Create New Game**.
2. Players open the app, enter their name and the room code, and tap **Join Game**. You can also share `…/All-night-werewolf/?room=ABCD` and the code is filled in for you.
3. On the **Setup** tab, the GM chooses how many of each role to include. The role count must match the number of players and include at least one Werewolf. The GM also sets **Rounds before Town Hall**.
4. The GM taps **Assign Roles & Start Game**. Roles are dealt at random and Night 1 begins.

### 2. Night
- Each player taps their role card to see their role, then taps again to hide it. The card also hides itself if they switch apps.
- Werewolves can see the rest of their pack.
- Players with a night ability choose a target on their phone and confirm. Abilities that can only be used once per game also have a **Not tonight** button.
- Everyone mingles, schemes and bluffs.
- On the **Actions** tab, the GM sees every action as it comes in, a step-by-step preview of how the night will play out, and the script that will be read.
- On the **Players** tab, the GM ends the night with either:
  - **End Night → Start Night N**, to play another night, or
  - **End Night → Call Town Hall**, which gets highlighted once the configured number of nights has passed.

Deaths are applied as soon as a night ends. Eliminated players become ghosts on their phones.

### 3. Town Hall
- The **Town Hall** tab shows a script covering every night since the last Town Hall. Lines in quotes are read aloud. Lines in `[brackets]` are notes for the GM only.
- The village discusses and votes. The GM counts the votes with the +/− buttons, and ghost votes are added automatically.
- The GM eliminates whoever leads the vote, or runs a tiebreak if it's a tie, then taps **Start Night** to begin the next round.

### Winning
- **Villagers** win when every Werewolf is dead.
- **Werewolves** win when they equal or outnumber everyone else still alive.
- **The Jester** wins on their own if the village votes them out at Town Hall.

The app checks for a win after every night and every elimination, and ends the game automatically.

## Roles

| Role | Team | What it does |
|---|---|---|
| 🐺 Werewolf | Wolves | Each night, **every werewolf makes their own kill**. Wolves can split up to kill several players, or team up on one target to get past a Doctor, a healing potion or a Tank. Werewolves can see their pack. |
| 🏡 Villager | Village | No ability. Use your wits at Town Hall. |
| 🔮 Seer | Village | Each night, inspect a player. When the night ends, your phone shows whether they are a Werewolf. |
| ⚕️ Doctor | Village | Each night, protect a player (yourself included). The protection cancels **one** attack on them, either a wolf kill or poison. Two wolves on the same target still get through. |
| 🧙 Witch | Village | One Healing Potion (cancels one wolf attack on a player) and one Poison Potion (kills anyone). Each can be used once, and only one per night. |
| 🎯 Hunter | Village | Once per game, shoot a player at night. Nothing can stop the silver bullet. |
| 🎵 Bard | Village | Once per game, choose a player whose vote counts double at the next Town Hall. The GM is reminded to count that vote twice. |
| 🐐 Scapegoat | Village | Once per game, choose a player. At the next Town Hall, every vote against them counts against you instead. The vote tracker applies this automatically. |
| 🃏 Jester | Themselves | Wins by getting voted out at Town Hall. |
| 💋 Seductress | Village | Each night, distract a player. Whatever action they take that night has no effect. |
| 🎭 Puppetmaster | Village | Each night, pick a player to control and a new target for them. Their action hits your chosen target instead. |
| 🔗 Symbiote | Village | Once per game, bond with a player. From then on, if either of you dies, so does the other. |
| ⭐ Mayor | Village | Revealed to everyone when the game starts. |
| 🛡️ Tank | Village | Survives the first night attack (they're wounded and it's announced). The second attack kills, whether it comes on a later night or the same night, so two wolves can kill an unwounded Tank in one night. A Town Hall vote still eliminates them outright. |
| 🧔 Hairy Villager | Village | A Villager, but the Werewolves see them listed as part of their pack. The Seer sees them as not a Werewolf. |

### Night resolution order

When the night ends, actions are applied in this order:

1. **Seductress.** Actions from distracted players have no effect, and a distracted Witch keeps her potion.
2. **Puppetmaster.** Controlled players' actions are redirected to the new target.
3. **Symbiote.** The bond is formed. It takes effect immediately, so it counts for deaths that same night.
4. **Doctor and the Witch's healing potion.**
5. **Seer.**
6. **Attacks.** Each werewolf's kill, then poison, then the Hunter's shot. Each protection cancels a single attack: a healing potion stops one wolf kill, and a Doctor's protection stops one wolf kill or poison. For example, two wolves against one Doctor means the target still dies. The Hunter's shot can't be stopped. A Tank who hasn't been hit before survives one hit that gets through, and two hits kill them.
7. **Symbiote deaths.** If one bonded player died, their partner dies too.
8. **Bard and Scapegoat.** Their effects are stored for the next Town Hall.

## Good to know

- **Refreshing is safe.** Each phone remembers its game, so reloading the page or reopening the browser puts you straight back in. A player who loses their place (for example, on a new phone) can rejoin by entering the same name and room code. The GM can only resume on the device that created the game.
- **Leave game** at the bottom of the screen takes a phone out of the current game.
- **Roles are not cryptographically secret.** All game data, including every player's role, is stored in an open Firebase database. Someone determined could read it with their browser's developer tools. It's built for friends playing in the same room, not for strangers online.

## Hosting your own copy

The whole app is a single file, `index.html`. There's no build step and nothing to install.

1. **Firebase:** create a free project at https://console.firebase.google.com and add a **Realtime Database**.
2. In the database **Rules**, allow reads and writes to the `games` path:
   ```json
   {
     "rules": {
       "games": { ".read": true, ".write": true }
     }
   }
   ```
3. In `index.html`, set `FIREBASE_URL` to your database URL.
4. **Hosting:** any static host works. This repo uses GitHub Pages, serving `index.html` from the `main` branch.

To try it locally, open `index.html` in a browser, or serve the folder with any static server (for example, `npx serve`). It still talks to whichever Firebase database `FIREBASE_URL` points at.

## How it works

- Plain HTML, CSS and JavaScript in one file, with no framework or dependencies apart from Google Fonts.
- Game state is stored in the Firebase Realtime Database through its REST API, so no Firebase SDK is needed. Each phone checks the game every 2 seconds and redraws when something changes.
- Each phone remembers which game it's in using `localStorage`.
- All night logic lives in a single function, `resolveNight()`. It drives the GM's live preview, the actual end-of-night result, and the Town Hall script, so all three always agree.
