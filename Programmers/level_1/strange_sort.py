# strigns: ["sun", "bed", "car"], n: 2
# ["abce", "abcd", "cdx"], 2
# => 2번째 숫자가 겹치는 문자열은 어떻게 해야할까?

def solution(strings, n):
    str_sort = sorted(strings)
    # 버블정렬(bubble sorted)
    list_len = len(str_sort) - 1
    for i in range(list_len):
        for j in range(0, list_len - i):
            if str_sort[j][n] > str_sort[j + 1][n]:
                str_sort[j], str_sort[j + 1] = str_sort[j + 1], str_sort[j]

    return str_sort

print(solution(["aea", "ba", "ce", "aee"], 1))
