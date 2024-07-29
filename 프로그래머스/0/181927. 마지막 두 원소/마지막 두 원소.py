def solution(num_list):
    num = int(num_list[-1]) - int(num_list[-2])
    if num > 0:
        num_list.append(num)
    else:
        num_list.append(int(num_list[-1]) * 2)        
    return num_list