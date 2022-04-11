# for문을 이용한 선형 탐색
# while문 보다 코드가 더 짧고 간결

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == '__main__':
    num = int(input('원소 수 입력: ')) # 총 몇개 배열
    x = [None] * num

    for i in range(num): # 배열 입력
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('찾는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
