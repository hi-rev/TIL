# 검문
# N개의 숫자가 모두 나누기 M을 했을 때 나머지가 같아야 함
import sys

n = int(input())
num = [int(sys.stdin.readline()) for i in range(n)]
num.sort()  # 1. 입력 받은 데이터 오름차순

# 2. 인접한 원소들 간의 차를 리스트로 만든다.
diff_num = []
for i in range(len(num) - 1):
    diff_num.append(num[i + 1] - num[i])


# 3. diff_num 리스트 원소들의 최대공약수 구하기 (유클리드 호제법)
# 유클리드 호제법 : a, b = b, a%b
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a  # 최대공약수


n_gcd = diff_num[0]
for i in range(1, len(diff_num)):
    n_gcd = gcd(n_gcd, diff_num[i])

# 4. n_gcd의 공약수들 구하기
res = set()
for i in range(2, int(n_gcd ** 0.5) + 1):
    if n_gcd % i == 0:
        res.add(i)
        res.add(n_gcd // i)
res.add(n_gcd)
print(*sorted(list(res)))

# min 요소를 잡고 루프를 도는 것은 시간 초과
# 10억번씩 for 문을 돌면 매우 오래 걸림
# for i in range(2, a + 1):
#     if a % i == b % i:
#         div = [j % i for j in num]
#         if len(set(div)) == 1:
#             print(i, end=' ')
