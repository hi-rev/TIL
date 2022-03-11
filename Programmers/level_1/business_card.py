# 명함 지갑 만들기
# 1. 각 리스트의 요소를 모두 정렬
# 2. 0번째 항목 중 가장 큰 것 X 1번째 항목 중 가장 큰 것

def solution(sizes):
    sizes_w = [max(i) for i in sizes]
    sizes_h = [min(i) for i in sizes]
    return max(sizes_w) * max(sizes_h)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
