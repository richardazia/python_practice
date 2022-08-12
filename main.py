
# Based on One Week Python by Colt Steele on Udemy

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

# we can also reassign the variable
# age = age + 1
# print ("age + 1")
# print (age)

# constant

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

# Write a Python script that does the following:

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

# from random import randint
#
# rand = randint(0,1)
# if rand == 0:
#     print("heads")
# else:
#     print("tails")

##############

# message = input("Please write your message: You have a 240 character limit: ")
#
# message_length = len(message)
# message_max = 240
#
# if message_length <= message_max:
#     print(f"That message can be sent. It is {message_length} characters long. You have {message_max - message_length} characters spare. " )
# elif message_length == message_max:
#     print("Double Twoosh, congrats")
# else:
#     print(f"Your message is {message_length} characters long. The character maximum is {message_max}. You are {message_length-message_max} over the limit.")

# noise = "annoyed"

# if noise == "noisy":
#     print("Please be quiet")
#     print(":-(" * 10)
#     elif noise == "quiet":
#         print("Excellent")
#         else

# mood = 'duck'
#
# if mood == 'content':
#     print("Excellent, perfect")
#     print(":-)" * 10)
# elif mood == 'not happy':
#     print("Mince alors")
# elif mood == 'annoyed':
#     print("I hope the issue is quickly resolved")
# elif mood == 'hypothermic':
#     print("Eat good food and wear appropriate clothing")
# else:
#     print("I have not learned of this expression yet")
#
# unit = input("What unit are you using? ")
# temp = int(input("What is the temperature of the water? "))
#
# if unit == 'f':
#     if temp >= 212:
#         print('water is boiling')
#     else:
#         print('Water is about to boil')
# elif unit == 'c':
#     if temp >= 100:
#         print('water is boiling')
#     else:
#         print('Water is about to boil')
# elif unit == 'k':
#     if temp >= 373:
#         print('water is boiling')
#     else:
#         print('Water is about to boil')
# else:
#     print("Input error, unit unknown")


# I would like to add a catch error for units and temperature

# weight = float(input("Please enter weight in kg: "))
# height = float(input("Please enter height in m: "))

# bmi = round(weight/(height*height))

# if bmi < 16:
#     print("Severely Underweight")
# elif 16 < bmi < 18.4:
#     print(f"With a bmi of {bmi} you are underweight. Join me for breakfast.")
# elif 18.5 < bmi < 24.9:
#     print(f"With a bmi of {bmi} you are normal. Congrats.")
# elif 25.0 < bmi < 29.9:
#     print(f"With a bmi of {bmi} you are overweight. Join me for a bike ride.")
# elif 30.0 < bmi < 34.9:
#     print(f"With a bmi of {bmi} you are morbidly obese. You may need to change lifestyle.")
# elif 35.0 < bmi < 39.9:
#     print(f"With a bmi of {bmi} you are severely obese.")
# elif bmi > 39.9:
#     print(f"With a bmi of {bmi} you are morbidly obese.")

# refactored
# if bmi < 16:
#     category = "Severely Underweight"
# elif 16 < bmi < 18.4:
#     category = "underweight. Join me for breakfast."
# elif 18.5 < bmi < 24.9:
#     category = "normal. Congrats."
# elif 25.0 < bmi < 29.9:
#     category = "overweight. Join me for a bike ride."
# elif 30.0 < bmi < 34.9:
#     category = "morbidly obese. You may need to change lifestyle."
# elif 35.0 < bmi < 39.9:
#     category = "severely obese."
# elif bmi > 39.9:
#     category = "morbidly obese."

# print(f"Your bmi of {bmi} makes you {category}")

# day = input("What day of the week is it? ")

# if day == 'saturday' or day == 'sunday':
#     print("Time to do some sports with other people. ")
# else:
#     print("Time to spend a few hours a day studying")

# age = int(input("How young are you? "))
# if age < 5 or age >= 65:
#     print("You get in for free")
# else: 
#     print("That will be 24 CHF.")
########
# year = input("What is your year of birth? ")

# if not year.isnumeric():
#     year = input("What is your year of birth? Please use a number: ")
# year = int(year)

# print(f"You were born in {2022-year} years ago")
######
# snack = input("Enter your favourite snack: ")
# # if snack != "":
# if snack:
#     print(f"I also like {snack} as a snack.")

# battery_percentage = 0
# if battery_percentage: 
#     print(f"{battery_percentage}% battery remaining")
# else:
#     print("Rechage the battery")

##############

# answer = input("Good morning ")

# while answer != "Good morning":
#     answer = input("Please say Good morning. ")

# print("Good Morning to you too, once again")
###############
# Pattern 1
# print("Welcome to the final countdown")
# num = 0
# while num <= 40:
#     print(f"We are current at {num}. Just a little more to go")
#     num += 1

##########

# count = 7
# while count > 0:
#     print("*" * count)
#     count -= 1

# count = 1
# while count < 8:
#     print("*" * count)
#     count += 1

##########

# word = "supercalifragiexpialidocious"
# for char in word:
#     print(char)

##########

# for num in range(-10, 10, 2):
#     print(num)

##########

# print("The 99 Bottles on the Wall song")

# for bottle in range(99, 0, -1):
#     print(f"{bottle} bottles of beer on the wall.\n{bottle} bottles of beer.\nTake one down, pass it around {bottle - 1} bottles of beer on the wall.")

# print("The While Loop version")

# total_bottles = 99
# while total_bottles > 0:
#     print(f"{total_bottles} bottles of beer on the wall.")
#     print(f"{total_bottles} bottles of beer.")
#     if total_bottles == 1:
#         print(f"Take one down, pass it around, no more bottles of beer on the wall.")
#     else:
#         print(f"take one down, pass it around, {total_bottles - 1} bottles of beer on the wall.")
#     print("*" * 40)
#     total_bottles -= 1

# for char in "bacon":
#     if char == "c":
#         break
#     print(char)
#################
# print("program exit code 0")

# for char in "struddel":
#     if char == "e":
#         break
#     print(char)
# print("Lunch is ready")

# message = input("Say Ecki Ecki eck ")
# while True: 
#     if message == "Ecki Ecki eck":
#         break
#     message = input("say that phrase: ")

# print("That phrase is nonsense isn't it? :-)")

# for char in "catnip":
#     if char == "i":
#         continue
#     print(char)
# print("Loop completed")

# for letter in "supercalifragilistiexpialidocious":
#     if letter in "aeiou":
#         continue
#     print(letter)
######
####################
# import datetime

# e = datetime.datetime.now()

# print ("Today is the %sth of %s %s" % (e.day, e.month, e.year))

# print ("Current date and time = %s" % e)

# print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

# print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))

# print(f"Today is the %a, %d, ")
####################

# def pandemic():
#     print("Rumours that the pandemic is over have been greatly exagerated " * 20)

# pandemic()

# def laugh(intensity):
#     print("Ha! " * intensity)

# laugh(12)
# laugh(6)
# laugh(8)

######################

# word = "chicken"

# print(word)
# print(word.replace("ck", "ldr"))

# def multiply(a,b):
    # print(a*b)

# def multiply(a,b):
#     return(a*b)

# multiply(12,56.12)
# multiply(15,15)
# multiply(12,12)

# def divide(a, b):
#     if a == 0 or b == 0:
#         return "Cannot divide by zero!"
#     return a/b

# divide(12,0)
# divide(0,12)
# divide(12,12)

# def is_even(number):
#     if number % 2 == 0:
#         return True    
#     return False

# def is_even(number):
#     return number % 2 == 0

######################

# print("*" * 20)
# print("For all your Slug needs, Slugify")
# print("*" * 20)

# def slugify(phrase):
#     return phrase.strip().lower().replace(" ", "-")
# vowel_count = int(0)
# print("The Vowel counter")
# def vowel_counter(count_vowels):
#     vowel_count = int(0)
#     for char in count_vowels:
#         if char in "aeiou":
#             vowel_count += 1
#     return(vowel_count)

# print(vowel_counter("The quick brown fox"))

# # Course solution

# def count_vowels(word):
#     count = 0
#     for char in word:
#         if char in "aeiou":
#             count += 1
#     return count

# print(count_vowels("The quick brown fox"))

# msg = "       Please reboot your computer now!.."

# msg.strip()

# msg.strip(".")

# msg.strip().strip(".")

# # We can chain them another way. 

# print(msg.strip(". "))

# def bounce(frequency=18):
#     print("boing! " * frequency)

# print("Three times\n\n")
# bounce(3)
# print("default\n\n")
# bounce()
# print("print boing 252 times\n\n")
# bounce(252)

# #Slugify Revisited

# def slugify(post_title, seperator="-"):
#     return post_title.lower().strip().replace(" ", seperator)

# print(slugify("The happy Goose Jumped over the harmonica playing chicken", "_"))

# def aeration(method, action="slam"):
#     print(f"Please {action} the {method}.")

# aeration("open", "window")
# aeration("wear", "mask")
# aeration("close", "door")
# aeration("window")

# def calc_total(price, qty=1, tax=0.05, discount=0):
#     subtotal = price * qty * (1-discount)
#     print(subtotal * (1 + tax))

# calc_total(25)

# calc_total(43, 2, 0.25, 0.05)

# # Being specific - we can pass the data in as: 

# calc_total(price=23.68, qty=17, tax=0.30)

# Local Scope

# def bike():
#     wheels = "Continental GP2 4000"
#     spec = 700
#     print(f"Inside the function: {wheels} with spec: {spec}")
# bike()

# Outside of local scope
# print(f"outside the function: {wheels} with spec: {spec}")

# for char in "duck":
#     colour = "green"
#     print(char)

# print("After the loop", colour)

# if True:
#     mammal = "cat"

# print("After conditional", mammal)
# print(f"Char is currently set to {char}")

# def outer():
#     fish = "cuttlefish"
#     def inner():
#         print("Inner:", fish)
#         def inner_inner():
#             print("Inside the inner inner:", fish)
#             def in_the_middle():
#                 print("And now even deeper: ", fish)
#             in_the_middle()
#         inner_inner()
#     inner()

# outer()

####################
# Priority of scope

# fish = "sea urchin"

# def outer():
#     fish = "swordfish"
#     print(fish)
# outer()

####################
# Global scope
# Despite being declared within the function it is made available globally. 

# def outer():
#     global animal
#     animal = "wolf"
# outer()

# print(animal)

# psi = 92

# def burst_tyre():
#     global psi # we make psi global so that we can modify it within the function. 
#     psi = psi * 2

# burst_tyre()
# print(psi)

###############
# Experimenting with lists

# distractions = ['recycling', 'hoovering', 'cooking', 'laundry', 'dinner', 'lunch']

# hello = ['h', 'e', 'l', 'l', 'o']

# range = list(range(2,24, 2)) #range works like in Ruby, if we add a third number it increments by that number
# print(range)

# languages = ['Ruby', 'JavaScript', 'Cobol', 'Pascal', 'QBasic']

# print(languages[3])

# print(languages[1])

# print(languages[1], [2], [3]) # will pass item [1] but not the others. 
# print(languages)
# print(languages[-1])

# # languages[12] = "Rust" # will not be allowed. "IndexError: list assignment index out of range"

# languages.append(range)
# # languages.append[8] # Gives an errror message as it thinks it is asked to fetch, not put data. 
# languages.append('Fortran')

# print(languages)

# languages.extend("bacon")

# print(languages)

# web_dev = ['html', 'css', 'xhtml']

# languages.extend(web_dev)
# languages.append(web_dev)
# print(languages)

# print(len(languages))

# languages.insert(4, 'PHP')

# print(languages)

# print(languages[0:5])
# print(languages[0:5:3]) #Now we only get every third item
# print(languages[:5]) # From the start
# print(languages[5:]) # To the end
# print(languages[::3])

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# letters[3:5] = [9,8,7,6,5]

# print(letters)
# ###############

# harmonica = ['MarineBand', 'special20', 'silverstar']
# print(harmonica)
# harmonica.clear()

# print(harmonica)

# ip = [192, 168, 0, 1]

# ip.remove(1) # removes the first instance it finds. 

# print(ip)

# print(ip.pop())
# print(ip.pop())
# print(ip)
# print(ip.pop(0))
# print(ip)

# ip = [192, 168, 0, 1]

# del ip[0]

# print(ip)

# emails = ['me@example.com', 'notme@example.com', 'yetanotherone@example.com', 'thequickbrownfox@example.com', 'thelemming@example.com']
# i = 0
# for email in emails:
#     print(f"Email sent to {email}")

# print(emails)

# while i < len(emails):
#     # print(f"Email sent to {email}")
#     print("e-mail sent to: " + emails[i] + " We will notify you when a response is read receipt is recieved.")
#     i += 1
##############
# Nested lists

# inception = [1,2,3,4, ['nested', 'within']]

# print(inception[4])
# print(inception[4][0])
# print(inception[4][1])

# meetings = [
#     ['monday', 'morning'],
#     ['wednesday', 'afternoon'],
#     ['friday', 'evening'],
#     ['saturday', 'full day'],
#     ['sunday', 'morning']
# ]

# print(meetings)

# print(len(meetings))

# print(meetings[1][0])
# print(meetings[1][1][2])

# print(meetings[3])

# for meeting in meetings:
#     print(meeting)
#     for specific in meeting:
#         print(f"Room booked for {specific}. Please check e-mail for confirmation")
############################
#Playing with List Operators
# print([1,2,3]+[4,5,6])
# print(['the', 'strict', 'goose'] + ['told', 'us', 'off'])
# evens = [10,12,14,16,18,20]
# odds = [11,13,15,17,19]
# print(odds + evens)
# print(evens + odds)

# print([3,6,9] * 3)

# # print(odds * evens) # TypeError: can't multiply sequence by non-int of type 'list'

# print("rine" in "marineband")

# print(10 in evens)
# print(11 in evens)
# print(1 in odds and 1 in evens)
# print(1 in odds)
# print(1 in evens)
############################

# ice_cream = ['absinthe', 'pistache', 'mint', 'cassis', 'nutella', 'fried chicken']

# selection = input("What ice cream flavour do you desire?")

# while selection.lower() not in ice_cream:
#     selection = input(f"We don't have {selection}, please choose another: ")

# print(f"Fantastic, we have {selection} ice cream. We will bring it shortly. ")

# print("absinthe" in ice_cream)
# print("fried" in ice_cream)
################################
# from unicodedata import digit


# numbers = [3,4,3,4,4,3,2,1,0,4,3,2,7,9]

# print(numbers.count(2))
# print(numbers.count(4))
# print(numbers.count(1))
# print(numbers.count(7))

# print(numbers.reverse()) #returns None 
# print(numbers)

# icao = ['alpha', 'hotel', 'whiskey', 'tango', 'echo', 'golf', 'juliet', 'x-ray', 'bravo' ]
# chaos_number = [-23, -65, 3, 5, 87, 12, 66, 34, 24, 89, 65, 43, 42, 12, 1 ,0, 2, 76]
# print(icao.sort()) # returns None
# print("Sort")
# print(icao)
# icao.sort(reverse=True)
# print("Reverse")
# print(icao)
# chaos_number.sort()
# print(chaos_number)
# chaos_number.sort(reverse=True)
# print(chaos_number)

# ################################
# # Using id:
# bird = ['duck']

# print(id(bird))

# digits = [1,2,3,4]

# digits_2 = digits

# print(id(digits))
# print(id(digits_2))

# digits_2.append(5)
# print(digits)
# print(id(digits))

################################
# print("Using ==")
# print(['a', 'b', 'c'] ==  ['a', 'b', 'c'])
# print(['a', 'b', 'c'] ==  ['a', 'b', 'c', 1, 2, 3])

# print("Using 'is'")
# print(['a', 'b', 'c'] is  ['a', 'b', 'c'])
# print(['a', 'b', 'c'] is  ['a', 'b', 'c', 1, 2, 3])

# # Split

# date = "07/08/2022"
# print(date.split("/"))

# lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dignissim tortor nec ligula molestie, non lobortis risus luctus. In eu."

# print(lorem.split(" "))

# # Join

# letters = ["M", "A", "S", "H"]
# print("Before: ")
# print(letters)
# print("*".join(letters))
# print("After being joined")
# print(letters)
# print("/|\\".join(letters))

# print("!".join("The key is sticking when I type."))

# # Unpacking

# colour = [162, 220, 32]
# red, green, blue = colour
# print(red)
# print(green)
# print(blue)

# triathlon_results = ['Durussel Raymond', 'Buchner Benjamin', 'Di Naro Sadri', 'Ryan Angela', 'Dominique Pierre']
# # data source: https://www.datasport.com/live/monitor/?lang=EN&racenr=24505 at around 10:55, results are not final. 
# gold, silver, bronze, *competitors = triathlon_results
# print(gold)
# print(silver)
# print(bronze)
# print(*competitors)

# # For a shallow copy

# triathlon_results_2 = triathlon_results.copy()
# print(id(triathlon_results))
# print(id(triathlon_results_2))

# print(triathlon_results_2 is triathlon_results) #False

# print(triathlon_results == triathlon_results_2) ## True

# # Shallow copy option two = slice [:]
# print(triathlon_results_2)

# print(triathlon_results_2[0:3])
# print(id(triathlon_results_2[:]))

# # Deep copy
# import copy

# item = [3,2,3[497],1,2,3,2,1,[213]]
# item2 = copy.deepcopy(item)

# print(item2)
#############################
# Dictionary 

# harmonica = {"brand": "Hohner", "model": "MarineBand", "key": "Key of C"}
# harmonica['portability'] = True
# print(harmonica)
# print(harmonica['brand'])
# print(harmonica['model'])
#############################
# prices = {
#     "chicken": 18.60,
#     "beef": 10.80,
#     "small peppers": 0.03,
#     "mentos": 1.20,
#     "redbull": 3.60,
#     "noix de coco": 1.90
# }

# # scanned_item = input("Please scan item: ")
# # if scanned_item in prices:
# #     price = prices[scanned_item]
# #     print(f"{scanned_item}: {price} CHF")
# # else: 
# #     print(f"{scanned_item} is not currently available")

# scanned_item = input("Please scan item: ")
# price = prices.get(scanned_item)
# if price:
#     print(f"{scanned_item}: {price} CHF")
# else: 
#     print(f"{scanned_item} is not currently available")

# print(prices.pop("noix de coco"))

# print(prices)
# #############################

# prices.popitem() # clears the most recent item
# print(prices)

# prices["lemon"] = 0.70
# print(prices)
# print(prices.popitem())
# # prices.clear()
# del prices["beef"]
# print(prices)
# prices.clear()
# print(prices)

# total = 0
# longest_read = 0
# shortest_read = 100
# most_read = ''
# least_read = ''

# random_durations = {
#     "Anna": 43,
#     "Bob": 76,
#     "Samantha": 32,
#     "Picsou": 23,
#     "Yakari": 78,
#     "Charlie": 45,
#     "Tintin": 12,
#     "Falbala": 23
# }

# print(random_durations.values())
# print(random_durations.keys())

# If we want to turn these into lists we can use:

# keys = list(random_durations.keys())
# values = list(random_durations.values())

# print(keys)
# print(values)

# for name in random_durations.keys():
#     print(name)

# for duration in random_durations.values():
#     total += duration

# avg_reading_time = total/len(random_durations)

# print(f"The average reading time per day for everyone is around {avg_reading_time} minutes")

# for k, v in random_durations.items():
#     print(f"{k}: {v}")

# for name, duration in random_durations.items():
#     if duration > longest_read:
#         longest_read = duration
#         most_read = name

# print(f"The longest read is {longest_read} minutes by {most_read}. ")

# # for name, duration in random_durations.items():
# for name, duration in random_durations.items():
#     if duration < shortest_read and duration != 0:
#         shortest_read = duration
#         least_read = name

# print(f"The shortest read is {shortest_read} minutes by {least_read}. ")

# for name in random_durations:
#     print(name)

# icao = {'a' : 'alpha', 'b' : 'bravo', 'c' : 'charlie', 'd' : 'delta'}

# add_letters = {'e' : 'echo', 'f' : 'foxtrot', 'g' : 'golf', 'h' : 'hotel'}

# icao.update(add_letters)
# print(icao)

# dict1 = {'a' : 'awesome', 'b' : 'bodacious'}
# dict2 = {'s' : 'stupendous', 'f' : 'fantastic'}
# dict4 = {'g' : 'grandiose', 'e' : 'exciting'}
# dict3 = {**dict1, **dict2}
# print(dict3)
# dict5 = {**dict3, **dict4}
# print(dict5)

# union_dict = dict1 | dict2 

# print(union_dict)

# three_union_dicts = dict1 | dict2 | dict4
# print(three_union_dicts)

# nested_dictionary = {
#     "pizza": {
#         'price': 4.80,
#         'qty': 1,
#         'frozen': True,
#         'producer': 'local'
#     },
#     "beef jerky": {
#         'price': 3.80,
#         'qty': 25,
#         'frozen': False,
#         'producer': 'Argentina'
#     }
# }

# print(nested_dictionary["pizza"])
# print(nested_dictionary["beef jerky"]['producer'])

# nested_reading = {
#     "Richard": [10,15,20,5,12],
#     "Tree": [20,15,5,16,32]
# }

# cycling_group = [
#     {
#         "name": "bob",
#         "location": "Lausanne",
#         "experience": "some"
#     },
#     {
#         "name": "Tiffany",
#         "location": "Morges",
#         "experience": "weekly rides"
#     },
#     {
#         "name": "Kadare",
#         "location": "Aubonne",
#         "experience": "some more"
#     }
# ]

# print(cycling_group)

####################
#### Tuples

# bike_parts = ("chain", "gear shifter", "tyres", "gears", "bar tape", "brakes", "saddle", "cables", "spokes")
# print(type(bike_parts))
# print(f"A single item: {bike_parts[2]}")
# print(f"A slice: {bike_parts[1:4]}")
# print(bike_parts.index("chain"))
# print(bike_parts.count("chain"))
# print("breaks" in bike_parts)
# print("mud" in bike_parts)

# for part in bike_parts:
#     print(f"A bike has: {part}")

# random_numbers = (3,4,5,32,1,3,2,6,3,7,3,8,5,34,2,4,5,6)
# print(random_numbers.count(3))

# varied_tuple = (True, False, (1,2,3,4), "The" "quick", 1,2,3,4, [2,3], {"duck": "tales"})
# print(type(varied_tuple))

# empty_tuple = ()
# empty_tuple = tuple()

# tuple = ("truck", )

# another_tuple = ("quantum dentistry", )
# print(type(tuple))
# print(type(another_tuple))

# tuple_with_brackets = (1,2,3,4,[])
# print(tuple_with_brackets)
# tuple_with_brackets[4].append("A work around")
# print(tuple_with_brackets)
# tuple_with_brackets[4].append("This adds flexibility")
# print(tuple_with_brackets)

####################
#### Sets

multiples_of_three = {3, 6, 9, 12, 15, 18, 21}
multiples_of_three.add(24)
multiples_of_three.add(27)
multiples_of_three.add(5)
print(multiples_of_three)
multiples_of_three.remove(5)
print(len(multiples_of_three))

diverse_set = {"a", "b", "c", 3, 6, 9, True, False}
diverse_set.discard("duck")
diverse_set.clear()

print(type(multiples_of_three))
print(type(diverse_set))

print({1,2,3} is {1,2,3})
print({1,2,3} == {1,2,3})

print(multiples_of_three)
print(diverse_set)

hiking = {"shoes", "walking", "versatile", "hiking shoes", "hiking sticks", "whenever possible"}

walking = {"shoes", "walking", "versatile", "daily"}

print(walking & hiking) # intersection

print(walking | hiking) # union

print(walking - hiking) # difference

union_walking = walking.union(hiking)

print(union_walking)

a = {1,2,3}
b = {2,4,6}

mystery = a - b

print(mystery)

duck = {'d', 'u', 'c', 'k'}
print('d' in duck)

print('d' in ['d', 'u', 'c', 'k'])

canton = ['AG', 'VD', 'AI', 'GE', 'FR', 'GE', 'VD']

set(canton) # converts to a set

list(set(canton))

min(2,3,4,6,4,3,7,6,8,9,0)

max(2,3,4,6,4,3,7,6,8,9,0)

def play_with_args(*args):
    print(f"Output: you should see {len(args)} items listed below: ")
    print(args)

print(play_with_args(2,3,4,5,4,3,2,3,9,8,5,4,'b', 'a', 'c', True, False))
print(play_with_args('roesti', 'bacon', 'pepper'))

def sum(*nums):
    tot = 0
    for num in nums:
        tot += num
    return tot

def phrase_maker(primary, secondary, *superfluous):
    print(f"Your primary goal is to: {primary}")
    print(f"Your secondary goal is to: {secondary}")
    print(f"We are just random things: {superfluous}")

print(phrase_maker('study', 'scramble', 1,2,3,4, True, False, 'more words'))

def see_for_yourself(**kwargs):
    print(kwargs)

# print(see_for_yourself('"the", "running", "albatros", "flew", "over", "the", "island", 12, "times"'))
# TypeError: see_for_yourself() takes 0 positional arguments but 1 was given

see_for_yourself(bird = "duck", sport = "cycling", danger = "low")
see_for_yourself(colour = "green", youth = 6, circumference = 152)

def circumference(**kwargs):
    for k,v in kwargs.item():
        print(f"A {k} wheel has a {v} circumference.")

# circumference(iso = "25-622", metric = 700)

def car_wash(**kwargs):
    for k,v in kwargs.items():
        print(f"The {k} model car was washed {v} days ago.")

car_wash(type = "C3", time_elapsed = 720) 

def print_ages(**kwargs):
    for k,v in kwargs.items():
        print(f"The great {k} is {v} years young.")

print_ages(Nameless = 52)
print_ages(bob = 58, Sue = 12, Jaberwocky = 15, Marina = 32)

#Keep this order, required info, field with a default, args and kwargs. 

def character_info(name, current_status="thirsty", *args , **kwargs):
    print(f"The individual's name is {name}.")
    print(f"The person is currently {current_status}.")
    print(f"Today's drink of choice will be filled with {args}.")
    print(f"kwargs: {kwargs}")

character_info("Richard", "dehydrated", "electrolytes", weather = "on a sunny day")

def laughter(val, list=[]):
    list.append(val)
    list.append(val)
    return list

print(laughter("ha"))
print(laughter("hi"))
print(laughter("ho"))
print(laughter("he"))

# The default value is shared, getting longer and longer with each iteration. 
# ['ha', 'ha']
# ['ha', 'ha', 'hi', 'hi']
# ['ha', 'ha', 'hi', 'hi', 'ho', 'ho']
####################