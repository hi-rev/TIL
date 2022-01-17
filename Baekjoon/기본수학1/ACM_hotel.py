T = int(input())

for i in range(T):
    hotel = []
    H, W, N = map(int, input().split())
    for i in range(1, W+1):
        for j in range(1, H+1):
            if i < 10:
                bang = f'{j}' + '0' + f'{i}'
                hotel.append(bang)
            else:
                bang = f'{j}' + f'{i}'
                hotel.append(bang)

    print(hotel[N-1])
