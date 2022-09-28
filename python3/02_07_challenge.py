import os
import time
from termcolor import colored


# From: https://www.linkedin.com/learning/python-essential-training-14898805/solution-it-s-hip-to-be-square?autoSkip=true&autoplay=true&contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))


class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1] - 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1] + 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0] + 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0] - 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)


# Create a new Canvas instance that is 30 units wide by 30 units tall
canvas = Canvas(50, 50)

# Create a new scribe and give it the Canvas object
scribe = TerminalScribe(canvas)


# Draw a small square

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.down()
# scribe.down()
# scribe.down()
# scribe.down()

# scribe.left()
# scribe.left()
# scribe.left()
# scribe.left()
# scribe.left()


# scribe.up()
# scribe.up()
# scribe.up()
# scribe.up()
# scribe.up()

# Draw another shape

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.down()
# scribe.down()
# scribe.down()
# scribe.down()

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.down()
# scribe.down()
# scribe.down()
# scribe.down()

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.down()
# scribe.down()
# scribe.down()
# scribe.down()

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.down()
# scribe.down()
# scribe.down()
# scribe.down()

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.up()
# scribe.up()
# scribe.up()
# scribe.up()


# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.up()
# scribe.up()
# scribe.up()
# scribe.up()


# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.up()
# scribe.up()
# scribe.up()
# scribe.up()


# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# scribe.up()
# scribe.up()
# scribe.up()
# scribe.up()

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.right()

# def draw_right():
#   scribe.right()
#   scribe.right()
#   scribe.right()
#   scribe.right()

# draw_right()

def downward_steps():
    scribe.right()
    scribe.right()
    scribe.right()
    scribe.right()

    scribe.down()
    scribe.down()
    scribe.down()
    scribe.down()


def upward_steps():
    scribe.right()
    scribe.right()
    scribe.right()
    scribe.right()
    scribe.up()
    scribe.up()
    scribe.up()
    scribe.up()



def square_wave():
    i = 0
    while i < 2:
        downward_steps()
        upward_steps()
        i += 1

# square_wave()

def square_shape(width, height):
    w = 0
    
    while w < width:
        scribe.right()
        w += 1
    h = 0
    while h < height:        
        scribe.down()
        h += 1
    while w > 0:
        scribe.left()
        w -= 1
    while h > 0:
        scribe.up()
        h -= 1

print("Welcome to this drawing app")
print("Which app would you like to use? \n 1. Square Shape or \n 2. Square Wave")
choice = input("please enter 1 or 2: ")
if choice == "1":
    print("Please specify a number between 1 and 50 for width")
    square_width = int(input(">> "))
    print("Please specify a number between 1 and 50 for width")
    square_height = int(input(">> "))
    square_shape(square_width,square_height)
elif choice == "2":
    square_wave()
else:
    print("Your choice was not recognised")

