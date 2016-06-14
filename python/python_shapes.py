from turtle import *


# START WRITING YOUR CODE HERE
def square(size, color):
    pencolor(color)
    pendown()
    for i in range(4):
        forward(size)
        right(90)
        
def triangle(size, color):
    pencolor(color)
    pendown()
    for i in range(3):
        left(120)
        forward(size)

def regular_polygon(side_length, number_of_sides, color):
    pendown()
    pencolor(color)
    for i in range(number_of_sides):
        forward(side_length)
        right(360 / number_of_sides)

def regular_polygon_row(side_length, number_of_sides, color):
    penup()
    goto(-275, 0)
    speed(0)
    for i in range(275):
        regular_polygon(side_length, number_of_sides, "maroon")
        penup()
        forward(2)  

def circle_squares(size, amount):
    for i in range(amount):
       speed(0)
       square(size, "lightblue")
       right(360 / amount)

def circle_triangles(size, amount):
    for i in range(amount):
        speed(0)
        triangle(size, "orange")
        right(360 / amount)

def compound_shape1():
    for i in range(120):
        speed(0)
        square(50, "blue")
        triangle(-50, "green")
        right(3)
        penup()
        forward(5)

def house(size, color):
    fillcolor(color)
    begin_fill()
    triangle(size, color)
    back(size)
    square(size, color)
    end_fill()
    door(size)


def door(size):
    penup()
    color("ghost white")
    forward(size/4)
    right(90)
    forward(size / 2 )
    left(90)
    square(size/2, "ghost white")
    penup()
    left(90)
    forward(size/2)
    right(90)
    back(size/4)

def row_of_houses():
    bgcolor("linen")
    penup()
    goto(-275, 0)
    size = 40
    for i in range(14):
        change = 0
        color_choice = "yellow2"
        if i % 5 == 0:
            change = 5
            color_choice = "cornflower blue"
        elif i % 3:
            change = 3
            color_choice = "burlywood"

        house(size + change, color_choice)
        penup()
        next_house_location  = (size + change) * 2
        forward(next_house_location)

row_of_houses()

def sun():
    penup()
    goto(-200, 250)
    dot(100, "yellow")

sun()
    




