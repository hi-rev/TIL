# 배열 중 특정값으로 나누어 떨어지는 값 찾기
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if not answer: # not answer => answer 배열이 비어있으면 True
        return [-1]
    else:
        return sorted(answer)

print(solution([5, 9, 7, 10], 11))
