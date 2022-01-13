from turtle import Turtle, Screen

h = Turtle()

for _ in range(3):
    h.forward(100)
    h.left(120)

my_screen = Screen()
my_screen.exitonclick()
