def solution(phone_number):
    list = [i for i in phone_number]
    for i in range(len(list)-4):
        list[i] = '*'
    answer = ''.join(list)
    return answer

# 더 간단한 풀이
# def solution(phone_number):
#     return '*'*(len(phone)-4) + phone[-4:])
# 문자열이 곱셈이 되고, 문자열도 [-4:]와 같이 표현할 수 있다는 것을 몰랐다.
# 그래서 리스트로 만들어 풀었는데 생각보다 string 타입도 리스트처럼 쓸 수 있는 방법이 많은 것 같다.
