# 1. 테스트 케이스의 개수 t가 주어짐
# 2. 두 정수 a와 b를 입력 받음
# 3. Case #와 함께 합 출력

'''
출력이 잘 되는데 왜 틀렸다고 나올까....?
-> 단순 출력이 아닌 포맷팅 방식을 사용해야 했다.
%s %d와 같은 것들이 파이썬에서도 사용되는지 몰랐음
아래와 같이 쓰는것은 이전 포맷팅 방식이고, python3 부터는 format 형식을 사용한다.
자세한 사항은 리드미 참고.
'''

import sys

t = int(input())

for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%s: %s" %(i, a + b))
