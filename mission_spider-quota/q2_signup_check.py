has_at_sign = True
pw_length = 4
is_joined = False
min_length = 6

is_short = pw_length < min_length

if not has_at_sign:
    message = "이메일 주소에 @ 가 들어갔는지 봐 주세요."
elif is_joined:
    message = "이미 가입된 이메일이에요. 로그인 화면에서 들어와 주세요."
elif is_short:
    message = f"비밀번호는 {min_length}자 이상으로 정해 주세요."
else:
    message = "가입됐어요. 메일함에서 인증 메일을 확인해 주세요."

can_join = has_at_sign and not is_joined and not is_short
can_fix_here = not has_at_sign or is_short

print(f"고객 안내: {message}")
print(f"가입할 수 있나 {can_join}")
print(f"칸을 고쳐 다시 누르면 되나 {can_fix_here}")
