import math

def rev_num(num):
    rev = 0
    while num > 0 :
        remainder = num % 10
        rev = (rev * 10) + remainder
        num = num // 10
    return rev

def create_num(l1):
    num = 0
    x = len(l1)
    for i in range((len(l1))):
        num += l1[i] * math.pow(10,len(l1) - i)
        
    return int(num // 10)


def main():
    l1 = [4,3,2,1]
    l2 = [1,2,3,4]
    print(rev_num(create_num(l1)) + rev_num(create_num(l2)))

main()
    
        

