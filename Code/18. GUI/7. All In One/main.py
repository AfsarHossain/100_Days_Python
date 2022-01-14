from turtle import Turtle, Screen
import random

timmy = Turtle()
x = 3

colors = ["red", "green", "yellow", "blue", "indigo", "cyan", "pink", "orange"]

while x < 11:
    timmy.color(random.choice(colors))
    for _ in range(x):
        timmy.forward(100)
        timmy.right(360/x)
    x += 1

my_screen = Screen()
my_screen.exitonclick()
