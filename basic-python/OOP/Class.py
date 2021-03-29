# Class is a way to group state and behaviour.
# So In this way only we want to use those state or behaviour we can create a instance of the class.

class car:
    model=2020
    name="Ford"

print("-------- Creating a basic Object ------------")
c = car()
print(c.model)
print(c.name)

# Every class mut have a constructur, the constructor is a function that is called when we want to build and object
# the constructor is named __init__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("-------- Creating a basic Object with init------------")
person = Person("Andres", 25)
print(person.name)
print(person.age)

## Self represent the instance of the class,

## Delete Object and property
class Motorcycle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return 'Motorcycle: ' \
               'Brand : {} ' \
               'Color: {}'.format(self.brand, self.color)

    def __str__(self):
        return 'Motorcycle Str: ' \
               'Brand : {} ' \
               'Color: {}'.format(self.brand, self.color)

    def print(self):
        print(self.brand)
        print(self.color)
print("-------- Deleting Object and Properties------------")
moto_one = Motorcycle("Suzuki", "Red")
moto_two = Motorcycle("Honda", "Blue")
print("Deleting Property")
moto_one.print()
print(moto_one)
#del moto_one.color
#moto_one.print()

print(bool(None))
print(bool(moto_one))
