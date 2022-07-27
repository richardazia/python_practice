from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)
print(num)

# Turn that random number into the computer's RPS move


# Ask a user to enter their move
print("Choose between 1: rock, 2: paper, 3: scissors")
player = int(input("Enter the number of your selection: "))

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("")
print("")
print("Player move: ")
if player == 1:
    print(rock)
elif player == 2:
    print(paper)
elif player == 3:
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Computer move")
if num == 1:
    print(rock)
elif num == 2:
    print(paper)
elif num == 3:
    print(scissors)

# Figure out who wins and print the result!
if num == player:
    print("You both tied!!")
elif num == 1 and player == 3:
    print("Computer wins!!")
elif num == 3 and player == 2:
    print("Computer wins!!")
elif num == 2 and player == 1:
    print("Computer wins!!")
elif player == 1 and num == 3:
    print("player wins")
elif player == 3 and num == 2:
    print("player wins")
elif player == 2 and num == 1:
    print("player wins")
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock
