def sum(n1, n2=1):
    return n1 + n2

def outer_function():
    print("Hello I'm outer function")
    def innerFunction():
        print("Im inner function")
    innerFunction()

if __name__ == '__main__':
    print(sum(100,15))
    print(sum(100))
    outer_function()