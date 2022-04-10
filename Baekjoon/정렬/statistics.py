# 통계값 구하기
# 1. 평균
# 2. 중앙값
# 3. 최빈값(가장 많이 나타나는 값)
# 4. 범위(최대값과 최소값 차이)
import sys
n = int(input())
num = [int(sys.stdin.readline()) for _ in range(n)] # 입력받은 숫자

# 최빈값
def mod():
    cnt = [0]*8001
    for i in num: # 해당되는 index에 +1
        cnt[i+4000] += 1 # -4000부터 시작하지만 index는 0부터 시작하기 때문에 +4000
    a = []
    result = []
    for i in range(2):
        a.append(max(cnt)) # 가장 큰 cnt의 값
        result.append(cnt.index(max(cnt))) # 가장 큰 cnt의 index
        cnt[cnt.index(max(cnt))] = 0
    if a[0] == a[1]:
        return result[1] - 4000
    else:
        return result[0] - 4000

# set_num = sorted(list(set(num)))
#
# cnt = [0]*4001
# for i in num: # 해당되는 index에 +1
#     cnt[i] += 1
# max_cnt = []
# for i in range(4001):
#     if cnt[i] != 0:
#         max_cnt.append(cnt[i])
#
# max_len = len(max_cnt)
#
# a = []
# if max_cnt.count(max(max_cnt)) != 1:
#     for i in range(max_len):
#         if max_cnt[i] == max_cnt[-1]:
#             a.append(set_num[i])
#     return a[1]
# else:
#     return set_num[max_cnt.index(max(max_cnt))]

# set_num = sorted(list(set(num)))
#
# cnt = [0]*4001
# for i in num: # 해당되는 index에 +1
#     cnt[i] += 1
# max_cnt = []
# for i in range(4001):
#     if cnt[i] != 0:
#         max_cnt.append(cnt[i])
#
# max_len = len(max_cnt)
#
# a = []
# if max_len != len(set(max_cnt)):
#     for i in range(max_len):
#         if max_cnt[i] == max_cnt[-1]:
#             a.append(set_num[i])
#     print(a[1])
# else:
#     print(set_num[-1])

# 평균: 반올림
print(round(sum(num) / n))

# 중앙값: n은 무조건 홀수이다.
num_sort = sorted(num)
print(num_sort[n // 2])

# 최빈값
print(mod())

# 범위
print(max(num) - min(num))

# for문 안에 또 count가 들어가면 시간초과 발생?
# 둘 다 배열 전체를 훑는 것 => 시간 복잡도 O(n**2)
