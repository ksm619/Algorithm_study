# 올바른 괄호
# 효율성 테스트 실패

def solution(s):
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            s = s.replace("()", "")
            print(i, s)
            if len(s) == 0:
                return True
    else :
        return False

    if len(s) > 0:
        return False