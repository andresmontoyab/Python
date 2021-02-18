import random

def suffle_list():
    print("Shuffle Random")
    list = [1,2,3,4]
    print(list)
    random.shuffle(list, random.random)
    print(list)

def concatenate_list():
    print("Merging List")
    list=[1,2,3,4]
    list2= [4,5,6,7]
    result = list + list2
    print(result)

## The List type is a container that hold a number of other objecst in a given order, allow you to add or remove.
def createList():
    list = [] # Empty_list
    character_list = ['a','b', 'c','d',12]
    number_list = [1,2,3,4,5,6]
    print(character_list)
    print(number_list)
    print(number_list[3])
    print(number_list[3:5])

## Mutable List, Is a list that we can change
def mutable_list():
    print('Appending Data')
    list=[]
    print(list)
    list.append('Python')
    list.append('Java')
    list.append('React')
    print(list)
    print('Removing Data')
    list.remove('Java')
    print(list)

def check_if_exist():
    number_list = [1, 2, 3, 4, 5, 6]
    if 12 in number_list:
        print("Yes")
    else:
        print("No")

def iterate_list():
    print("Iterating List")
    number_list = [1, 2, 3, 4, 5, 6,7,8,9]
    for i in number_list:
        print(i)


def updating_list():
    list = ['React', 'Java', 'Python']
    print(list)
    list[1] = 'Node'
    print(list)
if __name__ == '__main__':
    createList()
    updating_list()
    mutable_list()
    check_if_exist()
    iterate_list()
    suffle_list()
    concatenate_list()