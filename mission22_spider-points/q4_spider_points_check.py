print("--- Q4 ---")

# 1. 주어지는 자료 - 코드가 센 숫자 둘과 AI가 쓴 안내 문장 두 판
REPORT_FILE = "mission22_spider-points/points_check_20261022.txt"
final_price = 28300
points_left = 300
messages = [
    "sp-13 결제는 28300원, 남은 포인트는 300점입니다.",
    "sp-13 결제는 28,300원, 남은 포인트는 300점입니다.",
]


# 2. 대조한다
def check(message, final_price, points_left):
    if str(final_price) in message:
        price_check = f"검산 결제 {final_price}원 : O"
    else:
        price_check = f"검산 결제 {final_price}원 : X"

    if f"{points_left}점" in message:
        points_check = f"검산 남은 포인트 {points_left}점 : O"
    else:
        points_check = f"검산 남은 포인트 {points_left}점 : X"

    return price_check, points_check


# 3. 남긴다
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    for message in messages:
        price_check, points_check = check(message, final_price, points_left)

        print("AI 문장 :", message)
        print(price_check)
        print(points_check)

        f.write(f"AI 문장 : {message}\n")
        f.write(price_check + "\n")
        f.write(points_check + "\n")

print("보고 파일을 만들었습니다 :", REPORT_FILE)


