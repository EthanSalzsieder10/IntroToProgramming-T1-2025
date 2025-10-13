x = input("Number. NOW.\n> ")
if x == "6":
    print("X equals six")
elif x == "7":
    print("X equals seven")
else:
    print("X is not six or seven")

if True:
    print("This will run no matter what")
elif False:
    print("This will never print")
else:
    print("this will also never print")

password = "Six Sendy"
def password_ask():
    password_attempt = input("What is the password?\n> ")
    print()
    if password_attempt == password:
        print("Yaay you got the password")
    else:
        print("Nuh uh try again")
        print()
        password_ask()
password_ask()