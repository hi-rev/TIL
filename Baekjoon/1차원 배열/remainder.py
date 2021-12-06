remain_list = []
count = 0

for i in range(10):
    remain = int(input()) % 42
    remain_list.append(remain)

remain_list.sort()

for i in range(9):
    if remain_list[i] != remain_list[i+1]:
        count += 1

print(count+1)
