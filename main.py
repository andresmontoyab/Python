# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    print(f'Hi, {name}', end= " ")  # Press Ctrl+F8 to toggle the breakpoint.

def playing_with_variables():
    print('##### -Variables ######')
    ## integer -> Are used to define numeric values
    ## long_integer -> Are used to define values with a bigger value than a intenger
    ## float -> Are used to defining decimal values
    ## String -> Define characters
    an_integer = 10
    an_float= 2.1
    an_string = 'Name'
    print(an_string)
    print(an_integer)
    print(an_float )
    print(an_string, an_float, an_integer)

def local_scope():
    ## A local variable is define inside a funtion block
    var1 = "Python"
    print(var1)
    print(var2)


def variable_scopes():
    local_scope()

# Press the green button in the gutter to run the script.

var2 = "Another Python"


if __name__ == '__main__':
##    print_hi('PyCharm')
    playing_with_variables()
    variable_scopes()

