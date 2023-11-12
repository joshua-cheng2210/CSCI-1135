from gettext import find


def count_8(lists):
    counter = 0
    for i in lists:
        for j in i:
            if lists[i][j] == 8:
                counter += 1
    return counter

def mult_table(x):
    return_list = []
    for i in range(x):
        lists = []
        for j in range(x):
            lists.append((j + 1) * (i + 1))
        return_list.append(lists)
    return return_list

def remove_student(grades, name):
    temp = -1
    for xxx in range(len(grades)):
        if grades[xxx][0] == name:
            temp = xxx
            while (len(grades[xxx]) != 0):
                grades[xxx].pop(0)
    grades.pop(temp)
        

    return grades

# grades = [["a", 1,2,3,4,5,6], ["b", 1,2,3,4,5,6], ["c", 1,2,3,4,5,6], ["d", 1,2,3,4,5,5]]
# remove_student(grades, "b")
# print(grades)

def averagee(list):
    total = 0
    for x in list:
        total += x
    return (total / len(list))

def highest_avg(grades):
    highest_average = -1
    student = ""
    for xxx in range(len(grades)):
        marks = []
        marks = grades[xxx][1:]
        # print(marks, averagee(marks))
        if averagee(marks) > highest_average:
            student = grades[xxx][0]
            highest_average = averagee(marks)
            # print(f"averagee(marks) = {averagee(marks)}, student = {student}, highest_avg = {highest_avg}")
    return student

# grades = [["a", 1,2,3,4,5,6], ["b", 150], ["c", 1,2,3,4,5,6], ["d", 100]]
# print(highest_avg(grades))

def sort_students(grades):
    new_list = []
    while(len(grades) != 0):
        new_list.append(highest_avg(grades))
        remove_student(grades, new_list[-1])
    return (new_list)

# grades = [["a", 1,2,3,4,5,6], ["b", 150], ["c", 1,2,3,4,5,6], ["d", 100]]
# print(sort_students(grades))

def magic_square(x):
    number = sum(x[0])
    for hori in x:
        if number != sum(hori):
            return False

    number = sum(x[0])
    for i in range(len(x)):
        total = 0
        for j in range(len(x)):
            total += x[j][i]
        if total != number:
            return False
    
    number = sum(x[0])
    total = 0
    for yx in range(len(x)):
        # print(x[yx][yx])
        total += x[yx][yx]
    if number != total:
        # print(f"number = {number}, y = x sum = {total}")
        return False

    number = sum(x[0])
    total = 0
    for zzz in range(len(x)):
        print(x[zzz][len(x) - 1 - zzz])
        total += x[zzz][len(x) - 1 - zzz]
    if number != total:
        print(f"number = {number}, y = 1/x sum = {total}")
        return False
    return True

# print(magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))

def find_path(graph, start, end):
    steps = 0
    path = [start]
    # while (start != end):
    #     alternatives = -1
    #     # while (alternatives in range(len(graph[start])) and ):
    #     for alternatives in range(len(graph[start])):
    #         if (graph[start][alternatives] == True and alternatives == end):
    #             path.append(alternatives)
    #             steps+= 1
    #             return (steps, path)
    #         else:
    #             if (graph[start][alternatives] == True):
    #                 steps += 1
    #                 start = alternatives
    #                 return find_path(graph, start, end)
    if start == end:
        return(steps, path)
    else:
        while(start != end):
            for alternatives in range(len(graph[start])):
                

    
graph = [[False,  True,  True, False, False, False], #0
        [False, False, False,  True, False,  True], #1
        [False, False, False, False,  True, False], #2
        [False, False, False, False, False,  True], #3
        [False, False, False, False, False,  True], #4
        [False, False,  True, False, False, False]]

print(find_path(graph, 1, 4))