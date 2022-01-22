n = int(input())
num_list = list(map(int, input().split()))
cnt_list = []

for i in num_list:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    cnt_list.append(cnt)
    print(cnt_list)

print(cnt_list.count(2))
