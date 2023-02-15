def pyramid(rows):
    for i in range(rows+1):
        for j in range(rows-i):
            print(" ",end="")
        for k in range(i):
            print("* ",end="")
        print()

def flip_pyramid(rows):
    for i in range(rows+1):
        for j in range(i):
            print(" ",end="")
        for k in range(rows-i):
            print("* ",end="")
        print()

def left_triangle(rows):
    for i in range(rows+1):
        print("* " * i)

def right_triangle(rows):
    for i in range(rows+1,0,-1):
        print(" " * i,end="")
        for j in range(rows - i + 1):
            print("*",end="")
        print()

def right_pyramid(rows):
    for i in range(rows+1):
        for j in range(rows - i):
            print("-",end="")
        for k in range(i):
            print("*",end="")
        print()
    for i in range(rows):
        for j in range(rows - i):
            print("*",end="")
        for k in range(i):
            print("-",end="")
        print()
    

def rectangle(rows,columns):
    for i in range(rows):
        for j in range(columns):
            print("*",end="")
        print()
        


right_pyramid(5)