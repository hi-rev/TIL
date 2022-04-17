n = int(input()) # 점의 개수

array = []
for i in range(n): # 점의 좌표 이중 리스트로 만들기
    x, y = map(int, input().split())
    array.append([x, y])

array.sort()

for i in range(n):
    print(array[i][0], array[i][1])

# x만 정렬한 퀵 정렬
# def quick_sort(array, start, end):
#     if start >= end: # 원소가 1개인 경우 종료
#         return
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         while left <= end and array[left][0] <= array[pivot][0]:
#             left += 1
#         while right > start and array[right][0] >= array[pivot][0]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
# quick_sort(array, 0, len(array) - 1)
# print(array)
