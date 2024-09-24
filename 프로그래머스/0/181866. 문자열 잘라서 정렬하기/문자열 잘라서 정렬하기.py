def solution(myString):
    answer = []
    for i in myString.split('x'):
        if len(i) > 0:
            answer.append(i)
    return sorted(answer)