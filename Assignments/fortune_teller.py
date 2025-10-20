satisfied = False
while satisfied == False:
    try:
        number = int(input("Give me the first whole number that comes to mind.\n>"))
        satisfied = True
    except:
        print("That's not a whole number. Try again.")
satisfied = False
while satisfied == False:
    try:
        years = float(input("How many years do you want to see into the future? This can be a decimal.\n>"))
        satisfied = True
    except:
        print("That's not a number. Try again.")
satisfied = False
while satisfied == False:
    try:
        birth_yr = int(input("What year were you born?\n>"))
        satisfied = True
    except:
        print("That's not a number. Try again.")
satisfied = False
while satisfied == False:
    try:
        birth_day = int(input("What day of the month were you born?\n>"))
        if birth_day <= 31 and birth_day > 0:
            satisfied = True
        else:
            print("That's not a day of the month. Must be between 1 and 31. Try again.")
    except:
        print("That's not a whole number. Try again.")
satisfied = False
while satisfied == False:
    try:
        number_2 = int(input("Give me another whole number.\n>"))
        satisfied = True
    except:
        print("That's not a whole number. Try again.")
print()
print("FORTUNE:")
if birth_yr < 1950:
    print("You will be dead of old age. Holy unc.")
elif years > 100:
    print("You'll be dead and then reincarnated as a bacteria.")
elif years < 0:
    print("You set the years to negative, that's the past. Pick up a history textbook.")
elif birth_yr == 2010 and birth_day == 25:
    print("You will be mega successful and everyone will love you and nothing will ever go wrong.")
elif number < 0 or number_2 < 0:
    print("You will get drafted into WWIII and you will stay there until you die.")
elif number == 67 or number_2 == 67:
    print("Your friends will abandon you because you can't stop saying 6 7.")
elif number_2 > 99 or number > 99:
    print("You will be the world's first trillionare and everyone will hate you.")
elif number_2 == 13 or number == 13:
    print("You will slip on a banana peel and fall into an open manhole. How unlucky.")
elif birth_day > 10:
    print("You will become the first U.S. president to be removed from office.")
else:
    print("Nothing will happen. You're pretty boring.")