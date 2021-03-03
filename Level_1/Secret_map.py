# 비밀지도

def solution(n, arr1, arr2):
    bin1 = [[0 for x in range(n)] for y in range(n)]
    bin2 = [[0 for x in range(n)] for y in range(n)]

    for x in range(len(arr1)):
        count = n - 1
        while arr1[x] != 0:
            bin1[x][count] = int(arr1[x] % 2)
            count -= 1
            arr1[x] = arr1[x] // 2

        count = n - 1
        while arr2[x] != 0:
            bin2[x][count] = int(arr2[x] % 2)
            count -= 1
            arr2[x] = arr2[x] // 2

    answer = []
    for x in range(n):
        section = ""
        for y in range(n):
            if bin1[x][y] == 1 or bin2[x][y] == 1:
                section += "#"
            else:
                section += " "
        answer.append(section)

    return answer
