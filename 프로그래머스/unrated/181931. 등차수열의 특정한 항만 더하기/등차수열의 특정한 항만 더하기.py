def solution(a, d, included):
    answer = 0
    
    for index, value in enumerate(included) :
        if value == True :
            if index == 0:
                answer += a
            else:
                answer += a+(index*d)
    return answer