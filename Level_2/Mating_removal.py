# 짝 지어 제거하기
# 호율성 테스트 실패

def solution(s):
    answer = 0
    i = 0
    while len(s) > i+1:
        if s[i] == s[i+1]:
            s = s.replace(s[i:i+2], "")
            i = i-1 if i >= 1 else 0
        else :
            i += 1

    if len(s) == 0:
        answer = 1
    return answer