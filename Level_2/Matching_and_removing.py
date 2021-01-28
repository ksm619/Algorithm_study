# 짝지어 제거하기

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



def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0