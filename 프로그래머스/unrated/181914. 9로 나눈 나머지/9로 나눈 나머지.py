def solution(number):
    answer = 0
    number = str(number)
    number = sum(int(digit) for digit in number)
    answer = number % 9
    return answer