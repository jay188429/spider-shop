free_reads = 50000
daily_reads = [41000, 56000, 38000, 62500, 50000, 71000, 44500]

over_days = 0
over_total = 0
max_reads = 0

for reads in daily_reads:
    if reads > free_reads:
        over = reads - free_reads
        print(f"{reads:,}회 읽혀 {over:,}회 넘었습니다")
        over_days += 1
        over_total += over

    if reads > max_reads:
        max_reads = reads

print(f"넘은 날 {over_days}일")
print(f"넘은 횟수 합계 {over_total:,}회")
print(f"가장 큰 읽기 횟수 {max_reads:,}회")
