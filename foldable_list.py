def foldable(lst):
    if len(lst) <= 2:
        return True
    return (lst[0]+lst[-1]) == sum(lst[1:-1]) and foldable(lst[1:-1])
def main():
    lst = [0,11,4,1,3,2,2,1,24]
    #lst = [1,5,4]
    print(foldable(lst))
main()