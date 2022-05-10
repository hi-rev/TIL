import sys

n = int(input())
person = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    person.append([int(age), name])

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])
#
#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l][0] < high_arr[h][0]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr
#
# res = merge_sort(person)

person.sort(key = lambda x: x[0])

for i in range(n):
    print(person[i][0], person[i][1])
