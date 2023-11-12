# from turtle import *
# speed(10)
# # hideturtle()

# def black_square(length_of_box):
#     for lines in range(4):
#         color('black')
#         begin_fill()
#         for i in range(4):
#             forward(length_of_box)
#             left(90)
#         end_fill()

#         forward(length_of_box)

#         color('black')
#         begin_fill()
#         for i in range(4):
#             forward(length_of_box)
#             right(90)
#         end_fill()

#         forward(length_of_box)

# def black_total(length_of_box):
#     for total in range(4):
#         black_square(length_of_box)
#         penup()
#         setpos(0, (total + 1) * length_of_box * -2)
#         pendown()

# black_total(20)
# exitonclick()


'''
turtle.setpos(x, y) 
    -> teleport your turtle to the coordinate(x,y); maybe need to pen up first
turtle.write(349, font=("Arial", 20, "normal"))
    -> write in the middle of the turtle screen
turtle.exitonclick()
    -> a function that will only exit turtle programing when you click
'''

from turtle import *
from random import *

speed(0)
# hideturtle()

def checkerboard(length_of_box):
    for total in range(4):
        for two_lines in range(2):
            for one_line in range(4):
                # color('black')
                # r = random()
                # g = random()
                # b = random()
                color(random(),random(),random())
                begin_fill()
                for i in range(4):
                    forward(length_of_box)
                    left(90)
                end_fill()

                forward(length_of_box)

                # color('red')
                color(random(),random(),random())
                begin_fill()
                for i in range(4):
                    forward(length_of_box)
                    left(90)
                end_fill()

                forward(length_of_box)
            left(180)
        penup()
        right(90)
        forward(length_of_box * 2)
        left(90)
        pendown()

def perfect(length_of_box):
        penup()
        setpos((length_of_box * -8), (length_of_box * 8))
        pendown()
        for x in range(2):
            for i in range(2):
                checkerboard(length_of_box)
            penup()
            forward(length_of_box * 8)
            left(90)
            forward(length_of_box * (8 * 2) + 1)
            right(90)
            pendown()
        

perfect(1)
perfect(5)
exitonclick()
