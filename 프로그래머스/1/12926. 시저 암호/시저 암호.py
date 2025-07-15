def solution(s, n):
    answer = ''
    s = list(s)
    ord_list = []
    for i in s:
        ord_list.append(ord(i))
        to_chr_list = [] 
        for ordnum in ord_list:
            if ordnum == 32:
                pass
            
            elif 65 <= ordnum <= 90:
                ordnum = (ordnum-65+n)%26 + 65
            elif 97 <= ordnum+n <= 122:
                ordnum = (ordnum-97+n)%26 + 97
            else:
                ordnum += (n-26)
            to_chr_list.append(ordnum)
    for to_chr in to_chr_list:
        new_alpha = chr(to_chr)
        answer += new_alpha
    return answer