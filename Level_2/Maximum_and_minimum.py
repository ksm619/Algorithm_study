# 최댓값과 최소값

def solution(s):
    s = [int(i) for i in s.split(" ")]
    return str(min(s)) + " " + str(max(s))