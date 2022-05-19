# 골드바흐의 추측
import math
import sys
n = 10000
num = [True for _ in range(n+1)]  # 모든 수가 소수 라고 가정

for i in range(2, int(math.sqrt(n+1))):
    if num[i]:
        j = 2
        while i*j <= n:
            num[i*j] = False
            j += 1
num[0] = False
num[1] = False
prime = [i for i in range(n+1) if num[i]]  # 소수 List

t = int(sys.stdin.readline())  # 테스트 케이스 입력
for i in range(t):
    a = int(sys.stdin.readline())  # 정수값 입력

    one = 0
    two = 0
    for j in range(len(prime)):
        if prime[j] >= a/2:
            if (a - prime[j]) in prime:
                one = prime[j]
                two = a - prime[j]
                break

    print(two, one)
