def mainq1():
    count = 0
    num = int(input("Enter Integer Number: "))
    #Get user input
    print("List of divisors of %d: "%num,end="")
    
    
    if num < 0 :
        num *= -1
    if num == 0 :
        print("Infinity-All natural numbers are divisors of 0")
    else :
        for i in range(1,num+1):
            if num % i == 0 :
                count += 1
                print(i,end = " ")
        print("\nNumber of divisors is:",count)
            
mainq1()
        