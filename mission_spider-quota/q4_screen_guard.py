guard_list = [False, False, False, False, False, False, True, True]
is_logged_in = False

no = 0
shown = 0
blocked = 0

for has_guard in guard_list:
    no += 1

    if has_guard and not is_logged_in:
        print(f"{no}번 화면: 로그인 화면으로 보낸다")
        blocked += 1
    else:
        print(f"{no}번 화면: 그대로 보여 준다")
        shown += 1

print(f"보여 준 화면 {shown}장")
print(f"돌려보낸 화면 {blocked}장")
