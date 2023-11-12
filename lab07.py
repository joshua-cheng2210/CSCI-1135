import re


def unique_chars(str):
    out = []
    for ch in str:
        if ch not in out:
            out.append(ch)
    return out

# strings = "This is a sentence."
# print(unique_chars(strings))

def word_count(str, find):
    str = str.lower()
    counter = 0
    counter = str.count(find)
    return counter

# print(word_count("aBcabcabc", "abc"))

def flipcase(str):
    out = ""
    for ch in str:
        if ch.isupper():
            out += ch.lower()
        else:
            out += ch.upper()
    return out

# print(flipcase("AbC1d2"))

def reverseMe(str):
    out = ""
    str = flipcase(str)
    for ch in range(len(str) - 1, -1, -1):
        out += str[ch]
    return out

# print(reverseMe("AbC1d2"))

def substring_count(string):
    out = []
    counter = 0
    for i in range(2, len(string) + 1):
        for xxx in range(0, len(string) - i + 1):
            out.append(string[xxx:xxx + i])
            if (out[-1][0] == string[0] and out[-1][-1] == string[-1]):
                counter += 1
    print(out)
    return counter

# print(substring_count("dodo"))

# def parens_split(phrase):
#     phrase = phrase.replace(')', '(')
#     segments = phrase.split('(')
#     return segments[1::2]
#     # string = phrase
#     # out = []
#     # while string:
#     #     try:
#     #         start = string.index("(") + 1
#     #     except:
#     #         return out
#     #     start = string.index("(") + 1
#     #     end = string.index(")")
#     #     out.append(string[start : end])
#     #     string = string[(end + 1):]
    
# print(parens_split('One (Two) Three (Four Five) Six'))
# print(parens_split('No parentheses here'))
# print(parens_split("frtghygtrfe(rfvgthyjuhyg)erfvtghgb(gBHY)bh"))
# print(parens_split('y(hyhu)(yhy)(yhb)'))

def smallest_window1(haystack, need):

    hay = haystack

    index_list = []
    for char in need:
        try:
            f = hay.index(char)
            index_list.append(f)
            hay = hay[f:]
        except:
            return -1

    hayy = haystack[0: index_list[1] + index_list[0] + 1]
    start = []
    for char in range(len(hayy)):
        if hayy[char] == need[0]:
            start.append(char)

    if len(hay) != 1:
        return haystack[start[-1]: haystack.index(hay) + 1]
    else:
        return haystack[start[-1]:]

# print(smallest_window1("abcffammkmkmbmkcc", "fabc"))

def smallest_window2(haystack, need):
    string = haystack
    out = []
    out2 = []
    for i in range(2, len(string) + 1):
        for xxx in range(0, len(string) - i + 1):
            out.append(string[xxx:xxx + i])
    
    for xxx in out:
        try:
            for char in need:
                xxx.index(char)
            out2.append(xxx)
        except:
            x = 0

    return (min(out2))

# print(smallest_window2("abcffammkmkmbmkcc", "fabc"))