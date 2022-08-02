# Get player names

# Start with 23 toothpicks, work our way down to zero
toothpics = 23
# max number of toothpicks at a time = 3

player_1 = input("Please enter Player one name: ")
player_2 = input("Please enter Player two name: ")
current_player = player_1

print("*" * 30)
print("The toothpick game")
print("*" * 30)
print("You can remove one, two or three toothpicks at a time. The last person to remove a toothpick wins")
print(" | " * toothpics)

# while True: 
#         removed = int(input(f"{current_player}, how many toothpicks would you like to remove?: "))
#         toothpics = toothpics - removed            
#         print(" | " * toothpics)
#         print(f"There are {toothpics} remaining.")
#         if toothpics <= 0:
#             print(f"{current_player} has won this round of the game")
#             break
#         if current_player == player_1:
#             current_player == player_2
#         else:
#             current_player = player_1

while True:
    print(" | " * toothpics)
    print(f"There are {toothpics} remaining.")
    removed = int(input(f"{current_player}, how many toothpicks would you like to remove?: "))
    while removed != 1 and removed != 2 and removed != 3:
        removed = int("Input must be 1, 2 or 3")
    toothpics -= removed   
    if toothpics <= 0:
        print(f"{current_player} has won this round of the game")
        break
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1

print("Game over")