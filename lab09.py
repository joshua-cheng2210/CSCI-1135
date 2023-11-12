# data = {
#     "por":
#     {
#         "lis" : [("leo", "1700 - 097"), ("Nuno", "1050 - 100")],
#         "porto" : [("ana", "4150 - 036")]
#     },

#     "US":
#     {
#         "Miami" : [("nancy", "33136"),("fred", "34136")],
#         "chicago" : [("cesar", "60661")]
#     },

#     "UK":
#     {
#         "London": [("stuart", "SW1H 0B D")]
#     }
# }
# #1
# #a
# for key in data:
#     for key2 in data[key]:
#         print(data[key][key2])
# print(data[key][key2])

# #b
# print(data["por"]["porto"])
# print(data["por"]["porto"][0][0])
# print(data["US"]["Miami"][1])
# print(data["US"]["Miami"][1][0][0])
# print(data["US"]["Miami"][1][1][1])

#c
# data["por"] = {}
# data["London"] = {}
# print(len(data))

#d
# for i in data:
#     print(i)

#e
# out = {}
# for key in data:
#     for i in range(len(key)):
#         if i not in out:
#             out[i] = ""
#         out += key[i]
# print(out)

# for key in data:
#     for key2 in data[key]:
#         ele = data[key][key2]
#         key2 += "d"
#         ele.reverse()
#         ele = ele[::-1]
# print(data["por"]["lis"]])


#2
# users = {"a":"1", "b":"2","c":"3"}

# def accept_login(users, username, password):
#     if users[username] == password:
#         return True
#     else:
#         return False

# print(accept_login(users, "c","3"))

#3
# def count_chars(string):
#     out = {}
#     for char in string:
#         if char not in out:
#             out[char] = 1
#         else:
#             out[char] += 1
#     return out

# print(count_chars("abc"))

#4
def larger_values(dict1, dict2):
    out = {}
    for ele in dict1:
        if ele in dict2:
            if dict1[ele] > dict2[ele]:
                out[ele] = dict1[ele]
            else:
                out[ele] = dict2[ele]
        else:
            out[ele] = dict1[ele]
    for ele in dict2:
        if ele not in dict1:
            out[ele] = dict2[ele]
    return out

# print(larger_values({"a":"1", "b":"2","c":"3", "d":"5"}, {"a":"4", "b":"6","c":"8"}))

#5
def write():
    out = {}
    decade = "00s"
    years = []

    for t in range(0, 10):
        for o in range(0, 10):
            years.append(int(f"19{t}{o}"))

    while years:
        for k in range(0, 10):
            out[f"{k}0s"] = years[0:10]
            years = years[10:]
    return out

# print(write())

#6
import statistics

lee = {"hw": [90, 97, 75, 92], "quiz" : [88, 40, 94], "test": [75, 90]}
alice = {"hw": [100, 92, 98, 100], "quiz" : [82, 83, 91], "test": [89, 97]}
kiara = {"hw": [0, 87, 75, 22], "quiz" : [0, 75, 78], "test": [100, 100]}

gradebook = {"lee" : lee, "alice": alice, "kiara": kiara}

def weighted_average(student):
    if student in gradebook:
        return statistics.mean(gradebook[student]["hw"]) * 0.1 + statistics.mean(gradebook[student]["quiz"]) * 0.3 + statistics.mean(gradebook[student]["test"]) * 0.6

# print(weighted_average("lee"))
# print(weighted_average("alice"))
# print(weighted_average("kiara"))

#7
def get_class_grades(gradebook):
    out = {}

    for students in gradebook:
        if weighted_average(students) == 100:
            out[students] = "A"
        elif weighted_average(students) < 60:
            out[students] = "F"
        else:
            out[students] = chr(ord("A") + (10 - ((int(weighted_average(students)) + 10) // 10)))
    
    return out

print(get_class_grades(gradebook))

#8
