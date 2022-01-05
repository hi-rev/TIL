# 1. 100미만은 무조건 한수
num = int(input())
s = 0

def hansoo(n):
    global s # 전역 변수를 지역 범위에서 사용하기 위함
    if n < 100:
        s += 1
        return s
    else:
        num_list = [int(i) for i in str(n)]
        if (num_list[2] - num_list[1]) == (num_list[1] - num_list[0]):
            s += 1
            return s

for i in range(1, num+1):
    hansoo(i)
print(s)
