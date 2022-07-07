# 다리 놓기
# 핵심은 다리 끼리는 서로 겹쳐질 수 없다.
# ===> 두 숫자 간의 이항 계수를 구하는 문제 !
import sys
t = int(input())

for i in range(t):
    res1 = 1
    res2 = 1
    n, m = map(int, sys.stdin.readline().split())
    for j in range(m, m-n, -1):
        res1 *= j
    for j in range(n, 0, -1):
        res2 *= j
    binomial = int(res1 / res2)
    print(binomial)
