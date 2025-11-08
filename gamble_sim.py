money = 5000
import random
import time
import sys
def start():
	game = input("What game would you like to play?\n1. Roulette\n2. Blackjack(Wouldn't recommend, very poorly coded)\n3. Horse Racing\n>>>")
	print()
	if game == "1":
		roulette()
	elif game == "2":
		blackjack()
	elif game == "3":
		horse_race()
	else:
		print("Invalid Input\n")
		start()
def roulette():
	global money
	print("What do you want to bet on?")
	print("1. Color")
	print("2. Even/Odd")
	print("3. High/Low")
	print("4. Single Number(35 to 1 payout)")
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
		print("Even or Odd?")
		bet = input(">>>")
		print()
		bet = bet.lower()
		if bet != "even" and bet != "odd":
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
	else:
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
	wager = int(wager)
	print("The wheel is spinning . . .")
	time.sleep(2.5)
	number = random.randint(1, 38)
	print()
	if number == 37:
		print("The wheel lands on 0.\nYou lose.\n")
		money = money - wager
		cont()
	elif number == 38:
		print("The wheel lands on 00.\nYou lose.\n")
		money = money - wager
		cont()
	elif number == 32 or number == 19 or number == 21 or number == 25 or number == 34 or number == 27 or number == 36 or number == 30 or number == 23 or number == 5 or number == 16 or number == 1 or number == 14 or number == 9 or number == 18 or number == 7 or number == 12 or number == 3:
		print(f"The wheel lands on Black {number}.")
		color = "black"
	elif number == 	15 or number == 4 or number == 2 or number == 17 or number == 6 or number == 13 or number == 11 or number == 8 or number == 10 or number == 24 or number == 33 or number == 20 or number == 31 or number == 22 or number == 29 or number == 28 or number == 35 or number == 26:
		print(f"The wheel lands on Red {number}.")
		color = "red"
	if bet == "black" and color == "black":
		print("\nYou win!")
		money = money + wager
		print(f"Your new balance is {money}.")
		cont()
	elif bet == "red" and color == "red":
		print("\nYou win!")
		money = money + wager
		print(f"Your new balance is {money}.")
		cont()
	elif bet == "even" and number % 2 == 0:
		print("\nYou win!")
		money = money + wager
		print(f"Your new balance is {money}.")
		cont()
	elif bet == "odd" and number % 2 == 1:
		print("\nYou win!")
		money = money + wager
		print(f"Your new balance is {money}.")
		cont()
	elif bet == "high" and number >= 19:
		print("\nYou win!")
		money = money + wager
		print(f"Your new balance is {money}.")
		cont()
	elif bet == "low" and number <= 18:
		print("\nYou win!")
		money = money + wager
		print(f"Your new balance is {money}.")
		cont()
	elif bet.isdigit():
		if int(bet) == number:
			print("\nYou win!")
			money = money + (wager * 35)
			print(f"Your new balance is {money}.")
			cont()
		else:
			print("\nYou lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()
	else:
		print("\nYou lose.")
		money = money - wager
		print(f"Your new balance is {money}.")
		cont()

def blackjack():
	global money
	print(f"How much money do you want to bet? You currently have ${money}. Note: Must be a whole number.")
	wager = input(">>>")
	print()
	if not wager.isdigit():
		print("Invalid Input.\n")
		blackjack()
	elif int(wager) > money or int(wager)<=0:
		print("Invalid Input.\n")
		blackjack()
	wager = int(wager)
	sum = 0
	card1 = random.randint(1, 13)
	if card1 == 1:
		card1disp = "ace"
		card1 = 11
	elif card1 == 11:
		card1disp = "jack"
		card1 = 10
	elif card1 == 12:
		card1disp = "queen"
		card1 = 10
	elif card1 == 13:
		card1disp = "king"
		card1 = 10
	else:
		card1disp = str(card1)
	card2 = random.randint(1, 13)
	if card2 == 1:
		card2disp = "ace"
		if not card == 11:
			card2 = 11
	elif card2 == 11:
		card2disp = "jack"
		card2 = 10
	elif card2 == 12:
		card2disp = "queen"
		card2 = 10
	elif card2 == 13:
		card2disp = "king"
		card2 = 10
	else:
		card2disp = str(card2)
	print(f"\nYour starting hand is a/n {card1disp} and a/n {card2disp}")
	end = False
	sum = card1 + card2
	print()
	if (card1 == 10 and card2disp == "ace") or (card2 == 10 and card1disp == "ace"):
		print("You got a blackjack.")
		end = True
		sum = 22
	while end == False:
		print(f"Your total is {sum}.")
		print("1. Hit\n2. Stay")
		choice = input(">>>")
		if choice == "2":
			print("You stay.")
			end = True
		elif not choice == "1":
			print("Invalid Input. Now you have to restart the whole thing.\n")
			blackjack()
			return
		else:
			new_card = random.randint(1, 13)
			if new_card == 1:
				print("Ace.")
				if (sum + 11) > 21:
					sum = sum + 1
				else:
					choice = input(f"What do you play the ace as?\n1. 1(total:{sum + 1})\n2. 11(sum:{sum + 11})")
					if choice == "1":
						sum = sum + 1
					elif choice == "2":
						sum = sum + 11:
					else:
						print("Invalid Input. Now you have to restart the whole thing.\n")
						blackjack()
						return
			elif new_card == 11:
				print("Jack.")
				sum = sum + 10
			elif new_card == 12:
				print("Queen.")
				sum = sum + 10
			elif new_card == 13:
				print("King.")
				sum = sum + 10
			else:
				print(f"{new_card}.")
				sum = sum + new_card
			if sum == 21:
				print("You get 21 and must stay.")
				end = True
			elif sum > 21:
				print("You bust and lose.")
				end = True
				money = money - wager
				print(f"Your new balance is {money}.")
				cont()
				return
	print()
	dealer_blackjack = random.randint(1, 1000)
	if dealer_blackjack < 49:
		print("The dealer gets a blackjack.")
		if sum == 22:
			print("You push. No money is gained or lost.")
			cont()
		else:
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()
	else:
		dealer_hand = random.randint(17, 26)
		if dealer_hand > 21:
			print("The dealer busts.")
			print("You win!")
			money = money + wager
			print(f"Your new balance is {money}.")
			cont()
		elif sum == dealer_hand:
			print(f"The dealer gets a {dealer_hand}.")
			print("You push. No money is gained or lost.")
			cont()
		elif sum > dealer_hand:
			print(f"The dealer gets a {dealer_hand}.")
			print("You win!")
			money = money + wager
			print(f"Your new balance is {money}.")
			cont()
		else:
			print(f"The dealer gets a {dealer_hand}.")
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()

def horse_race():
	global money
	print("Which horse would you like to bet on?\nHorse 1: 1 to 1 odds\nHorse 2: 3 to 1 odds\nHorse 3: 7 to 1 odds\n Horse 4: 7 to 1 odds")
	bet = input(">>>")
	print()
	if not(bet == "1" or bet == "2" or bet == "3" or bet == "4"):
		print("Invalid Input\n")
		horse_race()
		return
	print(f"How much money do you want to bet? You currently have ${money}. Note: Must be a whole number.")
	wager = input(">>>")
	print()
	if not wager.isdigit():
		print("Invalid Input.\n")
		horse_race()
	elif int(wager) > money or int(wager)<=0:
		print("Invalid Input.\n")
		horse_race()
	wager = int(wager)
	print()
	outcome = random.randint(1, 40)
	if outcome < 21:
		print("Horse 1 wins.\n")
		if bet == "1":
			print("You win!")
			money = money + wager
			print(f"Your new balance is {money}.")
			cont()
		else:
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()
	elif outcome < 31:
		print("Horse 2 wins.\n")
		if bet == "2":
			print("You win!")
			money = money + (wager * 3)
			print(f"Your new balance is {money}.")
			cont()
		else:
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()
	elif outcome < 36:
		print("Horse 3 wins.\n")
		if bet == "3":
			print("You win!")
			money = money + (wager * 7)
			print(f"Your new balance is {money}.")
			cont()
		else:
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()
	else:
		print("Horse 4 wins.\n")
		if bet == "4":
			print("You win!")
			money = money + (wager * 7)
			print(f"Your new balance is {money}.")
			cont()
		else:
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
			cont()

def cont():
	global money
	if money <= 0:
		print("You go bankrupt and are kicked out of the casino.\n")
		stats()
	else:
		print("Would you like to play again?")
		print("1. Yes, Roulette\n2. Yes, Blackjack(Again, don't recommend)\n3. Yes, Horce Racing\n4. No")
		choice = input(">>>")
		print()
		if choice == "1":
			roulette()
		elif choice == "2":
			blackjack()
		elif choice == "3":
			horse_race()
		elif choice == "4":
			print("You decide to walk.\n")
			stats()
		else:
			print("Invalid Input.\n")
			cont()

def stats():
	global money
	if money < 5000:
		print(f"You lost {5000 - money} dollars overall.")
	elif money > 5000:
		print(f"You gained {money - 5000} dollars overall.")
	else:
		print("You broke even.")
	sys.exit(0)

print("You are a middle-aged father. You decide to gamble your kids' college fund so that you can afford more alcohol. You bring $5000 to the casino.\n")
roulette()
