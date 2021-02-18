def positive_index():
    name = "Andres"
    print(name[2])
    print(name[2:5])

def negative_index():
    name = "Andrés"
    print(name[-2])
    print(name[-4:-2])

def slice_example():
    str = "Hello world"
    slice_one = slice(3)
    slice_two = slice(1,3,2)
    print(str[slice_one])
    print(str[slice_two])


def input_strng():
    print("Enter the value")
    value = input()
    print (value)



if __name__ == '__main__':
    positive_index()
    negative_index()
    slice_example()
    input_strng()