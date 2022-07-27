import random

roll_one = random.randint(1,6)
roll_two = random.randint(1,6)
roll_count = 1

while roll_one != 1 or roll_two != 1:
    print(roll_one, roll_two)
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)
    roll_count += 1

print(roll_one, roll_two)
print("Victory, snake eyes!!")
print(f"And it only took {roll_count} rolls!")