hero_0 = {"Name": "Peter", "Power": "Sexiness", "Strength": 100}
hero_1 = {"Name": "Peeter", "Power": "Amazingness", "Strength": 100}
hero_2 = {"Name": "Peeeter", "Power": "Smartness", "Strength": 100}

hero_list = [hero_0, hero_1, hero_2]

for i in hero_list:
    print(f"{}")



if "Name" in hero_0:
    print(f"The superhero's Name is: {hero_0['Name']}")
else:
    print("There is no super hero Name")

if "Power" in hero_0:
    print(f"The superhero's Power is: {hero_0['Power']}")
else:
    print("There is no super hero Power")

if "Strength" in hero_0:
    print(f"The superhero's Strength is: {hero_0['Strength']}")
else:
    print("There is no super hero Strength")