# Encapsulation helps to expose behavior instead of state, in order to apply encapsulation we need to use private access modifer

class Person:
    def __init__(self, name, age):
        self.__name= name
        self.__age = age

    def show_details(self):
        print("Name :", self.__name)
        print("Age :", self.__age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


person = Person("Andres", 25)
person.show_details()

## In order to check the state of some field we can use getter and setter

print(person.get_name())
print(person.set_name("Felipe"))
print(person.get_name())
