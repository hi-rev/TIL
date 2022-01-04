n = int(input())

for i in range(n):
    cnt = 0
    count = 0
    ox = input()

    for s in ox:
        if s == 'O':
            cnt += 1
            count += cnt
        elif s == 'X':
            cnt = 0
    print(count)
