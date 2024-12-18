# ИТЕРАТОРЫ_______________________________
# Итераторы позволяют удобно проходить по коллекциям (спискам, словарям)
# без необходимости вручную управлять индексами.



# Пример: итератор с использованием for
colors = ["красный", "синий", "зеленый"]  # Это наш список (итерабельный объект)

# Итератор позволяет пройти по каждому элементу списка
for i in colors:
    print(i)


"""
Задание:
Создайте список с именами своих друзей. 
Напишите итератор, который будет поочередно выводить каждое имя из списка.
"""




# Пример: создание итератора в классе
class ColorIterator:
    def __init__(self, colors):
        self.colors = colors  # Наш список
        self.index = 0  # Индекс для отслеживания, какой элемент мы выводим

    def __iter__(self):
        return self  # Возвращаем сам объект для итерации

    def __next__(self):
        if self.index >= len(self.colors):
            raise StopIteration  # Останавливаем итерацию, если элементы закончились
        color = self.colors[self.index]
        self.index += 1
        return color

# Создаем объект итератора с нашим списком
color_iter = ColorIterator(["красный", "синий", "зеленый"])

# Используем итератор в цикле
for color in color_iter:
    print(color)









# ГЕНЕРАТОРЫ_______________________________
# Генераторы создают данные "по запросу" (не хранят их все сразу)


# Пример: генератор, который создает числа по одному
def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count  # Возвращаем число и "запоминаем" место, где остановились
        count += 1

# Используем генератор для вывода чисел от 1 до 3
for number in count_up_to(3):
    print(number)


"""
Задание:
Напишите генератор, который будет выводить числа от 1 до 5, 
по одному числу за раз.
"""






# Пример: генератор в классе
class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate(self):
        count = self.start
        while count <= self.end:
            yield count  # Генератор по аналогии с предыдущим примером
            count += 1

# Создаем объект генератора
counter = Counter(1, 3)

# Используем генератор для вывода чисел от 1 до 3
for number in counter.generate():
    print(number)







# ЗАМЫКАНИЯ_______________________________
# Замыкания позволяют запоминать значения,
# которые могут быть использованы позже, даже после выхода из функции.


# Пример замыкания: функция, которая запоминает значение
def outer(x):
    def inner(y):
        return x + y  # Функция inner "помнит" x, даже после выхода из outer
    return inner

# Создаем замыкание, где x = 5
add_five = outer(5)

# Используем замыкание
print(add_five(3))  # Выведет 8, потому что x + y = 5 + 3


"""
Задание:
Напишите функцию, которая принимает число 
и возвращает другую функцию, которая будет прибавлять 
это число к любому другому числу.
"""


# Пример: замыкание в классе
class Adder:
    def __init__(self, x):
        self.x = x

    def add(self):
        def inner(y):
            return self.x + y  # "Помнит" значение self.x
        return inner

# Создаем объект Adder
adder = Adder(5)

# Используем замыкание для сложения
add_five = adder.add()
print(add_five(3))  # Выведет 8, потому что x + y = 5 + 3




# ДЕКОРАТОРЫ_______________________________
# Декораторы добавляют дополнительные действия перед или после выполнения функции.


# Пример простого декоратора
def decorator(func):
    def wrapper(name):
        print("Привет, как ты?")
        func(name)  # Вызываем исходную функцию
    return wrapper

# Применяем декоратор к функции
@decorator
def say_hello(name):
    print(f"Привет, {name}!")

# Вызовем декорированную функцию
say_hello("Аня")



"""
Задание:
Создайте декоратор, который будет выводить "Функция выполняется..." 
перед тем, как будет вызвана любая функция.
"""



# Пример декоратора в классе
class Greeter:
    def greet(self, name):
        print(f"Привет, {name}!")

    def greeting_decorator(self, func):
        def wrapper(name):
            print("Привет, как ты?")
            func(name)
        return wrapper

# Создаем объект Greeter
greeter = Greeter()

# Применяем декоратор к методу greet
greeter.greet = greeter.greeting_decorator(greeter.greet)

# Вызовем декорированную функцию
greeter.greet("Аня")
