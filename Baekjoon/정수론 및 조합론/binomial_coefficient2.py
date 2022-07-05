# 이항 계수 2
n, k = map(int, input().split())
res1 = 1
res2 = 1

for i in range(n, n-k, -1):
    res1 *= i

for j in range(k, 0, -1):
    res2 *= j

binomial = res1//res2
print(binomial % 10007)
