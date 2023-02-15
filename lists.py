def func():
    global x
    x = 2
    for x in range(10):
        for x in range(5):
            print(x,end=" ")
func()
