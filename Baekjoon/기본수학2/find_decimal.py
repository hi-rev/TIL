# 에라토스테네스의 체
# M~N 사이의 소수 구하기
m, n = map(int, input().split())
import math

# 0부터 n까지의 True(소수) 리스트 만들기
num = [True] * (n+1)
num[0] = False
num[1] = False

# 2부터 n의 제곱근까지의 배수를 모두 False로 정의
for i in range(2, int(math.sqrt(n)) + 1):
    if num[i]:
        j = 2
        while i * j <= n:
            num[i*j] = False
            j += 1

for i in range(m, n+1):
    if num[i]:
        print(i)
