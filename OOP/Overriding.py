## Method overring means that we have two methods with the exact same name, but different behaviour
class Car:
    def __init__(self, name):
        self.name = name

    def show_detail(self):
        print(self.name)

class SuperCar(Car):
    def __init__(self, name):
        self.name = name

    def show_detail(self):
        print("Another Show Details ", self.name)


car = Car("Normal Car")
super_car = SuperCar("SuperCar Car")
car.show_detail()
super_car.show_detail()