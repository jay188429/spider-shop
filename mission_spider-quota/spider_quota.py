daily_visitors = 900
reads_per_visit = 15
free_reads = 50000

# 평상시 계산
daily_reads = daily_visitors * reads_per_visit
remain = free_reads - daily_reads
is_over = daily_reads > free_reads

# 행사일 계산: 방문 수가 평상시의 네 배
event_visitors = daily_visitors * 4
event_reads = event_visitors * reads_per_visit
event_remain = free_reads - event_reads
event_is_over = event_reads > free_reads

print(f"평상시 하루 읽기 {daily_reads:,}회")
print(f"평상시 남은 한도 {remain:,}회")
print(f"평상시 넘었나 {is_over}")

print(f"행사일 하루 읽기 {event_reads:,}회")
print(f"행사일 남은 한도 {event_remain:,}회")
print(f"행사일 넘었나 {event_is_over}")
