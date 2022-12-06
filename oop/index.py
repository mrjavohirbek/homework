# Class
# Nasledovanie
# Inkapsulyasiya - public, protected, private
# Polimorphism

class Cat:
    def __init__(self, name, age):   # Class constructor
        self.name = name  # Class atributes & Dynamic area
        self.age = age    # Class atributes & Dynamic area

    def sound(self):  # Class function & Class method
        return "meow - meow"

    def info(self):
        return f"Cat name: {self.name} age: {self.age}"


cat1 = Cat('Felix', 2)  # Class example

# print(cat1.sound(), cat1.info())


class Car:
    def __init__(self, brand, model, year, type_of, odometr, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.type_of = type_of
        self.odometr = odometr
        self.color = color
        self.is_going = False

    # стартовать машину
    def car_is_going(self, km):
        self.is_going = True
        self.odometr += km

    def info(self):
        return f"Бренд: {self.brand} Модель: {self.model}\nSpeed:{self.odometr} | Машина дивижение делает: {self.is_going}"

    def update_model(self, new_model):
        self.model = new_model


toyota = Car('Toyota', 'camry', 2015, 'sedan', 0, 'grey')
jeep = Car('Jeep', 'Grand Cherokee', 2012, 'внедорожник', 0, 'black')

# print(toyota.info())
# print(toyota.update_model("Mandarin"))
# print(toyota.info())

# print(toyota.car_is_going(60))
# print(jeep.car_is_going(130))
# print(jeep.info())


class Animal:
    def __init__(self, name, age, color='black'):  # конструктор класса
        self.name = name  # атрибуты класса & динамические поля
        self.age = age  # атрибуты класса & динамические поля
        self.color = color

    def update_name(self, new_name):
        self.name = new_name

    def info(self):
        return f"имя:{self.name} возраст: {self.age}\nЦвет: {self.color}"


class Cat(Animal):
    def sound(self):  # функция класса & метод класса
        return "mauv-mauv"


class Dog(Animal):
    def sound(self):  # функция класса & метод класса
        return "gav gav"


cat1 = Cat('Felix', 2)  # экземпляр класса
cat2 = Cat('Bagira', 1)  # экземпляр класса

dog1 = Dog('Taigan', 2)  # экземпляр класса
dog2 = Dog('Jolbors', -1, 'оранжево-черный')  # экземпляр класса

cat1.update_name('fenix')
print(cat1.sound(), cat1.info())
print(dog2.sound(), dog2.info())
