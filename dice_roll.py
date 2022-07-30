# import random

# print("*" * 20)
# print("The Dice Roller")
# print("*" * 20)

# n = 1
# dice_faces = int(input("Please enter the number of faces: "))
# dice_number = int(input("How many dice would you like to roll? "))
# dice_results = ""

# if isinstance(dice_faces, int):
#     while n <= dice_number:
#         result = random.randint(1, dice_faces)
#         print(result)
#         n += 1
# print(dice_results)

####
# Course solution

from random import randint
dice_faces = int(input("Please enter the number of faces: "))
dice_number = int(input("How many dice would you like to roll? "))

while True:
    result = "|"
    for die in range(dice_number):
        rand = randint(1, dice_faces)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (q to quit")
    if reply == "q":
        break
    