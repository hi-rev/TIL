# for문을 통하여 여러줄을 입력받아야 할 때는
# input() 대신 sys.stdin.readline()을 사용하도록 하자!

import sys

n = int(input())
num = sorted([int(sys.stdin.readline()) for i in range(n)])
for i in num:
    print(i)
