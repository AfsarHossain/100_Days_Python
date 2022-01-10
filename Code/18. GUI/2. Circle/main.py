from turtle import Turtle, Screen

h = Turtle()

#h.shape("turtle")

x = 75

while x > 0:
    h.forward(100)
    h.right(5)
    h.backward(100)
    x -= 1

my_screen = Screen()
my_screen.exitonclick()
