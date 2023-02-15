def main():
    a = float(input("Enter nominator: "))
    b = float(input("Enter denominator: "))
    while b == 0 :
        print("The denominator can't be zero!")
        b = float(input("Enter the denominator again: "))
    print(a/b)
main()