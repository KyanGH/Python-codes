def main():
    max_char = 0
    max_num = 0
    #Look for the biggest number and charachter
    for i in range(10) :
        #Get user input
        char = input("Enter a char: ")
        if ord(char) > 96 and ord(char) < 123 :
            if ord(char) > max_char :
                max_char = ord(char)
        if ord(char) > 47 and ord(char) < 58 :
            if ord(char) > max_num :
                max_num = ord(char)
    #print the triangle
    for i in range(int(chr(max_num)) + 1):
        for j in range(i):
            print(chr(max_char),end="")
        print()

main()
        
        