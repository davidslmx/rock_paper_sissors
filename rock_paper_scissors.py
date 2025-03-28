import random

def rock_paper_sissors():
    while True:

        print("\n===================")
        print("Rock Paper Scissors")
        print("===================")
        print("1) ✊ Rock\n2) ✋ Paper\n3) ✌️  Scissors")
        print("===================")

        # Choices with emojis
        choices = {1: "✊", 2: "✋", 3: "✌️ "}
        # Player choice
        player = int(input("Pick a number (1-3): "))
        # Computer choice
        computer = random.randint(1, 3)
    
        if player not in choices:
            print("Invalid choice! Please pick 1, 2, or 3.")
            continue 

        # Show choices
        print(f"Player {choices[player]} vs {choices[computer]} Computer")

        # Determine winner
        if player == computer:
            print("It's a tie! 🤝")
        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            print("Player wins! 🎉")
        else:
            print("Computer wins! 💻")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break 

rock_paper_sissors()