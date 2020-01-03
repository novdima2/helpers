# -*- coding: utf-8 -*-

class Dogs():

    def __init__(self, name, age):
        # Инициализация атрибутов 'name' и 'age'
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.upper() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " is rolling over")


my_fdog = Dogs('ferry', 10)
your_dog = Dogs('perry', 12)

print(my_fdog.name.upper() + " is " + str(my_fdog.age) + " age")
my_fdog.sit()
my_fdog.roll_over()

print(your_dog.name.upper() + " is " + str(your_dog.age) + " age")
your_dog.sit()
your_dog.roll_over()
