# 터렛
import sys
t = int(input())  # 테스트 케이스

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dd = (x2-x1) ** 2 + (y2-y1) ** 2
    if x1 == x2 and y1 == y2 and r1 == r2:  # 두 점이 동일할 때
        print(-1)
    elif (r2 - r1) ** 2 < dd < (r2 + r1) ** 2:  # 교점이 2개일 경우
        print(2)
    elif (r1+r2) ** 2 == dd or (r2-r1) ** 2 == dd:  # 교점이 1개일 경우
        print(1)
    elif dd > (r1+r2) ** 2 or dd < (r2-r1) ** 2:  # 교점이 0개일 경우
        print(0)
