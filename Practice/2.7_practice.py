def square(number):
    return number * number
num = input("gimme number now\n> ")
result = square(int(num))
print(result)

global_var = 5 #Outside of functions
def example():
    local_var = 5 #Inside of Functions
    global global_var
    global_var = 6 #edit inside of functions