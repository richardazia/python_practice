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

### String methods - split and join
- split is used to split a string where required

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
- enclosing - nested 'inner' functions have access to variables declared in outer parents
- global - available everywhere - use word global
- built-in - str and other built-in functionality that are accessible by default. 

# Lists
- ordered collections of values. 

## List index
- lists are 0 indexed so that we can work with individual items.

## List Append and extend
- Append adds elements to a list in their entirety
- extend adds elements item by item. 

## List insert
- We can insert an item in a specific position
- use insert(index, item to be inserted)
- it shifts items, rather than replaces them - languages.insert(4, 'PHP')

## List Slice

list[from:to:increment]

## List item deletion
- .clear clears all items
- .remove removes the first item in a list
- .pop removes the final element in a list and makes it available. It can be used to delete slices. 

# Nested lists
- you can access items using the name of the list followed by the coordinates of the data you want, down to the character if desired. 

# Logical Operators
- They allow you to add data from one list to a second. For example:
- It works with strings and integers etc. 
[1,2,3]+[4,5,6]
- when using 'in' it checks for the entire string, not specific characters or words. 

# Sort, count and reverse
- We can sort elements in the order we want
- We can count how often a string or item occurs. 
- we can reverse the order of the data. 
- capital letters are sorted before small letters

# ID
- each object has a unique id. 

# == and is
- == compares the content of two lists
- 'is' compares the id of two lists

# Deep copies
- deep copies allow us to make an independent item from a previous item. It will duplicate all the content. It can then be modified without affecting the original. 

# Dictionaries
- {} tells python that this will be a dictionary. 
- type({}) >> dict
- dict() = {} like list() = []
- uses key value pairs
- key: value
- dict.get() keyword
- pop, popitem, clear and del. Remember prices.popitem() has to be called to do something. 
- We can use .keys(), .values() or .items()
- dict_keys and dict_values are iterable
- update allows you to import dictionary A into dictionary B. 
- ** allows you to combine dictionary 1 with dictionary 2
- The Union command, to combine two dictionaries. Uses the | symbol. 
- Union can combine two or more dictionaries at a time. 

# Tuples
- simple list
- immutable - equivalent to constant
- Ordered lists
- fewer methods available
* bike_parts = ("chain", "gear shifter", "tyres")
- When you have a single tuple you need to write it as 
* tuple_name = "tuple with one item" or ("tuple with one item", )

- efficient, immutable
- If you use tuples as keys in a Digital Asset management tool then you can keep keys secure. 

# Sets
- unordered collections
- no duplicates
- only immutable elements
- add and delete
- iterable
- see whether an element is within a set or not
* use set() to create an empty set, not {}
* difference = '-'
* union = '|'
* intersection = '&'
* *args collects all arguments provided. (although args could be num, flamingos or anything else that is relevant to the context of the function)
* order is important when using params, *args, def params and **kwargs. 
* For kwargs remember to use a key and value every time. 
- We unpack by using a * sum(*numbers). If we passed numbers in sum directly we would get an unsupported operand type for += 'int' and 'list'

# Exceptions and errors
* https://docs.python.org/3/library/exceptions.html for up to date exceptions
- If we want to get our own error messages we use the keyword "raise". We can raise the defaults and provide our own error message.
## Try and except
- When we use except we can either use except by itself or we can specify what the error was, for example "except EOFError" or other. 

### Look Before you Leap - LBYL
- if this, then that, else do something else. 
- Use a conditional to see if something is true, before continuing. 
### Easier to Ask for Forgiveness than Permission (EAFP)
- Assume things will work, and see exceptions if and when they occur. 
- Python way of doing things

## Modules
-flexible functionality via small files for specific tasks
* Built in
* Custom
* 3rd party
- we can "import as" - import random as rand
* import calendar as cal 
* from random import randint - This will import just that function, nothing else. 
* from math import pi
* with comma we can write from math import randint, pi, e etc. 

## PIP
- to check pip version: python3 -m pip --version
- to look for packages
- to install packages python3 -m pip install <package>
* Playing with text to speech - Download the corpora lite package for the second part







