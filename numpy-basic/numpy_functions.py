import numpy

def sum():
    print("Numpy Sum Start -------")
    array = numpy.array([ [1, 2], [10, 11] ])
    print(numpy.sum(array, axis=0))
    print(numpy.sum(array, axis=1))
    print(numpy.sum(array))
    print("Numpy Sum End -------")


def prod():
    print("Numpy Prod Start -------")
    array = numpy.array([ [1, 2], [10, 11] ])
    print(numpy.prod(array, axis=0))
    print(numpy.prod(array, axis=1))
    print(numpy.prod(array))
    print("Numpy Prod End -------")

def min():
    print("Numpy Min Start -------")
    array = numpy.array([[1, 2], [10, 11]])
    print(numpy.min(array, axis=0))
    print(numpy.min(array, axis=1))
    print(numpy.min(array))
    print("Numpy Min End -------")

def max():
    print("Numpy Max Start -------")
    array = numpy.array([[1, 2], [10, 11]])
    print(numpy.max(array, axis=0))
    print(numpy.max(array, axis=1))
    print(numpy.max(array))
    print("Numpy Max End -------")


if __name__ == '__main__':
    sum()
    prod()
    min()
    max()