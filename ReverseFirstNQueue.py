## Reverse first n elements of a Queue
from Queue import Queue
from Stacks import stacks

def reverse(Q, n):
    stck = stacks()
    Q2 = Queue()
    if (n>Q.getCount()):
        print("Length of Queue is shorter than ", n)
        return Q
    for i in range(n):
        num = Q.dequeue()
        stck.push(num)

    while(not Q.isEmpty()):
        num = Q.dequeue()
        Q2.enqueue(num)

    while(not stck.isEmpty()):
        num = stck.pop()
        Q.enqueue(num)
    
    while(not Q2.isEmpty()):
        num = Q2.dequeue()
        Q.enqueue(num)

    return Q


if __name__ == '__main__':
    Q = Queue()
    for i in range(10):
        Q.enqueue(i)

    Q = reverse(Q,15)
    Q.print_Q()