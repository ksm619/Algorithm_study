# 3진법 뒤집기

def solution(n):
    rest = []
    while n > 0:
        rest.append(n % 3)
        n = int(n / 3)

    answer = 0
    for i in range(len(rest)):
        answer += rest[len(rest) - (i + 1)] * 3 ** i

    return answer