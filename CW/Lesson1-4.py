# Тема: Создание Классов!

"""
Главные термены сегодня:
- экземпляр класса, объект
- конструктор (нужен для инициализации полей, автоматически вызывается)- аргумент self (всегда ПЕРВЫЙ, ссылаемся/обращаемся к полям и методам ОБЪЕКТА, ВСЕРЕДИНЕ КЛАССА)
- параметр по умолчанию- методы

- методы
- grow()
- __str__() возвращает строку
- __del__() ДЕСТРУКТОР  (удаление обьекта)
- __bool__()  как будет вестит себя обьект в булевых конструкциях (например в if)
- __len__() что будет возвращать функция len() для объекта (чаще всего для определение длинны, списка строки и тп)

"""

# 1
class Student:
    print("Hi")


# first_student = Student()  #экземпляр класса, объект


"""    
    def __init__(self):     #конструктор, инициализация полей !!
        self.height = 160   #self - посилання на самого себе !!        
        print("I am alive!")

first_student = Student()
"""


# 2 параметры по умолчанию
"""
class Student:
    def __init__(self, height=160):      #параметр по умолчанию
        self.height = height
        
        
nick = Student()
kate = Student(height=170)
print(nick.height)
print(kate.height)
# что выведится в консоль?
 
"""


#3 Методы
"""
class Student:
    def __init__(self):        
        self.height = 170

    def printer(self):  # метод!!
        print(self.height)


student1 = Student()
student1.printer()
"""


#grow()
"""
class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students+=1
    def grow(self, height=1):
        self.height+=height
nick = Student()
kate = Student(height=170)
nick.grow(height=15)
print(kate.height)
print(nick.height)
"""


#__str__
"""
class Student:
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f"I am a student. My name is {self.name}."
nick = Student(name = "Nick")
print(nick)
"""

#__del__
"""
class Student:
    def __init__(self, name=None):
        self.name = name
    def __del__(self):
        print("Training is over. I am now an expert!")
nick = Student()
"""

#__bool__ и __len__
"""
class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height
    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
nick = Student()
print(nick.__len__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))
"""


# Задания:
"""
1
Створіть клас Circle з атрибутом radius (радіус кола) 
і методом calculate_area, 
який обчислює площу кола за формулою S = π * r^2, де π = 3.14159.


2
Створіть клас Book з атрибутами title (назва книги), author (автор книги) 
і year (рік видання книги), а також методом get_age, який повертає вік книги, 
обчислений як різниця поточного року і року видання книги

"""


# Тема: Связывание, Наследование!


#4 СВЯЗЫВАНИЕ объектов между собой
"""
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
car.add_passenger(nick, kate)
car.print_passengers_names()


"""

#Усовершенствование, добавление пассажиров, вывод
"""
    def add_passenger(self, *args):
            for passenger in args:
                self.passengers.append(passenger)
        def print_passengers_names(self):
            if self.passengers != []:
                print(f"Names of {self.brand} passengers: ")
                for passenger in self.passengers:
                    print(passenger.name)
            else:
                print(f"There are no passengers in {self.brand}")
     

"""