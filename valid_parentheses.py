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
def isValid(s):
    count = 0
    for i in range(len(s)) :
        count += parentheses(s[i])
        if count < 0 :
            return False
    return True if count == 0 else False
    
print(isValid("({)}"))