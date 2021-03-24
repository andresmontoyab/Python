# Polymorpishm basically is the skill to have different forms
class Animal:
    def noise(self):
        raise NotImplementedError

class Cat(Animal):
    def noise(self):
        print("Meow")

class Dog(Animal):
    def noise(self):
        print("Woof")

cat = Cat()
cat.noise()

dog = Dog()
dog.noise()


