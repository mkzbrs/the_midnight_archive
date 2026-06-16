# The Midnight Archive

- **Universiti Utara Malaysia**
- **Course:** STTHK2123 Interaction System and Tools (Session A252) 
- **Instructor:** Dr. Nurul Izzah Binti Abdul Aziz 
- **Engine:** Ren'Py Visual Novel Engine 

---

## 1. Project Summary & Objectives

Currently, many narrative games allow players to progress by just clicking randomly without understanding the story. "Midnight Archive" aims to solve this by creating a dialogue-based mystery game where every choice matters. 

The game relies on a time-loop system. If the player makes a logical mistake, the system resets them to the beginning. This forces players to actively learn from their mistakes and understand the story to win.

**Key Objectives:**
* **Active Engagement:** Require players to actively pay attention to hints to progress.
* **Recalling Memory:** Improve the player's memory by forcing them to use previously discovered clues to make correct decisions.
* **Critical Thinking:** Challenge players with mysteries that require logical reasoning (not just guessing).
* **Learning from Mistakes:** Use a time-loop retry system ("Imperfect Memory") that guides players toward the right decisions instead of a traditional "Game Over".

---

## 2. Story Plot & Core Mechanics

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

## 3. Interaction System & User Flow

The game is built with a simple, clean simulation interface. 
* **Explicit Inputs:** Clicking on dialogue choices to answer Aura. 
* **Implicit Inputs:** Clicking on the screen to search for hidden items (like the torn astronomy page).
* **User Interface (GUI):** Features an Inventory to store found hints, and a Fast-Travel Map to instantly move between the Courtyard, the Cafe, and the Playground.
* **System Output & Feedback:** The game provides visual feedback through layered character sprites and background changes. If a mistake is made, the screen uses an animation effect to "shatter" like glass before resetting. Aura also provides verbal feedback (e.g., "That didn't happen... try to remember it correctly").

---

## 4. Target Audience
* **Teenagers and Young Adults (Ages 16-25):** Users familiar with visual novels and interactive storytelling.
* **Mystery Solvers:** Players who enjoy narrative games that require critical decision-making.
* **Challenge Seekers:** Users who do not mind failing and are ready to overcome difficulties through trial and error.

---

## 5. Team Roles & Responsibilities

| Name | Matric No. | Role | Responsibilities |
| :--- | :--- | :--- | :--- |
| **Muhammad Khuzaimi Bin Ramli** | 307261 | **Lead Developer** | Writing the Ren'Py scripts, programming the time-loop system, managing variables, and managing GitHub. |
| **Adam Haris Bin Amran** | 307106 | **UI/UX Designer** | Designing the interface mockups, drawing the fast-travel map, and setting up the screen layouts. |
| **Muhammad Dany Iskandar Bin Mohd Shahir** | 307321 | **Lead Writer & Dialouge Scripter** | Drafting and implement all dialogue between Alice and Aura, writing the riddles, and creating the text for clue notes. |
| **Muhammad Hazri Bin Mohammad Zahir** | 306894 | **QA & Audio Programmer** | Implement sound effect, running Usability Testing, and gathering player feedback scores. |

---

## 6. Software & Development Tools
* **Ren'Py:** The main visual novel engine used to build the game.
* **GitHub:** Used to store the game files online so the team can work together without deleting each other's progress.
* **Visual Studio Code:** The code editor used to write the game scripts.
* **Ibis Paint:** Used to draw character sprites and edit backgrounds.
* **Google Docs:** Used for collaborative writing on reports and proposals.

---

## 7. Development Checklist & Status Tracker

### Phase 1: Project Proposal (Due Week 4)
- [x] Define Target Users & Objectives.
- [x] Answer Nielsen's 9 Usability Questions.
- [x] Submit Proposal Document to Dr. Nurul Izzah.

### Phase 2: Basic Prototype (Due Weeks 8-10)
- [x] Code the starting scene (Alice waking up at 00:00).
- [x] Add the first introductory dialogue with Aura.
- [x] Build the interactive fast-travel map (Courtyard, Cafe, Playground).
- [x] Create the first working interaction (finding a clue on the ground).
- [x] Code the loop system so the game successfully resets upon failure.
- [x] Submit Progress Report and present the working prototype.

### Phase 3: Final Game & Evaluation (Due Weeks 13-14)
- [x] Add all remaining puzzles (Constellation, History, Timeline).
- [x] Code the final ending (fixing the "Lost Record" book).
- [x] Conduct formal user testing.
- [x] Write the Final Article Report with screenshots and test results.
- [x] Final Project Presentation.

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

**Dany (Lead Writer & Dialogue Scripter)**
- Your main job is to write the entire story, characters' dialogue, and clues, AND format all of this text directly into the game's script files so it appears in the actual game.
* **Week 1 (Phase 1):**
- Write a short summary of what happens in each of the 7 scenes to guide the team.
- Learn the basic format for writing text in the game engine (for example, typing ⁠aura "Wake up, Alice."⁠ instead of just writing it like a normal script).
* **Weeks 8–10 (Phase 2):**
- Write the full dialogue and story for the first half of the game directly into the script files in the shared Google Drive.
- Type out all conversations into the code, ensuring you include both the "correct" dialogue paths and the text for the "wrong" choices that trigger the game to restart.
- Write and format the narrative text for the early-game hidden clues so they are ready for the developer to use.
* **Weeks 13–14 (Phase 3):**
- Write and format all the text for the remaining scenes, including the riddles and puzzles for the second half of the game, directly into the script files.
- Type out the complete ending sequence so the final conversations are fully implemented in the game.
- Do a final read-through of the script files to fix any typos, grammar mistakes, or coding format errors before the final game is built.

**Hazri (Audio Programmer & QA Tester)**
- Your main job is to add the music, sound effects, and visual settings into the game code, and handle the final testing and written report. You must upload your code changes directly to GitHub.

* **Week 1 (Phase 1):**
- Open the game's settings file and type in the basic info (the game's title, version number, and the "About" text).
- Find free, non-copyrighted background music and sound effects. Create an audio folder in the game files, put the music there, and upload it to GitHub.
* **Weeks 8–10 (Phase 2):**
- Open the game's visual settings file and change the code to match Adam's design (change the font style, text size, and make the text box transparent).
- Type the code to make the music and sound effects play at the right times during the story (like a clicking sound for buttons, or library music when the game starts).
- Type the code to add simple "fade in" and "fade out" effects when the scenes change. Upload all your code changes to GitHub.
* **Weeks 13–14 (Phase 3):**
- Write the code for the final Credits Screen at the end of the game, listing all our names and where you got the audio files. Upload this final code to GitHub.
- Give the finished game to 20 friends outside the group to play and ask them to fill out the usability survey.
- Write the "Methodology", "Findings and Discussion", and "Limitations" sections of our final written report based on what those testers said.

---
STRICT POLICY: NO COMMITS = NO CREDIT. YOU MUST PUSH ALL YOUR CHANGES TO THE GITHUB REPOSITORY. EVERY COMMIT MUST BE MADE ON YOUR OWN PERSONAL BRANCH "YOURNAME-BRANCH" AND YOU MUST SUBMIT A PULL REQUEST TO MERGE IT. ONLY PULL REQUESTS WILL BE CALCULATED AS VALID COMMITS. IF YOU HAVE ZERO MERGE REQUESTS, YOUR NAME WILL BE PERMANENTLY REMOVED FROM THE FINAL PROJECT REPORT.
---

## 8. Evaluation Plan

To prove the game is successful, the team will test the final prototype using two methods:
1. **System Usability Scale (SUS):** A 10-question survey given to testers to measure how easy the game is to play. Our target score is above **80.3 (Grade A)**.
2. **Narrative Engagement Scale (NES):** We will measure if the player successfully transitioned from passive clicking to active learning by asking if they understand the story, if the hints were helpful, and if they felt engaged in solving the mystery.

---

## 9. GitHub Guide: How to Work on This Project

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

Google Drive: [https://docs.google.com/document/d/1ELHNrHG6babtiUP31xfW9z8-q5sOIPVJZI_9cQKYfJU/edit?usp=sharing](https://drive.google.com/drive/folders/18Z0NYSGKPRSYWcnHXXaScC0-gwph-M2v?usp=share_link)
