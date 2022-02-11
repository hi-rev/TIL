def solution(seoul):
    # 다른 자료형 끼리는 합칠 수 없으므로 인덱스 값을 str로 변환해주어야 한다.
    return '김서방은 ' + str(seoul.index('Kim')) + '에 있다'

# 포맷팅 방법 ======>
# '김서방은 {}에 있다'.format(seoul.index('Kim'))도 가능!
# ===> 이게 더 직관적이고 편리한듯? format이 익숙해지도록 해야겠다.
