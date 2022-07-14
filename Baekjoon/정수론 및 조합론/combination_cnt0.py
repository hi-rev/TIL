# 조합 0의 개수
# n, m은 최대 20억까지 들어 오게 됨
# 따라서 단순 팩토리얼 계산은 시간 초과가 발생 하기 때문에 불가능
n, m = map(int, input().split())


def factorial_div_25(num, t):  # 인자는 n과 나눌 숫자(5or2)
    cnt = 0
    while num > 0:  # n이 0보다 같거나 작아 지면 멈춤
        cnt += num // t
        num //= t
    return cnt


cnt_5 = factorial_div_25(n, 5) - factorial_div_25(n - m, 5) - factorial_div_25(m, 5)
cnt_2 = factorial_div_25(n, 2) - factorial_div_25(n - m, 2) - factorial_div_25(m, 2)
res = min(cnt_5, cnt_2)
print(res)
