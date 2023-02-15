def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        #for j in range(i+1):
         
            # printing stars
            #print("* ", end="")
        print('* '*(n-i),end='')
        # ending line after each row
        print()
        

n = int(input("Enter triangle height: "))        
triangle(n)

