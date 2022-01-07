n = int(input())

for i in range(n):
    r, s = input().split()
    r = int(r)
    s = list(s)

    for j in s:
        print(j*r, end='')
    print('')
