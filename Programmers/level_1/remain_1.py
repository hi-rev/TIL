# 1. n % x == 1 이 되는 가장 작은 자연수 x 구하기

def solution(n):
    for i in range(1, n+1):
        if n % i == 1:
            return i

print(solution(12))
