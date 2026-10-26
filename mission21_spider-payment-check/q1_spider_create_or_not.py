print("--- Q1 ---")

# 1. 주어지는 자료 - 가격표와 조회 결과 넷
prices = {"거미 마스크": 33000, "거미줄 양말": 12500, "거미줄 머그컵": 17000}
results = [
    {"paymentId": "sp-01", "status": "PAID", "total": 33000, "items": [{"name": "거미 마스크", "qty": 1}]},
    {"paymentId": "sp-02", "status": "PAID", "total": 29500, "items": [{"name": "거미줄 머그컵", "qty": 1}, {"name": "거미줄 양말", "qty": 1}]},
    {"paymentId": "sp-03", "status": "PAID", "total": 1000, "items": [{"name": "거미 마스크", "qty": 2}]},
    {"paymentId": "sp-04", "status": "FAILED", "total": 0, "items": [{"name": "거미줄 양말", "qty": 3}]},
]

# 2. 결제마다 기준 금액을 세고 판정한다
for r in results:
    base = 0
    for item in r["items"]:
        base += prices[item["name"]] * item["qty"]

    if r["status"] != "PAID":
        decision = "만들지 않는다"
        reason = "결제가 완료되지 않았다"
    elif r["total"] != base:
        decision = "만들지 않는다"
        reason = "결제 금액이 기준 금액과 다르다"
    else:
        decision = "만든다"
        reason = "검증 통과"

    print(r["paymentId"], "· 기준 금액", base, "·", decision, "·", reason)
