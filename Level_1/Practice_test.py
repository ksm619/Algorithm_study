# 모의고사

def solution(answers):
    Examinee = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    a, answer =[], []
    for i in range(len(Examinee)):
        correct, cnt = 0, 0
        for x in answers:
            length = len(Examinee[i])
            if x == Examinee[i][cnt % length]:
                correct = correct + 1
            cnt = cnt + 1
        a.append(correct)

    if a.count(max(a)) == 1 :
        answer.append(a.index(max(a)) + 1)

    elif a.count(max(a)) >= 2 :
        for i in range(a.count(max(a))):
            max_idx = a.index(max(a))
            answer.append(max_idx + 1)
            del a[max_idx]
            a.insert(max_idx, 0)
    return answer
