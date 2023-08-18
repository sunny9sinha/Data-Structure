class PriorityQueue:
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
            return
        else:
            if (len(self.array) <= self.end +1):
                print("queue is full")
            else:
                self.end = self.end + 1
                j = self.end
                while(i<self.array[j-1]):
                    self.array[j] = self.array[j-1]
                    j = j - 1
                    if (j==0):
                        break
                self.array[j] = i
    
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
        return len(self.array) <= self.end-self.start+1
    

if __name__ == '__main__':
    pq = PriorityQueue(5)
    pq.enqueue(1)
    pq.enqueue(3)
    pq.enqueue(4)
    pq.enqueue(5)

    pq.enqueue(2)

    print("IS Queue Full? ", pq.isFull())

    print("IS Queue Empty? ", pq.isEmpty())
    print("Peeking: ", pq.peek())
    
    print(pq.dequeue())
    print(pq.dequeue())
    print("IS Queue Empty? ", pq.isEmpty())
    print("Peeking: ", pq.peek())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())

    print("IS Queue Empty? ", pq.isEmpty())
    print("Peeking: ", pq.peek())
    print("IS Queue Full? ", pq.isFull())

    pq.enqueue(6)
    print("Peeking: ", pq.peek())