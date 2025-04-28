def solution(s):
    s_upper = s.upper()
    if s_upper.count('P') == s_upper.count('Y'): 
        answer = True
    else:
        answer = False
    return answer