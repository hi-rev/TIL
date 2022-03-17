# 분해합
# 198은 216의 생성자
n = int(input())
def solution():
    answer = []

    for i in range(n, 0, -1):
        sum = i
        for j in range(len(str(i))):
            sum += int(i % 10 ** (j+1) / 10 ** j)
        if sum == n:
            answer.append(i)

    if len(answer) == 0:
        print("0")
    else:
        print(min(answer))

#------------------------------------------------
# 더 빠른 코드
def solution1():
    for i in range(1, n+1):
        num = sum(map(int, str(i))) + i # 해당숫자와 각 자리수의 합
        if num == n: # 가장 작은 생성자를 찾을 수 있음!
            print(i)
            break
        if i == n: # 생성자가 하나도 없어서 n까지 오면 0 출력
            print("0")
