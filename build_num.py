import math
def main():
    build = 0
    digit = int(input("Enter digit :"))
    while digit != -1 :
        build = build * 10 + digit
        digit = int(input("Enter digit :"))
    print(build)
main()
    