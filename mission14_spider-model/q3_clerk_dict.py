# 1. 함수
def can_refund(role):
    return role == "manager"


# 2. 딕셔너리
clerk = {
    "nickname": "웹슈터",
    "role": "clerk",
    "email": "clerk01@example.com",
    "createdAt": "2026-09-28",
}


# 3. 함수 호출
print(can_refund(clerk["role"]))


# 4. 멤버십 연산자
print("role" in clerk)
print("grade" in clerk)


# 5. 딕셔너리 반복
for key, value in clerk.items():
    print(f"{key} : {value}")
