import turtle

# The constants
WIDTH = 500
HEIGHT = 500
DELAY = 400

# use a dictionary for the offsets
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0),
}

# User direction instructions
def go_up():
    global snake_direction
    if snake_direction != "d0wnn":
        snake_direction = "up"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


# Tell the turtle what to do
def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

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

# And now to make it interactive using event handlers in python
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
# And now consolidation, genesis the Turtle, named after my bike, not the band

# Stamper the turtle
stamper = turtle.Turtle("square")
stamper.penup()

# Create the snake as a list of coordinated pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = 'up'


# Snake init
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set things in motion by calling the function
move_snake()

turtle.done()
