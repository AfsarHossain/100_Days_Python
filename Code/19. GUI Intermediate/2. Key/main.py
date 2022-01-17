from turtle import Turtle, Screen


timmy = Turtle()
my_screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


my_screen.listen()
my_screen.onkey(move_forward, "w")
my_screen.onkey(move_backward, "s")
my_screen.onkey(turn_left, "a")
my_screen.onkey(turn_right, "d")
my_screen.onkey(clear, "c")

my_screen.exitonclick()
