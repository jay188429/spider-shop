created = "2026-12-24"

print(created[0:4])
print(created[5:7])
print(created[8:10])

orders = []
for i in range(1, 31):
    orders.append(i)
print(len(orders))

for start in range(0, 30, 8):
    print(start)

start = 0
page = 0
reads = 0

while True:
    chunk = orders[start:start + 8]
    if not chunk:
        break

    page += 1
    reads += len(chunk)
    print(f"{page}쪽 {len(chunk)}건 누적 읽기 {reads}")
    start += 8
