money = 1000.00
def roulette():
	global money
	print("What do you want to bet on?")
	print("1. Color")
	print("2. Even/Odd")
	print("3. High/Low")
	print("4. Single Number")
	choice = input(">>>")
	print()
	if choice == "1":
		print("Red or Black?")
		bet = input(">>>")
		bet = bet.lower()
		if bet != "red" and bet != "black":
			print("Invalid Input.\n")
			roulette()
	elif choice == "2":
		print("Even or Odds?")
		bet = input(">>>")
		bet = bet.lower()
		if bet != "red" and bet != "black":
			print("Invalid Input.\n")
			roulette()
	elif choice == "3":
		print("High or Low?")
		bet = input(">>>")
		bet = bet.lower()
		if bet != "high" and bet != "low":
			print("Invalid Input.\n")
			roulette()
	elif choice == "4":
		print("What number(1-36) do you bet on?")
		bet = input(">>>")
		if bet.isdigit == False or "." in bet:
			print("Invalid Input.\n")
			roulette()
		elif int(bet) < 1 or int(bet) > 36:
			print("Invalid Input.\n")
			roulette()
	print(f"How much money do you want to bet? You currently have ${money}.")
	wager = input(">>>")
roulette()