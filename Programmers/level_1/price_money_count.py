# 1. N번째 이용한다면, 가격은 price X N
# 2. 계속 이용할 때, 돈이 얼마나 모자라는지 return
# 3. 금액이 부족하지 않다면 0 return

def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += price * i # 총 필요한 돈

    if sum >= money:
        return sum-money
    else:
        return 0

print(solution(3, 20, 4))
