import easygui

while True:

    places = easygui.enterbox("What are 5 places you would like to travel too"
                              "\n Separate each place with a comma", "Bucket list")
    bucket_list = places.split(",")
    if len(bucket_list) != 5:
        easygui.msgbox("You need to enter 5 places", "Error")
    else:
        destination = easygui.choicebox("Would you like to change one of your destinations", "Destinations",
                                        choices=["Yes", "No"])
        if destination == "Yes":
            break
        else:
            easygui.msgbox(f"This is your bucket list: {bucket_list}")
            exit()
    change = easygui.enterbox("Which location would you like to change", "Change destination")
    replace = easygui.enterbox("Which location would you like to replace it with", "Replace destination")
    new_list = [bucket_list.replace(f"{change}", f"{replace}",) for change in bucket_list]

