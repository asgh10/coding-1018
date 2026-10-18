import datetime

travel = input("여행출발일이 올해 인가요: ")

if travel == "Yes":
  year = 2026
elif travel == "No":
  year = int(input("그럼 언제 인가요: "))
else:
  print("Yes or No로 답하세요 ( 대소문자도 맞춰 주세요 )")
  exit() 
  

month = int(input("몇달의 출발 하나요(숫자만): "))
day = int(input("몇일에 출발 하나요(숫자만): "))

today = datetime.datetime.now().date()
travel_day = datetime.datetime(year, month, day).date()

legend_day = travel_day - today

if legend_day.days > 0:
  print(f"여행 출발까지 {legend_day.days}일 남았습니다")
elif legend_day.days == 0:
  print("여행 당일입니다")
else:
  print("여행일이 이미 지났습니다")