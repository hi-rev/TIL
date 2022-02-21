def solution(s):
    return ''.join(sorted(s)[::-1])

# sorted(s): 문자열(s)을 리스트로 변환 후 정렬함
# [::-1] => 리스트 역순
