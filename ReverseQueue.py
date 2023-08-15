from Queue import Queue
from Stacks import stacks

def reverse(Q):
    stck = stacks()
    while(not Q.isEmpty()):
        num = Q.dequeue()
        stck.push(num)
    
    while(not stck.isEmpty()):
        num = stck.pop()
        Q.enqueue(num)

    return Q


if __name__ == '__main__':
    Q = Queue()
    for i in range(10):
        Q.enqueue(i)

    Q = reverse(Q)
    Q.print_Q()