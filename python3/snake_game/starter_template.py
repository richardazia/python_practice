import turtle

# The constants
WIDTH = 500
HEIGHT = 500
DELAY = 20

# Tell the turtle what to do

def move_turtle():
    genesis_the_turtle.forward(1)
    genesis_the_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

# create the canvas/window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("The Garden")
screen.bgcolor("cyan")
screen.tracer(0) # We can also use False. It turns off the trace behind the turtle

# And now concolidation, genesis the Turtle, named after my bike, not the band

# The Turtle
genesis_the_turtle = turtle.Turtle()
genesis_the_turtle.shape("turtle")
genesis_the_turtle.color("green")

# Entice the turtle to move around

move_turtle()

turtle.done()