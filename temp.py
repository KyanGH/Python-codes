def func1(a,b):
    a += 2
    b -= 3
    x =a + b
    print(a,b,x,y)
    return x
def func2():
    global a,b
    a **=2
    b += a
    print(a,b)

a,b = 3,4
x,y = 10,0
print(a,b,x,y)
y= func1(a,b)
print(a,b,x,y)
func2()
print(a,b)