products = [
    {"id": "s1", "name": "스파이더맨 피규어", "price": 45000, "stock": 2, "isVisible": True},
    {"id": "s2", "name": "거미줄 양말", "price": 12500, "stock": 0, "isVisible": True},
    {"id": "s3", "name": "거미 마스크", "price": 33000, "stock": 4, "isVisible": True},
    {"id": "s4", "name": "웹슈터 장난감", "price": 53000, "stock": 7, "isVisible": False},
    {"id": "s5", "name": "거미줄 머그컵", "price": 17000, "stock": 11, "isVisible": True},
]

# 1. 상품 수
print(len(products))

# 2. 보이는 상품만 필터링
visible = []
for p in products:
    if p["isVisible"]:
        visible.append(p)
print(len(visible))

# 3. 이름이 거미로 시작하는 상품 수
count = 0
for p in visible:
    if p["name"].startswith("거미"):
        count += 1
print(count)

# 4. 가격을 돌려주는 함수로 정렬
def get_price(p):
    return p["price"]


visible.sort(key=get_price)

# 5. 가장 싼 상품 두 개 출력
top2 = visible[:2]
for p in top2:
    print(f"{p['name']} {p['price']}")
