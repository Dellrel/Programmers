def solution(numLog):
    answer = ''
    
    for i, v in enumerate(numLog):
        if i < len(numLog)-1 :
            if numLog[i+1] - v == 1:
                answer += 'w'
            elif numLog[i+1] -v == -1:
                answer += 's'
            elif numLog[i+1] -v == 10 :
                answer += 'd'
            else:
                answer += 'a'
    
    return answer