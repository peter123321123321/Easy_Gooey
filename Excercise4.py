import random

import easygui

while True:
    choices = ["Paper", "Scissors", "Rock"]
    computer_choice = random.choice(choices)
    play_again = easygui.buttonbox("Welcome to Rock-Paper-Scissors"
                                   "\nAs usual Rock beats Scissors\nScissors beats paper\nPaper beats Rock\nWould you "
                                   "like to play",
                                   "Welcome+Rules", choices=["Yes", "No"])
    if play_again == "No":
        easygui.msgbox("Thank you for playing", "Goodbye")
        break
    else:
        action = easygui.buttonbox("What would you like to play:", "Action", choices=["Rock", "Paper", "Scissors"])
        if action == computer_choice:
            result = "Drew"
        elif action == "Rock" and computer_choice == "Scissors" or action == "Paper" and computer_choice == "Rock" or \
                action == "Scissors" and computer_choice == "Paper":
            result = "Win"
        else:
            result = "Lost"

    easygui.msgbox(f"You choose {action}\n Your opponent chose {computer_choice}\n you {result}")
