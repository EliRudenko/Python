
"""
Специальные декораторы:
декораторы встроены в Python:

@abstractmethod (из модуля abc) — требует, чтобы метод был реализован в дочернем классе.
@staticmethod — превращает метод в статический.
@classmethod — делает метод класс-методом.
"""



# 1 Абстракция

"""
Абстрактные классы — это шаблоны, которые говорят
Этот класс нельзя использовать напрямую,
но его дочерние классы обязаны реализовать определённые методы

Чтобы создать абстрактный класс и определить,
что в дочерних классах обязательно должен быть определён
конкретный метод
"""


from abc import ABC, abstractmethod
# Abstract Base Class (ABC) - это базовый класс для создания абстрактных классов.

class Animal(ABC):
    @abstractmethod # это специальный декоратор, который говорит, что метод обязателен для реализации в дочерних классах.
    def sound(self):
        pass  # Мы говорим: "Каждое животное должно иметь этот метод"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Dog(Animal):
    def sound(self):
        return "Гав"

cat = Cat()
dog = Dog()
print(cat.sound())  # Вывод: Мяу
print(dog.sound())  # Вывод: Гав
"""
Задание:
Создайте абстрактный класс GameCharacter с абстрактным методом attack
Реализуйте два дочерних класса: Warrior и Mage, которые определяют этот метод по-своему
Напишите функцию, которая вызывает метод attack для всех объектов списка персонажей
"""






# 2 Инкапсуляция
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Владелец счета
        self.__balance = balance  # Приватный баланс (нельзя трогать снаружи)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance  # Возвращает текущий баланс

account = BankAccount("Иван", 1000)
# Пополняем счет
account.deposit(500)
# Проверяем баланс
print(account.get_balance())  # Вывод: 1500
# Пробуем снять деньги
account.withdraw(2000)  # Вывод: Недостаточно средств
# Пробуем напрямую изменить баланс (не получится)
account.__balance = 999999  # Ошибка: нельзя получить доступ

"""
Задание:
Создайте класс PlayerInventory, который содержит приватное поле __items 
для хранения предметов игрока. Реализуйте методы:

def add_item(item) — добавляет предмет в инвентарь.
def remove_item(item) — удаляет предмет, если он есть.
def show_inventory() — выводит все предметы в инвентаре.
"""




# 3 Полиморфизм
class Cat:
    def sound(self):
        return "Мяу"

class Dog:
    def sound(self):
        return "Гав"


# Функция, которая работает с любым животным
def make_animal_sound(animal):
    print(animal.sound())

cat = Cat()
dog = Dog()

make_animal_sound(cat)  # Вывод: Мяу
make_animal_sound(dog)  # Вывод: Гав


"""
Задание:
Создайте классы Zombie, Skeleton и Dragon, каждый из которых имеет метод make_sound 
Напишите функцию, которая вызывает этот метод для разных врагов
"""






# 4 Статические методы, клас-метод


"""
Когда нужен доступ к классу или его данным

Класс-метод — это метод, который работает с самим классом, а не с конкретным объектом.
Он часто используется, чтобы создать объект особым способом 
или чтобы работать с переменными, которые принадлежат классу 
(а не объекту)


смотрит на весь класс, а не на конкретную машину. 
Например, он может сказать: "Сколько машин в гараже?"
"""



"""
Когда метод никак не зависит от класса

Статический метод — это метод, который не зависит ни от объектов, 
ни от самого класса. Он просто выполняет какую-то задачу, 
которая логически связана с классом


Статический метод — это как калькулятор внутри класса: 
он просто делает свою работу и не зависит от конкретного объекта
"""



class Car:
    total_cars = 0  # Переменная класса для подсчета машин

    def __init__(self, model):
        self.model = model  # Обычное свойство объекта
        Car.total_cars += 1  # Увеличиваем общее количество машин

    @classmethod
    def get_total_cars(cls):
        # Этот метод работает с самим классом
        return f"Всего машин: {cls.total_cars}"

    @staticmethod
    def is_valid_model(model):
        # Этот метод просто проверяет, является ли строка валидной моделью
        return isinstance(model, str) and len(model) > 0
        # Функция isinstance проверяет, является ли объект экземпляром конкретного класса или его потомка.


"""
Задание:
Создайте класс GameWorld, который отслеживает количество активных игроков

Используйте:
Класс-метод для получения количества игроков
Статический метод для проверки, допустимо ли имя игрока
"""



"""
#1
from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass  # Метод должен быть реализован в дочерних классах

class Warrior(GameCharacter):
    def attack(self):
        return "Мечник атакует мечом!"

class Mage(GameCharacter):
    def attack(self):
        return "Маг запускает огненный шар!"

# Создайте список персонажей
characters = [Warrior(), Mage(), Warrior()]

# Проверьте, как каждый персонаж атакует
for character in characters:
    print(character.attack())
"""




"""
#2
class PlayerInventory:
    def __init__(self):
        self.__items = []  # Приватное поле для хранения предметов

    def add_item(self, item):
        if isinstance(item, str):
            self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def show_inventory(self):
        return f"Инвентарь: {', '.join(self.__items) if self.__items else 'пуст'}"

# Тестируем
inventory = PlayerInventory()
inventory.add_item("Меч")
inventory.add_item("Зелье")
print(inventory.show_inventory())  # Вывод: Инвентарь: Меч, Зелье

inventory.remove_item("Меч")
print(inventory.show_inventory())  # Вывод: Инвентарь: Зелье

"""




"""
#3
class Zombie:
    def make_sound(self):
        return "Зомби рычит: Ааааарргх!"

class Skeleton:
    def make_sound(self):
        return "Скелет хрустит костями: Хр-хр-хр!"

class Dragon:
    def make_sound(self):
        return "Дракон рычит: РРРРРАААА!"

def enemy_sounds(enemy):
    print(enemy.make_sound())

# Тестируем
zombie = Zombie()
skeleton = Skeleton()
dragon = Dragon()

for enemy in [zombie, skeleton, dragon]:
    enemy_sounds(enemy)
"""




"""
#4
class GameWorld:
    active_players = 0  # Количество активных игроков

    def __init__(self, player_name):
        if GameWorld.is_valid_name(player_name):
            self.player_name = player_name
            GameWorld.active_players += 1
        else:
            raise ValueError("Недопустимое имя игрока")

    @classmethod
    def get_active_players(cls):
        return f"Активных игроков: {cls.active_players}"

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 2

# Тестируем
player1 = GameWorld("Герой")
player2 = GameWorld("Маг")
print(GameWorld.get_active_players())  # Вывод: Активных игроков: 2

# Проверяем имя
print(GameWorld.is_valid_name("A"))  # Вывод: False
"""
