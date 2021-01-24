# 멀쩡한 사각형

W = 8
H = 12

if W > H :
    temp = W
    W = H
    H = temp

unit = H/W

if unit % 1 != 0:
    box = ((unit // 1) + 1) * W
else :
    box = (unit // 1) * W

answer = W*H - box
print(answer)