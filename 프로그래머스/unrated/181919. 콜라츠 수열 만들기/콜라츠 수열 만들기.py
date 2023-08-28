def solution(n):
    answer = []
    
    while True:
        if n % 2==0:
            if n==1:
                answer.append(int(n))
                break
            else:
                answer.append(int(n))
                n = n/2
        else:
            if n==1:
                answer.append(int(n))
                break
            else:
                answer.append(int(n))
                n = 3*n+1
            
    return answer