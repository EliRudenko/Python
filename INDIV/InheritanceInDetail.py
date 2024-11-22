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
а класс Patient — метод `introduce_doctor`, 
который будет выводить имя врача, 
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





"""
Задание: персонаж и инвентарь

Создайте базовый класс Character:

В классе Character должен быть атрибут name.
Добавьте метод introduce, который выводит сообщение с именем персонажа 
(например, "Character's name is <имя>").
Создайте класс Player, который наследует Character:

В классе Player переопределите метод introduce, чтобы он выводил сообщение 
"Player's name is <имя>".
Добавьте атрибут inventory, который будет объектом класса Inventory.
Создайте класс Inventory:

В классе Inventory должен быть метод add_item, который добавляет предмет в список items 
и выводит сообщение об этом, например, "Added <название предмета> to inventory".
Протестируйте структуру:

Создайте объект Player с именем по вашему выбору и вызовите метод introduce.
Добавьте предмет в инвентарь этого игрока с помощью метода add_item.
"""









class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Character's name is {self.name}")


class Player(Character):  # Player наследует Character
    def __init__(self, name):
        super().__init__(name)  # Инициализация атрибута name из Character
        self.inventory = Inventory()  # Создаем инвентарь для игрока

    def introduce(self):
        print(f"Player's name is {self.name}")


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to inventory")


# Пример использования
player = Player("Alice")
player.introduce()           # Вывод: "Player's name is Alice"
player.inventory.add_item("Potion")  # Вывод: "Added Potion to inventory"
