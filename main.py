import turtle
from turtle import Turtle, Screen
import random


os = Turtle()
screen = Screen()
screen


#moves turtle
def move_forwards():
    os.forward(10)

def move_backwards():
    os.backward(10)

def move_left():
    os.left(10)
    """or new_heading = os.heading() + 10
    os.setheading(new_heading)"""

def move_right():
    os.right(10)
    """or new_heading = os.heading() - 10
        os.setheading(new_heading)"""

def penup():
    os.penup()


def pendown():
    os.pendown()


def clear():
# reset turtle and clears drawing and resets.
    os.clear()
    os.penup()
    os.home()
    os.pendown()


def choosecolor():
    color = ["yellow", "gold", "orange", "red", "maroon", "violet",
             "magenta", "purple", "navy", "blue", "skyblue", "cyan",
             "turquoise", "lightgreen",
             "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
    r = random.choice(color)
    return os.color(r)




def computerdraw():

    direction = [0,  90, 180, 270]
    for i in range(300):
        os.pensize(2)
        choosecolor()
        os.speed("fastest")
        os.forward(15)
        os.setheading(random.choice(direction))




screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="l", fun=move_left)
screen.onkey(key="r", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="v", fun=choosecolor)
screen.onkey(key="u", fun=penup)
screen.onkey(key="d", fun=pendown)
screen.onkey(key="a", fun=computerdraw)

screen.exitonclick()

