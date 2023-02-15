def min_lst(lst):
    if len(lst) == 1:
        return lst[0]
    x = lst[0]
    y = min_lst(lst[1:])
    if x < y :
        return x
    return y

def main():
    print(min_lst([1,2,3,4,5,6]))    
main()