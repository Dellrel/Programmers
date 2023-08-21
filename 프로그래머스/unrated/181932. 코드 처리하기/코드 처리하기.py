def solution(code):
    answer = ''
    mode = 0
    
    for i, v in enumerate(code):
        if v == '1' and mode == 0:
            mode=1
        elif v == '1' and mode == 1:
            mode=0
            
        if mode==0 :
            if i%2==0:
                answer += code[i]
        else:
            if i%2!=0:
                answer += code[i]
        answer = answer.replace('1','')
    
    if not answer :
        answer = "EMPTY"
        
    
    return answer