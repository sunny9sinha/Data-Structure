from LinkedList import Linked_List

class Queue:
    frst = None
    l_ast = None
    LL = None
    count = None

    def __init__(self):
        self.LL = Linked_List()
        self.frst = self.LL.get_first()
        self.l_ast = self.LL.get_Last()
        self.count = 0

    def enqueue(self,num):
        self.LL.insert_last(num)
        self.frst = self.LL.get_first()
        self.l_ast = self.LL.get_Last()
        self.count = self.count + 1

    def dequeue(self):
        if (self.frst == None):
            return None
        num = self.LL.removeFirst()
        self.frst = self.LL.get_first()
        self.count = self.count - 1
        return num
    
    def peek(self):
        return self.frst
    
    def isEmpty(self):
        return (self.frst == None)
    
    def print_Q(self):
        if (self.count<=0):
            return
        
        while(not self.isEmpty()):
            print(self.dequeue())

    def getCount(self):
        return self.count

