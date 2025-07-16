# 🐍 Snake Water Gun Game

A simple command-line version of the classic **Snake, Water, Gun** game built using Python.

This game is a fun way to practice Python fundamentals such as conditionals, user input, randomness, and file handling.

---

## 🕹️ How to Play

- **s** for Snake  
- **w** for Water  
- **g** for Gun  

The game logic is:
- Snake drinks Water → Snake wins
- Water douses Gun → Water wins
- Gun kills Snake → Gun wins

If both the player and computer choose the same item, it's a **draw**.

---

## 🏆 Scoring System

- The game consists of **5 rounds**.
- Points per round:
  - Win → **+2 points**
  - Draw → **+1 point**
  - Loss → **0 points**
- After 5 rounds, your **total score** is calculated.

### 🔥 High Score Tracking
- A file named `hs.txt` is used to **store the highest score** ever achieved.
- If your current total score is higher than the stored high score, the file gets updated.
- Otherwise, it remains unchanged.

This lets you challenge yourself or your friends to **beat the high score** over multiple runs!

---

## 🚀 Running the Game

1. Make sure you have Python installed.
2. Open your terminal and navigate to the project directory:
   ```bash
   cd "Snake Water Gun Game"
   ```

3. Run the game:
   ```bash
   python main.py
   ```

---

## 📁 File Structure

```nginx
Snake Water Gun Game/
├── main.py         # Contains the game logic and high score feature
├── hs.txt          # Stores the high score
└── README.md       # You're reading it
```

---

## ✅ Features

- Round-based scoring system
- High score saved between sessions
- Input validation to prevent invalid entries
- Clean and modular game logic
- Randomized computer choice for fairness

> **Note:** This is a beginner-friendly project meant for learning and demonstration purposes. Feel free to improve or expand it!
