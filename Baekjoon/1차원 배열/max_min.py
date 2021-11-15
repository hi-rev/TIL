# 1. 생성할 정수 개수 선택 : N
# 2. N개의 정수 입력 받음
# 3. 출력 -> 최소값, 최대값

n = int(input())
a = list(map(int, input().split()))

if len(a) != n:
      print('리스트의 크기가 맞지 않습니다.')
else:
    print(min(a), max(a))
