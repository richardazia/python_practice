import random
import array as arr

print("*" * 20)
print("The Dice Roller")
print("*" * 20)

n = 1
dice_faces = int(input("Please enter the number of faces: "))
dice_number = int(input("How many dice would you like to roll? "))
dice_results = ""

while n <= dice_number:
    result = random.randint(1, dice_faces)
    print(result)
    n += 1

print(dice_results)
