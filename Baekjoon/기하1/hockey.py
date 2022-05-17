# 하키
import sys
w, h, x, y, p = map(int, sys.stdin.readline().split())  # p는 좌표 수

hockey = []
for i in range(p):  # 하키 선수들의 좌표 이중List
    a, b = map(int, sys.stdin.readline().split())
    hockey.append([a, b])

cnt = 0
r = int(h / 2)  # 원의 반지름
for i in range(p):
    if x <= hockey[i][0] <= x+w and y <= hockey[i][1] <= y+h:  # 좌표가 직사각형 안에 있을 때
        cnt += 1
    elif (hockey[i][0] - x) ** 2 + (hockey[i][1] - y - r) ** 2 <= r ** 2:  # 좌표가 왼쪽 원 안에 있을 때
        cnt += 1
    elif (hockey[i][0] - x - w) ** 2 + (hockey[i][1] - y - r) ** 2 <= r ** 2:  # 좌표가 오른쪽 원 안에 있을 때
        cnt += 1

print(cnt)
