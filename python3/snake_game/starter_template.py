import random
import turtle

# The constants
WIDTH = 500
HEIGHT = 500
DELAY = 300
FOOD_SIZE = 10

# use a dictionary for the offsets
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0),
}
global game_paused


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    screen.onkey(lambda: set_snake_direction("p"), "p")


def set_snake_direction(direction, game_paused=False):
    global snake_direction
    if direction == "up":
        if direction != "down":
            snake_direction = "up"
    elif direction == "down":
        if direction != "up":
            snake_direction = "down"
    elif direction == "right":
        if direction != "left":
            snake_direction = "right"
    elif direction == "left":
        if direction != "right":
            snake_direction = "left"
    else:
        if direction == "p":
            if not game_paused:
                True
            elif game_paused == True:
                game_paused == False


# Tell the turtle what to do
def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Collision detection
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # update snake head position
        snake.append(new_head)

        # remove snake tail
        if not food_collection():
            snake.pop(0)

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # update screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        def pause_game(game_paused):
            if not game_paused:
                # Set timer
                turtle.ontimer(game_loop, DELAY)
            else:
                screen.title(f"Game currently paused: {game_paused}")

        pause_game(game_paused)


def food_collection():
    global food_pos, score  # Notice that we can add more than one global value
    if get_distance(snake[-1], food_pos) < 20:
        score += 4
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras theorem used in gaming
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = 'up'
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


# create the canvas/window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("cyan")
screen.tracer(0)  # We can also use False. It turns off the trace behind the turtle

# And now to make it interactive using event handlers in python
screen.listen()
bind_direction_keys()
# And now consolidation, genesis the Turtle, named after my bike, not the band

# Stamper the turtle
stamper = turtle.Turtle("square")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()
# Set things in motion by calling the function
reset()

turtle.done()
