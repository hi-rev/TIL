# 어린 왕자
import sys
t = int(input())  # 테스트 케이스
for i in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())  # 출발점, 도착점 좌표
    n = int(input())  # 행성의 개수
    stars = []
    for i in range(n):  # 행성의 중심과 반지름
        cx, cy, r = map(int, sys.stdin.readline().split())
        stars.append([cx, cy, r])

    # 행성의 중심 좌표와 출발점, 도착점 좌표 사이의 거리
    go = 0
    fin = 0
    for i in range(n):
        if (stars[i][0] - x1) ** 2 + (stars[i][1] - y1) ** 2 < stars[i][2] ** 2 < (stars[i][0] - x2) ** 2 + (stars[i][1] - y2) ** 2:
            go += 1

    for i in range(n):
        if (stars[i][0] - x2) ** 2 + (stars[i][1] - y2) ** 2 < stars[i][2] ** 2 < (stars[i][0] - x1) ** 2 + (stars[i][1] - y1) ** 2:
            fin += 1

    print(go+fin)





