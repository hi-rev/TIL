# 베르트랑 공준
# 1. n과 2n 사이에는 적어도 하나 이상의 소수가 있다.
import math
while 1:
    n = int(input())
    n2 = int(n * 2)
    if n == 0:
        break

    num = [1] * (n2+1)
    num[0] = 0
    num[1] = 0

    for i in range(2, int(math.sqrt(n2)) + 1):
        if num[i]:
            j = 2
            while i * j <= n2:
                num[i*j] = 0
                j += 1

    print(sum(num[n+1:n2+1]))
