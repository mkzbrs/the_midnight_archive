# 🕰️ The Midnight Archive

- **Universiti Utara Malaysia**
- **Course:** STTHK2123 Interaction System and Tools (Session A252) 
- **Instructor:** Dr. Nurul Izzah Binti Abdul Aziz 
- **Engine:** Ren'Py Visual Novel Engine 

---

## 📖 1. Project Summary & Objectives

Currently, many narrative games allow players to progress by just clicking randomly without understanding the story. "Midnight Archive" aims to solve this by creating a dialogue-based mystery game where every choice matters. 

The game relies on a time-loop system. If the player makes a logical mistake, the system resets them to the beginning. This forces players to actively learn from their mistakes and understand the story to win.

**Key Objectives:**
* **Active Engagement:** Require players to actively pay attention to hints to progress.
* **Recalling Memory:** Improve the player's memory by forcing them to use previously discovered clues to make correct decisions.
* **Critical Thinking:** Challenge players with mysteries that require logical reasoning (not just guessing).
* **Learning from Mistakes:** Use a time-loop retry system ("Imperfect Memory") that guides players toward the right decisions instead of a traditional "Game Over".

---

## 🎭 2. Story Plot & Core Mechanics

### The Story
The year is 2030. The main character, Alice, is an exhausted student who falls asleep in the library. She wakes up at exactly midnight (00:00) to find the school completely locked and frozen in time. She is trapped in a "Temporal Blindspot"—a gap in reality where time and memory are unstable. 

She meets a mysterious girl named Aura, a "Memory Keeper". Aura asks Alice to help her collect missing pieces of time called "Echoes" to fix a book called the "Lost Record". If Alice succeeds, Aura will send her back to the real world. 

### Core Gameplay Mechanics
* **Imperfect Memory (The Time Loop):** If Alice makes a wrong choice or fails a puzzle, reality "shatters". Time resets back to the moment she woke up in the library. 
* **Knowledge is Power:** Even though time resets, Alice keeps the clues and notes she found. She uses this knowledge to choose the correct path on her next attempt.

### Planned Puzzles
* **Constellation Puzzle:** The player finds a torn astronomy page, goes to the Courtyard, and must drag-and-drop constellation lines to match the stars in the sky.
* **History Riddle:** The player must gather information scattered around the school about a past artist to answer a specific riddle.
* **Timeline Puzzle:** The player finds scattered notes and must arrange them in the correct chronological order.

---

## 🕹️ 3. Interaction System & User Flow

The game is built with a simple, clean simulation interface. 
* **Explicit Inputs:** Clicking on dialogue choices to answer Aura. 
* **Implicit Inputs:** Clicking on the screen to search for hidden items (like the torn astronomy page).
* **User Interface (GUI):** Features an Inventory to store found hints, and a Fast-Travel Map to instantly move between the Courtyard, the Cafe, and the Playground.
* **System Output & Feedback:** The game provides visual feedback through layered character sprites and background changes. If a mistake is made, the screen uses an animation effect to "shatter" like glass before resetting. Aura also provides verbal feedback (e.g., "That didn't happen... try to remember it correctly").

---

## 🎯 4. Target Audience
* **Teenagers and Young Adults (Ages 16-25):** Users familiar with visual novels and interactive storytelling.
* **Mystery Solvers:** Players who enjoy narrative games that require critical decision-making.
* **Challenge Seekers:** Users who do not mind failing and are ready to overcome difficulties through trial and error.

---

## 👨‍💻 5. Team Roles & Responsibilities

| Name | Matric No. | Role | Responsibilities |
| :--- | :--- | :--- | :--- |
| **Muhammad Khuzaimi Bin Ramli** | 307261 | **Lead Developer** | Writing the Ren'Py scripts, programming the time-loop system, managing variables, and managing GitHub. |
| **Adam Haris Bin Amran** | 307106 | **UI/UX Designer** | Designing the interface mockups, drawing the fast-travel map, and setting up the screen layouts. |
| **Muhammad Dany Iskandar Bin Mohd Shahir** | 307321 | **Lead Writer** | Drafting all dialogue between Alice and Aura, writing the riddles, and creating the text for clue notes. |
| **Muhammad Hazri Bin Mohammad Zahir** | 306894 | **QA & Testing** | Playing the game to find errors, running Usability Testing, and gathering player feedback scores. |

---

## 🛠️ 6. Software & Development Tools
* **Ren'Py:** The main visual novel engine used to build the game.
* **GitHub:** Used to store the game files online so the team can work together without deleting each other's progress.
* **Visual Studio Code:** The code editor used to write the game scripts.
* **Ibis Paint:** Used to draw character sprites and edit backgrounds.
* **Google Docs:** Used for collaborative writing on reports and proposals.

---

## 📅 7. Development Checklist & Status Tracker

### Phase 1: Project Proposal (Due Week 4)
- [x] Define Target Users & Objectives.
- [x] Answer Nielsen's 9 Usability Questions.
- [x] Submit Proposal Document to Dr. Nurul Izzah.

### Phase 2: Basic Prototype (Due Weeks 8-10)
- [ ] Code the starting scene (Alice waking up at 00:00).
- [ ] Add the first introductory dialogue with Aura.
- [ ] Build the interactive fast-travel map (Courtyard, Cafe, Playground).
- [ ] Create the first working interaction (finding a clue on the ground).
- [ ] Code the loop system so the game successfully resets upon failure.
- [ ] Submit Progress Report and present the working prototype.

### Phase 3: Final Game & Evaluation (Due Weeks 13-14)
- [ ] Add all remaining puzzles (Constellation, History, Timeline).
- [ ] Code the final ending (fixing the "Lost Record" book).
- [ ] Conduct formal user testing.
- [ ] Write the Final Article Report with screenshots and test results.
- [ ] Final Project Presentation.

---

**Khuzaimi (Lead Developer)**
- Your main job is to put the game together in Ren'Py and make sure it actually runs.

* **Week 1 (Phase 1):**
- Set up the GitHub repository.
* **Weeks 8–10 (Phase 2):** 
- Write the Ren'Py code to make the game start at the library.
- Code the conversation menu so the player can choose answers when talking to Aura.
- Code the "Imperfect Memory" time-loop: Make the game restart if the player chooses the wrong answer.
* **Weeks 13–14 (Phase 3):** 
- Put Adam's art and Dany's writing into the game.
- Code the final puzzles (like making the constellation puzzle clickable).
- Build the final game file (.exe / .app) so the lecturer can play it.

**Adam (UI/UX Designer)**
- Your main job is to create how the game looks and how the player clicks on things.

* **Week 1 (Phase 1):** 
- Sketch out a simple, clean interface. Decide where the text box goes and what the buttons look like.
* **Weeks 8–10 (Phase 2):** 
- Draw the Fast-Travel Map screen showing the Courtyard, Cafe, and Playground.
- Find or draw the background image for the Library and the character art for Aura using Ibis Paint.
- Design a simple "Inventory" button so players can see the clues they collect.
* **Weeks 13–14 (Phase 3):** 
- Create the visual effects, like the "shattered glass" screen effect when the player fails and time resets.
- Create the glowing effect for the "Lost Record" book at the end of the game.

**Dany (Lead Writer)**
- Your main job is to write everything the characters say and the clues the player finds.

* **Week 1 (Phase 1):** 
- Write a short summary of what happens in each of the 7 scenes.
* **Weeks 8–10 (Phase 2):** 
- Write the exact script for Alice waking up at 00:00.
- Write the first conversation between Alice and Aura. You must write both the "correct" choices and the "wrong" choices that cause the game to restart.
- Write the text for the first hidden clue (the torn astronomy page).
* **Weeks 13–14 (Phase 3):** 
- Write the riddles for the History puzzle and the Timeline puzzle.
- Write the final ending conversation where Aura says goodbye and Alice wakes up in the real world.

**Hazri (QA Tester & Evaluator)**
- Your main job is to play the game, find bugs, and write the final testing report for the class.

* **Week 1 (Phase 1):** 
- Read through the project proposal and double-check that the 9 Usability Questions make sense before handing it in.
* **Weeks 8–10 (Phase 2):** 
- Play first version of the game.
- Click every wrong answer on purpose to make sure the game successfully restarts.
- Tell Adam if the map buttons are too small or confusing.
* **Weeks 13–14 (Phase 3):** 
- Give the finished game to 3-5 friends outside the group to play.
- Ask them to fill out the System Usability Scale (SUS) survey.
- Write the "Findings and Discussion" and "Limitations" sections of the final report based on what those testers said.

---

## 📊 8. Evaluation Plan

To prove the game is successful, the team will test the final prototype using two methods:
1. **System Usability Scale (SUS):** A 10-question survey given to testers to measure how easy the game is to play. Our target score is above **80.3 (Grade A)**.
2. **Narrative Engagement Scale (NES):** We will measure if the player successfully transitioned from passive clicking to active learning by asking if they understand the story, if the hints were helpful, and if they felt engaged in solving the mystery.

---

## 💻 9. GitHub Guide: How to Work on This Project

To edit the game, you need to download the files from this page to your computer, make your changes, and send them back.

## 💻 How to Work on This Project (Terminal Guide)

To keep the game from breaking, **no one should make changes directly to the `main` branch.** Everyone will create their own branch, do their work there, and then ask for it to be merged into the main game.

**Step 1: First-Time Setup (Downloading the Game)**
If you haven't downloaded the game yet, open your terminal and run:
```bash
git clone https://github.com/mkzbrs/the_midnight_archive.git
cd the_midnight_archive
```

**Step 2: Before You Start Working (Getting Updates)**
Always do this so you have the newest code before making any changes:
```bash
git checkout main
git pull origin main
```

**Step 3: Creating Your Own Branch**
Never work directly on main. Create a safe workspace using your name and task:
```bash
# Example: git checkout -b adam-map-ui
git checkout -b <your-name>-<your-task>
```

**Step 4: Saving Your Work**
After making your edits in Ren'Py, save your work and upload it to GitHub:
```bash
# 1. Add all the files you changed
git add .
# 2. Add a short message explaining what you did
git commit -m "Finished the Courtyard map"
# 3. Upload your branch to GitHub
git push origin <your-branch-name>
```

**Step 5: Sending Your Work to the Main Game (Pull Request)**
When your task is completely done and you want Khuzaimi to add it to the final game:

1. Go to the project page on the GitHub website.
2. You will see a green Compare & pull request button for your newly pushed branch. Click it.
3. Click Create Pull Request.
4. Khuzaimi will review your code. If it looks good, he will merge it into the main game!

---

## Documentation

Google Docs: https://docs.google.com/document/d/1ELHNrHG6babtiUP31xfW9z8-q5sOIPVJZI_9cQKYfJU/edit?usp=sharing