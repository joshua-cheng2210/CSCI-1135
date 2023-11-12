# error1: #8: class Derived(Base):
# error2: #7: def __str__(self):
# error3: 

#2
class Media:
    def __init__(self, title, yearPublished):
        self.title = title
        self.year = yearPublished
    
    def __repr__(self):
        return "\nTitle: " + self.title + "; Year: " + str(self.year)

def is_palindrome(word):
    if word[0] != word[-1]:
        return False
    else:
        if len(word[1:-1]) == 1:
            return True
        elif len(word[1:-1]) == 2 and word[1] == word[2]:
            return True
        else:
            return is_palindrome(word[1:-1])

def phone(word):
    out = ""
    for xxx in word:
        if xxx.isalnum() == True:
            out += xxx

    out2 = out.lower()
    for x in out:
        if x.isnum() == True:
            out2 += x
        else:
            key = {"a":2, "b":2, "c":2, "d":3, "e":3, "f":3, "g":4, ""}
            if ord(x) <= ord("o"):
                out2 += (ord(x) - ord('`'))


print(phone("gotmIv2lk"))
    
