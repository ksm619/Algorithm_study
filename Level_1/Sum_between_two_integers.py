# 두 정수 사이의 합

def solution(a, b):
    return sum([x for x in range(a, b+1)]) or sum([x for x in range(b, a+1)])