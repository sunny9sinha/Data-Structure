def findFirstNonRepeatingChar(sent):
    dic = {}
    for s in sent:
        if s in dic.keys():
            dic[s] = dic[s] + 1
        else:
            dic[s] = 1

    for k in sent:
        if dic[k] == 1:
            return k 
    
    return "No non repeating char"
    
if __name__ == '__main__':
    sent = input("Please input string to check: ")
    print("First non repeating character: ", findFirstNonRepeatingChar(sent))
