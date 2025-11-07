import random
number = random.randint(1, 101)
guessed = False
while guessed == False:
    guess = input("\nGuess the Number\n>>>")
    try:
        guess = int(guess)
        if guess == number:
            print("\nYou got it!")
            guessed = True
        elif guess > number:
            print("\nToo high. Guess again.")
        elif guess < number:
            print("\nToo low. Guess again.")
    except:
        print("\nInvalid Input.")