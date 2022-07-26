# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from calendar import FRIDAY, weekday
from datetime import datetime
from sqlite3 import DateFromTicks
from unittest.util import _MAX_LENGTH


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print(1+2+3+4)
# print("Go for a bike ride")

# print (45*45)

# print (45 * 45 * 45)

# print (12 ** 12)

# print (5//2)
# print (10//3)

# print (10 % 2)
# print (12 % 4)

# print (33 % 2)

# print (700 % 200)

# print (10 % 7)
# no comment, or maybe there is. I am a comment.

# age = 48
# print(age)

# birthday = age + 1
# print (birthday)

#we can also reassign the variable
# age = age + 1
# print ("age + 1")
# print (age)

#constant

# PI = 3.14159

# week_day = "Friday"

# print (PI)

# print (week_day)

# site_visitors = 1942
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)
# site_visitors += 1
# print (site_visitors)

# print ("hello"[1])

# first_name = "Duck"
# last_name = "McDuck"

# print (first_name[0])
# print (last_name[0])

# alf = "I love to eat cats"

# print (alf[2:6])

# bianimal = "CatDog"

# print(bianimal[0:3])
# print(bianimal[3:6])

# number_sequence = "0,1,2,3,4,5,6,7,8,9,0"
# We don't need to specify the end if we want every number beyond the in point. 
# print (number_sequence[2:])
# print (number_sequence[2:20:3]) #with this notation we can say go from position two to 12 but take every third number
# print (number_sequence[2:20:2])

# word = "pineapples"

# print (word[:4])

# print('''hello''') #triple quote

# print("****** The quick Brown Password Guesser ******")

# guess_password = input("Can you guess the password? ")

# print("You guessed: " + guess_password + ". You were wrong!")

# question_one = input("What is your first name?")
# question_two = input("Are you watching the Tour De France?")

# combined_answers = question_one + ": "+ question_two
# print("blah blah, " + combined_answers)

# year = 365
# age = 18
# int_age = int(age)
# type(int(age))

# days_old = int_age * year

# print(days_old)

# age_in_years = input("How many years old are you? ")
# int_age_in_years = int(age_in_years)

# age_in_days = int_age_in_years * year
# f_phrase = f"You are {age_in_days} days old"
# print(f_phrase)

# print("You are at least " + str(age_in_days) + " days old. Congrats on being on this planet for so many revolutions.")

# eff = f"There are {24*60*60} seconds in a day"

# print(eff)

# The challenge

# Shopping Cart Exercise

#Write a Python script that does the following:

# - Prints out a “banner” to welcome users to our shop
# print("*" * 42)
# print("***** Welcome to the Harmonica Store *****")
# print("*" * 42)
# print("")

# - Asks the user for the name of the item they are buying
# item_name = input("Which item would you like to buy? ")

# - Asks the user for the price of that item
# item_price = input(f"Please specify the price of the {item_name}. ")

# - Asks the user for the quantity they are purchasing
# item_quantity = input(f"How many {item_name} would you like to purchase? ")

# - Prints out a message that includes their subtotal (quantity 𝚡 price)
# subtotal = float(item_price) * float(item_quantity)
# round(subtotal, 2)
# summary = "You have selected to buy " + str(item_quantity) + " " + item_name + " at " + str(item_price) + ". This will cost " + str(subtotal) + " CHF."
# print(summary)

# And as an f string
# eff = f"You have selected to buy {item_quantity} {item_name} at {item_price}. This will cost {subtotal} CHF."
# print(eff)

# speed = input("How fast are you going?")
# velocity = int(speed)

# if velocity <= 50: 
#     print("Perfect, you are driving safely")
# else:
#     print("SLOW DOWN")
#     print("I will not always run")
# print("I will always run")

# python is indentation based. 

# colour = "purple"

# if colour == "green":
#     print("Beginner")
# elif colour == "blue":
#     print("intermediate")
# elif colour == 'black':
#     print("For good skiers")
# else:
#     print(f"Pardon me, I haven't a clue. {colour} is unknown to me.")

# num = 6
# if num < 5:
#     print("from if")
# elif num == 3:
#     print("num = 3 elif")
# elif num < 10:
#     print("from elif 2")

# age = 4

# if age < 10:
#     print("The child price is 10€")
# elif age > 65:
#     print("The OAP cost is 12€")
# else: 
#     print("The adult price is 15€")

# The name challenge
# average english name is six characters long

# print("*" * 30)
# print("The Name Length Checker")
# name = input("What is your name? ")
# name_length = len(name)

# if name_length > 6:
#     print(f"You have a long name, by English standards, with {name_length} characters.")
# elif name_length < 6:
#     print(f"Your name is shorter than the English average name. It is {name_length}.")
# else:
#     print(f"Your name is the Englisha verage name length with {name_length} characters.")

# Option 1
###############
# import random

# test = random.randint(2,5)
# print(test)
# test = random.randint(1,10)
# print(test)
# test = random.randint(1,10)
# print(test)
# test = random.randint(1,10)
# print(test)
# test = random.randint(1,10)
# print(test)
# test = random.randint(1,10)
# print(test)

# from random import randint
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))
# print(randint(1,6))

# import random

# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))

###############

from random import randint

rand = randint(0,1)
if rand == 0:
    print("heads")
else:
    print("tails")

##############

message = input("Please write your message: You have a 240 character limit: ")

message_length = len(message)
message_max = 240

if message_length <= message_max:
    print(f"That message can be sent. It is {message_length} characters long. You have {message_max - message_length} characters spare. " )
elif message_length == message_max:
    print("Double Twoosh, congrats")
else:
    print(f"Your message is {message_length} characters long. The character maximum is {message_max}. You are {message_length-message_max} over the limit.")
