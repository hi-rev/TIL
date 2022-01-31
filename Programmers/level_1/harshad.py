# 하샤드 수
def solution(x):
    div = sum([int(i) for i in str(x)])
    return x % div == 0 # return에 조건식을 쓰면 True or False가 출력됨
