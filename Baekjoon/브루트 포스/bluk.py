# 덩치 구하기
n = int(input())
wh = []
answer = [1]*n

for i in range(n):
    weight, height = map(int, input().split())
    wh.append([weight, height]) # 각각 키 몸무게 2중 List

for i in range(n-1):
    for j in range(i+1, n):
        if wh[i][0] > wh[j][0] and wh[i][1] > wh[j][1]:
            answer[j] += 1
        if wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1]:
            answer[i] += 1
print(*answer)

# 맞게 풀었지만 출력문을 int형으로 하나씩 출력해야하는데
# 그대로 list로 출력해버려서 3번이나 틀렸다. 주의하도록 하자!
# 지금까지 리스트 풀때는 ''.join()을 썼는데 *으로도 간단하게 리스트를 풀 수 있다.
