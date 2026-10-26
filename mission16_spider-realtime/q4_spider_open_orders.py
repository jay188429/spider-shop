orders = [
    {"id": "o1", "status": "placed"},
    {"id": "o2", "status": "sent"},
    {"id": "o3", "status": "packing"},
    {"id": "o4", "status": "void"},
    {"id": "o5", "status": "placed"},
]

# 1. 끝난 상태값 리스트 만들기
done_values = ["sent", "void"]

# 2. 끝나지 않은 주문 세기
open_ids = []
count = 0

for order in orders:
    if order["status"] not in done_values:
        count += 1
        open_ids.append(order["id"])

# 3. 끝나지 않은 주문 수 출력
print(count)

# 4. 끝나지 않은 주문 ID 출력
for open_id in open_ids:
    print(open_id)
