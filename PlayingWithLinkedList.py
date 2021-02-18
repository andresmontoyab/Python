class SinglyLinkedListNode:
     def __init__(self, data, next):
         self.data = data
         self.next = next

def printLinkedList(head, index):

    counter = 0
    node = 0
    while (head.data is not None and head.next is not None):
        node = head.data
        head = head.next

        if counter == index:

            return node
        counter += 1
    print(node)

if __name__ == '__main__':
    seven = SinglyLinkedListNode(7, None)
    four = SinglyLinkedListNode(4, seven)
    three = SinglyLinkedListNode(3, four)
    two = SinglyLinkedListNode(2, three)
    head = SinglyLinkedListNode(1, two)
    print(printLinkedList(head, 3))


x = 'el burro me la chupa'
print('-'.join(x.split()))
print(x.center(50,'*'))