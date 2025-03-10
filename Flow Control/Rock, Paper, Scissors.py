import random

# Track scores
wins = 0
losses = 0
ties = 0

# Choices mapping
choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
GAME = list(choices.keys())  # ["R", "P", "S"]

# Game loop
while True:
    print("\n===== ROCK, PAPER, SCISSORS Game =====")
    print(f"Score: Wins = {wins}, Losses = {losses}, Ties = {ties}")

    # User input with validation
    user_choice = input("Choose (R for Rock, P for Paper, S for Scissors, Q to Quit): ").upper()

    if user_choice == "Q":
        print("\nThanks for playing! Exiting the game.")
        break  # Exit the loop

    if user_choice not in GAME:
        print("❌ Invalid choice! Please enter R, P, or S.")
        continue  # Restart loop for valid input

    print(f"\nYou chose {choices[user_choice]}")

    # Computer choice
    computer_choice = random.choice(GAME)
    print(f"Computer chose {choices[computer_choice]}")

    # Game result logic
    if user_choice == computer_choice:
        print("🟰 It's a TIE!")
        ties += 1
    elif (user_choice == "P" and computer_choice == "R") or \
            (user_choice == "R" and computer_choice == "S") or \
            (user_choice == "S" and computer_choice == "P"):
        print("🏆 You WIN!")
        wins += 1
    else:
        print("💔 You LOSE!")
        losses += 1

    print("======================================")

