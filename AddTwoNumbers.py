l1 = [2,4,3]
l2 = [5,6,4]
l1.reverse()
l2.reverse()

def listtonum(lst):
    num = 0
    for i in range(len(lst)):
        num = num * 10 + lst[i]
    return num  
    
print(listtonum(l1))