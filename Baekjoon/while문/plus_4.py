# EOF(End If File)로 구현
# 아무것도 입력받지 않았을 때 종료하도록 함
# 예외처리를 통해 구현 : 아무것도 입력하지 않으면 종료된다.

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
