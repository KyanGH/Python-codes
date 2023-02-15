def findDigit(num,n):
    if num == 0 :
        return False
    if num%10 == n:
        return True
    return findDigit(num//10,n)

def cntstr(str,ch):
    if str == "":
        return 0
    if str[-1] == ch:
        return 1+cntstr(str[:-1],ch)
    return cntstr(str[:-1],ch)

def cntsimilar(x,y):
    if x == 0 or y == 0:
        return 0
    if x % 10 == y % 10:
        return 1 + cntsimilar(x//10,y//10)
    return cntsimilar(x//10,y//10)

def geometric(a1,q,n):
    if n < 0:
        return
    geometric(a1,q,n-1)
    print(a1*q**n,end=",")
    
def print_reverse(st):
    if st == "":
        return
    print_reverse(st[1:])
    print(st[0],end="")

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

def mypow(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / mypow(x,-n)
    return x * mypow(x,n-1)


def main():
    print(mypow(2,-3))
main()