# first_python_projects

This repository contains my first Python programs — small, functional scripts I wrote while learning the basics.

---

## 1. Password Strength Checker

A command-line Python tool that scores password strength based on length, character variety, predictability, and membership in a common-password list.

### How it works

- **Common-password check (instant fail):** if the password matches an
  entry in a known-weak list, it scores 0 and stops there — no partial
  credit for a bad password just because it also has a digit in it.
- **Length (0–3 points):** 8+ chars = 1, 12+ = 2, 16+ = 3. Length
  contributes more to real-world entropy than any single character class,
  so it's weighted accordingly.
- **Character variety (0–4 points):** one point each for a digit,
  uppercase letter, lowercase letter, and special character.
- **Predictability penalty (−1):** deducted if the password contains a
  repeated run (`aaa`) or an ascending sequence (`abc`, `123`).
- **Rating:** score ÷ max score (7) → `STRONG` (≥85%), `MEDIUM` (≥50%),
  or `TOO WEAK` (below that).

### Usage

```bash
python3 password_strength_checker.py
```

You'll be prompted for a password via `getpass`, so it won't echo to the
terminal. The tool prints what's missing (if anything) and a final rating.

**Example:**

```
Enter your password: 
- Add at least one uppercase letter.
- Add at least one special character.

REMARKS -- Password is MEDIUM (4/7)
```

### Requirements

Python 3.6+, standard library only (`getpass`, `string`). No external
dependencies.

---

## 2. Snake, Water, Gun Game

A CLI variation of Rock-Paper-Scissors. Snake beats water, water beats gun, gun beats snake.

### How it works

The win logic is driven by a lookup dictionary instead of a chain of `if/elif` statements:

```python
beats = {1: -1, -1: 0, 0: 1}  # key beats value
```

Each entry encodes one rule (e.g. `1: -1` means snake beats water). A result is checked with a single lookup — `beats[computer] == you` — rather than six separate hand-written comparisons for every possible matchup. 

### Features

- Input is validated in a loop — invalid entries re-prompt instead of crashing.
- Score (wins / losses / draws) is tracked across rounds and printed at the end.
- The game repeats until the player chooses not to play again.

### Usage

```bash
python3 snake_water_gun.py
```

**Example:**

```
Enter Your Choice (s/w/g): s

You chose snake
Computer chose gun
You lose!

Play again? (y/n): n

Final Score — Wins: 0, Losses: 1, Draws: 0
Thank you! Hope you enjoyed
```

### Requirements

Python 3, standard library only (`random`). No external dependencies.