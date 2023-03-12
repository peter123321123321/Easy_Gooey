import easygui
import random

easygui.enterbox("Hi What is your name? ")
easygui.integerbox("How old are you? ")
easygui.buttonbox("Do you want to continue?", choices=["Yes", "No", "Maybe"])

words = ["peter", "meter", "3 seater", "competer"]
my_word = random.choice(words)
print(my_word)

word = "Iridocyclitis"
letter = random.choice(word)
print(letter)



