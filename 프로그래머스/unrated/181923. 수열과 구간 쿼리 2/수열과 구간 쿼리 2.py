def solution(arr, queries):
    answer = []
    
    for s,e,k in queries :
        temp = []
        int_list = []
        for i, v in enumerate(arr) :
            if i>=s and i<=e and v>k :
                temp.append(v)
        int_list = list(map(int, temp))
        
        if int_list : 
            answer.append(min(int_list))
        else:
            answer.append(-1)
    
    return answer