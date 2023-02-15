def parentheses(str):
        if str == '[' :
            return 1
        if str == ']' :
            return -1
        if str == '{' :
            return 1
        if str == '}' :
            return -1
        if str == '(' :
            return 1
        if str == ')' :
            return -1
    
def main(s):
    count = 0
    count2 = 0
    count3 = 0
    for i in range(len(s)):
        if s[i] == '(' or  s[i] == ')' : 
            count += parentheses(s[i])
            if count < 0 :
                return False
    for i2 in range(len(s)):
        if s[i2] == '[' or s[i2] == ']' : 
            count2 += parentheses(s[i2])
            if count2 < 0 :
                return False
    for i3 in range(len(s)):
        if s[i3] == '{' or s[i3] == '}' : 
            count3 += parentheses(s[i3])
            if count3 < 0 :
                return False
    return True if count == 0 and count2 == 0 and count3 == 0 else False
s = "([)]"
print(main(s))