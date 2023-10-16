def solution(a, b):
    answer = 0
    a1 = int(str(a) + str(b))
    a2 = int(str(b) + str(a))
    if(a1>a2):
        return a1
    if(a1==a2):
        return a1
    else:
        return a2
    
    return answer