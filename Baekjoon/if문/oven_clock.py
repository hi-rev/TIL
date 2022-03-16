min, sec = map(int, input().split()) # 현재 분 초 입력
n = int(input()) # 걸리는 시간 입력
sec_n = sec + n # 현재 초 + 걸리는 시간

if min + sec_n // 60 > 23:
    print(min + sec_n // 60 - 24, sec_n % 60)
elif sec_n >= 60:
    print(min + sec_n // 60, sec_n % 60)
else:
    print(min, sec_n)
