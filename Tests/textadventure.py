# Setup
def game_mode():
    print()
    print("What game mode do you want to play?")
    print("1. Trophy Road")
    print("2. Classic 1v1")
    print("3. Classic 2v2")
    print("4. None, play Clash of Clans")
    choice = input(">>>")
    print()
    if choice == "1":
        tr_first_play()
    elif choice == "2":
        print("You load into a Classic 1v1. Your opponent sends a 'good luck!' emote. You don't know if that is friendly or a warning.")
    elif choice == "3":
        print("You load into a 2v2. Your teammate immediately leaves.")
    elif choice == "4":
        ending_1()
    else:
        print("Invalid Input. Must be a number 1-4.")
        game_mode()
def tr_first_play():
    print("You load into a trophy road game. Your opponent's tower level is two above yours and they are already spamming the goblin 'mimimimimi' emote.")
    print()
    print("The first 10 seconds pass and no one has played a card. You are leaking elixer, as is the enemy. Your current cards are Valkyrie, Prince, Fireball, and Skarmy. What do you do?")
    print("1. Push Valkyrie and Prince on the bridge")
    print("2. Wait for the opponent to play first")
    print("3. Fireball the king tower")
    print("4. Split Skarmy in the back")
    choice = input(">>>")
    print()
    if choice == "1":
        tr_prince_valk()
    elif choice == "2":
        print("Your opponent ")
    elif choice == "3":
        print("You fireball the king tower. It's tower damage, right?")
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        encounter()
def tr_prince_valk():
    print("You push a Valk and Prince on the bridge. Your opponent plays a Pekka, which mostly defends, but you get a few hundred damage on the tower.")
    print()
    print("")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    choice = input(">>>")
    print()
    if choice == "1":
        print("")
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    elif choice == "4":
        print("")
    else:
        print("")
        encounter()

def encounter():
    print()
    print("")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    choice = input(">>>")
    print()
    if choice == "1":
        print("")
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    elif choice == "4":
        print("")
    else:
        print("")
        encounter()
def ending_1():
    print()
    print("You played Clash of Clans.")
    print("Ending 1 of 5: Worst Ending")
    print()
def ending_2():
    print()
    print("You stop playing Clash indefinitely. You become much happier as a person and you go on to get married to your soulmate and become a trillionaire with 3 kids.")
    print("Ending 2 of 5: Good Ending")
    print()
# Gameplay
print()
print("You are a high school boy who is hopelessly addicted to Clash Royale. You pull out your phone in the middle of math class because you physically can't live without it.")
game_mode()

# Deck: Prince, Evo Valk, Fireball, Evo Inferno Dragon, Baby Dragon, Log, Cannon, Skarmy
# TR Op Deck: Pekka, Skarmy, Evo Mega Knight, Tesla Tower, Rocket, Log, Evo Goblin Barrel, Freeze
# C1v1 Op Deck: Hog, Musketeer, Ice Golem, Fireball, Ice Spirit, Fire Spirit, Skeletons, Cannon