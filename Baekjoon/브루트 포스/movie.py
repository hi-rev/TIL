# 숫자에 666이 들어가는 수 차례로 알기
n = int(input())
list_666 = []
num = 0

while len(list_666) < n:
    num = str(num)
    if '666' in num:
        list_666.append(num)
    num = int(num) + 1

print(list_666[-1])
