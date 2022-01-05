# 1. d(n)은 n과 n의 각 자리를 더하는 함수
# 2. 이 연산을 사용하면 어떤 수로도 절대 나오지 않는 값들이 있음
# 3. 1부터 10000까지 함수를 실행하여 해당 값들 전체 값들을 제외하여 출력

def d(n):
    num = [int(i) for i in str(n)]
    return sum(num) + n

num_list = []
for i in range(1, 10000):
    num_list.append(i)

non_s = []
for i in range(1, 10001):
    if d(i) < 10000:
        non_s.append(d(i))
non_selfnum = list(set(non_s)) # 셀프 넘버를 제외한 리스트

for i in num_list:
    if i not in non_selfnum:
        print(i)
