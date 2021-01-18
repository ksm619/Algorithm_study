# K-번째 수

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(temp[commands[i][2]-1])
    return answer