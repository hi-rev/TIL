m = int(input())
n = int(input())
cnt_list = []
num = [i for i in range(m, n+1)]

for i in num:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    cnt_list.append(cnt)

final = [num[i] for i in range(len(cnt_list)) if cnt_list[i] == 2]

if len(final) == 0:
    print('-1')
else:
    print(sum(final))
    print(min(final))
