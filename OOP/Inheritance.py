# Inheritance is when a class use a code within another class.
class Parent:
    parent_name = "Parent Class"


class Child(Parent):
    child_name = "Im the new child"
    def show_child(self):
        print(self.parent_name)

child = Child()
print(child.parent_name)

class Baby(Child):
    baby_name = "Im the baby"

baby = Baby()
print(baby.baby_name)
print(baby.parent_name)
print(baby.child_name)