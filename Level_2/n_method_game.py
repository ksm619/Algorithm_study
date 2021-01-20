#  n진수 게임

def solution(n, t, m, p):
    string = ""
    rest = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    score = 0
    while len(string) <= t*m:
        num = score
        print(score)
        answer = ""
        if num != 0:
            while num != 0:
                k = num % n
                num = num // n
                answer += rest[k]
        else :
            answer = rest[0]
        answer =''.join(reversed(answer))
        string += str(answer)
        score += 1
    string = string[:t*m]
    member = [string[x*m+(p-1)] for x in range(len(string)//m)]
    answer = ""
    for i in member :
        answer += i
    return answer