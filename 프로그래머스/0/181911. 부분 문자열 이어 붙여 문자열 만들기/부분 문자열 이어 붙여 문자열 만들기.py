def solution(my_strings, parts):
    answer = ''
    for string, part in zip(my_strings, parts):
        s, e = part[0], part[1]
        answer += string[s:e+1]
    return answer