# 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        if i[0]+i[1] not in answer:
            answer.append(i[0]+i[1])

    return sorted(answer)