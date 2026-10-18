import datetime

# 1. 일반 datetime.now() (시간까지 포함)
now_dt = datetime.datetime.now()
print("시간 포함:", now_dt) 
# 출력 예: 2026-10-18 15:45:12.123456

# 2. .date()를 붙인 경우 (날짜만 포함)
now_d = datetime.datetime.now().date()
print("날짜만 추출:", now_d) 
# 출력 예: 2026-10-18 (시간이 사라졌죠?)

'''
.date()는 년-월-일 을 추출해내는 즉 우리가 보통 사용하는 날짜만 추출하는코드이다
보통 코딩에선 .now()써서 밀리초까지 불러오지만 밀리초까진 잘 안쓰기에 .date()를 써서 년도와 월,일만 가져오게 만든 기능중 한 개다
'''