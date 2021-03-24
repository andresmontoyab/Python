# Queu follow FIFO first in first out.

from collections import deque
def using_queue():
    queue = deque(['Python', 'Java', 'React'])
    print(queue)
    queue.append('JS')
    print(queue)
    queue.popleft()
    print(queue)

if __name__ == '__main__':
    using_queue()