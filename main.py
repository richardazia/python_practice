# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from calendar import FRIDAY, weekday
from datetime import datetime
from sqlite3 import DateFromTicks


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print(1+2+3+4)
print("Go for a bike ride")

print (45*45)

print (45 * 45 * 45)

print (12 ** 12)

print (5//2)
print (10//3)

print (10 % 2)
print (12 % 4)

print (33 % 2)

print (700 % 200)

print (10 % 7)
# no comment, or maybe there is. I am a comment.

age = 48
print(age)

birthday = age + 1
print (birthday)

#we can also reassign the variable
age = age + 1
print ("age + 1")
print (age)

#constant

PI = 3.14159

week_day = "Friday"

print (PI)

print (week_day)

site_visitors = 1942
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)
site_visitors += 1
print (site_visitors)

print ("hello"[1])

first_name = "Duck"
last_name = "McDuck"

print (first_name[0])
print (last_name[0])

alf = "I love to eat cats"

print (alf[2:6])

bianimal = "CatDog"

print(bianimal[0:3])
print(bianimal[3:6])

number_sequence = "0,1,2,3,4,5,6,7,8,9,0"
# We don't need to specify the end if we want every number beyond the in point. 
print (number_sequence[2:])
print (number_sequence[2:20:3]) #with this notation we can say go from position two to 12 but take every third number
print (number_sequence[2:20:2])

word = "pineapples"

print (word[:4])