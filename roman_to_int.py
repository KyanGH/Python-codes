def create_num(s):
    output = 0
    N = len(s)
    i = N-1
    while i >= 0 :
        if i < N-1 and roman_map[s[i]] < roman_map[s[i+1]]:
            output -= roman_map[s[i]]
        else:
            output += roman_map[s[i]]
        i -= 1
    return output
    
roman_map = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    }

 
roman = str(input("Enter roman number: "))
print(create_num(roman))