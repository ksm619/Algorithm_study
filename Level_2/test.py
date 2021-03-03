#

from itertools import combinations

numbers = [2,1,3,4,1]

answer = []
for i in combinations(numbers, 2):
    if i[0]+i[1] not in answer:
        answer.append(i[0]+i[1])
print(sorted(answer))