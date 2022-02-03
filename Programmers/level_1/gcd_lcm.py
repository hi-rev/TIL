# 두 수의 최대공약수, 최소공배수 구하기
def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for j in range(max(n, m), n*m + 1):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
    return answer
#---------------------------------------------
# 유클리드 호제법
# def solution(n, m):
#     mul = n*m
#     while(m):
#         n, m = m, n%m
#     return [n, int(mul/n)]
#---------------------------------------------
# import math
# print(math.gcd(3, 12))
# print(math.lcm(3, 12))
