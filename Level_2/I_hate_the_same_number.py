# 같은 숫자는 싫어

def solution(arr):
    arr.append(-1)
    return [arr[i] for i in range(len(arr) - 1) if arr[i] != arr[i + 1]]