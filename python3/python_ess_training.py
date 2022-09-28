# import sys
# from termcolor import colored, cprint
#
# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')
#
# print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')
#
# print_green_on_cyan("The Very Quick Brown Fox")
#
#
# for i in range(21):
#     cprint(i, 'blue', end=' ')
#
# cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
# cprint("Warning!", 'yellow', attrs=['bold'], file=sys.stderr)
#
# # see: https://pypi.org/project/termcolor/
#
# def multiplication(v1, v2):
#   return v1 * v2
#
# print(print(multiplication(12,6)))
#
# class Smog:
#   def __init__(self, name):
#     self.name = name
#     self.weather = 'True'
#     self.pollution = "combustion sources"
#
#   def cough(self):
#     print("Cough Cough" + " " + self.name + ", behave. ")
#
#   def eyes(self):
#     print('My eyes are stinging')
#
# my_smog = Smog("Flora")
# not_good = Smog("Not Good, at all")
#
# print("The Smog function")
# my_smog.eyes()
# my_smog.cough()
# not_good.cough()
# not_good.eyes()

from datetime import datetime

seconds = datetime.now().second
minutes = datetime.now().minute
hours = datetime.now().hour

print(f"It is now {hours}:{minutes}:{seconds}")

if 10 <= hours <= 12:
    print("Time to study")
elif hours < 12:
    print("Good Morning")
elif 15 <= hours <= 18:
    print("Time to do some sports")
elif 22 <= hours <= 23:
    print("Sweet dreams")
else:
    print("Good afternoon")

# I tried using the seconds var but this gave an infinite loop.
# You need to use the live result for this to work
wait_until = datetime.now().second + 2
# while datetime.now().second != wait_until:
# #    print(f'launch imminent')
#     pass
# print(f'Rocket ignition and liftoff ')

while True:
    if datetime.now().second < wait_until:
        continue
    break

print(f'MECO at {wait_until} seconds')

# revision

for number in range(2, 100):
    for factor in range(2, int(number ** 0.5)):
        if number % factor == 0:
            break
        else:
            print(f'{number} is prime')


# Named parameters example

def perform_operations(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2


sum_example = perform_operations(4, 3, 'sum')
multiply_example = perform_operations(3, 4, 'multiply')
print(sum_example)
print(multiply_example)


# *args revisited

# def revision(args):
#     print(args)
#
# print(revision(1,2,3)) # We will get an error message

# Use *args to pass several arguments
def revised_args(*args):
    print(f'We can pass {args} now.')


revised_args(2, 7, 3, 6, 8, 8, 1, 1, 0)


class Rollerblade:
    def __init__(self, name):
        self.name = name
        self.slope = 'False'
        self.comfort = "still learning"

    def grass_stop(self):
        print("Perfect stopping grass")

    def fell_over(self):
        print("I fell so fast I helicoptered")


fun_roller = Rollerblade("Richard")

fun_roller.grass_stop()
fun_roller.fell_over()

class Hike:
    def __init__(self, name, gain, effort):
        self.name = name
        self.gain = gain
        self.effort = effort

    def easy_pease(self):
        print(f"{self.name} is not easy peasy. Very comfortable")

    def quite_exhausting(self):
        print("That was quite exhausting. I'm impatient to have a drink later")


day_36 = Hike("Leukerbad", 1000, "strenuous")


day_36.quite_exhausting()
day_36.easy_pease()

