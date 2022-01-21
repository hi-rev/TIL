while True:
    x, y, z = map(int, input().split())
    list = [x*x, y*y, z*z]
    list.sort()
    list.reverse()
    z = list[0]
    x = list[1]
    y = list[2]

    if x == 0 and y == 0 and z == 0:
        break
    elif x + y == z:
        print('right')
    else:
        print('wrong')
