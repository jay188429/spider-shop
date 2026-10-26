import pandas as pd

print("--- Q4 ---")

# 1. 결제 장부와 주문 장부를 불러온다
payments = pd.read_csv("mission21_spider-payment-check/spider_payments.csv")
orders = pd.read_csv("mission21_spider-payment-check/spider_orders.csv")

# 2. 실패한 결제를 빼고, 실제 받은 돈을 계산한다
payments = payments[payments["status"] != "FAILED"].copy()
payments["net"] = payments["paidAmount"] - payments["cancelledAmount"]

# 3. paymentId 기준으로 양쪽 장부를 모두 남기며 맞붙인다
payment_amounts = payments[["paymentId", "net"]]
merged = pd.merge(payment_amounts, orders, on="paymentId", how="outer")

# 4. 한쪽 장부에만 있는 금액은 0으로 채운다
merged["net"] = merged["net"].fillna(0)
merged["paidAmount"] = merged["paidAmount"].fillna(0)

# 5. 두 장부의 금액을 나란히 출력한다
print(merged[["paymentId", "net", "paidAmount"]])

# 6. 금액이 서로 다른 결제 ID를 찾는다
mismatch = merged[merged["net"] != merged["paidAmount"]]
print(mismatch["paymentId"])

# 7. 받은 돈 합계, 주문 합계, 차액을 출력한다
received_total = merged["net"].sum()
order_total = merged["paidAmount"].sum()
difference = order_total - received_total
print(received_total, order_total, difference)
