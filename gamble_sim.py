money = 5000
import random
import time
import sys
def start():
	game = input("What game would you like to play?\n1. Roulette\n2. Blackjack\n3. Horse Racing\n4. Slots\n>>>")
	print()
	if game == "1":
		roulette()
	elif game == "2":
		blackjack()
	elif game == "3":
		horse_race()
	elif game == "4":
		slots()
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
		if not card2 == 11:
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
	print(f"\nYour starting hand is a {card1disp} and a {card2disp}")
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
			print("\nYou stay.")
			end = True
		elif not choice == "1":
			print("Invalid Input. I'll take it as a stay.")
			end = True
		else:
			new_card = random.randint(1, 13)
			print()
			if new_card == 1:
				print("Ace.")
				if (sum + 11) > 21:
					sum = sum + 1
				else:
					choice = input(f"What do you play the ace as?\n1. 1(total:{sum + 1})\n2. 11(sum:{sum + 11})")
					if choice == "1":
						sum = sum + 1
					elif choice == "2":
						sum = sum + 11
					else:
						print("Invalid Input. I'll take it as 11.\n")
						sum = sum + 11
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
			print()
			if sum == 21:
				print("\nYou get 21 and must stay.")
				end = True
			elif sum > 21:
				print("You bust and lose.\n")
				end = True
				money = money - wager
				print(f"Your new balance is {money}.")
				cont()
				return
	print()
	print("The dealer is playing . . .\n")
	time.sleep(2.5)
	dealer_blackjack = random.randint(1, 1000)
	if dealer_blackjack < 49:
		print("The dealer gets a blackjack.\n")
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
			print("The dealer busts.\n")
			print("You win!\n")
			money = money + wager
			print(f"Your new balance is {money}.\n")
			cont()
		elif sum == dealer_hand:
			print(f"The dealer gets a {dealer_hand}.\n")
			print("You push. No money is gained or lost.\n")
			cont()
		elif sum > dealer_hand:
			print(f"The dealer gets a {dealer_hand}.\n")
			print("You win!\n")
			money = money + wager
			print(f"Your new balance is {money}.\n")
			cont()
		else:
			print(f"The dealer gets a {dealer_hand}.\n")
			print("You lose.\n")
			money = money - wager
			print(f"Your new balance is {money}.\n")
			cont()

def horse_race():
	global money
	print("Which horse would you like to bet on?\nHorse 1: 1 to 1 odds\nHorse 2: 3 to 1 odds\nHorse 3: 7 to 1 odds\nHorse 4: 7 to 1 odds")
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
	print("Race is in progress . . .\n")
	time.sleep(2.5)
	outcome = random.randint(1, 8)
	if outcome < 5:
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
	elif outcome < 7:
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
	elif outcome < 8:
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

def slots():
	symbols = ["7","%","#","@","&"]
	global money
	print("3 of a kind: 1 to 1 payout\n4 of a kind: 3 to 1 payout\n5 of a kind: 5 to 1 payout\n5 7's: 10 to 1 payout\n\nEnter to Continue")
	input("")
	print(f"How much money do you want to bet? You currently have ${money}. Note: Must be a whole number.\nThis bet will be applied to all spins.")
	wager = input(">>>")
	print()
	if not wager.isdigit():
		print("Invalid Input.\n")
		slots()
	elif int(wager) > money or int(wager)<=0:
		print("Invalid Input.\n")
		slots()
	wager = int(wager)
	end = False
	input("Enter to spin\n")
	while end == False:
		print("\nSpinning . . .\n")
		time.sleep(1)
		s1 = symbols[random.randint(0, 4)]
		s2 = symbols[random.randint(0, 4)]
		s3 = symbols[random.randint(0, 4)]
		s4 = symbols[random.randint(0, 4)]
		s5 = symbols[random.randint(0, 4)]
		print(f"{s1} | {s2} | {s3} | {s4} | {s5}\n")
		if s1 == "7" and s2 == "7" and s3 == "7" and s4 == "7" and s5 == "7":
			print("You Got The Jackpot!")
			money = money + (wager * 10)
			print(f"Your new balance is {money}.")
		elif s1 == s2 and s2 == s3 and s3 == s4 and s4 == s5:
			print("Five of a kind!")
			money = money + (wager * 5)
			print(f"Your new balance is {money}.")
		elif (s1 == s2 and s2 == s3 and s3 == s4) or (s1 == s2 and s2 == s3 and s3 == s5) or (s1 == s2 and s2 == s4 and s4 == s5) or (s1 == s3 and s3 == s4 and s4 == s5) or (s2 == s3 and s3 == s4 and s4 == s5):
			print("Four of a Kind!")
			money = money + (wager * 3)
			print(f"Your new balance is {money}.")
		elif (s1 == s2 and s2 == s3) or (s1 == s2 and s2 == s4) or (s1 == s2 and s2 == s5) or (s1 == s3 and s3 == s4) or (s1 == s4 and s4 == s5) or (s1 == s3 and s3 == s5) or (s2 == s3 and s3 == s4) or (s2 == s3 and s3 == s5) or (s2 == s4 and s4 == s5) or (s3 == s4 and s4 == s5):
			print("Three of a Kind!")
			money = money + wager
			print(f"Your new balance is {money}.")
		else:
			print("You lose.")
			money = money - wager
			print(f"Your new balance is {money}.")
		print()
		if money < wager:
			print("You don't have enough money to keep playing.")
			end == True
			break
		x = input('Enter to spin or input "stop" to stop playing\n')
		if x.lower() == "stop":
			end == True
			break
	print()
	cont()
		

def cont():
	global money
	if money <= 0:
		print("You go bankrupt and are kicked out of the casino.\n")
		stats()
	else:
		print("Would you like to play again?")
		print("1. Yes, Roulette\n2. Yes, Blackjack\n3. Yes, Horse Racing\n4. Slots\n5. No")
		choice = input(">>>")
		print()
		if choice == "1":
			roulette()
		elif choice == "2":
			blackjack()
		elif choice == "3":
			horse_race()
		elif choice == "4":
			slots()
		elif choice == "5":
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
start()
