from LinkedList import Linked_List

class Queue:
    frst = None
    l_ast = None
    LL = None

    def __init__(self):
        self.LL = Linked_List()
        self.frst = self.LL.get_first()
        self.l_ast = self.LL.get_Last()

    def enqueue(self,num):
        self.LL.insert_last(num)
        self.frst = self.LL.get_first()
        self.l_ast = self.LL.get_Last()

    def dequeue(self):
        if (self.frst == None):
            return None
        num = self.LL.removeFirst()
        self.frst = self.LL.get_first()
        return num
    
    def peek(self):
        return self.frst
    
    def isEmpty(self):
        return (self.frst == None)
    
    def print_Q(self):
        while(not self.isEmpty()):
            print(self.dequeue())


