from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(6):
    timmy.forward(100)
    timmy.right(60)

my_screen = Screen()
my_screen.exitonclick()
