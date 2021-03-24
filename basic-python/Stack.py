# If you want to use Stack, we can use a list
# Stack follow the LIFO
# Push -> Adding item to the stack -> In Python is the same as append
# Pop -> Remove item from the stack -> Retrieve the last element
def using_stack():
    stack = ['Python', 'Java', 'Php']
    print(stack)
    stack.append('React')
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)

if __name__ == '__main__':
    using_stack()