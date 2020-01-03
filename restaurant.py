# -*- coding: utf-8 -*-

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print ('Restaurant name ' + self.restaurant_name + ' and cuisine - ' + self.cuisine_type)

    def open_restaurant(self):
        print ("The restaurant is opened")


class Users():
    def __init__(self, user_name, user_sourname, gender, age):
        self.user_name = user_name
        self.user_sourname = user_sourname
        self.gender = gender
        self.age = age

    def describe_user(self, id):
        self.id = id
        print (self.user_name + ' has ' + str(self.id) + " ID")
        print ('User name: ' + self.user_name.title())
        print ('User sourname: ' + self.user_sourname.title())
        print ('User gender: ' + self.gender)
        print ('User age: ' + str(self.age))

    def greet_user(self):
        print ('Hello ' + self.user_name.title() + " " + self.user_sourname.title() + "!")

restaurant = Restaurant('Constantine', 'Belorussian national')
print restaurant.restaurant_name
print restaurant.cuisine_type
restaurant.describe_restaurant()
restaurant.open_restaurant()

rest1 = Restaurant('Restaurant1', 'Greek')
rest2 = Restaurant('Restaurant2', 'French')
rest3 = Restaurant('Restaurant3', 'England')
rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

albert = Users('albert', 'sivakov', 'male', 44)
lara = Users('lara', 'cage', 'female', 33)
albert.describe_user(id=5)
albert.greet_user()
lara.describe_user(id=6)
lara.greet_user()
