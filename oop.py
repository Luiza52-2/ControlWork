from abc import ABC, abstractmethod
import math

# Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0  # Прячем возраст

    def set_age(self, age):
        if age < 0:
            print("Возраст не может быть отрицательным!")  # Предупреждаем друга
        else:
            self._age = age  # Устанавливаем возраст

    def get_age(self):
        return self._age  # Возвращаем возраст

# Наследование
class Animal:
    def __init__(self, name):
        self.name = name  # У всех есть имя

    def speak(self):
        return "Я животное"  # Говорим как животное

class Dog(Animal):
    def speak(self):
        return "Гав!"  # Собачий голос

class Cat(Animal):
    def speak(self):
        return "Мяу!"  # Кошачий голос

# Полиморфизм
class Vehicle:
    def move(self):
        return "Транспорт движется"

class Car(Vehicle):
    def move(self):
        return "Машина едет"

class Bicycle(Vehicle):
    def move(self):
        return "Велосипед едет"

def move(vehicle):
    return vehicle.move()

# Абстракция
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Только обещаем, что будет метод

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Считаем площадь прямоугольника

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # Считаем площадь круга

# Примеры использования
# Инкапсуляция
p = Person()
p.set_age(25)
print(f"Возраст: {p.get_age()}")  # Увидишь: 25
# p.set_age(-5)  # Просто скажем: "Возраст не может быть отрицательным!"

# Наследование
dog = Dog("Бим")
cat = Cat("Мурка")
print(f"{dog.name} говорит: {dog.speak()}")  # Бим говорит: Гав!
print(f"{cat.name} говорит: {cat.speak()}")  # Мурка говорит: Мяу!

# Полиморфизм
car = Car()
bike = Bicycle()
print(move(car))  # Машина едет
print(move(bike))  # Велосипед едет

# Абстракция
rect = Rectangle(10, 5)
circle = Circle(7)
print(f"Площадь прямоугольника: {rect.area()}")  # 50
print(f"Площадь круга: {round(circle.area(), 2)}")  # Округлённая: 153.94