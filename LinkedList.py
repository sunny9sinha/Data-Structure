class Node:
    value =None
    next = None

    def __init__(self,val=None,nxt=None):
        self.value = val
        self.next = nxt
    
    def set_value(self,val=None):
        self.value = val

    def set_next(self,nxt=None):
        self.next = nxt

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next


class Linked_List:
    First = None
    Last = None

    def __init__(self):
        self.First = Node()
        self.Last = Node()

    def get_Last(self):
        return self.Last.get_value()
    
    def get_first(self):
        return self.First.get_value()

    def insert_last(self,val):
        nw_node = Node(val=val)
        self.Last.set_next(nw_node)
        if (self.First.get_value()==None and self.Last.get_value()==None):
            self.First = nw_node
            self.Last = nw_node
        else:
            self.Last = nw_node

    def insert_first(self,val):
        nw_node = Node(val=val)
        nw_node.set_next(self.First)
        if (self.Last.get_value()==None and self.First.get_value()==None):
            self.First = nw_node
            self.Last = nw_node
        else:
            self.First = nw_node
    
    def indexOf(self,val):
        index = -1
        found = False
        trvlr = self.First
        while(trvlr!=None):
            if(trvlr.get_value()==val):
                index = index+1
                found = True
                break;
            index = index+1
            trvlr = trvlr.get_next()
        
        if(found):
            return index
        else:
            return 'Not Found'
        
    def contains(self,val):
        found = False
        trvlr = self.First
        while(trvlr!=None):
            if(trvlr.get_value()==val):
                found=True
                break;
            trvlr = trvlr.get_next()
        return found
    
    def removeFirst(self):
        val = self.First.get_value()
        if ((self.First.get_value() == self.Last.get_value()) and (self.First.get_next() == self.Last.get_next())):
            self.First = Node()
            self.Last = Node()
        else:
            self.First = self.First.get_next()
        return val

    def removeLast(self):
        val = self.Last.get_value()
        if (self.First.get_value() == self.Last.get_value() and (self.First.get_next() == self.Last.get_next())):
            self.First = Node()
            self.Last = Node()
        else:
            trvlr = self.First
            p_trvlr = trvlr
            while(trvlr.get_next()!=None):
                p_trvlr = trvlr
                trvlr = trvlr.get_next()
            self.Last = p_trvlr
            self.Last.set_next(None)
            trvlr = None
        return val
    
    def size(self):
        siz = 0
        trvlr = self.First
        while(trvlr!=None):
            siz = siz + 1
            trvlr = trvlr.get_next()
        return siz
    
    def to_array(self):
        ar = []
        trvlr = self.First
        while(trvlr!=None):
            ar.append(trvlr.get_value())
            trvlr = trvlr.get_next()
        return ar

    def reverse(self):
        trvlr_1 = self.First
        trvlr_2 = self.First.get_next()
        dummy = None
        while(trvlr_2!=None):
            trvlr_1.set_next(dummy)
            dummy = trvlr_2.get_next()
            trvlr_2.set_next(trvlr_1)
            trvlr_1 = dummy
            dummy = trvlr_2
            if (trvlr_1==None):
                break
            trvlr_2 = trvlr_1.get_next()
        if (trvlr_1!=None):
            trvlr_1.set_next(dummy)
        dummy = self.First
        self.First = self.Last
        self.Last = dummy

    def reverse_(self):
        if (self.size()<=0):
            return
        prev = self.First
        current = self.First.get_next()
        while(current!=None):
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.Last =self.First
        self.Last.set_next(None)
        self.First = prev
            

    def k_frm_Last(self,k):
        if (k>self.size()-1):
            return None
        pos = self.size() - k
        dummy = self.First
        for i in range(pos):
            dummy = dummy.get_next()
        print(k,'th Node from Last: ', dummy.get_value())

    def kth_frm_last(self,k):
        if (self.First==None):
            print("No nodes")
        else:
            frst = self.First
            scnd = self.First
            count = k-1
            for i in range(count):
                frst = frst.get_next()
                if(frst==None):
                    print("K is greater than size")
                    return
            
            while(frst!=None):
                frst = frst.get_next()
                scnd = scnd.get_next()
            
            print(k,"th node from Last: ",scnd.get_value())

    def find_middle(self):
        first = self.First
        second = self.First
        sz = 0
        while(first.get_next()!=None):
            if (sz%2 == 0):
                first = first.get_next()
            else:
                first = first.get_next()
                second = second.get_next()
            sz = sz + 1
        
        if (sz%2==0):
            print("Middle of the list is : ", second.get_value())
        else:
            print("Middle of the list is: ",second.get_value(), " and: ", second.get_next().get_value())

    def find_circle(self):
        first = self.First
        second = self.First

        while(second!=None and second.get_next()!=None):
            first = first.get_next()
            second = second.get_next().get_next()
            if(first == second):
                print("Loop found: ",first.get_next().get_value())
                return
        print("Loop not found")
        return

    def create_loop(self):
        self.Last.set_next(self.First.get_next())

    def print_List(self):
        trvlr = self.First
        while(trvlr!=None):
            print(trvlr.get_value())
            trvlr = trvlr.get_next()
        
    
# if __name__=="__main__":
#     LL = Linked_List()
#     LL.insert_last(1)
#     LL.insert_last(2)
#     LL.insert_last(3)
#     LL.insert_first(0)
#     LL.insert_first(-1)
#     LL.insert_first(-2)
#     LL.insert_first(-3)
#     # LL.print_List()
#     LL.create_loop()
#     LL.find_circle()
    # LL.find_middle()
    # LL.kth_frm_last(4)
    # print('Index of 3: ', LL.indexOf(3))
    # print('Index of -1: ', LL.indexOf(-1))
    # print('Index of 7: ', LL.indexOf(7))
    # print('Contains 3: ', LL.contains(3))
    # print('Contains -1: ', LL.contains(-1))
    # print('Contains 7: ', LL.contains(7))
    # print('Removing First: ', LL.removeFirst())
    # print('Removing First: ', LL.removeFirst())
    # LL.print_List()
    # print('Removing Last: ', LL.removeLast())
    # print('Removing Last: ', LL.removeLast())
    # LL.print_List()
    # print('Size of Linked List: ', LL.size())
    # print('Linked List to Array: ', LL.to_array())
    # LL.reverse_()
    # print('Linked List Reversed: ')
    # LL.print_List()

