n = int(input()) # 점의 개수

array = []
for i in range(n): # 점의 좌표 이중 리스트로 만들기
    x, y = map(int, input().split())
    array.append([y, x])

array.sort()

for i in range(n):
    print(array[i][1], array[i][0])
