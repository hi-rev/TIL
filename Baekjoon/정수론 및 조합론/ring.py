import sys
import math
n = int(input())  # 링의 개수

# 각각 링의 반지름
ring = list(map(int, sys.stdin.readline().split()))
first = ring[0]  # 첫 번째 원과 다른 원들의 비교를 위함

for i in range(1, n):
    g = math.gcd(first, ring[i])  # 최대공약수
    a = int(first / g)
    b = int(ring[i] / g)
    print(f'{a}/{b}')
