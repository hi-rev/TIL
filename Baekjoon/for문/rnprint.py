# 1. n 입력 받고
# 2. 역순 출력

n = int(input())
a = []

for i in range(1, n+1):
    a.append(i)

for i in a[::-1]:
    print(i)
