# Exceptions, exceptions are situations that happens and we need to deal with that.

#ValueError, IndezxError, Keyerror, ZeroDivisionError some common exceptions
def playing_try_block():
    try:
        text = input("Enter a value or something you like")
    except EOFError:
        print("EOF error")
    except KeyboardInterrupt:
        print("You cancelled the operations")
    else:
        print("You entered" , format(text))


def raising_exceptions():
    letter = "python"
    if not type(letter) is int:
        raise TypeError("Please enter only integers")

def try_with_finally():
    try:
        print("This is the try")
    except:
        print("This is the catch")
    finally:
        print("Finally is here")

if __name__ == '__main__':
    playing_try_block()
    try_with_finally()
    raising_exceptions()
