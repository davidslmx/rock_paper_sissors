import random

def show_instructions():
    print("\nGame Instructions:")
    print("===================")
    print("Scissors ✌️ cut Paper ✋")
    print("Paper ✋ covers Rock ✊")
    print("Rock ✊ crushes Lizard 🦎")
    print("Lizard 🦎 poisons Spock 🖖")
    print("Spock 🖖 smashes Scissors ✌️")
    print("Scissors ✌️ beat Lizard 🦎")
    print("Lizard 🦎 eats Paper ✋")
    print("Paper ✋ disproves Spock 🖖")
    print("Spock 🖖 vaporizes Rock ✊")
    print("Rock ✊ breaks Scissors ✌️")
    print("===================")

def rock_paper_scissors():
    while True:
        print("\n===================")
        print("Rock Paper Scissors Lizard Spock")
        print("===================")
        print("1) ✊ Rock\n2) ✋ Paper\n3) ✌️ Scissors\n4) 🦎 Lizard\n5) 🖖 Spock\n6) 📜 Show Instructions")
        print("===================")

        # Choices with emojis
        choices = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}

        # Player choice
        try:
            player = int(input("Pick a number (1-5) or 6 for instructions: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if player == 6:
            show_instructions()
            continue  # Show instructions and restart the loop

        # Computer choice
        computer = random.randint(1, 5)

        if player not in choices:
            print("Invalid choice! Please pick a number between 1 and 5.")
            continue  

        # Show choices
        print(f"Player {choices[player]} vs {choices[computer]} Computer")

        # Determine winner
        winning_cases = {
            (3, 2), (2, 1), (1, 4), (4, 5), (5, 3), 
            (3, 4), (4, 2), (2, 5), (5, 1), (1, 3)  
        }

        if player == computer:
            print("It's a tie! 🤝")
        elif (player, computer) in winning_cases:
            print("Player wins! 🎉")
        else:
            print("Computer wins! 💻")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break 

rock_paper_scissors()
