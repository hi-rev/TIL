# 1. 3개의 자연수 A, B, C
# 2. A X B X C
# 3. 0부터 9까지 각각 숫자가 몇 번씩 쓰였는지 계산

a = int(input())
b = int(input())
c = int(input())

num = a * b * c

n_list = list(map(int, str(num)))

print(num, n_list)

for i in range(10):
    count = 0
    for j in n_list:
        if j == i:
            count += 1
    print(count)
