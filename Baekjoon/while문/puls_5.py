# while True는 무한히 반복하는 무한 루프문이다.
# for은 반복횟수가 정해져 있을 때 주로 사용하지만
# while은 반복횟수가 정해져있지 않을 때 주로 사용한다.

while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        print(a+b)
    else:
        break
