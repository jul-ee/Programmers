def solution(before, after):
    answer = 1
    before = list(before)
    after = list(after)
    
    before.sort()
    after.sort()
    
    if after != before :
        answer = 0
        
    return answer