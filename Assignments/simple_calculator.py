def add(x, y):
    print(float(x) + float(y))
def subtract(x, y):
    print(float(x) - float(y))
def multiply(x, y):
    print(float(x) * float(y))
def divide(x, y):
    print(float(x) / float(y))
def exponent(x, y):
    print(float(x) ** float(y))
def modulus(x, y):
    print(float(x) % float(y))
def floor_divide(x, y):
    print(float(x) // float(y))

add_x = input("What number do you want to add?\n> ")
add_y = input("What number do you want to add to it?\n> ")
add(add_x, add_y)
sub_x = input("What number do you want to subtract from?\n> ")
sub_y = input("What number do you want to subtract from it?\n> ")
subtract(sub_x, sub_y)
mult_x = input("What number do you want to multiply?\n> ")
mult_y = input("What number do you want to multiply it by?\n> ")
multiply(mult_x, mult_y)
div_x = input("What number do you want to divide?\n> ")
div_y = input("What number do you want to divide it by?\n> ")
divide(div_x, div_y)
exp_x = input("What number do you want to exponent?\n> ")
exp_y = input("What power to you want to take it to?\n> ")
exponent(exp_x, exp_y)
mod_x = input("What number do you want to modulus divide?\n> ")
mod_y = input("What number do you want to modulus divide it by?\n> ")
modulus(mod_x, mod_y)
floor_div_x = input("What number do you want to floor divide?\n> ")
floor_div_y = input("What number do you want to floor divide it by?\n> ")
floor_divide(floor_div_x, floor_div_y)