# 문자열 s에서 'p'의 개수와 'y'의 개수를 비교해 같으면 true, 다르면 false
def solution(s):
    s_low = s.lower()
    cnt_p = 0
    cnt_y = 0

    for i in s_low:
        if i == 'p':
            cnt_p += 1
        elif i == 'y':
            cnt_y += 1

    return cnt_p == cnt_y

def solution1(s): # count 사용
    s_low = s.lower()
    return s_low.count('p') == s_low.count('y')

print(solution('pPoooyY'))
print(solution1('pPoooyY'))
