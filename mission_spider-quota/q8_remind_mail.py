wait_days = [1, 3, 8, 15, 2, 30, 7, 10, 4, 12]

resend_line = 6
close_line = 14
mail_limit = 3

no = 0
waiting = 0
resend = 0
closing = 0

for days in wait_days:
    no += 1

    if days > close_line:
        action = "계정 정리 안내를 보낸다"
        closing += 1
    elif days > resend_line:
        action = "인증 메일을 다시 보낸다"
        resend += 1
    else:
        action = "기다린다"
        waiting += 1

    print(f"{no}번 계정: 가입 {days}일째 - {action}")

print(f"기다린다 {waiting}명")
print(f"인증 메일을 다시 보낸다 {resend}명")
print(f"계정 정리 안내를 보낸다 {closing}명")

if resend > mail_limit:
    later = resend - mail_limit
    print(f"한도 {mail_limit}통 - {later}통은 미룬다")
else:
    print(f"한도 {mail_limit}통 - 모두 보낸다")
