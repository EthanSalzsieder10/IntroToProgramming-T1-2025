# Setup
mode = None
def game_mode():
    print()
    print("What game mode do you want to play?")
    print("1. Trophy Road")
    print("2. Classic 1v1")
    print("3. Classic 2v2")
    choice = input(">>>")
    print()
    global mode
    if choice == "1":
        mode = 1
        print("You load into a trophy road game. Your opponent's tower level is two above yours and they are already spamming the goblin 'mimimimimi' emote.")
    elif choice == "2":
        mode = 2
        print("You load into a Classic 1v1. Your opponent sends a 'good luck!' emote. You don't know if that is friendly or a warning.")
    elif choice == "3":
        mode = 3
        print("You load into a 2v2. Your teammate immediately leaves.")
    else:
        print("Invalid Input. Must be a number 1-3.")
        game_mode()

def first_play():
    print()
    print("The first 10 seconds pass and no one has played a card. You are leaking elixer, as is the enemy. What do you do?")
    print("1. Push valkyrie and prince on the bridge")
    print("2. Wait for the opponent to play first")
    print("3. Fireball the king tower")
    print("4. Split skarmy in the back")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You push a valk and prince on the bridge. Your opponent tries to counter with a skarmy, but the valkyrie makes quick work of them and you get juicy tower damage.")
    elif choice == "2":
        print("Your opponent plays lumberloon.")
    elif choice == "3":
        print("You fireball the king tower. It's tower damage, right?")
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        encounter()
    
def encounter():
    print()
    print("")
    print("1. ")
    print("2. ")
    print("3. ")
    choice = input(">>>")
    print()
    if choice == "1":
        print("")
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    else:
        print("")
        encounter()

# Gameplay
print()
print("You are a high school boy who is hopelessly addicted to Clash Royale. You pull out your phone in the middle of math class because you physically can't live without it.")
game_mode()
first_play()

# Deck: Prince, valk, fireball, evo inferno dragon, baby dragon, log, cannon, skarmy