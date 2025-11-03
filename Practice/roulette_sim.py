money = 1000
import random
import time
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
		print()
		bet = bet.lower()
		if bet != "red" and bet != "black":
			print("Invalid Input.\n")
			roulette()
	elif choice == "2":
		print("Even or Odds?")
		bet = input(">>>")
		print()
		bet = bet.lower()
		if bet != "red" and bet != "black":
			print("Invalid Input.\n")
			roulette()
	elif choice == "3":
		print("High or Low?")
		bet = input(">>>")
		print()
		bet = bet.lower()
		if bet != "high" and bet != "low":
			print("Invalid Input.\n")
			roulette()
	elif choice == "4":
		print("What number(1-36) do you bet on?")
		bet = input(">>>")
		print()
		if bet.isdigit == False or "." in bet:
			print("Invalid Input.\n")
			roulette()
		elif int(bet) < 1 or int(bet) > 36:
			print("Invalid Input.\n")
			roulette()
	print(f"How much money do you want to bet? You currently have ${money}. Note: Must be a whole number.")
	wager = input(">>>")
	print()
	if not wager.isdigit():
		print("Invalid Input.\n")
		roulette()
	elif int(wager) > money or int(wager)<=0:
		print("Invalid Input.\n")
		roulette()
	print("The wheel is spinning . . .")
	time.sleep(5)
	number = random.randint(1, 38)
	print()
	if number == 37:
		print("The wheel lands on 0. You lose.")
		money = money - wager
		cont()
	elif number == 38:
		print("The wheel lands on 00. You lose.")
		money = money - wager
		cont()
	elif number == 32 or number == 19 or number == 21 or number == 25 or number == 34 or number == 27 or number == 36 or number == 30 or number == 23 or number == 5 or number == 16 or number == 1 or number == 14 or number == 9 or number == 18 or number == 7 or number == 12 or number == 3:
		print(f"The wheel lands on Black {number}.")
		color = "black"
	elif number == 	15 or number == 4 or number == 2 or number == 17 or number == 6 or number == 13 or number == 11 or number == 8 or number == 10 or number == 24 or number == 33 or number == 20 or number == 31 or number == 22 or number == 29 or number == 28 or number == 35 or number == 26:
		print(f"The wheel lands on Red {number}.")
		color = "red"


def cont():
	print("Would you like to play again?")
	print("1. Yes\n2. No")
	choice = input(">>>")
	print()
	if choice == "1":
		roulette()
	elif choice == "2":
		print("You decide to walk.\n")
		stats()
	else:
		print("Invalid Input.\n")
		cont()
def stats():
	global money
	if money < 1000:
		print(f"You lost {1000 - money} dollars.")

print("You are a middle-aged father. You decide to gamble your kids' college fund so that you can afford more alcohol.\n")
roulette()