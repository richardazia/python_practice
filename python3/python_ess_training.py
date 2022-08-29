import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')

print_green_on_cyan("The Very Quick Brown Fox")


for i in range(21):
    cprint(i, 'blue', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
cprint("Warning!", 'yellow', attrs=['bold'], file=sys.stderr)

# see: https://pypi.org/project/termcolor/

def multiplication(v1, v2):
  return v1 * v2

print(print(multiplication(12,6)))

class Smog:
  def __init__(self, name):
    self.name = name
    self.weather = 'True'
    self.pollution = "combustion sources"

  def cough(self):
    print("Cough Cough" + " " + self.name + ", behave. ")

  def eyes(self):
    print('My eyes are stinging')

my_smog = Smog("Flora")
not_good = Smog("Not Good, at all")

print("The Smog function")
my_smog.eyes()
my_smog.cough()
not_good.cough()
not_good.eyes()



