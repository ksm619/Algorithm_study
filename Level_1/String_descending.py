# 문자열 내림차순으로 배치하기

def solution(s):
    s = sorted(s, reverse=True)
    answer = str()
    for i in range(len(s)):
        answer += s[i]

    return answer