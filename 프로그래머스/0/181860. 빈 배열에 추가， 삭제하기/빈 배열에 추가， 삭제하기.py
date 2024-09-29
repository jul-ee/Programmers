def solution(arr, flag):
    answer = []
    
    for idx, val in enumerate(arr):
        for i in range(val):
            if flag[idx]:
                answer += [val, val]
            else:
                answer.pop()
    
    return answer