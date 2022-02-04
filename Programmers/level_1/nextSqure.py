import math
def solution(n):
    num_sqrt = math.sqrt(n)
    while 1:
        if (num_sqrt).is_integer():
            return (num_sqrt + 1) ** 2
        else:
            return -1
