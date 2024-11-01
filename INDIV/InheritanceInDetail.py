#1 Связь классов: Учитель и Ученик


"""
передача объекта одного класса (Teacher)
в метод другого класса (Student)
"""


class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name

    def introduce_teacher(self, teacher):   # teacher — параметр, который ожидает объект класса Teacher
        print(f"My teacher is {teacher.name}")  # обращаемся к атрибуту name объекта Teacher


# Пример использования
teacher1 = Teacher("Mr. Ivanov")  # Создание объекта класса Teacher
student1 = Student("Petya")
student1.introduce_teacher(teacher1) # объект как аргумент teacher



# Задание для самостоятельного выполнения:
"""
Создайте классы Doctor и Patient. 
Класс Doctor должен иметь атрибут `name`, 
а класс **Patient** — метод `introduce_doctor`, который будет выводить имя врача, 
переданного в качестве аргумента.
"""







#2 Наследование: Животные и их разновидности

class Animal:
    def sound(self):
        print("Some sound")


class Cat(Animal):
    def sound(self):
        print("Meow")


# Пример использования
my_pet = Cat()
my_pet.sound()



# Задание для самостоятельного выполнения:
"""
Создайте классы Vehicle и Car. 
Vehicle должен иметь метод `move`, выводящий на экран "Vehicle moves". 
Car должен наследовать Vehicle и переопределять метод `move`, 
выводя "Car drives". Создайте объект Car и вызовите метод `move`.
"""





#3 Множественное наследование: Устройство и его модификации
class Phone:
    def call(self):
        print("Calling")

class Camera:
    def take_photo(self):
        print("Taking a photo")

class Smartphone(Phone, Camera):
    pass

# Пример использования
my_phone = Smartphone()
my_phone.call()
my_phone.take_photo()

# Задание для самостоятельного выполнения:
"""
Создайте классы Pen и Highlighter. 
Pen должен иметь метод `write`, который выводит "Writing". 
Highlighter должен иметь метод `highlight`, который выводит "Highlighting". 
Создайте класс Marker, который наследует оба класса, и вызовите оба метода.
"""
