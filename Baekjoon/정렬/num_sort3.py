# 카운팅 정렬(counting sort)
# counting sort는 non-comparison sort 정렬이다.
# 1. array의 원소값의 빈도 값을 센다.
# 2. 저장된 빈도값별로 값 정렬
import sys
n = int(input())

# 0부터 10000까지의 리스트 생성
# => 문제 조건이 10000이하의 자연수까지만 입력받음
cnt = [0]*10001

# 입력 받은 숫자 index에 +1
for i in range(n):
    cnt[int(sys.stdin.readline())] += 1

# 각 인덱스 숫자만큼 인덱스를 출력하기
for i in range(10001):
    for j in range(cnt[i]):
        print(i)

# Counting Sort
# import sys
# n = int(input())
#
# num_list = [int(sys.stdin.readline()) for i in range(n)] # 원소 입력 받기
#
# # 빈도값 세기
# counting = [0] * (max(num_list) + 1) # 리스트 생성
# for i in num_list:
#     counting[i] += 1
#
# # 누적값으로 환산
# for i in range(len(counting) - 1):
#     counting[i+1] += counting[i]
#
# # 정렬하기
# answer = [0] * n # 리스트 생성
# for i in num_list:
#     answer[counting[i] - 1] = i
#     counting[i] -= 1
#
# for i in answer:
#     print(i)
