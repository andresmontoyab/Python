def creating_set():
    first_set = {1,2,3,4,5,1,2,3,4,5}
    print(first_set)
    another_set = set([1,2,3,4,5,5,5,5,6])
    print(another_set)
    another_set.add("a")
    another_set.add("b")
    print(another_set)


def set_union():
    print("Set Unions")
    numbers_one = {1, 2, 3, 4, 5}
    numbers_two = {4, 5, 6, 7, 8, 9}
    result = numbers_one.union(numbers_two)
    print(result)


def set_intersection():
    print("Set Intersection")
    numbers_one = {1, 2, 3, 4, 5}
    numbers_two = {4, 5, 6, 7, 8, 9}
    result = numbers_one.intersection(numbers_two)
    print(result)


if __name__ == '__main__':
    creating_set()
    set_union()
    set_intersection()