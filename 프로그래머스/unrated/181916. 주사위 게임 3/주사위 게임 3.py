def solution(a, b, c, d):
    answer = 0
    num=[a,b,c,d]
    count=[num.count(i) for i in num]
    
    if max(count) == 4:
        answer = a*1111
    elif max(count) == 3:
        p = num[count.index(3)]
        q = num[count.index(1)]
        answer = (10*p+q)**2
    elif max(count) == 2:
        if min(count) == 2:
            answer = (a+c) * abs(a-c) if a == b else (a+b) * abs(a-b)
        else:
            p = num[count.index(2)]
            answer = (a*b*c*d) / p**2
    else:
        answer = min(num)
    
    return answer