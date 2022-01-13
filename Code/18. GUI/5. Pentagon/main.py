from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(5):
    timmy.forward(100)
    timmy.right(72)

my_screen = Screen()
my_screen.exitonclick()
