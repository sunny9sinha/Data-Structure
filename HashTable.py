class Node:
    key = None
    value =None
    next = None

    def __init__(self,val=None,nxt=None,key=None):
        self.value = val
        self.next = nxt
        self.key = key
    
    def set_value(self,val=None):
        self.value = val

    def set_key(self,key=None):
        self.key = key

    def set_next(self,nxt=None):
        self.next = nxt

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def get_key(self):
        return self.key


class Linked_List:
    First = None
    Last = None

    def __init__(self):
        self.First = Node()
        self.Last = Node()

    def get_Last(self):
        return (self.Last)
    
    def get_first(self):
        return (self.First)

    def insert_last(self,key,val):
        nw_node = Node(val=val,key=key)
        self.Last.set_next(nw_node)
        if (self.First.get_value()==None and self.Last.get_value()==None):
            self.First = nw_node
            self.Last = nw_node
        else:
            self.Last = nw_node

    def insert_first(self,key,val):
        nw_node = Node(val=val,key=key)
        nw_node.set_next(self.First)
        if (self.Last.get_value()==None and self.First.get_value()==None):
            self.First = nw_node
            self.Last = nw_node
        else:
            self.First = nw_node
    
    def indexOf(self,key,val):
        index = -1
        found = False
        trvlr = self.First
        while(trvlr!=None):
            if(trvlr.get_value()==val and trvlr.get_key()==key):
                index = index+1
                found = True
                break;
            index = index+1
            trvlr = trvlr.get_next()
        
        if(found):
            return index
        else:
            return 'Not Found'
        
    def contains(self,key):
        found = False
        trvlr = self.First
        while(trvlr!=None):
            if(trvlr.get_key()==key):
                found=True
                break;
            trvlr = trvlr.get_next()
        return found
    
    def removeFirst(self):
        val = self.First.get_value()
        key = self.First.get_key()
        if ((self.First.get_key() == self.Last.get_key()) and (self.First.get_next() == self.Last.get_next())):
            self.First = Node()
            self.Last = Node()
        else:
            self.First = self.First.get_next()
        return (key,val)

    def removeLast(self):
        val = self.Last.get_value()
        key = self.Last.get_key()
        if (self.First.get_key() == self.Last.get_key() and (self.First.get_next() == self.Last.get_next())):
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
        return (key,val)
    
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
            ar.append((trvlr.get_key(),trvlr.get_value()))
            trvlr = trvlr.get_next()
        return ar

    def print_List(self):
        trvlr = self.First
        while(trvlr!=None):
            print(trvlr.get_key(), trvlr.get_value())
            trvlr = trvlr.get_next()
    
    def removeKey(self,k):
        trvlr1 = self.First
        trvlr2 = self.First
        if (self.contains(k)):
            if (trvlr1.get_key()==k):
                self.First = trvlr1.get_next()
            else:
                trvlr1 = trvlr1.get_next()
                while(trvlr1!=None):
                    if(trvlr1.get_key()==k):
                        trvlr2.set_next(trvlr1.get_next())
                        return
                    trvlr1 = trvlr1.get_next()
                    trvlr2 = trvlr2.get_next()
        else:
            print('Does not contain key: ',k)

    
class HashTable:
    HashNode =None
    sz = None

    def __init__(self, sz):
        self.HashNode = [None]*sz
        self.sz = sz

    def hashFunction(self, i):
        return i%self.sz

    def contains(self,k):
        h_index = self.hashFunction(k)
        if (self.HashNode[h_index]!=None):
            return True
        else:
            return False
        

    def put(self,k,v):
        h_index = self.hashFunction(k)
        if (self.HashNode[h_index] == None):
            self.HashNode[h_index] = Linked_List()
        elif (self.contains(k)):
            trvlr = self.HashNode[h_index].get_first()
            while(trvlr!=None):
                if (trvlr.get_key()==k):
                    trvlr.set_value(v)
                    return
                trvlr = trvlr.get_next()
        
        self.HashNode[h_index].insert_last(k,v)

    
    def get(self,k):
        h_index =self.hashFunction(k)
        if (self.contains(k)):
            print("Index = ",h_index)
            trvlr = self.HashNode[h_index].get_first()
            while(trvlr!=None):
                if (trvlr.get_key()==k):
                    print('Value at key :',k, ' is ',trvlr.get_value())
                    break
                trvlr = trvlr.get_next()
        else:
            print("Does not exist.")

    def remove(self,k):
        h_index = self.hashFunction(k)
        if (self.contains(k)):
            self.HashNode[h_index].removeKey(k)
        else:
            print('Does not contain k: ',k)

    

if __name__ == '__main__':
    hash = HashTable(5)
    hash.put(0,'Raj')
    hash.put(1,'Vikram')
    hash.put(2, 'Mohan')
    hash.put(3,'Sohan')
    hash.put(4, 'Tinu')
    hash.put(5, 'Tipu')
    hash.put(6, 'Rahul')

    for i in range(7):
        hash.get(i)

    hash.remove(3)

    for i in range(7):
        hash.get(i)
