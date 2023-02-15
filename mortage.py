def main():
    
    salary = int(input("Enter your monthly salary :"))
    num_kids = int(input("Enter number of children : "))
    service = str(input("Military or civil service? \nfor Yes enter 'y', -otherwise any other charachter: "))
    
    
    if salary >= 17500 :
        print("The mortage has been approved with monthly paymnet of ",int(salary * (35/100)),".",sep="")
       
    elif num_kids >= 5 and salary >= 14000 :
        print("The mortage has been approved with monthly paymnet of ",int(salary * (25/100)),".",sep="")
        
    elif service == 'y' and salary >= 15000 :
        print("The mortage has been approved with monthly paymnet of ",int(salary * (25/100)),".",sep="")
    
       
    else :
        print("The mortage is not approved.")
        
main()