# 124 나라의 숫자


def solution(n):
    answer = []
    while n != 0:
        if n % 3 != 0:
            answer.append(str(n%3))
            n = n // 3
        else:
            answer.append('4')
            n = n // 3 - 1
    answer = list(reversed(answer))

    result = ""
    for i in answer:
        result += i

    return result
