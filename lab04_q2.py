def main():
    #insert number
    num = int(input("Enter a positive 4-digits number: "))
    
    a = num % 10
    b = (num // 10) % 10
    c = (num // 100) % 10
    d= (num //1000) % 10
    diff = d - c
    #print(diff)
    
    #Check if number is negative
    if num < 0 :
        print(num, "is a negative number. Bye bye.")
    
    #check if number is 4 digits (not finished)
    elif num % 10000 != num or num // 10000 != 0  :
        print(num, "is not a 4-digits number. Bye bye.")
    
    #Number is in decending sequence
    elif d > c and c > b and b > a :
        print("Decending sequence (from left to right)")
        
    #Number is in increasing aritheitic squence
    elif d < c and c < b and b < a :
        print("increasing arithmetic squence (from left to right")
    
    
    #
    
        
print(5555%1111)