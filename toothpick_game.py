# Get player names

# Start with 13 toothpicks, work our way down to zero
toothpics = 13
# max number of toothpicks at a time = 3

player_1 = input("Please enter Player one name: ")
player_2 = input("Please enter Player two name: ")

print("*" * 30)
print("The toothpick game")
print("*" * 30)
print(" | " * toothpics)
print("You can remove one, two or three toothpicks at a time. The last person to remove a toothpick wins")

while True: 
    if toothpics != 0:
        removed = int(input(f"{player_1}, how many toothpicks would you like to remove?: "))
        toothpics = toothpics - removed            
        print(" | " * toothpics)
        print(f"There are {toothpics} remaining.")
    else:
        print("Someone has won the game")
        print("Game Over")
        break
