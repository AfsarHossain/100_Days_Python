from turtle import Turtle, Screen
import random

timmy = Turtle()

# timmy.colormode(255)
colors = ["red", "green", "blue", "yellow", "indigo", "pink", "cyan", "orange"]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     random_color = (r, g, b)
#     return random_color

direction = [0, 90, 180, 270]

timmy.speed("fastest")
timmy.pensize(15)

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

my_screen = Screen()
my_screen.exitonclick()
