from ch03_ssearch_while import seq_search

print('실수 검색하기')
print('주의: "End"를 입력하면 종료')

number = 0
x = [] # 새로운 배열 생성

# 배열 크기가 정해지지 않고 자유롭게 입력
while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값을 입력하세요: '))

idx = seq_search(x, ky)
if idx == -1:
    print('찾는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')
