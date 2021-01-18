#기능개발

def solution(progresses, speeds):
    work = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            day = (100 - progresses[i]) // speeds[i]
        else:
            day = (100 - progresses[i]) // speeds[i] + 1
        work.append(day)

    for i in range(len(work) - 1):
        if work[i] >= work[i + 1]:
            work[i + 1] = work[i]

    count = 1
    answer = []
    for i in range(len(work) - 1):
        if work[i] == work[i + 1]:
            count += 1
        else:
            answer.append(count)
            count = 1
    answer.append(count)

    return answer