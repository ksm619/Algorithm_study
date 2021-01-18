# 다음 큰 숫자

def solution(n):
    target = []
    temp = n
    while temp // 2 != 0:
        target.insert(0, temp % 2)
        temp = temp // 2
    target.insert(0, temp % 2)

    while True:
        n += 1
        binary = []
        temp = n
        while temp // 2 != 0:
            binary.insert(0, temp % 2)
            temp = temp // 2
        binary.insert(0, temp % 2)

        if sum(target) == sum(binary):
            break
    return n