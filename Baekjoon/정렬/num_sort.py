# 수 오름차순 출력

n = int(input()) # 수의 개수
num = sorted([int(input()) for i in range(n)]) # 입력받은 수 정렬

for i in num:
    print(i)
