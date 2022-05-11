# 좌표 압축 하기
import sys
n = int(input())

coo = list(map(int, sys.stdin.readline().split())) # 바로 list 로 만들 어짐
sort_coo = sorted(list(set(coo))) # 원소 정렬
dic = {sort_coo[i]: i for i in range(len(sort_coo))}
for i in coo:
    print(dic[i], end = " ")

