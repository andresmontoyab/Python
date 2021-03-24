class Father:
    def __init__(self, name):
        self.father_name = name

class Mother:
    def __init__(self, name):
        self.mother_name = name

class Son(Father, Mother):
    def __init__(self, father_name, mother_name):
        Father.__init__(self,father_name)
        Mother.__init__(self,mother_name)

son = Son("Father Name 2000", "Mother Name 4000")
print(son.father_name)
print(son.mother_name)