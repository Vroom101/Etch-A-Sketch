from turtle import Turtle, Screen
swimmy = Turtle()
screen = Screen()


def forward():
    swimmy.forward(10)

def backward():
    swimmy.backward(10)

def left():
    swimmy.left(10)

def right():
    swimmy.right(10)
def clear():
    swimmy.clear()
    swimmy.penup()
    swimmy.home()
    swimmy.pendown()
screen.listen()
screen.onkey(forward , "w")
screen.onkey(backward , "s")
screen.onkey(left , "a")
screen.onkey(right , "d")
screen.onkey(clear , "c")
screen.exitonclick()
