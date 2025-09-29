fav_animal = input("What is your favorite animal?\n> ")
# asks for the name of users favorite animal
fav_reason = input("What do you like about them?\n> ")
# asks why the user likes that animal
animal_color = input("What color/s are they?\n> ")
# asks for the animal's color
animal_habitat = input("Where do they live?\n> ")
# asks where the animal lives. could be a country or biome
animal_food = input("What do they eat?\n> ")
# asks for the animals diet
animal_sound = input("What sound do they make?\n> ")
# asks user to spell out the sound the animal makes
animal_size = input("Would you say they are a small, medium, or large animal?\n> ")
# asks the user what size they consider the animal
animal_type = input("Are they a mammal, reptile, amphibian, etc.?\n> ")
# asks what type of animal it is
animal_fact = input("What is a fun fact about your animal?\n> ")
# asks the user for a fun fact about the animal
animal_texture = input("Are they furry, scaly, feathery, etc.?\n> ")
# asks the user what the texture of the animal is
print("Your favorite animal is the " + fav_animal + " because " + fav_reason + ". They are a " + animal_type + " and they live in " + animal_habitat + ". They are " + animal_color +  " and the make a " + animal_sound + " sound. They are " + animal_size +  " and " + animal_texture + ". They eat " + animal_food + ". A fun fact about them is that " + animal_fact + ".")
# puts all of the information in a short paragraph, not necessarily in the order the user was asked