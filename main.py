artifactlist = ["Feather", "Flower", "Sands", "Goblet", "Circlet"]
print("Which artifact are you calculating for?")
print(f"1. {artifactlist[0]}")
print(f"2. {artifactlist[1]}")
print(f"3. {artifactlist[2]}")
print(f"4. {artifactlist[3]}")
print(f"5. {artifactlist[4]}")
artifactans = int(input("Enter the corresponding number here: "))

critrate = float(input("Enter your crit rate here as a decimal number: "))
critdmg = float(input("Enter your crit damage here as a decimal number: "))

if artifactans == 1:
    critvalue = critdmg +(2* critrate)
    print(f"The crit value of your feather is {critvalue}.")
elif artifactans == 2:
    critvalue = critdmg +(2* critrate)
    print(f"The crit value of your flower is {critvalue}.")
elif artifactans == 3:
    critvalue = critdmg +(2* critrate)
    print(f"The crit value of your sands is {critvalue}.")
elif artifactans == 4:
    critvalue = critdmg +(2* critrate)
    print(f"The crit value of your goblet is {critvalue}.")
elif artifactans == 5:
    mainstat=(input("Which stat is your main stat? Please type: ATK, DEF, EM, Crit Rate, or Crit Damage: "))
    if mainstat == 'ATK' or mainstat == 'DEF' or mainstat == 'EM':
        critvalue = critdmg +(2* critrate)
        print(f"The crit value of your circlet is {critvalue}.")
    elif mainstat == 'Crit Rate':
        print(f"The crit value of your circlet is {critrate}.")
    elif mainstat == 'Crit Damage':
        print(f"The crit value of your circlet is {critdmg}.")