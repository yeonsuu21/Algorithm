def solution(my_string, is_suffix):
    answer = 0
    index = []
    for i in range(0, len(my_string)):
        index.append(my_string[i::])
    if(is_suffix in index):
        answer = 1
    else:
        answer = 0
    return answer