orders = [
    {"totalPrice": 40500, "status": "placed"},
    {"totalPrice": 81000, "status": "void"},
    {"totalPrice": 12500, "status": "placed"},
    {"totalPrice": 53000, "status": "sent"},
]

total = 0
for order in orders:
    total += order["totalPrice"]

live_total = 0
live_count = 0
for order in orders:
    if order["status"] != "void":
        live_total += order["totalPrice"]
        live_count += 1

print(f"전체 합계 {total:,}원")
print(f"취소 빼고 합계 {live_total:,}원")
print(f"취소 빼고 {live_count}건")
