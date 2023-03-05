import random
import easygui
new_word = list()
word = "audiobookinthetoiletatthegymconvention"

for i in range(14):
    letter = random.choice(word)
    new_word.append(letter)
    easygui.msgbox(letter, f"letter {i+1} chosen")

print(new_word)