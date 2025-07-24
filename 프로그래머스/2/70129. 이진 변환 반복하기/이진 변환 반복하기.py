def solution(s):
    count_zero = 0
    i = 0
    while len(s) > 1 and s != '1':
        i += 1
        count_zero += s.count('0')
        s = bin(s.count('1'))[2:]
    return [i, count_zero]