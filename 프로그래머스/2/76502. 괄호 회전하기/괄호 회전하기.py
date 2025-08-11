def check(s) :
    stack = []
    
    for i in range (len(s)) :
        if( s[i] == '(' or s[i] =='{' or s[i] == '['):
            stack.append(s[i])
        elif ( s[i] == ')' or s[i] == '}' or s[i] == ']' ) :
            if (len(stack) == 0) :
                return False
            else :
                if ( s[i] == ')' and stack[-1] == '(' ) :
                    stack.pop()
                elif ( s[i] == '}' and stack[-1] == '{' ) :
                    stack.pop()
                elif ( s[i] == ']' and stack[-1] == '[' ) :
                    stack.pop()
                else :
                    return False
        
    if (len(stack) != 0) :
        return False
    
    return True
                    

def solution(s):
    answer = 0
    
    for j in range(len(s)) :
        if ( check(s) == True) :
            answer +=1
        
        a = s[0]
        s = s[1:] + a
    return answer