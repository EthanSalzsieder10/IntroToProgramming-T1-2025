import time
for i in range(10):
    print(10-i)
    time.sleep(1)

print()

sum = 0
integers = [5, 6, 8, 10, 25, 67, 35, 5, 2, 19]
for i in integers:
    sum = sum + i
print(sum)

print()

integers_2 = [1, 2, 3, 4, 5]
for i in range(len(integers_2)):
    integers_2[i] = integers_2[i]**2
print(integers_2)

print()

vowels = 0
string = input("Enter a String.\n>>>")
for i in string:
    if i == "A" or i == "a" or i == "E" or i == "e" or i == "I" or i == "i" or i == "O" or i == "o" or i == "U" or i == "u":
        vowels += 1
print(f"vowels: {vowels}")

print()

mult_num = input("Enter a number to multiply.\n>>>")
try:
    mult_num = int(mult_num)
except:
    print("Thats not a number sigma")
for i in range(11):
    print(f"{mult_num} x {i} = {mult_num * i}")

print()

names = ["Ben", "Noah", "Owen", "Overleveled Prince"]
for i in names:
    print(f"Hello, {i}!")