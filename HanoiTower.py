import time
def hanoi(n,start,end):
    if n == 1:
        pm(start,end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        pm(start,end)
        hanoi(n-1, other, end)
        
def pm(start,end):
    print(start,'->',end)

def main():
    n = int(input("Emter number of discs: "))
    StartTime = time.time()
    hanoi(n,1,3)
    EndTime = time.time()
    print("Steps:",2**n-1)
    print("Time:",EndTime - StartTime)
main()