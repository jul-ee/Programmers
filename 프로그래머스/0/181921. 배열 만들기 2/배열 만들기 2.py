def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
    return answer if answer else [-1]