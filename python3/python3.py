# COLT Steele Python 3 course notes

# We can use += with strings

#month = "The month of"
#month += " August, and it is the 18th day"

#print(month)

#print("How far did you cycle today?")
#distance = input()
#distance_in_miles = float(distance) * 0.621371
#print(f"You cycled {distance} kilometres. That is equal to {round(distance_in_miles, 2)} miles.")

#print("How far did you cycle this year?")
#distance = input()
#distance_in_miles = float(distance) * 0.621371
#print(f"You cycled {distance} kilometres. That is equal to {round(distance_in_miles, 2)} miles.")

# # NO TOUCHING PLEASE---------------
# from random import randint
# choice = randint(1,10)
# # NO TOUCHING PLEASE---------------

# # YOUR CODE GOES HERE:
# if choice == 7:
#     print("lucky")
# elif choice == 3:
#     print("Three, not free")
# elif choice == 4:
#     print("Four, not for")
# elif choice == 8:
#     print("not as lucky")
# elif choice == 9:
#     print("Nine, not nein")
# elif choice != 7:
#     print("unlucky")

  
# city = input("What city do you live in? ")

# if city == "Nyon" or city == "Lausanne" or city == "Geneva":
#     print("You live within cycling distance.")
# else:
#   print("That's not within easy cycling distance. ")
  
# print("How old are you?: ")
# age = int(input("> "))

# if age < 9:
#   print(f"At age {age} You are too young to scuba dive. You can snorkel instead")
# elif age >= 9 and age <= 16:
#   print(f"At {age} You can scuba dive, but you need permission from a parent.")
# elif age >= 16 and age <= 65:
#     print(f"You can scuba dive freely at {age}, but you need a medical certificate.")
# else: 
#     print(f"Snorkeling is always an option at any {age}. Just hope the water is warm enough.")

# print(f"Does {age} require someone to work, or go to school, or be retired")


# if not ((age >= 0 and age <= 17) or (age > 65 and age < 140)):
#   print(f"At {age} you are stuck either at work, or at school")
# else: 
#   print("You are too young, or you are already retired, and can do whatever you want.")

# speed = input("How fast are you going? ")
# if speed != "":
#   if int(speed) >= 100 and int(speed) <= 120:
#     print(f"Welcome onto the motorway. You are travelling at {speed}")
#   elif int(speed) >= 120:
#     print(f"Slow down, you are {str(int(speed) -120)} above the speed limit")
#   else: 
#     print(f"You must be at 100 KM/h or more kilometres per hour to join the motorway. You are at {speed}km/h. Speed up")

# for char in "revision":
#   print(char)

# for number in range(1, 10):
#   print(number)

# #It prints from smallest to largest, but not vice versa 
# # Add up all odd numbers between 10 and 20
# # Store the result in x:
# x = 0

# # YOUR CODE GOES HERE:
# for x in range (10,21):
#     if x % 2 != 0:
#         x += x

#     print(x)

# times = int(input("How many times do I have to ask you kindly?"))
# # My solution to this challenge
# print("Don't slam the door!\n" * times)

# print("Rewind the VHS tape after you have finished watching the film!\n" * times)

# # Course solution
# for time in range(times):
#   print("Don't fly a kite during a hailstorm, you will damage the kite.")

  # challenge: 
  # For numbers from 1-20
  # 4 and 13 are unlucky
  # print no. is even for even numbers
  # print no. is odd for odd numbers

# My solution - the unlucky conditions need, to be first, to be displayed.

# for number in range(1, 21):
#   if number == 4:
#     print(f"{number} is unlucky")
#   elif number == 13:
#     print(f"{number} is unlucky")
#   elif number % 2 != 0:
#     print(f"{number} is odd")
#   else:
#     print(f"{number} is even")
# print("\n\n")
# # Course refactor:
# print("Course refactor\n\n")
# for num in range(1,21):
#   if num == 4 or num == 13:
#     state = "unlucky"
#   elif num % 2 == 0:
#     state = "even"
#   else: 
#     state = "odd"
#   print(f"{num} is {state}")

# pwd = input("You may enter, after having told us the pass phrase: ")
# while pwd != "I am wearing a mask":
#   print("Access denied")
#   pwd = input("You may enter, after having told us the pass phrase: ")
# print("Fantastic, you may now enter")

for smiley in range(1,11):
  print("\U0001f600" * smiley)

smile = 0
while smile <= 10:
  print("\U0001f600" * smile)
  smile += 1

# Nested loop course example
print("I want this in triplicate")
for x in range(3): # The next loop will repeat three times
  for num in range(1,11):
    print("\U0001f600" * num)

print("The inelegant way of solving the challenge")
# Without string multiplication 
for num in range(1,11):
  count = 1
  smileys = ""
  while count <= num:
    smileys += "\U0001f600"
    count += 1
  print(smileys)

# The Stop Copying Me App

imitate = input("Hey, how are you? What are you up to? ")
while imitate != "oh behave":
  print(f"{imitate} - " )
  imitate = input(f"{imitate}: ")
print("Fine, I will, but this isn't over. ")
