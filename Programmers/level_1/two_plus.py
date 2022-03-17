# numbers 리스트로 만들 수 있는 모든 합의 경우의 수
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    return answer

print(solution([2,1,3,4,1]))
