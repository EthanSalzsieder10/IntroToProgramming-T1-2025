for i in range(20):
    if i == 15:
        break
    print(i + 1)

print()

for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i)

print()

for i in range(50):
    pass #TODO:Print i times 10

print()

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

print()

list = [5, 7, 67, 90, -5, "there will be an error if it gets to this"]
sum = 0
for i in list:
    if i < 0:
        break
    sum += i
print(sum)