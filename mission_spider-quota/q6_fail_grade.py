fail_counts = [
    0, 2, 7, 1, 12,
    0, 4, 6, 0, 3,
    0, 9, 1, 0, 5,
    8, 0, 2, 0, 1,
]

lock_line = 5
total = len(fail_counts)
normal = 0
caution = 0
locked = 0

for failures in fail_counts:
    if failures > lock_line:
        locked += 1
    elif failures > 0:
        caution += 1
    else:
        normal += 1

locked_rate = locked / total * 100

print(f"전체 {total}명")
print(f"정상 {normal}명")
print(f"주의 {caution}명")
print(f"잠금 {locked}명")
print(f"잠금 비율 {locked_rate}%")
