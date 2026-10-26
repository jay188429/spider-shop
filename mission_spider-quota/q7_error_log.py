error_log = [
    "auth/invalid-credential",
    "auth/weak-password",
    "auth/invalid-credential",
    "auth/email-already-in-use",
    "auth/too-many-requests",
    "auth/invalid-credential",
    "auth/weak-password",
    "auth/invalid-email",
    "auth/invalid-credential",
    "auth/email-already-in-use",
    "auth/weak-password",
    "auth/invalid-credential",
]

total = len(error_log)
wrong_login = 0
weak_pw = 0
joined = 0
others = 0

for error_code in error_log:
    if error_code == "auth/invalid-credential":
        wrong_login += 1
    elif error_code == "auth/weak-password":
        weak_pw += 1
    elif error_code == "auth/email-already-in-use":
        joined += 1
    else:
        others += 1

if wrong_login > weak_pw and wrong_login > joined:
    first_fix = "로그인 정보 불일치"
elif weak_pw > wrong_login and weak_pw > joined:
    first_fix = "비밀번호 기준 미달"
else:
    first_fix = "이미 가입된 이메일"

print(f"전체 오류 {total}건")
print(f"로그인 정보 불일치 {wrong_login}건")
print(f"비밀번호 기준 미달 {weak_pw}건")
print(f"이미 가입된 이메일 {joined}건")
print(f"그 밖 {others}건")
print(f"먼저 고칠 것: {first_fix}")
