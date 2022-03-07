# 문자열 가운데 수 반환
def solution(s):
    a = len(s)
    if a % 2 == 0:
        return ''.join([s[a//2-1], s[a//2]])
    else:
        return s[a//2]

print(solution('abcdef'))
