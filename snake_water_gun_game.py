"""
Snake, Water, Gun Game

Rules:
- Snake drinks Water (Snake wins)
- Water ruins Gun (Water wins)
- Gun kills Snake (Gun wins)

Internal Values:
 1 = Snake
-1 = Water
 0 = Gun
"""
import random

# --- Game Configuration ---
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
beats = {1: -1, -1: 0, 0: 1}  # key beats value

# --- Score Trackers ---
wins = 0
losses = 0
draws = 0

# --- Main Game Loop ---
while True:
    computer = random.choice([1, -1, 0])

    # --- Input Validation Loop ---
    while True:
        yourstr = input("\nEnter Your Choice (s/w/g): ").lower()
        if yourstr in yourDict:
            break
        print("Invalid input. Choose s, w, or g.")

    you = yourDict[yourstr]

    print(f"\nYou chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    # --- Game Logic: Determine the Winner ---
    if computer == you:
        print("It's a draw!")
        draws += 1
    elif beats[computer] == you:
        print("You lose!")
        losses += 1
    else:
        print("You won!")
        wins += 1

    # --- Replay Prompt ---
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break

# --- End of Game ---
print(f"\nFinal Score — Wins: {wins}, Losses: {losses}, Draws: {draws}")
print("\nThank you! Hope you enjoyed")