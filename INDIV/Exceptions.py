# Попытка поделить на 0
a = 10
b = 0
print(a / b)  # Ошибка! Делить на 0 нельзя


"""
Задание: Сложение строки и числа
Попробуй сложить строку и число, например: "Hello" + 5. Что произойдёт? Объясни, почему это ошибка.
"""


# Пример обработки ошибки
try:
    a = 10
    b = 0
    print(a / b)  # Попытка поделить на 0
except ZeroDivisionError:
    print("Ошибка! Делить на 0 нельзя.")  # Если ошибка, выводим сообщение



"""
Задание: Проверка на ноль
Напиши программу, которая делит два числа. Если знаменатель равен 0, 
программа должна вывести сообщение "Ошибка: деление на ноль!". 
В других случаях она должна вывести результат деления.
"""



class Divider:
    # Конструктор, где создаем два числа
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # Числитель
        self.denominator = denominator  # Знаменатель

    # Метод для деления
    def divide(self):
        try:
            # Пытаемся разделить
            result = self.numerator / self.denominator
            return result  # Возвращаем результат
        except ZeroDivisionError:
            # Если деление на 0, возвращаем сообщение
            return "Ошибка! Делить на 0 нельзя."

# Пример использования:
divider = Divider(10, 0)  # Создаем объект с числом 0 в знаменателе
print(divider.divide())  # Выводит: Ошибка! Делить на 0 нельзя.

divider = Divider(10, 2)  # Создаем объект с числом 2 в знаменателе
print(divider.divide())  # Выводит: 5.0



"""
Задание: Создание класса с обработкой ошибок
Создай класс Rectangle, который принимает длину и ширину. 
Реализуй метод для вычисления площади прямоугольника. 
Если одна из сторон равна 0 или меньше, программа должна 
вывести ошибку "Длина и ширина должны быть больше нуля".
"""






# Создаем свою ошибку
class LargeNumberError(Exception):
    pass  # Наша ошибка не делает ничего особенного, просто наследуется от Exception

class Divider:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def divide(self):
        # Проверяем, если числитель слишком большой
        if self.numerator > 1000:
            raise LargeNumberError("Число слишком большое!")  # Выбрасываем ошибку
        try:
            result = self.numerator / self.denominator
            return result
        except ZeroDivisionError:
            return "Ошибка! Делить на 0 нельзя."

# Пример использования:
divider = Divider(2000, 2)  # Число больше 1000
try:
    print(divider.divide())  # Ошибка! Число слишком большое!
except LargeNumberError as e:
    print(e)  # Выведет: Число слишком большое!


"""
Задание: Проверка отрицательных значений
Создай свою ошибку NegativeValueError, которая будет выбрасываться, 
если передано отрицательное значение. 
В классе Rectangle добавь проверку, чтобы выбросить эту ошибку, если одна из сторон отрицательная.
"""







class Divider:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def divide(self):
        try:
            if self.denominator == 0:
                raise ZeroDivisionError("Нельзя делить на 0!")  # Исключение для деления на 0
            result = self.numerator / self.denominator
            return result
        except ZeroDivisionError as e:
            return str(e)  # Выводим ошибку
        except Exception as e:
            return f"Произошла ошибка: {e}"  # Ловим все другие ошибки

# Пример использования:
divider = Divider(10, 0)  # Деление на 0
print(divider.divide())  # Выведет: Нельзя делить на 0!

divider = Divider(10, "три")  # Ошибка, потому что второй аргумент — строка
print(divider.divide())  # Выведет: Произошла ошибка: unsupported operand type(s) for /: 'int' and 'str'




"""
Задание: Обработка разных типов ошибок
Напиши программу, которая пытается разделить два числа и обработать ошибки:
Ошибка деления на ноль.
Ошибка, если одно из чисел не является числом.

"""