#1
# a) 4 + 4 + 4
# b) multiply "b" by "a" number of times
# c) a = 0
# d) yes
# e)
# def enigma(a,b):
#     total = 0
#     for x in range(a):
#         total += b 
#     return total

#2
# a) [10, 6, 14]
# b) double every value in the list
# c) lst = []
# d) yes
# e) 
# def mystery(lst):
#     for i in range(len(lst)):
#         lst[i] = lst[i] * 2
#     return lst

#3 
# a) False
# b) stops when theres 2 consequtively same characters
# c) return True
# d) yes, it will return True or False
# e) 
# def puzzle(word):
#     for i in range(len(word) - 1):
#         if word[i] == word[i + 1]:
#             return False
#     return True

#4
def series_sum(n):
    if n == 1:
        total = 1
        return total
    else:
        total = n ** n
        return total + series_sum(n - 1)

#5
def count_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num // 10)

#6
def mirrorstring(word):
    if word == "":
        return ""
    else:
        # return word + word[-1] + mirrorstring(word[:-1])
        return word[0] + mirrorstring(word[1:]) + word[0]

# print(mirrorstring("abcdef"))

#7
def list_prod(lst):
    if lst == []:
        return 1
    elif type(lst[0]) == list:
        return list_prod(lst[0]) * list_prod(lst[1:])
    else:
        return lst[0] * list_prod(lst[1:])

# print(list_prod([1,[2,3],[4,5,[6]],1]))

#8
import turtle
turtle.speed(0)
turtle.delay(0)
# turtle.hideturtle()

def triangle(size):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def sierpinski(n, size):
    # the base is not n = 0,
    if n == 0:
        triangle(size)
    # the base is n = 1,
    elif n == 1:
        for i in range(3):
            triangle(size / 2)
            turtle.forward(size / 2)
            if i == 1:
                turtle.left(180)
                turtle.forward(size)
                turtle.right(120)
                turtle.forward(size / 2)
                turtle.right(60)
        turtle.right(60)
        turtle.forward(size / 2)
        turtle.left(60)
    else:
        sierpinski((n - 1), (size / 2))
        sierpinski((n - 1), (size / 2))
        turtle.left(120)
        turtle.forward(size * 0.5)
        turtle.left(60)
        turtle.forward(size * 0.5)
        turtle.left(180)
        sierpinski((n - 1), (size / 2))
        turtle.right(60)
        turtle.forward(size / 2)
        turtle.left(60)

sierpinski(10, 500)
turtle.exitonclick()