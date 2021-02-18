## Tuples is pretty similar to List with the small difference that is inmutable
def create_tuple():
    tuple=()
    print(tuple)
    another_tuple = (1,2,3,4,5,6,7)
    print(another_tuple)

def acces_tuple_item():
    another_tuple = (1, 2, 3, 4, 5, 6, 7)
    print(another_tuple[0])
    print(another_tuple[0:3])

def delete_tuple():
    another_tuple = (1, 2, 3, 4, 5, 6, 7)
    del another_tuple ## Entire delete the tuple
    print(tuple)

if __name__ == '__main__':
    create_tuple()
    acces_tuple_item()
    delete_tuple()