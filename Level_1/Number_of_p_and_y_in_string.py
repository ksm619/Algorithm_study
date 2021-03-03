# 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    if s.count('p') != s.count('y'):
        return False
    else :
        return True