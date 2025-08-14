# rock_paper_scissors.py
# Hassaan Ahmed - Certura Internship Task 3

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"


print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

player_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"Round {round_number}")
    player = input("Your choice: ").lower()

    if player == "quit":
        break

    if player not in ["rock", "paper", "scissors"]:
        print("Invalid input! Try again.\n")
        continue

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")

    result = determine_winner(player, computer)

    if result == "player":
        print(" You win this round!")
        player_score += 1
    elif result == "computer":
        print(" Computer wins this round.")
        computer_score += 1
    else:
        print(" It's a draw.")

    print(f"Score => You: {player_score} | Computer: {computer_score}\n")
    round_number += 1

print("\n Final Score:")
print(f"You: {player_score} | Computer: {computer_score}")
print(" Thanks for playing!")