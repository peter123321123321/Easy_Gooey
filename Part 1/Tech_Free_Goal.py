import easygui

while True:
    goal = easygui.integerbox("How many days do you want to go tech free", "Goal")
    tech_free = easygui.enterbox("how many days have you gone tech free"
                                 "\n Separate each place with a space", "Tech Free Days")
    tech_days = tech_free.split()
    if len(tech_days) >= goal:
        easygui.msgbox(f"Your goal was {goal} Tech free days"
                       f"\nYou completed this goal with {len(tech_days)} Tech free days", "Goal Achieved")
    else:
        easygui.msgbox(f"Your goal was {goal} Tech free days"
                       f"\nYou failed this goal with {len(tech_days)} Tech free days", "Goal not Achieved")
