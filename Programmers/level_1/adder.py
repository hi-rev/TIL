# 두 수 사이의 수의 sum 구하기
def solution(a, b):
    if a > b:
        answer = [i for i in range(b, a+1)]
        return sum(answer)
    elif b > a:
        answer = [i for i in range(a, b+1)]
        return sum(answer)
    else:
        return a

def solution1(a, b):
    if a > b:  # a가 더 큰 경우에만 자리를 바꿔 사용
        a, b = b, a

    return sum(range(a, b+1))

# 불필요하게 list를 만들 필요가 없었다.
# sum(range(a, b+1))를 이용하면 a부터 b까지의 합 구하기 가능!

print(solution(5, 3))
print(solution1(3, 5))
