class D_stack_array:
    array = None
    top_1 =None
    top_2 =None
    cur_1 =None
    cur_2 =None
    sz_1 =None
    sz_2 =None
    def __init__(self,k,m):
        self.sz_1 = k
        self.sz_2 = m
        self.array = [0]*(k+m)
    
    def push_1(self, i):
        if (self.top_1 == None):
            self.array[0] = i
            self.top_1 = i
            self.cur_1 = 0
        else:
            if (self.cur_1 == self.sz_1 -1):
                print("Stack 1 is full.")
                return
            self.cur_1 = self.cur_1+1
            self.array[self.cur_1] = i
            self.top_1 = i

    def push_2(self, i):
        if (self.top_2 == None):
            self.array[self.sz_1] = i
            self.top_2 = i
            self.cur_2 = self.sz_1
        else:
            if (self.cur_2 == (self.sz_1 + self.sz_2 -1)):
                print("Stack 2 if full.")
                return
            self.cur_2 = self.cur_2 + 1
            self.array[self.cur_2] = i
            self.top_2 = i

    def pop_1(self):
        if(self.cur_1==None or self.cur_1<0):
            print("Stack 1 is empty.")
            return
        else:
            elem = self.array[self.cur_1]
            self.array[self.cur_1] = 0
            self.cur_1 = self.cur_1 - 1
            self.top_1 = self.array[self.cur_1]
            return elem
        
    def pop_2(self):
        if(self.cur_2==None or self.cur_2<self.sz_1):
            print("Stack 2 is empty.")
            return
        else: 
            elem = self.array[self.cur_2]
            self.array[self.cur_2] = 0
            self.cur_2 = self.cur_2 - 1
            self.top_2 = self.array[self.cur_2]
            return elem
        
    def peak_1(self):
        return self.top_1
    
    def peak_2(self):
        return self.top_2
    
if __name__ == '__main__':
    newstack = D_stack_array(4,2)
    newstack.push_1(1)
    newstack.push_1(2)
    newstack.push_1(3)
    newstack.push_1(4)
    newstack.push_2(5)
    newstack.push_2(6)

    print("popping stack 1: ")
    print(newstack.pop_1())
    print(newstack.pop_1())
    print(newstack.pop_1())
    print(newstack.pop_1())
    print("Popping Stack 2: ")
    print(newstack.pop_2())
    print(newstack.pop_2())



