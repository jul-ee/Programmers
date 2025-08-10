def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        can_buy = {}
        for j in range(i, i+10):
            if can_buy.get(discount[j]):
                can_buy[discount[j]] += 1
            else:
                can_buy[discount[j]] = 1
        for k in range(len(want)):
            if (want[k] not in can_buy) or can_buy[want[k]] < number[k]:
                break
        else:
            answer += 1    
    return answer