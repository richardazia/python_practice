import turtle

# The constants
WIDTH = 500
HEIGHT = 500
DELAY = 400

# The Turtle
snake = turtle.Turtle()
snake.shape("square")
snake.penup()

# Tell the turtle what to do


def move_snake():
    snake.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    snake.append(new_head)

    snake.pop(0)

    for segment in snake:
        snake.goto(segment[0], segment[1])
        snake.stamp()

    # update screen
    screen.update()

    # Set timer
    snake.ontimer(move_snake, DELAY)


# create the canvas/window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("cyan")
screen.tracer(0)  # We can also use False. It turns off the trace behind the turtle

# And now consolidation, genesis the Turtle, named after my bike, not the band

# Create the snake as a list of coordinated pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]


# Snake init
# for segment in snake:
#     snake.goto(segment[0], segment[1])
#     snake.stamp()

# Set things in motion by calling the function
move_snake()

turtle.done()
