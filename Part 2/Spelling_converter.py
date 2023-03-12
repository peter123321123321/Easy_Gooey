import easygui

while True:
    word = easygui.enterbox("What word would you like to translate? ")
    translate = [word]
    if "our" in word:
        translated = [word.replace("our", "or",) for word in translate]
    elif "ise" in word:
        translated = [word.replace("ise", "ize",) for word in translate]
    elif "yse" in word:
        translated = [word.replace("yse", "yze",) for word in translate]
    else:
        easygui.msgbox("There is no change in translation" )

    easygui.msgbox(f"The word {word} translated is {translated}")
    another = easygui.buttonbox("Would you like to translate another word", "Translate again", choices=["Yes", "No"])
    if another == "No":
        break
