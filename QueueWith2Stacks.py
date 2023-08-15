from Stacks import stacks

class Q_2Stacks:
    stck_1 = None
    stck_2 = None

    def __init__(self):
        self.stck_1 = stacks()
        self.stck_2 = stacks()

    def enqueue(self, i):
        self.stck_1.push(i)

    def dequeue(self):
        if (self.isEmpty()):
            return None
        if (self.stck_2.isEmpty()):
            while(not self.stck_1.isEmpty()):
                num = self.stck_1.pop()
                self.stck_2.push(num)
        numb = self.stck_2.pop()
        return numb
    
    def peek(self):
        if (self.isEmpty()):
            return None
        if (self.stck_2.isEmpty()):
            while(not self.stck_1.isEmpty()):
                num = self.stck_1.pop()
                self.stck_2.push(num)
        return self.stck_2.peek()
    
    def isEmpty(self):
        if (self.stck_1.isEmpty() and self.stck_2.isEmpty()):
            return True
        return False
    
if __name__ == '__main__':
    Q = Q_2Stacks()
    for i in range(5):
        Q.enqueue(i)

    print("Is queue empty? ", Q.isEmpty())
    print('Peeking: ', Q.peek())

    while (not Q.isEmpty()):
        print(Q.dequeue())

    print(Q.dequeue())


