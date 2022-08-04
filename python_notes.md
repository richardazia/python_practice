# Python Notes

## escape characters
- newline \b
- single quote \'
- double Quote - \"
- Tab \t
- Backslash - \\

## Triple quotes
''' 
Hello
world
'''

## Input
Input prompts the user to enter data

## Casting types
age = 19
int(age)

## f strings
a way to generate strings that contain interpolated expressions

## methods
thing.method
they are part of objects
.upper
.lower
.capitalize

### Strip Method
str.strip([chars])
strip works like chomp in ruby

" hello     ".strip()  gives 'hello

"      hello \t\n    ".strip() 
'hello'

In [44]: "-----Goodbye------".strip("-")
Out[44]: 'Goodbye'

In [45]: "-|-|-|-|-|-|-|Hello-|-|-|-|-|-|-|-|-|-|".strip("-|")
Out[45]: 'Hello'

### Strip Replace
str.replace(old, new[, count])

In [52]: distance = "1kilometre 2kilometre, 3kilometre, 4kilometre, 5 kilometre"

In [53]: distance.replace('kilometre', 'kilomètre')
Out[53]: '1kilomètre 2kilomètre, 3kilomètre, 4kilomètre, 5 kilomètre'

In [54]: distance.replace('kilomètre', 'km')
Out[54]: '1kilometre 2kilometre, 3kilometre, 4kilometre, 5 kilometre'

In [56]: prices = '1.99€, 2.99€, 4.65€'

In [57]: prices.replace('€', '£')
Out[57]: '1.99£, 2.99£, 4.65£'

In [62]: email = 'genius@example.com      '

In [63]: email
Out[63]: 'genius@example.com      '

In [64]: email.strip()
Out[64]: 'genius@example.com'

In [74]: email = 'GeNius@ExAmple.Com      '

In [75]: email.strip().lower()
Out[75]: 'genius@example.com'

### Playing with the in operator

- works with letters
- case sensitive

In [21]: "A" in "abba"
Out[21]: False

In [22]: "a" in "abba"
Out[22]: True

In [23]: "i" in "supercalifragiexpialidocious"
Out[23]: True

### String comparisons.

In [24]: 'a' < 'w'
Out[24]: True

In [25]: 'a' > 'w'
Out[25]: False

In [26]: ord('a)
  Input In [26]
    ord('a)
           ^
SyntaxError: EOL while scanning string literal


In [27]: ord('a')
Out[27]: 97

In [28]: ord('1')
Out[28]: 49

#### ord numbers
https://docs.python.org/3/library/functions.html#ord

### elif
elif is like - else if in other languages but it short circuits as soon as one condition is true

### Nested conditionals
- Conditions can be nested
- if condition a is true, look at condition b, if be is true look at c...
- if a is false then nothing runs

### Rounding floats
bmi = round(bmi, 2) where bmi is the float and 2 is the number of decimal places.


### isnumeric
- return true if the string is a numeric string, false if not
- a string is numeric if all characters in the string are numbers

## Break
works in a similar way to JS and other languages

## Continue
skips a letter, character or item 

## Nested loops
If we run an outer loop with an innter loop then the outer loop will go through one loop, and the inner loop will go through all items, and then it will jump to item 2 of the inner loop, and then all items of the inner looop. 

## Functions
- use def to define them They have a name, and then the action that they're meant to carry out. 

## return
- return returns what it is expected to return but after this the function stops. 
- code after a return will not run. 

## Defaut Parameters
- We can add defaults to parameters. 

def bounce(frequency=18):
    print("boing! " * frequency)

if we write bounce(252) then the frequency will be 252. Boing will be printed 252 times. If we leave "boing()", blank, then it will default to 18 boings. 

## Parameter Order
- When writing parameters the default must be second, not first. 
- def aeration(method, action="slam"):

# Scope in Python
- lexical or local - available only within a function.
- enclosing 
- global - available everywhere
- built-in