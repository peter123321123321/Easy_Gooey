import easygui
import random

while True:
    card_list = ["Ace", "King", "Queen", "Jack", "10", "9","8", "7", "6", "5","4", "3", "2"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    while True:
        button = easygui.buttonbox("Click to choose your card", "Mysterious card chooser", choices=["Button"])
        if button == "Button":
            player_choice = [random.choice(card_list), random.choice(suits)]
            computer_choice = [random.choice(card_list), random.choice(suits)]
            if card_list.index(player_choice[0]) == card_list.index(computer_choice[0]):
                result = "You've drawn"
            elif card_list.index(player_choice[0]) < card_list.index(computer_choice[0]):
                result = "You've won"
            else:
                result = "You've lost"

            play_again = easygui.buttonbox(f"You have the {player_choice[0]} of {player_choice[1]}"
                                           f"\nAnd I have the {computer_choice[0]} of {computer_choice[1]}"
                                           f"\nCongrats {result}"
                                           f"\nWould you like to play again", "Result", choices=["Yes", "No"])
            if play_again == "No":
                easygui.msgbox("Thanks for playing", "Goodbye")
                exit()
