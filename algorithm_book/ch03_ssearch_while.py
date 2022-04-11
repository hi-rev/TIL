# 탐색 알고리즘
# 배열 a에서 값이 key인 원소를 선형 검색

from typing import Any, Sequence

# 배열 a에서 값이 key인 원소를 선형 검색
# 타입 힌트
# def seq_search(a, key):
def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(a): # 일치하는 값을 못찾았을 경우
            return -1
        if a[i] == key: # 일치하는 값을 찾았을 경우
            return i # 해당 인덱스 값 반환
        i += 1 # i(인덱스) 증가

# 파이썬에는 main문이 존재X
# __main__이란 현재 모듈의 이름을 담고 있는 내장 변수
# 직접 실행된 모듈일 경우 __main__의 값을 가지며, 직접 실행되지 않은 import된 모듈은 모둘의 이름(파일명)을 가지게 됨
# -> 직접 실행됐을 경우만 실행
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
