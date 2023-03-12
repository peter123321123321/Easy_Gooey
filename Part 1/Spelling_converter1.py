import easygui

while True:
    word = easygui.enterbox("What word would you like to translate? ")
    translate = [word]
    if "our" in word:
        translated = [word.replace("our", "or",) for word in translate]
        easygui.msgbox(f"The word {word} translated is {translated}")

    another = easygui.buttonbox("Would you like to translate another word", "Translate again", choices=["Yes", "No"])
    if another == "No":
        break
