print("--- Q3 ---")

# 1. 주어지는 자료 - 포인트를 쓰려는 주문 둘
# 주문 ID · 주문 금액 · 가진 포인트 · 쓰려는 포인트
# sp-11 · 45500 · 2000 · 1500
# sp-12 · 17000 · 800 · 3000

# 2. 클래스 만들기
class PointOrder:
    def __init__(self, order_id, total_price, points, use_points):
        self.order_id = order_id
        self.total_price = total_price
        self.points = points
        self.use_points = use_points

    def final_price(self):
        return self.total_price - self.use_points

    def points_left(self):
        return self.points - self.use_points

    def summary(self):
        if self.use_points > self.points:
            return f"{self.order_id} · 거절 · 가진 포인트 {self.points}점보다 많이 쓸 수 없습니다"
        return f"{self.order_id} · 결제 {self.final_price()}원 · 남은 포인트 {self.points_left()}점"


# 3. 인스턴스로 메서드 부르기
order1 = PointOrder("sp-11", 45500, 2000, 1500)
order2 = PointOrder("sp-12", 17000, 800, 3000)

print(order1.summary())
print(order2.summary())
