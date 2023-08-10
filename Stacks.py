from LinkedList import Linked_List

class stacks:
    LL = None
    top = None

    def __init__(self):
        self.LL = Linked_List()
        self.top = self.LL.get_first()
    
    def push(self,num):
        self.LL.insert_first(num)
        self.top = self.LL.get_first()

    def pop(self):
        elem = self.LL.removeFirst()
        self.top = self.LL.get_first()
        return elem
    
    def peek(self):
        return self.top
    
    def isEmpty(self):
        if(self.top == None):
            return True
        else:
            return False

# if __name__ == "__main__" :
#     sent = input("Write the sentence: ")
#     stck = stacks()
#     for s in sent:
#         stck.push(s)
    
#     print("Sentence in reverse: ")
#     rvrse_sent =""
#     while(not stck.isEmpty()):
#         rvrse_sent = rvrse_sent + stck.pop()
    
#     print(rvrse_sent)

if __name__ == '__main__':
    exp = input("Please enter the expression: ")
    stack_1 = stacks()
    stack_2 = stacks()
    operands = stacks()
    isnum = False

    for e in exp:
        if e in ['(','{','[','<']:
            stack_1.push(e)
            isnum = False
        elif e in [')','}',']','>']:
            try:
                popped = str(stack_1.pop())
                eval(popped+str(e))
            except:
                stack_1.push(e)
                break;
        if e in ['+','-','*','/']:
            operands.push(e)
        if e.isnumeric():
            if isnum:
                a = str(stack_2.pop())
                op = operands.pop()
                res = eval(a+op+e)
                stack_2.push(res)
                isnum = False
            else:
                stack_2.push(e)
                isnum = True    
    
    if (stack_1.isEmpty()):
        print("Brackets are balanced")
        if (operands.isEmpty()):
            print("Result is: ",stack_2.pop())
        else:
            while(not operands.isEmpty()):
                op = operands.pop()
                a = str(stack_2.pop())
                b = str(stack_2.pop())
                res = eval(a+op+b)
                stack_2.push(res)
            print("The result is: ", stack_2.pop())
    else:
        print("Brackets are not balanced")



