class ArrayQueue:
    array = None
    start = None
    end = None

    def __init__(self, num):
        self.array = [0]*num
        
    def enqueue(self, i):
        if (self.end == None):
            self.end = 0
            self.start = 0
            self.array[self.end] = i
        else:
            if (len(self.array) <= self.end +1):
                print("queue is full")
            else:
                self.end = self.end + 1
                self.array[self.end] = i
    
    def dequeue(self):
        if (self.start == None):
            print("queue is empty")
            return None
        else:
            num = self.array[self.start]
            self.start = self.start + 1
            if (self.start == self.end+1):
                self.start = None
                self.end = None
            return num
    
    def peek(self):
        if (self.start==None or self.start==self.end+1):
            return None
        
        return self.array[self.start]
    
    def isEmpty(self):
        return self.end == None
    
    def isFull(self):
        if (self.end == None):
            return False
        return len(self.array) <= self.end+1
    
if __name__ == '__main__':
    AQ = ArrayQueue(4)
    AQ.enqueue(1)
    AQ.enqueue(2)
    AQ.enqueue(3)
    AQ.enqueue(4)

    AQ.enqueue(5)

    print("IS Queue Full? ", AQ.isFull())

    print("IS Queue Empty? ", AQ.isEmpty())
    print("Peeking: ", AQ.peek())
    
    print(AQ.dequeue())
    print(AQ.dequeue())
    print("IS Queue Empty? ", AQ.isEmpty())
    print("Peeking: ", AQ.peek())
    print(AQ.dequeue())
    print(AQ.dequeue())

    print("IS Queue Empty? ", AQ.isEmpty())
    print("Peeking: ", AQ.peek())
    print("IS Queue Full? ", AQ.isFull())

    AQ.enqueue(6)
    print("Peeking: ", AQ.peek())
    




        
