import easygui

while True:

    places = easygui.enterbox("What are 5 places you would like to travel too"
                              "\n Separate each place with a comma", "Bucket list")
    bucket_list = [places.split(",")]
    if len(bucket_list) != 5:
        easygui.msgbox("You need to enter 5 places", "Error")


