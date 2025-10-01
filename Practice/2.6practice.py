'''
def greet():
    print("Hello!")
    print("How are you?") #indented lines are inside the function

greet()

# Parameters and Arguments
def add(x,y):
    print(x + y)

add(10, 30) #woah its 40!!!!!

x = 6
y = 7

add(x, y)
'''

# Part 1

def add_five_numbers(num_1, num_2, num_3, num_4, num_5):
    print(num_1 + num_2 + num_3 + num_4 + num_5)

add_five_numbers(1, 2, 3, 4, 5)
add_five_numbers(6, 7, 8, 9, 10)
add_five_numbers(10, 20, 30, 40, 50)

# Part 2

def full_name(first, last):
    print(f"Your name is {first} {last}.")

first_name = input("What is your first name?\n> ")
last_name = input("What is your last name?\n> ")

full_name(first_name, last_name)

# Part 3

def area_calculator(length, width):
    print(f"The Area is {length * width}")

area_calculator(5, 5)
area_calculator(6, 7)
area_calculator(10,20)

# Part 4

def word_smash(word_1, word_2):
    print(f"{str(word_1)} {str(word_2)}")

word_smash("six", "seven")
word_smash(6, 7)
word_smash(6.7, 4.1)

# Part 5

def echo(string, number):
    print(str(string) * number)

echo("6 7", 6)
echo("cat", 20)
echo(5, 5)

# Part 6

def happy_birthday(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {str(name)}")
    print("Happy Birthday to you")

happy_birthday(first_name)