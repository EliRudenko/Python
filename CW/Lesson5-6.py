#1 Зв'язок класів


#1
class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []








    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers_names()


"""
def add_passenger(self, *args):
    for passenger in args:
        self.passengers.append(passenger)
        
        
nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passenger(nick, kate)
car.print_passengers_names()       
"""






"""
#2 СПАДКУВАННЯ
class Grandparent:
    height = 170
    satiety = 100
    age = 60


class Parent(Grandparent):
    age = 40


class Child(Parent):
    height = 50

    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)


nick = Child()
"""



class Grandparent:
    def about(self):
        print("I am GrandParent")

    def about_myself(self):
        print("I am Grandparent")


class Parent(Grandparent):

    def about_myself(self):
        print("I am Parent")


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()




#3 МНОЖИННЕ СПАДКУВАННЯ
