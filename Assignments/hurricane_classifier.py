speed = int(input("What is the speed of the hurricane in MPH?\n>"))
if speed < 74:
    print("The hurricane is a tropical storm")
elif speed < 96:
    print("The hurricane is a category 1")
elif speed < 111:
    print("The hurricane is a category 2")
elif speed < 130:
    print("The hurricane is a category 3")
elif speed < 157:
    print("The hurricane is a category 4")
elif speed >= 157:
    print("The hurricane is a category 5")