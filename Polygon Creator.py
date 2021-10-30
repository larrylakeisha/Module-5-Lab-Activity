# Lakeisha Larry
# October 30, 2021

# This program creates a polygon from information given by the user

import turtle
window = turtle.screensize
alex = turtle.Turtle()

sides = int(input("Please enter the number of sides"))
length = int(input("Please enter the length of the side"))
colorname = input("Enter the color of the fill line")
fillcolor = input("Please enter the fill color of the polygon")

alex.begin_fill()
alex.color(colorname)
alex.pencolor(fillcolor)

for i in range(sides):
    alex.forward(length)
    alex.left(360 / sides)

alex.end_fill()
