import time
print("Booting up AI.....")
time.sleep(1)
print("=== Your Menu Maker ===")
time.sleep(1)
print("Welcome to your menu maker")
time.sleep(1)
print("I will take your input to make a delicious menu ^_^")
time.sleep(1)
food = input("Name a food: ")
time.sleep(1)
plant = input("Name a plant: ")
time.sleep(1)
cooking_method = input("Name a cooking method: ")
time.sleep(1)
food_description = input("Give me a word to describe burnt food: ")
time.sleep(1)
household_item = input("Name a household item: ")
time.sleep(1)
description = input("Choose either base, bed or broth: ")
time.sleep(1)
ioa = input("Choose in or on: ")
time.sleep(1)
DIY_item = input("Name a DIY item: ")
time.sleep(1)
print("Compling items....")
time.sleep(3)
print("Generating Menu....")
time.sleep(3)
print("Here is your menu!")
time.sleep(1.5)
print("""-----MENU-----
""",cooking_method, food, "with", food_description, plant, ioa, " a flavorful", description, "of", DIY_item)