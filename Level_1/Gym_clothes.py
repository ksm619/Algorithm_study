# 체육복

def solution(n, lost, reserve):
    clothes = [1 for i in range(n)]

    for i in lost:
        clothes[i - 1] -= 1
    for i in reserve:
        clothes[i - 1] += 1

    for i in range(n):
        if (i - 1) > 0 and clothes[i] == 0 and clothes[i - 1] == 2:
            clothes[i - 1] -= 1
            clothes[i] += 1
        elif (i + 1) < n and clothes[i] == 0 and clothes[i + 1] == 2:
            clothes[i + 1] -= 1
            clothes[i] += 1

    answer = 0
    for i in range(n):
        if clothes[i - 1] >= 1:
            answer += 1

    return answer