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

# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
elif choice == 3:
    print("Three, not free")
elif choice == 4:
    print("Four, not for")
elif choice == 8:
    print("not as lucky")
elif choice == 9:
    print("Nine, not nein")
elif choice != 7:
    print("unlucky")

  
city = input("What city do you live in? ")

if city == "Nyon" or city == "Lausanne" or city == "Geneva":
    print("You live within cycling distance.")
else:
  print("That's not within easy cycling distance. ")
  
print("How old are you?: ")
age = int(input("> "))

if age < 9:
  print(f"At age {age} You are too young to scuba dive. You can snorkel instead")
elif age >= 9 and age <= 16:
  print(f"At {age} You can scuba dive, but you need permission from a parent.")
elif age >= 16 and age <= 65:
    print(f"You can scuba dive freely at {age}, but you need a medical certificate.")
else: 
    print(f"Snorkeling is always an option at any {age}. Just hope the water is warm enough.")

print(f"Does {age} require someone to work, or go to school, or be retired")


if not ((age >= 0 and age <= 17) or (age > 65 and age < 140)):
  print(f"At {age} you are stuck either at work, or at school")
else: 
  print("You are too young, or you are already retired, and can do whatever you want.")

speed = input("How fast are you going? ")
if speed != "":
  if int(speed) >= 100 and int(speed) <= 120:
    print(f"Welcome onto the motorway. You are travelling at {speed}")
  elif int(speed) >= 120:
    print(f"Slow down, you are {str(int(speed) -120)} above the speed limit")
  else: 
    print(f"You must be at 100 KM/h or more kilometres per hour to join the motorway. You are at {speed}km/h. Speed up")