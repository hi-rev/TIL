h, m = map(int, input().split())

if m >= 45:
    b = m - 45
    print(h, b)

if m < 45:
    if h == 0:
        a = 23
    else:
        a = h - 1
    b = 60 + (m - 45)
    print(a, b)
