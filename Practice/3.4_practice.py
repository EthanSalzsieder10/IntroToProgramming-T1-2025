try:
    numerator = input("numerator\n>")
    denominator = input("denominator\n>")
    result = (int(numerator) / int(denominator))
except ZeroDivisionError:
    result = "Error: cannot divide by zero."
except ValueError:
    result = "Error: must be integers"
finally:
    print(result)

import random #you need to do this for every script you want to use random in
r = random.randint(0, 10)
print()
print("random number")
print(r)
r2 = random.random()
print(r)