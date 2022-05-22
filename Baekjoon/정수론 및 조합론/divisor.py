# 약수
import sys
n = int(input())  # 1과 자기 자신을 제외한 약수의 개수
divisor = list(map(int, sys.stdin.readline().split()))  # 약수 입력 받기
divisor.sort()  # 정렬

print(int(divisor[0] * divisor[-1]))