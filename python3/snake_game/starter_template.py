import turtle

# The constants
WIDTH = 500
HEIGHT = 500
DELAY = 400

# Tell the turtle what to do


def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    # update snake head position
    snake.append(new_head)

    # remove snake tail
    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # update screen
    screen.update()

    # Set timer
    turtle.ontimer(move_snake, DELAY)


# create the canvas/window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("cyan")
screen.tracer(0)  # We can also use False. It turns off the trace behind the turtle

# And now consolidation, genesis the Turtle, named after my bike, not the band

# Stamper the turtle
stamper = turtle.Turtle("square")
stamper.penup()

# Create the snake as a list of coordinated pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]


# Snake init
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set things in motion by calling the function
move_snake()

turtle.done()
