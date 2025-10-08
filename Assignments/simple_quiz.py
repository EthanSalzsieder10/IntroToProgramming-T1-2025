tally_score = 0
q_1 = input("What is 1 + 1\n>")
if q_1 == "2":
    tally_score = tally_score + 1
q_2 = input("What year was Al Pacino born\n>")
if q_2 == "1940":
    tally_score = tally_score + 1
q_3 = input("What grade do I have in Intro to programming\n>")
if q_3 == "A":
    tally_score = tally_score + 1
q_4 = input("What does Noah keep going on during class\n>")
if q_4 == "facebook marketplace":
    tally_score = tally_score + 1
q_5 = input("What button does Owen spam to complete assignments\n>")
if q_5 == "Tab":
    tally_score = tally_score + 1
q_6 = input("What's the best Snap to go to\n>")
if q_6 == "Osowski":
    tally_score = tally_score + 1
q_7 = input("What's the worst and best game of all time\n>")
if q_7 == "Clash Royale":
    tally_score = tally_score + 1
q_8 = input("If soemeone is better at clash than you, what are they\n>")
if q_8 == "Sweat":
    tally_score = tally_score + 1
q_9 = input("If someone is worse than you at clash, what are they\n>")
if q_9 == "Trash":
    tally_score = tally_score + 1
q_10 = input("Who had it out for owen\n>")
if q_10 == "Mr. Krebsbach":
    tally_score = tally_score + 1

print(f"You scored {tally_score} out of 10")
if tally_score > 6:
    print("You passed")
else:
    print("U failed lol")