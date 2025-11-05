fav_fruits = ["Strawberry", "Banana", "Pear", "Grapes", "Kiwi"]

print(fav_fruits[0])
print(fav_fruits[-1])

fav_fruits.append(input("enter a new fruit sima\n"))
print(fav_fruits)

fav_fruits.remove(input("enter a fruit to remove sima\n"))
print(fav_fruits)

fav_fruits.sort()
print(fav_fruits)

new_list = ["apple", "banana", "apple", "orange", "apple"]
print(new_list.count("apple"))

for i in fav_fruits:
    print(i)