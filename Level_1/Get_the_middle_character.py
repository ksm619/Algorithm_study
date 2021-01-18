# 가운데 글자 가져오기

def solution(s):
    if len(s)%2==1:
        answer = s[(len(s)-1)//2]
    else:
        answer = s[(len(s)//2)-1:(len(s)//2)+1]

    return answer