a, b, c = map(int, input().split())
import math

try:
    sol = int(a / (c-b))
    if (str(type(sol)) == "<class 'int'>") and (sol >= 0):
        print(sol + 1)
    elif sol < 0:
        print('-1')
    else:
        print(math.ceil(sol))
except ZeroDivisionError:
    print('-1')
