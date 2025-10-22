king_activate = False
score = 0
doubt = 0
def start():
    print("\nWhat game mode do you want to play?")
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
    elif choice == "5":
        secret_ending()
    else:
        print("Invalid Input. Must be a number 1-4.")
        game_mode()
def tr_first_play():
    print("You load into a trophy road game. Your opponent's tower level is two above yours and they are already spamming the goblin 'mimimimimi' emote.\n")
    print("The first 10 seconds pass and no one has played a card. You are leaking elixer, as is the enemy. What do you do?")
    print("1. Push Valkyrie and Prince on the bridge")
    print("2. Fireball the King Tower")
    print("3. Split Skarmy in the back")
    print("4. Wait for the opponent to play first")
    choice = input(">>>")
    print()
    if choice == "1":
        tr_prince_valk()
    elif choice == "2":
        tr_fire_king()
    elif choice == "3":
        print()
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        tr_first_play()
def tr_prince_valk():
    global score
    score += 2
    print("You push a Valk and Prince on the bridge. Your opponent plays a Pekka, which mostly defends, but you get a few hundred damage on the tower.\n")
    print("Your opponent is being a little coward and still not playing any offense. What do you do?")
    print("1. Fireball the King Tower")
    print("2. Play Log to cycle")
    print("3. Place Baby Dragon in the back")
    print("4. Wait for your opponent to stop being a little baby while you spam chicken emotes")
    choice = input(">>>")
    print()
    if choice == "1":
        tr_fire_king()
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        tr_prince_valk()
def tr_fire_king():
    global king_activate
    king_activate = True
    print("You fireball the King Tower. That's tower damage, right?\n")
    print("Your Opponent sends a laughing emote and then plays a Mega Knight. What do you do?")
    print("1. Place a cannon to distract")
    print("2. Play Inferno Dragon on the Mega Knight")
    print("3. Push Skarmy on the other lane")
    print("4. Accept Defeat")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You place a cannon to distract the Mega Knight.")
        tr_cannon()
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    elif choice == "4":
        global doubt
        doubt += 1
        print("No you don't. You must keep playing. This is why we Clash. You place a cannon to distract the Mega Knight.")
        tr_cannon()
    else:
        print("Invalid Input. Must be a number 1-4.")
        encounter()
def tr_cannon():
    global score
    score += -1
    print("\nThe cannon distracts the Mega Knight long enough for the tower to only take a few hits. You suspect the opponent has no elixer. What do you do?")
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
        print("Invalid Input. Must be a number 1-4.")
        tr_cannon()

def encounter():
    global score
    score += 0
    print("\n")
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
        print("Invalid Input. Must be a number 1-4.")
        encounter()
def ending_1():
    print("You play Clash of Clans.")
    print("Ending 1 of 5: Worst Ending")
    print()
def ending_2():
    print("Your opponent spams the laughing emote as you have to watch yourself get 3-Crowned no diff. You will never psycologically recover from this game.")
    print("Ending 2 of 5: Crashout")
    print()
def ending_3():
    print("You let out a huge sigh as your opponent barely edges out a win. Why bother playing this garbage game?")
    print("Ending 3 of 5: Regret")
    print()
def ending_4():
    print("You won, but what does it matter? You will only be disappointed again in the future. Do we really wade through the frustration and agony just for a slight hit of dopamine?...\n...\n...\n...Is this why we Clash?")
    print("Ending 4 of 5: Doubt\n")
def ending_5():
    print("LOOOL GGS TOO EZ THIS IS THE BEST GAME EVER")
    print("Ending 5 of 5: Pride")
    print()
def secret_ending():
    print("You decide that is enough screwing around with your life. You delete Clash and you invest in your future. You grow up to marry your soulmate and have 3 children who live with you in your mansion.")
    print("Secret: Best Ending")
    print()
# Gameplay
print()
print("You are a high school boy who is hopelessly addicted to Clash Royale. You pull out your phone in the middle of math class because you physically can't live without it.")
start()

# Deck: Prince, Evo Valk, Fireball, Evo Inferno Dragon, Baby Dragon, Log, Cannon, Skarmy
# TR Op Deck: Pekka, Skarmy, Evo Mega Knight, Tesla Tower, Rocket, Log, Evo Goblin Barrel, Freeze
# 1v1 Op Deck: Hog, Musketeer, Ice Golem, Fireball, Ice Spirit, Fire Spirit, Skeletons, Cannon
# 2v2 Op Deck: Whatever I want it to be
