# n의 약수의 합 구하기
def solution(n):
    cnt = [i for i in range(n, 0, -1) if n%i==0]
    return sum(cnt)
