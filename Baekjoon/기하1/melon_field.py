# 참외밭
k = int(input())  # 1m^2당 참외의 개수

field = []
for i in range(6):  # 6개의 변 입력 받기
    x, y = map(int, input().split())
    field.append([x, y])

loc = [i[0] for i in field]  # [4, 2, 3, 1, 3, 1] 변의 위치만 담기(field[i][0]의 값들)
one = []
for i in range(6):
    if loc.count(loc[i]) == 1:  # 변의 개수가 하나일 경우 == 가장 긴 변들
        one.append(loc[i])

square = 1
minus = 0
cnt = 0
for i in range(6):  # 큰 직사각형과 작은 직사각형(뺄 것) 구하기
    if field[i][0] in one:
        square *= field[i][1]  # 큰 직사각형 곱셈
        if i == 5 and cnt == 1:  # 작은 직사각형 곱셈 == 긴 변의 값들이 맨 마지막 요소에 있을 때
            if field[0][0] in one:
                minus = field[2][1] * field[3][1]
            else:
                minus = field[1][1] * field[2][1]
        cnt += 1
    elif bool(minus):  # minus 가 이미 연산 되었다면 넘어가기
        continue
    elif cnt == 2:  # 작은 직사각형 곱셈 == 긴 변의 값이 맨 마지막 요소에 있지 않을 때
        idx = (i + 1) % 6
        idx_2 = (i + 2) % 6
        minus = field[idx][1] * field[idx_2][1]
        cnt = 0

print((square - minus) * k)  # 결과
