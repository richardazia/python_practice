# Unordered list search
# Linear search

# Course code

items = [20,24,13,12,65,4,3,2,7,9,12,17,5,4,33,23,12]

def find_items(item, itemList):
    for i in range(0, len(items)):
        if item == itemList[i]:
            return i

    return None

print(find_items(17, items))
print(find_items(0, items))

# Refactored code to find an anmial/word

animals = ["Duck", "Goose", "Cheeta", "Lion", "Coyote", "wolf", "Blue whale", "elephant"]

def find_animals(animal, animalList):
    for i in range(0, len(animals)):
        if animal == animalList[i]:
            return animal
    return ("Animal not found")

print(find_animals("cat", animals))
print(find_animals("Duck", animals))

# Ordered list search / Binary search
ordered_items = [1, 5, 6, 7, 8, 9, 10, 12, 15, 28, 32]
def binarysearch(item, itemlist):
    listsize = len(itemlist) -1
    # start at both ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # Find the mid point
        midPt = (lowerIdx + upperIdx) // 2
        # If item is found return the index
        if itemlist[midPt] == item:
            return midPt
        # If item not found, find the next mid point. 
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt -1

    if lowerIdx > upperIdx:
        return None

print(binarysearch(7, ordered_items))
print(binarysearch(9, ordered_items))
print(binarysearch(42, ordered_items))

print(binarysearch(12, items))

items1 = [1,2,3,4,5,6,7,8,9,10]
items2 = [12,25,6,7,3,6,2,1,90,24]

# Normal approach
def is_sorted(itemlist):
    for i in range(0, len(itemlist) -1 ):
        if (itemlist[i] > itemlist[i+1]):
            return False
    return True

print(is_sorted(items1))
print(is_sorted(items2))

#Boolean approach

def is_sorted_all(itemlist):
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

print(is_sorted_all(items1))
print(is_sorted_all(items2))