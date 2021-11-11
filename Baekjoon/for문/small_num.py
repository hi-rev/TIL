n, x = map(int, input().split())

# list()를 통해 입력받은 데이터들을 리스트로 만듦
num = list(map(int, input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end=" ")
