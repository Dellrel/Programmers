def solution(num_list):
    answer = 0
    a = ''
    b = ''
    
    for i in num_list:
        if i%2 ==0:
            b+=str(i)
        else:
            a+=str(i)
    
    answer = int(a)+int(b)
    
    return answer