from turtle import Turtle, Screen


timmy = Turtle()
timmy.color("red")

for _ in range(4):
    timmy.forward(100)
    #timmy.right(90)
    timmy.left(90)

my_screen = Screen()
my_screen.exitonclick()
