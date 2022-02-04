def solution(n):
    num = [i for i in str(n)] # num = list(str(n))
    num.sort(reverse=True)
    return int(''.join(num))

# 굳이 for문으로 리스트를 만들어주지 않아도
# list()로 간단하게 스트링->리스트 변환 가능
