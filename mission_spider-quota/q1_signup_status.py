total_users = 250
verified_users = 200
goal_rate = 70

unverified_users = total_users - verified_users
verified_rate = verified_users / total_users * 100
is_goal_met = verified_rate > goal_rate

print(f"가입자 수 {total_users}명")
print(f"인증 안 한 가입자 수 {unverified_users}명")
print(f"인증 비율 {verified_rate}%")
print(f"목표 달성 {is_goal_met}")
