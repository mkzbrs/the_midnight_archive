# 🕰️ The Midnight Archive: A Problem-Solving Visual Novel

**Course:** STTHK2123 Interaction System and Tools (Session A252)
**Instructor:** Dr. Nurul Izzah Binti Abdul Aziz 
**Engine:** Ren'Py Visual Novel Engine 

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

## 📊 8. Evaluation Plan

To prove the game is successful, the team will test the final prototype using two methods:
1. **System Usability Scale (SUS):** A 10-question survey given to testers to measure how easy the game is to play. Our target score is above **80.3 (Grade A)**.
2. **Narrative Engagement Scale (NES):** We will measure if the player successfully transitioned from passive clicking to active learning by asking if they understand the story, if the hints were helpful, and if they felt engaged in solving the mystery.

---

## 💻 9. GitHub Guide: How to Work on This Project

To edit the game, you need to download the files from this page to your computer, make your changes, and send them back.

### Step 1: Downloading the Game (First Time Only)
1. Download and install **GitHub Desktop**.
2. Sign in with your GitHub account.
3. Click on **File > Clone Repository**.
4. Click the **URL** tab and paste the link to this project page.
5. Choose a folder on your computer to save it, and click **Clone**.

### Step 2: Opening the Game in Ren'Py
1. Open your **Ren'Py Launcher**.
2. Click **Preferences > Projects Directory**.
3. Select the folder where you saved the GitHub files in Step 1.
4. "Midnight Archive" will now appear in your Ren'Py menu. Click it to launch or edit the game!

### Step 3: Getting Updates & Saving Your Work (Do This Every Time)
* **BEFORE you start working:** Open GitHub Desktop and click the **Fetch Origin** (or **Pull Origin**) button at the top. This downloads any new code Khuzaimi has written so you don't break the game.
* **AFTER you finish working:** In GitHub Desktop, type a short message in the bottom left corner explaining what you added (e.g., "Added dialogue for Scene 2"), click **Commit to main**, and then click **Push Origin** to upload your work to the internet.