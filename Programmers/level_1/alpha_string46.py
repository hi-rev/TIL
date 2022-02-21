import re
def solution(s):
    if re.findall('[a-zA-Z]', s): # 문자열에 문자가 존재하면 True
        return False
    elif len(s) != 4 and len(s) != 6:
        return False
    else:
        return True

def solution1(s):
    return s.isdigit() and len(s) in (4, 6)

# str.isdigit(): 해당 문자열이 모두 숫자일 때 True를 반환
# len(s) in (4, 6)은 len(s) == 4 or len(s) == 6과 동일
# len(s) 값이 4 또는 6에 포함 되어 있는지를 확인

# ==> 문자열이 모두 숫자이고, 길이가 4 또는 6일때 True를 반환
