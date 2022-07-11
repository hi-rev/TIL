n = int(input())
factorial = 1
cnt = 0

for i in range(n, 0, -1):
    factorial *= i

r_fact = list(reversed(list(str(factorial))))
for i in r_fact:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break
