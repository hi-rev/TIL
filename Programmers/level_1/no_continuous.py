# 리스트에서 연속적인 수만 제거
def solution(arr):
    a = arr[0]
    ind = 1
    answer = [a]
    while ind < len(arr):
        if a != arr[ind]:
            a = arr[ind]
            answer.append(a)
        ind += 1
    return answer

print(solution([3,3,1,1,2,2,1]))
