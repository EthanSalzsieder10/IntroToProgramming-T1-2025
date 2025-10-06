# Assignment 1
word_1 = input("Give me a word\n> ")
word_2 = input("Give me a second word\n> ")
word_3 = input("Give me a third word\n> ")
print(f"{str(word_1)} {str(word_2)} {str(word_3)}")

# Assignment 2
def add_three(x, y, z):
    print(int(x) + int(y) + int(z))
int_1 = input("Give me an integer\n> ")
int_2 = input("Give me a second integer\n> ")
int_3 = input("Give me a third integer\n> ")
add_three(int_1, int_2, int_3)

# Assignment 3
def data_three():
    word = input("Give me a word\n> ")
    integer = input("Give me a integer\n> ")
    flt = input("Give me a float\n> ")
    print(f"{float(integer) + float(flt)} {str(word)}")
data_three()