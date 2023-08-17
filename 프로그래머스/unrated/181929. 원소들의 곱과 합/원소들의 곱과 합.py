def solution(num_list):
    answer = 0
    a = 0
    b = 1
    
    for index, value in enumerate(num_list):
        a += value
        b *= value
        
    if a**2 > b :
        answer=1
    else:
        answer=0
    
    return answer