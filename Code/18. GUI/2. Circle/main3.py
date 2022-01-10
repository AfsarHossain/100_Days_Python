from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed("fastest")


colors = ["red", "green", "blue", "yellow", "indigo", "pink", "cyan", "orange"]


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random.choice(colors))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
