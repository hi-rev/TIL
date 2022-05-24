# 최대공약수 최소공배수
import math
import sys
a, b = map(int, sys.stdin.readline().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
