grades = {"Alice": "A", "Bob":"B", "Charlie":"C", "David":"A", "Eve":"B"}
for i, j in grades.items():
    print(f"{i} has a {j}.")

print()

student = {"name": "Alice", "age": 16, "grade": "A"}
print(f"{student["name"]} is {student["age"]} years old.")

print()

student["grade"] = "A+"
print(student)

print()

movies = {"Tropic Thunder": "2008", "Tenacious D in The Pick of Destiny": "2006", "Inception":"2010"}
movie = input("Favorite movie?????????/\n>")
release = input("When was it released?\n>")
movies[movie] = release
print(movies)

print()

