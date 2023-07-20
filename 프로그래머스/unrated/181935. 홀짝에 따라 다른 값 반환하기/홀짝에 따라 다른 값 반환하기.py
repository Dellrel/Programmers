def solution(n):
    answer = 0
    
    if n % 2 == 0 :
        for x in range(1, n+1) :
            if x % 2 == 0 :
                answer += x * x
            else :
                continue
    else:
        for x in range(1, n+1) :
            if x % 2 == 0 :
                continue
            else:
                answer += x
    return answer