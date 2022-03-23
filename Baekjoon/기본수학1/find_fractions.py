# x번째 분수 구하기
x = int(input())
line = 0 # 몇 번째 줄인지
sum = 0 # 총 합

while sum < x:
    line += 1
    sum += line
sum = sum - line # 이전 합
turn = x - sum # 줄에서 몇 번째인지

# line이 짝수면 오름차순, 홀수이면 내림차순
if line % 2 == 0: # 짝수일 때
    one = turn
    two = (line + 1) - turn
else: # 홀수일 때
    one = (line + 1) - turn
    two = turn

print(f'{one}/{two}')

# 1/1  ---- 1
# 1/2 2/1  ---- 2
# 3/1 2/2 1/3  ---- 3
# 1/4 2/3 3/2 4/1  ---- 4
# 5/1 4/2 3/3 2/4 1/5 ----- 5
# ....
