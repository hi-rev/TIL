# n의 소수의 개수 반환
# 에라토스테네의 체 알고리즘
# 1. 2부터 N까지의 모든 수 나열
# 2. 2부터 [N의 제곱근]까지 수 x 구하기
# 3. x들의 배수 제거(x는 제거하지 않음)

import math

def solution(n):
	num = [True for i in range(n+1)] # 모든 숫자가 True

	for i in range(2, int(math.sqrt(n)) + 1): # int()는 내림
		if num[i] == True:
			j = 2
			while i * j <= n:
				num[i*j] = False
				j += 1

	answer = num.count(True) - 2
	return answer
