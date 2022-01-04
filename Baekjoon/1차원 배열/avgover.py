c = int(input()) # test case 개수

for i in range(c):
    cnt = 0
    t = list(map(int, input().split())) # 점수 입력

    count = int(t[0]) # 점수 개수
    test = t[1:] # 점수

    avg = sum(test) / count

    for j in range(count):
        if test[j] > avg:
            cnt += 1

    print("{:.3f}%".format(cnt/count*100))
