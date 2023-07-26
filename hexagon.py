from turtle import *

def draw_rectangle(colour,length):
    begin_fill()
    forward(length)
    right(90)
    forward(100)
    right(90)
    forward(length)
    right(90)
    forward(100)
    color(colour)
    end_fill()

draw_rectangle("red")
penup()
right(270)
forward(66.6)
right(180)
draw_rectangle("white")
exitonclick()