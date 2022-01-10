from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed("fastest")


colors = ["red", "green", "blue", "yellow", "indigo", "pink", "cyan", "orange"]


def random_color():
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)

    colors = (r, g, b)
    return colors


for _ in range(100):
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.left(5)

my_screen = Screen()
my_screen.exitonclick()
