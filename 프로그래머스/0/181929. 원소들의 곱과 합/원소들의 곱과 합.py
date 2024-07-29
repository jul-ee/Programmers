def solution(num_list):
    mul = 1
    add = 0
    
    for i in num_list:
        mul *= i
        add += i
        
    return 1 if mul < add**2 else 0