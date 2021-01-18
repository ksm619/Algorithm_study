# 폰켓몬

def solution(nums):
    answer = []
    for i in nums:
        if i not in answer:
            answer.append(i)
        if len(nums)//2 == len(answer):
            break
    return len(answer)