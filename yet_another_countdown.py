# Recursion and a countdown
# Code from Programming Foundations: Algorithms, on Linkedin Learning
# I might change some code to see if I understand the concepts. 

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)
        print("I am looped second")
        print("Third loop; loading new number...")

countdown(10)

def power(num, pwr):
    if pwr == 0:
        return 1
    else: 
        return num * power(num, pwr-1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{} to the power of {} is {}".format(3, 4, power(3, 4)))
print("{} to the power of {} is {}".format(10, 9, power(10, 9)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
print("{}! is {}".format(8, factorial(8)))

def efun(num):
    if num == 0:
        return 1
    else:
        return num * efun(num-2)

print(efun(8))
