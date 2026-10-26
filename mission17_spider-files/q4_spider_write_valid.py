import csv

# 1. 전체 주문 읽기
rows = []
with open("mission17_spider-files/spider_orders.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

print(len(rows))

# 2. 취소되지 않은 주문만 남기기
valid_rows = [rows[0]]
for row in rows[1:]:
    if row[4] != "void":
        valid_rows.append(row)

print(len(valid_rows))

# 3. 파일 이름 만들기
date_text = "2026-11-05".replace("-", "")
file_name = "_".join(["spider", "valid", date_text]) + ".csv"

# 4. 새 CSV 저장
with open(
    f"mission17_spider-files/{file_name}",
    "w",
    newline="",
    encoding="utf-8-sig",
) as f:
    writer = csv.writer(f)
    for row in valid_rows:
        writer.writerow(row)

print(f"{file_name} 저장")
