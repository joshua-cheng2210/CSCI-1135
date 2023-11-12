#2
def vowel_count(fname):
    f = open(fname)
    fp = f.read()
    vowel = ["a","e","i","o","u"]
    out = {}

    fp = fp.lower()
    for char in fp:
        if char in vowel:
            if char not in out:
                out[char] = 1
            else:
                out[char] += 1
    f.close()
    return out

# print(vowel_count("cake.txt"))

#3
def reverse_file(fname):
    f = open(fname)
    fp = f.readlines()
    f_out = open(f"copy_{fname}", "w")
    f_out.write("".join(fp[::-1]))
    f.close()
# reverse_file('cake.txt')

#4
def reverse_lines(fname):
    f = open(fname)
    fp = f.readlines()
    f_out = open(f"copy_{fname}", "w")
    "".join(fp[::-1])
    for lines in range(len(fp)):
        fp[lines] = fp[lines][::-1]
    f_out.write("".join(fp))
    f_out.close()

# reverse_lines('cake.txt')

#5
def get_nums(fname):
    out = []
    try:
        f = open(fname)
    except:
        return out
    fp = f.read()

    fp = fp.replace("\n", "").split(",")
    for nums in range(len(fp)):
        fp[nums] = int(fp[nums])
    for nums in fp:
        if fp.count(nums) > 1:
            fp.remove(nums)
    f.close()
    return fp

# print(get_nums('nums.csv'))

#6
def double_csv(fname):
    f = open(fname)
    f_out = open(f"double_{fname}", "w")
    fp = f.readlines()
    for line in fp:
        line = line.split(",")
        for nums in range(len(line)):
            line[nums] = str(int(line[nums]) * 2)
        string = ",".join(line)
        f_out.write(f"{string}\n")
    f.close()
    f_out.close()

# double_csv('nums.csv')

#7
def transpose_csv(fname):
    out = []
    out_nest = []
    out_2 = []
    with open(fname) as f:
        fp = f.readlines()
        for xxx in range(len(fp)):
            fp[xxx] = fp[xxx].split(",")
            for yyy in range(len(fp[xxx])):
                fp[xxx][yyy] = fp[xxx][yyy].strip()
        for nest in range(len(fp)):
            for nested in range(len(fp[nest])):
                for lst in range(len(fp)):
                    out_nest.append(fp[lst][nested])
                out.append(out_nest)
        out = out[0]
        x = int(len(out) / 2)
        out = out[0:x]
        # print(out)
        for nums in range(len(out)):
            if nums % (len(fp)) == 0:
                out_2.append("\n")
            out_2.append(f"{out[nums]},")
        out_2 = out_2[1:]
        with open(f"transpose_{fname}", "w") as f_out:
            f_out.write("".join(out_2))
            
# transpose_csv('nums.csv')












