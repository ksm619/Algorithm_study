# 큰 수 만들기
# TIME OUT

from itertools import combinations

def solution(number, k):
    return str(max([int(''.join(i)) for i in combinations(number, len(number) - k)]))