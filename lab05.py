def reverse_inner(x):
    temp = ""
    for i in range(len(x)):
        j = len(x[i]) - 1
        while (j >= 0):
            temp += x[i][j]
            j -= 1
        x[i] = temp

# list = ["asd", "qwer", "cvbnm", "ghjkl"]
# reverse_inner(list)
# print(list)

def counter_of_values(list):
    element = 0
    type_of_element = []
    new_list = []
    while (element < len(list)):
        if list[element] not in type_of_element:
            type_of_element.append(list[element])
            index = element
            counter = 0
            while(index < len(list)):
                if(type_of_element[-1] == list[index]):
                    counter += 1
                index += 1
            new_list.append([type_of_element[-1], counter])
        element += 1
    return new_list

# test = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
# print(counter_of_values(test))

from turtle import *
from random import *

def draw_circles(i):
    speed(0)
    xcoords = [randint(-300, 300) for dd in range(i)]
    ycoords = [randint(-300, 300) for dd in range(i)]
    if (len(xcoords) == len(ycoords)):
        for i in range(len(xcoords)):
            penup()
            goto(xcoords[i], ycoords[i])
            pendown()
            dot(50, random(), random(), random())
    exitonclick()



draw_circles(50)