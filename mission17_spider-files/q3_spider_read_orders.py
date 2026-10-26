# 1. 예외 처리와 파일 읽기
try:
    with open("mission17_spider-files/spider_orders.csv", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. 주문 건수와 합계 계산
    count = 0
    total = 0

    for line in lines[1:]:
        row = line.strip().split(",")
        count += 1
        total += int(row[3])

    # 3. 결과 출력
    print(f"주문 {count}건")
    print(f"합계 {total:,}원")

except FileNotFoundError:
    # 4. 파일을 찾지 못했을 때
    print("스파이더맨 상점 주문 파일을 찾을 수 없습니다.")
