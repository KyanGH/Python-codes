def notin(lst):
    for i in range(10):
        if str(i) not in lst :
            print(i,end=" ")

def main():
    phone_number = input("Enter phone number: ")
    notin(phone_number)
main()