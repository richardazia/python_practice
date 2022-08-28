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