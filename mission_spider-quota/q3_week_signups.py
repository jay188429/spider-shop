week_signups = [12, 9, 15, 10, 21, 33, 26]
daily_goal = 15

days = len(week_signups)
total = 0

for signup in week_signups:
    total += signup

average = total / days

if average > daily_goal:
    result = "넘었습니다"
else:
    result = "넘지 못했습니다"

print(f"일주일 가입자 합계 {total}명")
print(f"하루 평균 {average}명")
print(f"하루 목표를 {result}")
