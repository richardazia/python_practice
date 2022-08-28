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

# for smiley in range(1,11):
#   print("\U0001f600" * smiley)

# smile = 0
# while smile <= 10:
#   print("\U0001f600" * smile)
#   smile += 1

# # Nested loop course example
# print("I want this in triplicate")
# for x in range(3): # The next loop will repeat three times
#   for num in range(1,11):
#     print("\U0001f600" * num)

# print("The inelegant way of solving the challenge")
# # Without string multiplication 
# for num in range(1,11):
#   count = 1
#   smileys = ""
#   while count <= num:
#     smileys += "\U0001f600"
#     count += 1
#   print(smileys)

# The Stop Copying Me App

# imitate = input("Hey, how are you? What are you up to? ")
# while imitate != "oh behave":
#   print(f"{imitate} - " )
#   imitate = input(f"{imitate}: ")
# print("Fine, I will, but this isn't over. ")

# Using break:

# while True:
#   command = input("Type ':q' to exit: ")
#   if (command == ":q"):
#     break

#   from random import randint  # use randint(a, b) to generate a random number between a and b

# # Challenge solution: 

# number = 0 # store random number in here, each time through
# i = 0  # i should be incremented by one each iteration

# number = randint(1,10)

# while number != 5:
#     number = randint(1,10)
#     i += 1

  # Define my_stuff 
# my_stuff = ["A phone", "a laptop", 3.5, True, False, "a second laptop", "a chair", "a desk"]

# Define nums - two ways of getting numbers from 1-99 
# The functional approach
# def nums():
#   for nums in range(1,100):
#     print(nums)
# nums()

# getting a range of numbers into a list. (1-99)
# i = 0
# nums = list(range(1,42))
# while i < len(nums):
#   print(nums[i])
#   i+= 1


# # List
# ducks = ["Donald", "Daisy", "Riri", "Zaza"]

# #Iterate over the list
# # For
# for duck in ducks:
#   print(f"{duck} Duck")

# # While
# i = 0
# while i < len(ducks):
#   print(f"While loop item {i + 1}: {ducks[i]} Duck")
#   i += 1

# #######################
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # Define your code below:
# # Tried with a while loop
# # The While Loop did not play nicely. 
# # i = 0
# # result = ""
# # results = []
# # while i < len(sounds):
# #   print(sounds[i])
# #   # results.append(sounds[i])
# #   sounds[i] = (result)
# #   print(result)
# #   result += results
# #   print(results)
# #   i += 1
# # print(results)

# results = ''.join(sounds)
# print(results.upper())
# # With a for Loop

# result = ''
# for segment in sounds:
#   result += segment.upper()
# print(result)

# #######################

# # Compare append to extend
# nums = [1,2,3]

# nums.append([4,5])
# print(nums)

# # And now if we extend instead
# nums2 = [6,7,8]
# print(nums2)
# nums2.extend([9,10,11])
# print(f"Now everything is in the same list: {nums2}") 

# # Insert allows something to inserted precisely

# phrase = ["The", "duck", "across", "lake"]

# phrase.insert(1, "quick")
# print(phrase)
# phrase.insert(-1, "reflective")
# phrase.insert(-2, "the")
# phrase.insert(3, "skates")
# print(phrase)

# barcode = [4,0,2,1,4,8,0,1,2,3]

# barcode.sort() # this changes the original set so be careful. 

# print(barcode)

#     # Create a list called instructors
#     instructors = []
     
#     # Add the following strings to the instructors list 
#         # "Colt"
#         # "Blue"
#         # "Lisa"
#     instructors.extend(["Colt", "Blue", "Lisa"])
     
#     # Remove the last value in the list
#     instructors.pop()
     
#     # Remove the first value in the list
#     instructors.pop(0)
     
#     # Add the string "Done" to the beginning of the list
#     instructors.insert(0, 'Done')
################################

# Slices revision

# barcode = [4,0,2,1,4,8,0,1,2,3]

# print(barcode[2:]) # From position 2 onwards
# print(barcode[-2:]) # From the end, the last two numbers

# # Although the examples are with numbers this also works with sets of words. 

# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# weekend = weekdays[-2:]
# print(weekend)
# work_week = weekdays[0:5]
# print(work_week)
# copy_weekdays = weekdays[:]

# print(f"{copy_weekdays is weekdays}: because although the data is the same they are stored in different bits of memory. ")
# print(f"Both contain the same data: {copy_weekdays == weekdays}")

# # New idea: List comprehension

# nums = [1,2,3]

# print([x * 10 for x in nums])

# print([d / 3 for d in nums])

# print([str(c) + " " +  "chf" for c in nums]) # Useful for currency, for payments

# emotion = 'fascinated'

# print([letter.upper() for letter in emotion])

############################################
# List Comprehension practice

# acronym = [word[0] for word in ["Electronic", "Dance", "Music"]]
# print(acronym)

# icao = [letter[0] for letter in ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]]
# cheeky = [letter[0] for letter in ["Tango", "Whiskey", "India", "Tango"]]

# print(icao)
# print(cheeky)

# even = [num for num in [6,1,2,1,8,5,1] if num % 2 == 0]
# odd = [num for num in [6,1,2,1,8,5,1] if num % 2 != 0]
# print(even)
# print(odd)


# practice = [val for val in [3,6,9] if val in [9,1,3,2,8]]
# print(practice)
# practice2 = [val for val in [0,7,9] if val in [7,9,3]]
# print(practice2)

# reverse = [val[::-1].lower() for val in ['retteb', 'no', 'a', 'lemac']] # 
# da_vinci_writing = [val[::-1].lower() for val in ['peek', 'gniyduts', 'yreve', 'yad']]
# print(da_vinci_writing)
# print(reverse)

# It works for 12 but doesn't itterate beyond this number
# for number in range(1,100):
#   if number / 12 == True:
#     print(number)
#   elif number / 12 == False:
#     number + 1
# multiplication_table_1 = [val for val in range(1,11) if val % 1 == 0]
# multiplication_table_2 = [val for val in range(1,21) if val % 2 == 0]
# multiplication_table_3 = [val for val in range(1,31) if val % 3 == 0]
# multiplication_table_4 = [val for val in range(1,41) if val % 4 == 0]
# multiplication_table_5 = [val for val in range(1,51) if val % 5 == 0]
# multiplication_table_6 = [val for val in range(1,61) if val % 6 == 0]
# multiplication_table_7 = [val for val in range(1,71) if val % 7 == 0]
# multiplication_table_8 = [val for val in range(1,81) if val % 8 == 0]
# multiplication_table_9 = [val for val in range(1,91) if val % 9 == 0]
# multiplication_table_10 = [val for val in range(1,101) if val % 10 == 0]
# multiplication_table_11 = [val for val in range(1, 122) if val % 11 == 0]
# multiplication_table_12 = [val for val in range(1, 145) if val % 12 == 0]

# print(multiplication_table_1)
# print(multiplication_table_2)
# print(multiplication_table_3)
# print(multiplication_table_4)
# print(multiplication_table_5)
# print(multiplication_table_6)
# print(multiplication_table_7)
# print(multiplication_table_8)
# print(multiplication_table_9)
# print(multiplication_table_10)
# print(multiplication_table_11)
# print(multiplication_table_12)

# play_with_boolean = [bool(val) for val in [1, True, '', "", 0]]

# print(play_with_boolean)

# voweled = "The Quick brown fox jumped over the lazy sheep dog"
# original_phrase = "The happy goat jumped acrosss the high alpine pass before spending some time watching cyclists as they headed up the hill"
# devoweled = ''.join(char for char in voweled if char not in "aeiou")
# devoweled_list_comprehension = [char for char in voweled if char not in "aeiou"]
# devoweled_2 = ''.join(char for char in original_phrase if char not in "aeiou")
# devoweled_2_list_comprehension = [char for char in original_phrase if char not in "aeiou"]
# devcon = ''.join(char for char in original_phrase if char in "aeiou")
# devcon_list_comprehension = [char for char in original_phrase if char in "aeiou"]
# print(devoweled)
# print(devoweled_list_comprehension)
# print(devoweled_2)
# print(devoweled_2_list_comprehension)
# print(devcon)
# print(devcon_list_comprehension)

# # answer = ''.join(char for char in 'amazing' if char not in "aeiou") # Incorrect

# answer = [char for char in "amazing" if char not in "aeiou"]

# print(answer)

# nested_list = [["list one", "part two", "part three"], ["list two", "another part", "part six"], ["list three", "random stuffn", "more random stuff"]]

# print(nested_list)
# print(nested_list[1][2])
# print(nested_list[2][2])

# nested_number_list = [[1,2,3],[4,5,6],[7,8,9]]

# for l in nested_number_list:
#   for val in l:
#     print(val) # prints each number on a seperate line. 

# # For mapping

# coords = [[12.23, 6.12], [12.24, 6.15], [12.26, 6.17]]

# for loc in coords:
#   for coord in loc:
#     print(coord)

# #tic tac toe logic
# #Draw the board
# board = [[num for num in range(1,4)] for val in range(1,4)]

# print(f"tic tac toe logic: {board}")

# #Draw the player moves
# tct_output = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]

# print(f"Hypothetical Tic Tac Toe output: {tct_output}")

# line_of_crosses = ["*" for i in range(1,4)]
# line_of_naughts = ["0" for i in range(4,7)]
# line_of_empties = [" " for i in range(7,10)]
# print(line_of_crosses)
# print(line_of_naughts)
# print(line_of_empties)
# three_count = [[(i * 15) for i in range(1,4)] for num in range(1,4)]
# print(three_count)
# tap_tap_tap = [["t", "a", "p"] for i in range(1,4)]
# print(tap_tap_tap)
# ten_times_ten = [[num for num in range(0,10)] for i in range(0,10)]
# print(ten_times_ten)

############################################################
#Playing with dictionaries

from calendar import weekday

week_day = {"name": "Saturday", "weekend": True, "weather": "sunny", "pandemic": True, "sick": False }
another_week_day = dict(name="Sunday", duration=24, day=7, weekend=True, weather="sunny")
print(week_day)
print(another_week_day)
print(week_day["pandemic"])
print(week_day["name"])
print(week_day.values())
print(week_day.keys())

for k in week_day.keys():
  print(f"The key is: {k}")
for v in week_day.values():
  print(f"The value is: {v}")
print("And now for both at once: ")
print(f"Tuples: {week_day.items()}")
print(f"Tuples: {another_week_day.items()}")

# An other option is to use:

for k, v in another_week_day.items():
  print(f"Key: {k}\n value: {v}") 

# This code is a reminder
##################################
# for value in donations.values():
#   total_donations += value
# print(total_donations)
##################################

# Using "in"
print(f"Duration is in another_weekday: {'duration' in another_week_day}")

# We have clear, copy, fromkeys

copy_me = dict(c=1, o=2, m=3, e=4, d=5, i=6, a=7, n=8)

copycat = copy_me.copy()

print(f"Copy_me and Copycat are cloned: {copycat == copy_me}")
print(f"Copy_me and Copycat are the same: {copycat is copy_me}")

new_bike = {}.fromkeys(['name', 'ype of bike', 'tire width', 'size'])
print(week_day)
new_copy = week_day.fromkeys(['name', 'ype of bike', 'tire width', 'size'])
print(new_bike)
print(new_copy)

print(week_day.fromkeys(range(1,10), 'unknown')) # {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown'}

