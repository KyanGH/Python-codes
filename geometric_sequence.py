def mainq2():
    a1 = float(input("Enterfirst element of geometric Progression Series: "))
    d = float(input("Enter the common ratio: "))
    n = int(input("Enter integer n: "))
    
    print("Geometric Progression Series:")
    for i in range(n,0,-1):
        print(a1 * d**(n-i), end=" ")

mainq2()
