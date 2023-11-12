#1
#A) 
# K.init 1 2
# 1&2
#B) 
# L.init 3 4
# K.init 5 4
# K.init 3 3
# K.sub
# 5&2
#C)
# L.init 5 6
# K.init 5 6
# K.init 5 5
# M.sub
# K.sub
# 5&-2

class K:
    def __init__(self, x, y):
        print("K.init",x,y)
        self.a = x
        self.b = y

    def __repr__(self):
        return str(self.a) + "&" + str(self.b)

    def __sub__(self, other):
        print("K.sub")
        return self.a - other.b

class L(K):
    def __init__(self,x,z):
        print("L.init",x,z)
        self.a = z
        K.__init__(self,5,self.a)
        self.b = self - K(x,x)

class M(L):
    def __sub__(self,other):
        print("M.sub")
        return (other -self) * 2

# print(K(1,2))
# print(L(3,4))
# print(M(5,6))

class Item:
    def __init__(self, name, weight, value, quantity):
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = quantity

    def sell_item(self):
        if self.quantity > 0:
            self.quantity -= 1
            print(self.name, "sold for", self.value, "rupees.")
        else:
            print("You don't have any more to sell")

class QuestItem(Item):
    def __init__(self, name, weight, value, quantity):
        Item.__init__(self, name, weight, value, quantity)
        self.quest_completed = False

    def sell_item(self):
        if self.quest_completed == False:
            print(f"You must complete a quest before you cans ell the {self.name}")
        else:
            Item.sell_item(self)

# item1 = QuestItem("Korok seed", 1, 50, 2)
# item1.sell_item()
# item1.quest_completed = True
# item1.sell_item()
# item1.sell_item()
# item1.sell_item()

class EquippableItem(Item):
    def __init__(self, name, weight, value):
        Item.__init__(self, name, weight, value, 1)
        self.equiped = False

    def sell_item(self):
        if self.equiped == True:
            print(f"You must unequip the {self.name} before you can sell it.")
        else:
            Item.sell_item(self)

# item2 = EquippableItem("Boko Club", 5, 100)
# item2.equiped = True
# item2.sell_item()
# item2.equiped = False
# item2.sell_item()
# item2.sell_item()

class Vector(list):
    def __mul__(self, other):
        total = 0
        for i in range(len(self)):
            total += self[i] * other[i]       
        return total

    def __add__(self,other):
        out = []
        for i in range(len(self)):
            out.append(self[i] + other[i])
        return Vector(out)

# print(Vector([1,0,5]) * Vector([3,6,2]))
# print(Vector([1,4,5,0]) + Vector([2,3,-1,2]) + Vector([0,8,0,-2]))

class Time:
    def __init__(self, hours = 0, minutes = 0):
        self.hours = hours
        self.minutes = minutes
    
    def set_hours(self, other):
        self.hours = other

    def set_minutes(self, other):
        self.minutes = other

    def accessor(self):
        return (self.hours, self.minutes)

    def __str__(self):
        return f"{str(self.hours):.2f}:{str(self.minutes):.2f}"

    def __add__(self, other):
        min = self.minutes + other.minutes
        hrs = self.hours + other.hours
        while(min >= 60):
            min = min - 60
            hrs += 1
        hrs = hrs % 24
        return Time(min, hrs)
    
    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
            else:
                return False
        else:
            return False

class FlightArrival(Time):
    def __init__(self, arrival_hour, arrival_minute, city_of_origin, flight_number):
        Time.__init__(arrival_hour, arrival_minute)
        self.city_of_origins = city_of_origin
        self.flight_number = flight_number

    def accessor(self):
        return self.city_of_origins

    def __str__(self):
        return f"{self.flight_number} {self.city_of_origins} ETA: {str(self.hours):.2f}:{str(self.minutes):.2f}"


