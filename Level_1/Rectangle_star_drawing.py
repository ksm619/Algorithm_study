# 직사각형 별찍기

a, b = map(int, input().strip().split(' '))
answer = ""
for y in range(b):
    for x in range(a):
        answer += "*"
    answer += "\n"
print(answer)
