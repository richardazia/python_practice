# Use a hashtable to filter duplicates

items = ["raclette", "fondue", "tartiflette", "fondue", "raclette", "croute au fromage", "raclette", "cheese on toast", "macaroni and cheese", "ice cream", "cheese on toast", "tartiflette"]

# Create a hashtable to filter data
filter = dict()

for key in items:
    filter[key] = 0

# Create a set from the resulting keys in the hashtable

result = set(filter.keys())
print(result)

counter = dict()

for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)

# Find the Maximum value

items = [20,24,13,12,65,4,3,73,2,7,9,12,17,5,4,33,23,12]

def find_max(items):
    # Check to see if the list is at the final item
    if len(items) == 1:
        return items[0]
    
    op1 = items[0]
    op2 = find_max(items[1:]) #1: go from item 1 onwards

    if op1 > op2:
        return op1
    else:
        return op2

print(find_max(items))

def find_min(items):
    if len(items) == 1:
        return items[0]

    op1 = items[0]
    op2 = find_min(items[1:])

    if op1 < op2:
        return op1
    else:
        return op2

print(find_min(items))