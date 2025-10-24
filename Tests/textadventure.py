king_activate = False
op_tower = 3000
my_tower = 3000
doubt = 0
def start():
    print("\nWhat game mode do you want to play?")
    print("1. Trophy Road")
    print("2. Classic 2v2")
    print("3. None, play Clash of Clans")
    choice = input(">>>")
    print()
    if choice == "1":
        tr_first_play()
    elif choice == "2":
        print("You try to play a 2v2, but the server for 2v2s seems to be down. It's as if the developers of the game were too lazy to fix the issue and are instead investing all of their time and energy into Trohpy Road. You play a trophy road game instead.\n")
        tr_first_play()
    elif choice == "3":
        ending_1()
    else:
        print("Invalid Input. Must be a number 1-3.")
        start()
def tr_first_play():
    print("You load into a trophy road game. Your opponent's tower level is two above yours and they are already spamming the goblin 'mimimimimi' emote.\n")
    print("The first 10 seconds pass and no one has played a card. You are leaking elixer, as is the enemy. What do you do?")
    print("1. Push Valkyrie and Prince on the bridge")
    print("2. Fireball the Towers")
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
    global op_tower
    op_tower = op_tower - 500
    print("You push a Valk and Prince on the bridge. Your opponent plays a Pekka, which mostly defends, but you get a few hundred damage on the tower.\n")
    print("Your opponent is being a little coward and still not playing any offense. What do you do?")
    print("1. Fireball the Towers")
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
    global op_tower
    king_activate = True
    op_tower = op_tower - 150
    print("You strategically place your fireball to hit the King and Princess tower. You're a genius.\n\nYour Opponent sends a laughing emote and then plays a Mega Knight. What do you do?")
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
        doubt = doubt + 1
        print("No you don't. You must keep playing. This is why we Clash. You place a cannon to distract the Mega Knight.")
        tr_cannon()
    else:
        print("Invalid Input. Must be a number 1-4.")
        encounter()
def tr_cannon():
    global my_tower
    my_tower = my_tower - 500
    print("\nThe cannon distracts the Mega Knight long enough for the tower to only take a few hits. You suspect the opponent has no elixer. What do you do?")
    print("1. Push with Inferno Dragon")
    print("2. Push with Skarmy")
    print("3. Push with Prince")
    print("4. Wait to build more elixer before pushing.")
    choice = input(">>>")
    print()
    if choice == "1":
        tr_inferno_dragon()
    elif choice == "2":
        print("He didn't have a lot of elixer, but he had a little. Your push gets ruined by a single log.")
    elif choice == "3":
        print("Prince is the best and most balanced card. Your opponent's tower effectively never existed.")
    elif choice == "4":
        print("As you gain more elixer, so does your opponent. He rockets your Tower.")
    else:
        print("Invalid Input. Must be a number 1-4.")
        tr_cannon()
def tr_inferno_dragon():
    global op_tower
    global king_activate
    if king_activate == True:
        print("It would've worked, but you activated the King Tower by fireballing it so you only get chip damage.")
        op_tower = op_tower - 500
    else:
        print("Your opponent can't defend the dragon and you get a lot of damage on the tower.")
        op_tower = op_tower - 2000
def tr_final_minute():
    print("\nYou enter the last minute of the game, and 2x elixer activates. No towers have been taken yet. What do you do?")
    print("1. Push with Valkyrie and Prince")
    print("2. Spell the tower")
    print("3. Wait for your opponent to play first")
    print("4. Why play at all?")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You push Valkyrie and Prince. Your opponent can only stall with a tesla tower, and takes some good damage.")
    elif choice == "2":
        print("You spell the tower. It gets a little damage.")
    elif choice == "3":
        print("You decide its better to wait for your opponent to plays first so you can properly counter.")
    elif choice == "4":
        global doubt
        doubt = doubt + 1
        print("But think of the trophies. Think of the evolutions you'll unlock. You have some time to reflect on this while you wait for your opponent to play first.")
    else:
        print("Invalid Input. Must be a number 1-4.")
        encounter()
def tr_final_wait():
    global my_tower
    my_tower = my_tower - 0.0
    print("Aaaaaand he played a Mega Knight and a Pekka together somehow. How do you defend?")
    print("1. Skarmy")
    print("2. Cannon")
    print("3. Fireball and prayers")
    print("4. Accept the Defeat and send a 'good game!' emote")
    choice = input(">>>")
    print()
    if choice == "1":
        print("")
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    elif choice == "4":
        global doubt
        doubt = doubt + 1
        print("You can't give up when you came this far. You must keep pushing. You must reach 10k trophies or your life will have no meaning. You place a skarmy behind the Pekka and hope it works.")
    else:
        print("Invalid Input. Must be a number 1-4.")
        encounter()
def encounter():
    global op_tower
    op_tower += 0.0
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
def check_towers():
    if op_tower <= 0:
        print("You successfully take your opponent's tower.")
    elif my_tower <= 0:
        print("Your opponent takes your tower.")
def ending_1():
    print("You play Clash of Clans.")
    print("Ending 1 of 5: Worst Ending\n")
def ending_2():
    print("Your opponent spams the laughing emote as you have to watch yourself get 3-Crowned no diff. You will never psycologically recover from this game.")
    print("Ending 2 of 5: Crashout\n")
def ending_3():
    print("You let out a huge sigh as your opponent somehow edges out a win. But if you play ONE more game, you'll come back.")
    print("Ending 3 of 5: Denial\n")
def ending_4():
    print("")
    print("Ending 4 of 5: Doubt\n")
def ending_5():
    print("LOOOL GGS TOO EZ THIS IS THE BEST GAME EVER")
    print("Ending 5 of 5: Pride\n")
def secret_ending():
    print("You decide that is enough screwing around with your life. You delete Clash and you invest in your future. You grow up to marry your soulmate and have 3 children who live with you in your mansion.")
    print("Secret: Best Ending\n")

print("\nYou are a high school boy who is hopelessly addicted to Clash Royale. You pull out your phone in the middle of math class because you physically can't live without it.")
start()
import turtle
t = turtle.Turtle()
t.speed(6)
t.shape("turtle")
t.penup()
t.goto(-175, 100)
t.pendown()
t.goto(-75, 100)
t.goto(-175, 100)
t.goto(-175, 0)
t.goto(-75, 0)
t.goto(-175, 0)
t.goto(-175, -100)
t.goto(-75, -100)
t.penup()
t.goto(-50, -100)
t.pendown()
t.goto(-50, 100)
t.goto(50, -100)
t.goto(50, 100)
t.penup()
t.goto(75, 100)
t.pendown()
t.goto(75, -100)
t.goto(175, -50)
t.goto(175, 50)
t.goto(75, 100)
# Deck: Prince, Evo Valk, Fireball, Evo Inferno Dragon, Baby Dragon, Log, Cannon, Skarmy
# TR Op Deck: Pekka, Skarmy, Evo Mega Knight, Tesla Tower, Rocket, Log, Evo Goblin Barrel, Freeze
# 2v2 Op Deck: Whatever I want it to be
