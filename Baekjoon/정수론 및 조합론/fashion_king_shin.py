# 패션왕 신해빈
import sys
t = int(input())

for i in range(t):
    n = int(input())
    clothes = []
    res = 1

    for j in range(n):  # 해빈이의 의상 입력
        a, b = sys.stdin.readline().split()
        clothes.append(b)

    clothes_set = list(set(clothes))  # 중복 제거
    for cloth in clothes_set:
        cnt = clothes.count(cloth)
        res *= (cnt + 1)

    print(res-1)


