# 정확하게 N 킬로그램 배달해야 함
# 봉지는 3 킬로그램과 5 킬로그램 봉지가 있음
# ==> 최대한 적은 봉지 개수 구하기

# 1. n % 5 == 0
# 2. 나누어 떨어지지 않으면 5의 배수를 뺀 후 3과 나누어 떨어지는지 확인
# 3. n % 3 == 0
# 4. -1

n = int(input())

def solution(n):
    num = n//5
    if n % 5 == 0: # 1. n % 5 == 0
        return n//5

    for i in range(num, 0, -1): # 2. 5의 배수를 뺀 후 3과 나누어 떨어지는지 확인
        if (n - i*5) % 3 == 0:
            return i + (n - i*5)//3

    if n % 3 == 0: # 3. n % 3 == 0
        return n//3
    else: # 4. 아무것도 반환 못하면 마지막에 -1 반환
        return -1

print(solution(n))
