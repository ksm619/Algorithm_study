# 이진 변환 반복하기

def solution(s):
    answer = ""
    zero = 0
    count = 0
    while answer != "1":
        target = []
        temp = sum([1 for i in s if i == '1'])
        zero += sum([1 for i in s if i == '0'])
        while temp // 2 != 0:
            target.insert(0, str(temp % 2))
            temp = temp // 2
        target.insert(0, str(temp % 2))
        print(target)

        answer = ""
        for i in target:
            answer += i
        s = answer
        count += 1
    return [count, zero]