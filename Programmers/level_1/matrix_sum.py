def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr1[0])
    answer = [[arr1[i][j] + arr2[i][j] for j in range(b)] for i in range(a)]
    return answer
