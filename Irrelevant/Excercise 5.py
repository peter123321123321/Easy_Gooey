import easygui
import math

while True:
    school = easygui.enterbox("Welcome, What school are you from", "Welcome")
    children = easygui.integerbox("How many children are allowed per class\nBetween 10 and 30", "Children per class",
                                  lowerbound=10, upperbound=30)
    total_children = easygui.integerbox(f"How many children go to {school}\nBetween 10 and 1400", "Children enrolled",
                                        lowerbound=10, upperbound=1400)
    teachers_needed = math.ceil(total_children/children)
    teachers_available = easygui.integerbox("How many Teachers are available", "Teachers available")
    if teachers_available == teachers_needed:
        easygui.msgbox("You have the right amount of Teachers")
    elif teachers_needed != teachers_available:
        if teachers_available < teachers_needed:
            easygui.msgbox(f"You dont have enough Teachers"
                           f"\n you need {teachers_needed-teachers_available} more",
                           "Not enough Teachers")
        elif teachers_available > teachers_needed:
            easygui.msgbox(f"You have too many Teachers"
                           f"\n you could do without {teachers_available - teachers_needed}",
                           "Too many Teachers")
    calculate_again = easygui.choicebox("Would you like to do another calculation", "More Calculations", ["Yes", "No"])
    if calculate_again == "No":
        break
