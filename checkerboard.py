from turtle import *

def draw_square(length, colour):
    begin_fill()
    color(colour)
    for i in range(4):
        forward(length)
        left(90)
    end_fill()

def draw_row(first_color, second_color):
    for i in range(4):
        draw_square(60, first_color)
        penup()
        forward(60)
        pendown()
        draw_square(60, second_color)
        penup()
        forward(60)
        pendown()

def move_to_next():
    penup()
    left(90)
    forward(60)
    left(90)
    forward(480)
    left(180)

pendown()
speed(10000)
setup(480, 480)
penup()
setposition(-240, -240)

for i in range(4):
    draw_row("red", "black")
    move_to_next()
    draw_row("black", "red")
    move_to_next()


exitonclick()