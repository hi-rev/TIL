# Case #x: A + B = C 형식으로 출력
# 앞에 fastplus.py에서는 input() 으로 여러줄 입력 받으니까 런타임 에러가 나던데
# 여기는 안나네....?! 문제에서 그렇게 설정을 해놓은건가

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print("Case #%s: %s + %s = %s" %(i, a, b, a + b))
