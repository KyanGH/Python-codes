def shift(lst):
    lst2 = lst.copy()
    for i in range(len(lst)):
        lst[i] = lst2[i-1]
    return lst

def main():
    lst = [1,2,3,4,5]
    print(lst)
    print(shift(lst))
main()