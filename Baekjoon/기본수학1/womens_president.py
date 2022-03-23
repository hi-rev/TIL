# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input()) # 층, 호수
    home = []

    first = [i+1 for i in range(n)] # 0번째 층은 미리 만들기
    home.append(first)

    for i in range(k):
        indx = [] # 이중 리스트
        sum = 0
        for j in range(n):
            sum = sum + home[i][j]
            indx.append(sum)
        home.append(indx)

    print(home[-1][-1])

# 1 5 15 35 70  home[3]
# 1 4 10 20 35  home[2]
# 1 3 6 10 15   home[1]
# 1 2 3 4 5    home[0]
