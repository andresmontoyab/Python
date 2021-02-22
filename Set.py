def creating_set():
    first_set = {1,2,3,4,5,1,2,3,4,5}
    print(first_set)
    another_set = set([1,2,3,4,5,5,5,5,6])
    print(another_set)
    another_set.add("a")
    another_set.add("b")
    print(another_set)



if __name__ == '__main__':
    creating_set()