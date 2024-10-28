# Тема: Создание Классов!


# 1. Пример создания базового класса
# (понятия конструктор и метод)
class Plant:
    def __init__(self):
        self.height = 30  # высота растения в см

    def show_height(self):  # метод для вывода высоты растения
        print("Current height:", self.height, "cm")


# Создание объекта класса Plant
plant1 = Plant()
plant1.show_height()






# 2. Метод роста (grow)
# с параметром по умолчанию
class Tree:
    total_trees = 0  # атрибут класса для подсчета деревьев

    def __init__(self, height=100):
        self.height = height
        Tree.total_trees += 1

    def grow(self, height=10):  # метод для увеличения высоты дерева
        self.height += height


# Создаем экземпляры класса Tree
oak = Tree()
pine = Tree(height=150)
oak.grow(20)
print("Height of oak:", oak.height, "cm")
print("Height of pine:", pine.height, "cm")








# 3. Специальные методы (__str__, __bool__, __len__)
class Flower:
    def __init__(self, name=None, petals=5):
        self.name = name
        self.petals = petals

    def __str__(self):  # возвращает строковое представление объекта
        return f"{self.name} has {self.petals} petals."

    def __bool__(self):  # булевое поведение объекта
        return self.name is not None

    def __len__(self):  # длина объекта как количество лепестков
        return self.petals


rose = Flower(name="Rose", petals=20)
print(str(rose))
print("Number of petals:", len(rose))
print("Is flower defined?", bool(rose))







# Задания для самостоятельного выполнения:
"""
1. Создайте класс Square с атрибутом side (сторона квадрата) 
и методом calculate_area, 
который вычисляет площадь квадрата по формуле: площадь = side^2.

2. Создайте класс Bicycle с атрибутами 
brand (бренд велосипеда), model (модель) и year (год выпуска). 
Добавьте метод get_age, который вычисляет возраст велосипеда 
как разницу между текущим годом и годом выпуска.
"""
