import csv

daily_visitors = 900
hidden_product_id = "s4"
free_storage_kb = 5_000_000
free_download_gb = 100
free_download_count = 50_000

with open("mission17_spider-files/spider_photo_sizes.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

total_kb = sum(int(row["sizeKB"]) for row in rows)
hidden_kb = next(int(row["sizeKB"]) for row in rows if row["productId"] == hidden_product_id)
visible_rows = [row for row in rows if row["productId"] != hidden_product_id]
list_kb = total_kb - hidden_kb
monthly_gb = list_kb * daily_visitors * 30 / 1_000_000
monthly_count = len(visible_rows) * daily_visitors * 30

print(f"올려 둔 사진 {len(rows)}장")
print(f"담아 둔 양 {total_kb:,}KB")
print(f"목록에서 받는 양 {list_kb:,}KB")
print(f"한 달 내려받는 양 {monthly_gb:.2f}GB")
print(f"한 달 내려받는 횟수 {monthly_count:,}회")
