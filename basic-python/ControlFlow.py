def if_statement():
    print("PLaying with basic if statement")
    age = 20
    if age > 18:
        print("You're adult")

def if_and_else():
    print("PLaying with if  and else statement")
    age = 10
    if (age > 18):
        print("You're adult")
    else:
        print("You're not adult")

def el_if_condition():
    print("PLaying with if  and elif statement")
    age = 10
    if age > 18:
        print("You're adult")
    elif age < 12:
        print("You're just a child")
    else:
        print("You're a young boy")

def for_loop():
    print("PLaying with for loop")
    programming_lenguage = "Java", "Python", "React"
    for P in programming_lenguage:
        print (P)

def for_range():
    print("PLaying with for range")
    for v in range(1,7):
        print(v)

def while_loop():
    print("PLaying with while loop")
    x = 0
    while(x<5):
        print(x)
        x+=1

def for_with_else():
    for a in range(5):
        print(a)
    else :
        print("The for is completed")

def break_continue_pass():
    print("Playing with break, continue and pass")
    print("break")
    for char in "Python3":
        if (char == "o"):
            break
        print("Character", char)

    print("Continue")
    for char in "Python3":
        if (char == "o"):
            continue
        print("Character", char)

    print("Pass")
    for char in "Python3":
        if (char == "o"):
            pass
        print("Character", char)



if __name__ == '__main__':
    if_statement()
    if_and_else()
    el_if_condition()
    for_loop()
    for_range()
    while_loop()
    break_continue_pass()
    for_with_else()