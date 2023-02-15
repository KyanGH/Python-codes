def change(sum):
    change20 = sum//20
    change10 = sum%20//10
    change5 = sum%20%10//5
    change1 = sum%20%10%5//1
    str ="The change of {0} is {1} 20's, {2} 10's, {3} 5's, {4} 1's".format(sum,change20,change10,change5,change1)
    print(str)
change(sum = int(input("Enter amount of money: ")))