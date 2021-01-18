# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        array = ""
        for j in skill_trees[i]:
            if j in skill:
                array += j
        if skill[:len(array)] == array:
            answer += 1

    return answer