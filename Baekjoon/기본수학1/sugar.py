N = int(input())
list = []

a = N // 5
if N == 3:
    print('1')
else:
    for i in range(a, 0, -1):
        if (N - i*5) % 3 == 0:
            print(i + (N - i*5) // 3)
            list.append(1)
            break
        elif N % 3 == 0:
            print(N//3)
            list.append(1)
            break
        else:
            list.append(0)

    if sum(list) == 0:
        print('-1')
