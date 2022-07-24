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

