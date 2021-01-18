# 카펫

def solution(brown, yellow):
    length = brown + yellow
    config = 0
    for i in range(1, length+1):
        for j in range(1, i+1):
            if i * j == length and (i-2) * (j-2) == yellow:
                answer = [i, j]
                config = 1
                break
        if config == 1:
            break
    return answer