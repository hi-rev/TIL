from typing import Any, Sequence

# 이진 탐색 알고리즘
# 시퀀스 a에서 key와 일치하는 원소를 이진 탐색
def bin_search(a: Sequence, key: Any) -> int:
    pl = 0 # 맨 앞 원소 인덱스
    pr = len(a) - 1 # 맨 뒤 원소 인덱스

    while True:
        pc = (pl + pr) // 2 # 중앙 원소 인덱스
        if a[pc] == key:
            return pc
        elif a[pc] > key: # key 값이 더 작을 때
            pr = pc - 1
        else: # key 값이 더 클 때
            pl = pc + 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    print('배열 데이터를 오름차순 입력')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True: # 이전 값보다 작은 값을 입력 받으면 다시 입력하기
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    ky = int(input('검색할 값 입력: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
