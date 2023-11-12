class Media:
    def __init__(self, title, yearPublished):
        self.title = title
        self.year = yearPublished
    def __repr__(self):
        return "\nTitle: " + self.title + "; Year: " + str(self.year)
    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False
        
class Book(Media):
    def __init__(self, title, yearPublished, no_pages):
        Media.__init__(self, title, yearPublished)
        self.no_pages = no_pages
    def __repr__(self):
        return Media.__repr__(self) + "; Pages: " + str(self.no_pages)
class Video(Media):
    def __init__(self, title, yearPublished, runtime, rating):
        Media.__init__(self, title, yearPublished)
        self.rating = rating
        self.runtime = runtime
    def __repr__(self):
        return Media.__repr__(self) + "; Runtime: " + str(self.runtime) + "; Rating: " + str(self.rating)

class Library:
    def __init__(self, file_name):
        self.catalog = []
        fp = open(file_name, 'r')
        fp_out = fp.readlines()
        for i in range(1, len(fp_out)):
            fp_out[i] = fp_out[i].strip('\n').split(',')
            if fp_out[i][0] == 'Book':
                self.catalog.append(Book(fp_out[i][1], fp_out[i][2], fp_out[i][3]))
            else:
                self.catalog.append(Video(fp_out[i][1], fp_out[i][2], fp_out[i][4], fp_out[i][5]))
        fp.close()
    def search(self, query):
        obj = []
        for media in self.catalog:
            if query in media.title:
                obj.append(media)
        return obj
    def sort(self):
        self.catalog = sorted(self.catalog)

keypad = {'1': '', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}

def phone(ph_no):
    out = ''
    for i in range(len(ph_no)):
        if ph_no[i].isalnum():
            out += ph_no[i]
    print(out)
    out_lst = list(out.upper())
    if (len(out) != 7) and (len(out) != 10):
        print('Invalid Number')
    else:
        for i in range(len(out_lst)):
            if out_lst[i].isalpha():
                for key in keypad:
                    if out_lst[i] in keypad[key]:
                        out_lst[i] = key
        out = ''.join(out_lst)
        if len(out) == 7:
            return out[0:3] + '-' + out[3: ]
        else:
            return out[0:3] + '-' + out[3:6] + '-' + out[6: ]
    

            
    





                 
            
            
    


