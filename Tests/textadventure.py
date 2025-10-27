king_activate = False
op_tower = 3000
my_tower = 3000
doubt = 0
def start():
    print("\nWhat game mode do you want to play?")
    print("1. Trophy Road")
    print("2. Classic 2v2")
    print("3. Neither, play Clash of Clans")
    choice = input(">>>")
    print()
    if choice == "1":
        first_play()
    elif choice == "2":
        print("You try to play a 2v2, but the server for 2v2s seems to be down. It's as if the developers of the game were too lazy to fix the issue and are instead investing all of their time and energy into Trohpy Road. You play a trophy road game instead.\n")
        first_play()
    elif choice == "3":
        ending_1()
    else:
        print("Invalid Input. Must be a number 1-3.")
        start()
def first_play():
    print("You load into a trophy road game. Your opponent's tower level is two above yours and they are already spamming the goblin 'mimimimimi' emote.\n")
    print("The first 10 seconds pass and no one has played a card. You are leaking elixer, as is the enemy. What do you do?")
    print("1. Push Valkyrie and Prince on the bridge")
    print("2. Fireball the Towers")
    print("3. Split Skarmy in the back")
    print("4. Wait for the opponent to play first")
    choice = input(">>>")
    print()
    if choice == "1":
        prince_valk()
    elif choice == "2":
        fire_king()
    elif choice == "3":
        print()
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        first_play()
def prince_valk():
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
        fire_king()
    elif choice == "2":
        log_cycle()
    elif choice == "3":
        print("")
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        prince_valk()
def fire_king():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@#.-%@:-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@+.:#@-=+@@@@@@#+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@%%@*.:*@-.:*@@@@*.-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("% .%#  :@-..=@@@@::+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+%@@@@=+#@@@@@@@@")
    print("%..+%  .%=  =@@@=.:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-+%@@@-=*@*=%@@@@")
    print("@  :#.  *+  =@@*.:=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-=+%@@--+%%-*@@@@")
    print("@.  *:  #+  *@@:.-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#*+*=-=*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:=*%@-.-#@-=@@++")
    print("@+  :.    ...::-=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.  .:---:==-+*%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-:-*@+.:+@.:%%++")
    print("@*.      .:..:-=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= .: :-==+*+**+**#*#%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.:-==----=+@@++")
    print("@-. ....::::=+=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= .....:-=++*###%@@@@##%@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@%@@%@+ ....-:.:=:=%@")
    print("@-  .. .::-----=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  ..  .:-==++****#%@@@@@%%@@%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+=+#%%--::+=.   .=-+")
    print("@+...:::.::::-:::::::-+*#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=      ..:-==++===++*#%@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:=****#@@*-=@%:.    .=")
    print("@#:.:::..:::::.:-:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=   . . .:---===--==+*#@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%@@@@@@@@@%@%%  -.....:..*#*")
    print("@=. ..::.::-::--=%%*====*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       .:-+++++++**#%@@@@@%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%###*+=+*@+:  .=")
    print("@@-:.::.:::---==+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   :.    :--+=:---=++##%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+=+**+-#@@+. -#")
    print("@@---==-----=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   . .-*%%%#*+-+*%@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%#%#++#%%@++.+@")
    print("@@-:::::-=+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    .+#**####=-*@@####@@@@@@@%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####%#%#***+*@%%#=%@")
    print("@%:...:-=-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*    -#%%@@%*=:-=@@==*%@@@@@@@@####################%%%%%%%%%%%%##########+=*+*+*-=+%@")
    print("@#:....-=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+-   :=:===*+=-:=%@@++*%@@@@@@%###########################################+*=--..==#@")
    print("@= . .:-=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#- :.  :=*#%=-=  :-@@*+***#@@@@%*##########################################*- :--+#@@@")
    print("%+=**##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=-. .:-=++--=. ::+@@@%**#@@@@@############################################%@@@@@@@@@@")
    print("*%***##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%:- .:-*=:=*==##@@@@@@@@%@@@@@#############################################@@@@@@@@@@")
    print("*@+**##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%*..::-:-++=-:-==+#@@@@@@@@@@@*####################################################%@")
    print("#@***##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@.. .:-+=====+*#%@@@@##%@@@%######################***********#########****#@%%%@@@@@")
    print("@****%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%%%-.--:*#*=-:---+#%@#=@@@@*##########************************************#@@%%%%%@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%@+-+-*====---=*%@@@%@@@#**#********************************************#@@%%%%%@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%@%%%+.-*+==---==*%@@@@@@@@*###********************************************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@%%%%%@%*:%=--*@@%##@@@@@@@@@@@@@%**##******************************************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%%%%%%%%%%%%%%###%%%%#+-=*@++%**%%@@@@@@@@@@@@@@@@@@@#******************************************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@-. ...=*%@%#****#**#*########**#*++++@@@**==+*@%*#@@@@@@@@@@@@@@@@@@%*++*%@@@@@@@@@@@#**********************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@#   . :***@@%%@@@%@%@@@@@@@@@@%#@@###+*@@@@#:=+==*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@********++************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@=:    +@#%@@@@@@@@@@@@@@@@@@@@@@@@@@##%@@@@*+=+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**+++*++++++**+++*@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@-.  :#@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@%**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##++*+**+++*++++*@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++++++++++++#@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+*@@@@@@%@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+++++#@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@%%@#@@+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@%%%%*#@+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@%%@@@@@@@%%%%%%#%@+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@#%@@@@@@@@%%%@%%@%@+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@%@@@@%%%%*%@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@%@#%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("====*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@%##%%@@@##@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%@@%@@@@@@@%%%%@@@@@@%#@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#**")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% +@@    -@+   =@*   =@.-@@@ :@@ *     *    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+===:..::-==")
    print("@@@@@@@@@@@@@**%%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ : %@ .%= @. +@@* #@@ @.-@@@ -@@ #%# =@@ -%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*--=+-..::--=+*%")
    print("@@@@@@@@@@@@@#*%@@*-:#@@@@@@@@@@@@@@@@@@@@@@@@@@: *  @ :@# #@@% .+ #@@ %.-@@@ -@@ *## =@@ =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@====+=..::-==+#%%")
    print("@@@@@@@@@@@@@%#%@@@-+@@@@@@@@@@@@@@@@@@@@@@@@@@* @@@ +  . -%+ : =@*.. =@. . =* . -@#* =@@    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+====+:.::--=+*%%%")
    print("@@@@@@@@@@@@@@%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@%%@@@@@@@%@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+===+=.::-==++%%%@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@%@%@@@@%%@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@++++++-.:-==++*%@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@#         .@@@@%    @@@.    @@@@@%#   -@@@            :@@     +@@@@@@@@.     @@@@@@@@    -@@@@@@@@++++*+:.--==+**%@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@.   .*#*=    #@@%    @@@.     %%%%@%   -@%@    ========*@@      %@@@@@@=      @@@@@@@-     *@@@@@@@++++*=::-==++*#@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@:   +@@@@@@    @@%    @@@.      @%@%%   -@%@    @@@@@@@@@@@      :@@@@@@       @@@@@@%       @@@@@@%+++**-::-==+**%@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@%%%@@%    @@@:   .   *@%%   -@@@    @@@@@@@@@@@   :.  #@@@@-  =    @@@@@@   :@   .@@@@@#++**=::-==+**#%@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@#   .@@@@@@@@@@@@@%    @@@:   @=   *@%   -@@@           *@@@   -#   @@@#   @    @@@@@:   %@%   +@@@@@+***-.:-=++**#@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@%   .@@@@@@@@@@@@@%    @@@.   @@+   =%   -@@@    .......%@@@   :@-  .@@   %@    @@@@*   -@@@-   @@@@@#**#::--=+**#%@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@%    @@@@@@@@@@@@@%    @@@:   @@@*       -@@@    @@@@@@@@@@@   :@@   *:  =@%    @@@@            .@@@@@**#-:-==++*#@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@:   =@@@@@@    @@#    @@@.   @@@@%      -@@@    @@@@@@@@@@@   .@@#      @@%    @@@-             -@@@@**#=--+*+*##@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@.    -==:    %@@%    @@@.   @@@@@@     -@@@    :..:::..+@@   .@@@-    #@@%    @@*   :@@@@@@@    #@@@*#%=-=*#**##@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@%         =@@@@%   .@@@:   @@@@@@@    -@@@            :@@   .@@@@   -@@@%    @@    %@@@@@@@@   .@@@*#%==*###*#%@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###%=+**##@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%*+**%@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%@#+*#@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%@%*##@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@%*#@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@#%@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@#@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    global king_activate
    global op_tower
    king_activate = True
    op_tower = op_tower - 150
    print("You strategically place your fireball to hit the King and Princess tower. You're a genius.\n")
    print("Your Opponent sends a laughing emote and then plays a Mega Knight. What do you do?")
    print("1. Place a cannon to distract")
    print("2. Play Inferno Dragon on the Mega Knight")
    print("3. Push Skarmy on the other lane")
    print("4. Accept Defeat")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You place a cannon to distract the Mega Knight.")
        mk_cannon()
    elif choice == "2":
        mk_inferno()
    elif choice == "3":
        mk_skarmy()
    elif choice == "4":
        global doubt
        doubt = doubt + 1
        print("No you don't. You must keep playing. This is why we Clash. You place a cannon to distract the Mega Knight.")
        mk_cannon()
    else:
        print("Invalid Input. Must be a number 1-4.")
        fire_king()
def log_cycle():
    print("\nYou play the log to cycle your cards. What do you do?")
    print("1. Fireball the Towers")
    print("2. Place Baby Dragon in the back")
    print("3. Play Inferno Dragon on the Bridge")
    print("4. Wait for your opponent to play and spam chicken emotes")
    choice = input(">>>")
    print()
    if choice == "1":
        fire_king()
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    elif choice == "4":
        print("")
    else:
        print("Invalid Input. Must be a number 1-4.")
        log_cycle()
def mk_cannon():
    global my_tower
    global op_tower
    my_tower = my_tower - 500
    print("\nThe cannon distracts the Mega Knight long enough for the tower to only take a few hits. You suspect the opponent has no elixer. What do you do?")
    print("1. Push with Inferno Dragon")
    print("2. Push with Skarmy")
    print("3. Push with Prince")
    print("4. Wait to build more elixer before pushing.")
    choice = input(">>>")
    print()
    if choice == "1":
        if king_activate == True:
            print("It would've worked, but you activated the King Tower by fireballing it so you only get chip damage.")
            op_tower = op_tower - 500
            print(op_tower)
            final_minute()
        else:
            print("Your opponent can't defend the dragon and you get a lot of damage on the tower.")
            op_tower = op_tower - 2000
            final_minute()
    elif choice == "2":
        print("He didn't have a lot of elixer, but he had a little. Your push gets ruined by a single log.\n")
        final_minute()
    elif choice == "3":
        prince_push()
    elif choice == "4":
        tower_rocket()
    else:
        print("Invalid Input. Must be a number 1-4.")
        mk_cannon()
def mk_inferno():
    global my_tower
    my_tower = my_tower - 500
    print("The dragon kills the Mega Knight in a decently short time, but there was nothing distracting it, so it gets a few hits on the tower.\n")
    print("Mega Knight costs 7 elixer, so you should be able to play something.")
    print("1. Push with Prince")
    print("2. Push with Skarmy")
    print("4. Wait to build elixer")
    choice = input(">>>")
    print()
    if choice == "1":
        prince_push()
    elif choice == "2":
        print("He didn't have a lot of elixer, but he had a little. Your push gets ruined by a single log.\n")
        final_minute()
    elif choice == "3":
        tower_rocket()
    else:
        print("Invalid Input. Must be a number 1-3.")
        mk_inferno()
def mk_skarmy():
    global my_tower
    my_tower = my_tower - 2500
    global op_tower
    op_tower = op_tower - 2
    print("Why? You get like 2 damage on the opponents tower, and he gets 2500 on yours.\n")
    print("What do you do now?")
    print("1. Push with Inferno Dragon")
    print("2. Push with Prince")
    print("3. Spam the 6 7 emote and do nothing else.")
    choice = input(">>>")
    print()
    if choice == "1":
        if king_activate == True:
            print("It would've worked, but you activated the King Tower by fireballing it so you only get chip damage.")
            op_tower = op_tower - 500
            final_minute()
        else:
            print("Your opponent can't defend the dragon and you get a lot of damage on the tower.")
            op_tower = op_tower - 2000
            final_minute()
    elif choice == "2":
        prince_push()
    elif choice == "3":
        secret_ending_2()
    else:
        print("Invalid Input. Must be a number 1-4.")
        mk_skarmy()
def prince_push():
    global op_tower
    op_tower = op_tower - 2000
    global my_tower
    print("Prince is the best and most balanced card. Your opponent's tower takes massive damage.\n")
    print("Your opponent tries to get you back with a goblin barrel. You have almost no elixer. What do you do?")
    print("1. Play Log on the goblins")
    print("2. Let the tower take care of the goblins")
    choice = input(">>>")
    print()
    if choice == "1":
        print("The log takes the goblins out quickly. They get no damage on the tower.")
        final_minute()
    elif choice == "2":
        print("Your opponent freezes the tower and the goblins get a lot of damage.")
        my_tower = my_tower - 500
        final_minute()
    else:
        print("Invalid Input. Must be a number 1-2.")
        prince_push()
def tower_rocket():
    global my_tower
    global op_tower
    my_tower = my_tower - 600
    print("As you build more elixer, so does your opponent. He rockets your tower\n")
    print("Rocket costs 6 elixer, so he has to be low. What do you do?")
    print("1. Push with Baby Dragon")
    print("2. Push with skarmy")
    print("3. Fireball the towers")
    print("4. Wait for more elixer again")
    choice = input(">>>")
    print()
    if choice == "1":
        print("Your opponent can't defend, good play.")
        op_tower = op_tower - 1000
        final_minute()
    elif choice == "2":
        print("Your opponent plays log. Why do people have swarm decks?")
        final_minute()
    elif choice == "3":
        print("You know, you should save spells for when your opponent can actually defend, but okay.")
        op_tower = op_tower - 200
        final_minute()
    elif choice == "4":
        print("Your opponent mirrors rocket on the tower. Just play a card, you coward.")
        my_tower = my_tower - 600
        final_minute()
    else:
        print("Invalid Input. Must be a number 1-4.")
        tower_rocket()
def final_minute():
    global op_tower
    global doubt
    print("\nYou enter the last minute of the game, and 2x elixer activates. No towers have been taken yet. What do you do?")
    print("1. Push with Valkyrie and Prince")
    print("2. Spell the tower")
    print("3. Wait for your opponent to play first")
    print("4. Why play at all?")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You push Valkyrie and Prince. Your opponent can only stall with a tesla tower, and takes some good damage.")
        op_tower = op_tower - 500
        if op_tower <= 0 and doubt > 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_4()
        elif op_tower <= 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_5()
        else:
            universal_final_play()
    elif choice == "2":
        print("You spell the tower. It gets a little damage.")
        op_tower = op_tower - 200
        if op_tower <= 0 and doubt > 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_4()
        elif op_tower <= 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_5()
        else:
            universal_final_play()
    elif choice == "3":
        print("You decide its better to wait for your opponent to plays first so you can properly counter.")
        final_wait()
    elif choice == "4":
        doubt = doubt + 1
        print("But think of the trophies. Think of the evolutions you'll unlock. You have some time to reflect on this while you wait for your opponent to play first.")
        final_wait()
    else:
        print("Invalid Input. Must be a number 1-4.")
        final_minute()
def final_wait():
    global my_tower
    global doubt
    print("\nAaaaaand he played a Mega Knight and a Pekka together somehow. How do you defend?")
    print("1. Skarmy")
    print("2. Cannon")
    print("3. Fireball and prayers")
    print("4. Accept the Defeat and send a 'good game!' emote")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You place a skarmy behind the Pekka as a last desperate play. It somehow works and distracts both troops long enough to not take damage. Your opponent must be fuming.")
        universal_final_play()
    elif choice == "2":
        print("You place a cannon to distract. It takes out the Mega Knight, but the Pekka still does massive damage to your tower")
        my_tower = my_tower - 2000
        if my_tower <= 0 and doubt > 0:
            print("The Pekka takes your tower and your opponent sends a chicken emote.\n")
        elif my_tower <= 0:
            print("The Pekka takes your tower and your opponent sends a chicken emote.\n")
        else:
            universal_final_play()
    elif choice == "3":
        print("You fireball the troops and pray. It takes about half of their health. You have no elixer and your towers are doomed.\n")
        if doubt > 0:
            ending_2()
            return
        else:
            ending_3()
            return
    elif choice == "4":
        doubt = doubt + 1
        print("You can't give up when you came this far. You must keep pushing. You must reach 10k trophies or your life will have no meaning. You place a skarmy behind the Pekka and hope it works.\n\nIt somehow works and distracts both troops long enough to not take damage. Your opponent must be fuming.")
        universal_final_play()
    else:
        print("Invalid Input. Must be a number 1-4.")
        final_wait()
def universal_final_play():
    global op_tower
    global my_tower
    print("\nIt's overtime now. You feel like this game has lasted forever. If you lose this game, you might consider thinking about deleting the game. What do you do?")
    print("1. Push with Prince and Valkyrie")
    print("2. Push with Baby Dragon and Inferno Dragon")
    print("3. Push with Skarmy and freeze on the tower")
    print("4. Place skarmy in the back and cannon in the center for defense")
    if doubt == 3:
        print("-OR-")
        print("5. Delete Clash and end the pain")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You play a strong push and the opponent is unable to defend.\n")
        op_tower = op_tower - 2000
        if op_tower <= 0 and doubt > 0:
            ending_4()
            return
        elif op_tower <= 0:
            ending_5()
            return
        else:
            print("But it's not enough. The tower is till hanging on by a thread and you are out of elixer. The opponent plays evo goblin barrel and freezes the tower.\n")
            if doubt > 0:
                ending_2()
                return
            else:
                ending_3()
                return
    elif choice == "2":
        print("You play a completely arial push. The opponent did not prepare for this and you ravage the tower.\n")
        if doubt > 0:
            ending_4()
            return
        else:
            ending_5()
            return
    elif choice == "3":
        print("Your opponent counters with a single log. You're done for. He plays evo goblin barrel and freezes the tower.")
        if doubt > 0:
            ending_2()
            return
        else:
            ending_3()
            return
    elif choice == "4":
        print("Your Opponent spams in one lane to get a quick win, but your defense tanks most of the damage.\n")
        my_tower = my_tower - 500
        if my_tower <= 0:
            print("But most doesn't cut it. That little bit of damage is all he needs.\n")
            if doubt > 0:
                ending_2()
                return
            else:
                ending_3()
                return
        else:
            print("Your opponent runs out of elixer and you are free to place one prince and take the tower.\n")
            if doubt > 0:
                ending_4()
                return
            else:
                ending_5()
                return
    elif choice == "5" and doubt == 3:
        secret_ending()
    else:
        if not doubt == 3:
            print("Invalid Input. Must be a number 1-4.")
        else:
            print("Invalid Input. Must be a number 1-5.")
        universal_final_play()
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
def ending_1():
    print("You play Clash of Clans.")
    print("Ending 1 of 5: Worst Ending\n")
def ending_2():
    print("Your opponent spams the laughing emote as you have to watch yourself get 3-Crowned no diff. You will never psycologically recover from this game. Why DO we Clash?")
    print("Ending 2 of 5: Crashout\n")
def ending_3():
    print("You let out a huge sigh as your opponent somehow edges out a win. But if you play ONE more game, you'll come back.")
    print("Ending 3 of 5: Denial\n")
def ending_4():
    print("You won, but what does it matter? You will only lose a thousand more games. You would dwell on this thought, but you fingers already clicked the 'play again' button. Eh, one more game.")
    print("Ending 4 of 5: Doubt\n")
def ending_5():
    print("LOOOL GGS TOO EZ THIS IS THE BEST GAME EVER")
    print("Ending 5 of 5: Pride\n")
def secret_ending():
    print("You decide that is enough screwing around with your life. You delete Clash and you invest in your future. You grow up to marry your soulmate and have 3 children who live with you in your mansion.")
    print("Secret: Best Ending\n")
def secret_ending_2():
    print("****###********####*+-::-*####*##%%%*#%%####**#%##%%%%%%%%#####*+:...:--==+*#=+#####*++**#%%@@@#%@@@")
    print("****#%%%@@@@@%#####%%*-+###%#**%%%%%#*%####%######%%%%%%%%%%####*+:=#@%***###%#%%#%@%###*#%@@##**#%#")
    print("***#%@@@@%@@%%%%@@@@%**#**##**####%%%##%#%##%#%%%#%%@%@%%%%%%#%##*=:+@%##%#####%#*%%%@#%%#*#@#%%%%%%")
    print("*##%@%@@%%%##%@@@@@%**#**##*###%#%@@@%#%#%##%#%%%#%%@%%%%##%%%#%##*=:-*##%#**#%%*#%#*%%%%%%%@@%#%@@%")
    print("*#%%%@@%%@##%@@@@@%**#**######%%%%@@@%##%%%%%%#%%###%%######%%#%%##*+:.+%%#+**%@%@#*#@*=%@@@@%*-*%%@")
    print("**%#%%###%%%@@@@@%**##**###%%%%%%@@@%#*%%%%%%%###%%#########%#%%###**+::#%*=+*##%%#%%#+*%@@%%%#+*%%@")
    print("*#%#%#**#%@%%%%%%+*##**#########%%%%##%%%@%%%%%%%%%%%%%%%%%%%%%%%%%#**+:-*#=-*#*###%@*-+%@%#*#***%%%")
    print("*###%#**#%%####%-*###**%#%%%%%%#####%%#%@@%%%%%%%@@@@@@@@@@@@@@%%%%%#**+::*#+*%#%#***+=*%###+#+--=*%")
    print("##%#%###%%%@@@@*+####*%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%%%@@@@@%%%###+-+**#@%##*%#+*##***%@#**##%")
    print("#%%%@%@@%%%*=+=-#####%%%%%%%%%########%%%%%%##%%%%%%%%###***##%%%@@%%%%##+-=*#@@#**%%*#*#***#%#####@")
    print("%@@@%@@@%%####=**###%%%@%%%##**++++***##%%%%###%%%%%##**====+*##%%@@@@%%%#+::*%%***###%%##%%#*+*##@@")
    print("@@%@@@@@%@@@%*=######%#%####**+=---==+*#####**##%%%%#*+:....-=*#%%@@@@@@%%#*-+%@%#+***##%%%@%***#@%@")
    print("@@%@@@@@%@@@%=**#%%%%%%@%%##*+-.....-=+**##****#%%%##*+:....-=+#%%%@@@@@@%%#*++%#%@%**+#@@@@@%**###%")
    print("@@%@@@@@@@@@%=##%%@@@@@@%%%#*+=....:-=+***##***###%##*+=-::-=+*##%%@@@@@@@%%#*=----=*#*#@@@@@%@%#*#%")
    print("@@%@@@%@@@@@#+#%%@@@@@@@%%##*++-:::-=+*********#######**++++**###%%%@@@@@@@%%#**=-*%@@@%%@@@@%#####%")
    print("@@%@@@@@@@@@++#%@@@@@@@@###***++=++++++*********#####*********###%%%@@@@@@@@@%##*++#%%%%%%%#***##%#%")
    print("@@%@%@@@@@@%+*%%@@@@@@@%##****+++++++*********###%#%###*******####%@@@@@@@@@@@%%#*+=:=*%%####**#%%%%")
    print("%@%%##%%##%%++%%@%@@@@@%#******+++********####%%%%%%%%%##**######%%@@@@@@@@@@@@%%##***#%%#*#%%%%%%%%")
    print("%@%%**+#**##*+#%%%@@@@@##******+****#####%%@%%%%@@@@%%%%%#######%%%@@@@@@@@@@@@%%%#****%%#*#%@%%%%##")
    print("@@%%#*=--=+**+*#%@@@@@@##********##%#**##%###%%%%%%%%%#%%%%%%%%%%%@@@@@@@@@@@@%#*+=++##@@%##%@@@%%%#")
    print("@@%@%#*=----=+#%%@@@@@@###***####%%#********#############%%%@@%%%@@@@@@@@@@@@@%%#**#%@@@@@@@%@@@@%%%")
    print("@@@@@%*==+***##%%@@@@@@%#######%%#***++++++++*****#####%%%%%%@@@@@@@@@@@@@@@@@%%####%@@@@@@@@@@@@@@@")
    print("%@@@@@%+-=**##%%%@@@@@@%####%%@%#***************######%%%%%@@@@@@@@@@@@@@@@@@%####%@@@@@@@@@@@@@@@%@")
    print("##@@@@@@%++**##%@@@@@@@@#%%%%@%#*#####*****=--:+=-+***####%@@@@@@@@@@@@@@@@@@@%#*#@@@@@@@@@@@@@@@@@@")
    print("#%@@@@%*=++**#%%@@@@@@@@%%%%%@%#%%%#**---:::::.:.::---*+*##%@@@@@@@@@@@@@@%%@%%###%@@@#%%%%@@@@@@@@%")
    print("%%%##*=-==+*#%%%@@@@@@@@@%%%%@%%@@%#+=::::........:+#*###%%%@@@@@@@@@@@@@@%%%%*##*%@@@*###*#######%@")
    print("#**##*--=+**#%%%%%@@@@@@@@%%%@%@@@%#####**********#**####%%%@@@@@@@@@@@@@@@%###=+*#@@#+#%%%##%%%%%@@")
    print("%%##**%#***####%@@@@@@@@@@@%%%%@@@%%####**********#######%%%@@@@@@@@@@@@@@@@%%%#+-+%@@@%%@@@@%%%%%@@")
    print("%####%@@@%#*##%%@@@@@@@@@@@@%%@%@@%%%####*********#######%%%@@@@@@@@@@@@@@@@@@%##*+*@%%++**%@@@%%@@@")
    print("#%@@@@%@@@@%#*#%%@@@@@@@@@@@%%%@@@@%%#####********#######%%%@@@@@@@@@@@@@@@@@@@%##**+#+-=*#@%@@%@@#%")
    print("@%%@@%%@@@%%%%###%@@@@@@@@@@@%#%%@@%%####**********#######%%@%@@@@@@@@@@@@@@@@@%%##**=:-=%@@@@@@###@")
    print("@@@@@%%@@@@@@@@@%*%%@@@@@@@@@@%#%%%%%%###************#####%%%%@@@@@@@@@@@@@@@@@%%%###*==@@@@@@@@#%@@")
    print("@@@@%%@@%@@@@@@@%+*#%%@@@@@@@@%##%%%%%##***************###%%%%@@@@@@@@@@@@@@@@@@@%%###*=#@@@@@@@@@@@")
    print("@@@@@@@#+=+%@@@*-+*##%%%%@@@@@@####%%%###*************#######@@@@@@@@@@@@@@@@@@@@@%%%%###%@@@@@@@@@@")
    print("@@@@@@#==--*@#-=+**##%%%%%%@@@@%####%%#%##***********######%%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@#@@@@@@@@")
    print("@@@@@@#=--+%@+=+***#%%%%%%%%@@@@#####%%%%##**********#######%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%#@@@@@@@@")
    print("%@@@@@@@@@@@%=+**####%%%%%%%%@@@%#####%%%#####*****#########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%%@@@@@@@@@*-=***###%%%%%%%%%%@@@######%%#####***##*#######%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%###@@@@@*--+**#%##%%%%%%%%%%%%@@@#########################%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("##*===+=--=+***##%%%%%%%%%%%%%%%@@%#######################%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("##*+--::=+***#####%@@%%%%%%%%%%%%%%%#####################%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("#**=-:-=+***##%%%#%%%@@%%%%%%%%%%%%%%###################%@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@")
    print("#**=::=***#####%%%%%%%@@@@%%%%%%%%%@%%###%%###########%%@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@")
    print("%**=:-=***####%%%%%%%%%@@@@@@@%%%%%@%@%###%%%#%####%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@")
    print("@#*=-=+**#######%%%%%%%%@@@@@@@@@@@@@@@%#%%%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@")
    print("@%*=-+**######%%%%%@%%%%%%@@@%%@@@@@@@@@%#%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@")
    print("@%+==**#######%%%%@@@%%%%%%@@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@")
    print("%#*=+*#####%%%%%%%%@@@%%%%%%@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@")
    print("%#*=*######%%%%%%%%%@@@@%%%%%%@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@")
    print("%#*+*####%%%%%%%%%%%@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%#*+*#####%%%%%@%%%%@@@@@@@%%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Siiix Seeeveeeeen. That's a real emote you can get in the game now.")
    print("Ending 6 of 7: 6 7\n")

print("\nYou are a high school boy who is hopelessly addicted to Clash Royale. You pull out your phone in the middle of math class because you physically can't live without it.")
start()


# Deck: Prince, Valk, Skarmy, Evo inferno dragon, baby dragon, fireball, log, cannon