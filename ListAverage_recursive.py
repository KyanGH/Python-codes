def average(a):  
    if len(a) == 1:  
        return a[0]  
    else:  
        return (a[0] + (len(a) - 1) * average(a[1:])) / len(a)

print(average([1,2,3]))
