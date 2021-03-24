def sum(n1, n2=1):
    return n1 + n2

def outer_function():
    print("Hello I'm outer function")
    def innerFunction():
        print("Im inner function")
    innerFunction()

def function_docs(dict):
    """ This function return the name of a dict"""
    return dict['name']


def function_annotation(x: str, y: int) -> dict:
    pass


def default_parameters(x, y=100):
    print(x+y)


def keyword_asignment(name, last_name):
    print("The name is ", name)
    print("The last_name is ", last_name)


if __name__ == '__main__':
    print(sum(100,15))
    print(sum(100))
    outer_function()
    default_parameters(5)
    keyword_asignment(last_name="Montoya", name="Andres")
    help(function_docs)
    help(function_annotation)