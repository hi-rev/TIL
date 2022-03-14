# 2016년 요일 찾기
# 2016년 1월 1일은 금요일
# SUN,MON,TUE,WED,THU,FRI,SAT
from datetime import datetime

def solution(a, b):
    date = '2016-{0}-{1}'.format(a, b) # 날짜
    datetime_date = datetime.strptime(date, '%Y-%m-%d') # 날짜의 타입을 datetime형으로 변경
    dateDict = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    return dateDict[datetime_date.weekday()]

# 1년 중 첫 시작 요일을 알기 때문에
# 이전 달까지 모두 더하고, 일 수를 더한 후 7로 나눠주면 요일을 알 수 있다.
# 조건이 1년 내이고, 첫번째 날의 요일을 알기 때문에 이런 연산 방법이 더 적합할 것 같다.
def solution1(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

print(solution(5,24))
