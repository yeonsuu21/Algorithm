def solution(my_string, overwrite_string, s):
    a = my_string
    b = overwrite_string
    answer = a[0 : s] + b + a[s+ len(b) : ]
    return answer