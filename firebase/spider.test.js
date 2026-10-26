// 스파이더맨 상점 Firestore 보안 규칙 테스트 - 통과 3 / 차단 3

// 1. 쓸 도구 불러오기
import { readFileSync } from "node:fs";
import { test, before, beforeEach, after } from "node:test";
import {
  initializeTestEnvironment,
  assertSucceeds,
  assertFails,
} from "@firebase/rules-unit-testing";
import { doc, getDoc, setDoc, updateDoc } from "firebase/firestore";

// 2. 어느 규칙 판으로 돌릴지 고르는 한 줄
const RULES = "spider.rules";

let testEnv;

// 3. 테스트 환경 만들기 - 데모 프로젝트에 규칙 파일을 읽힌다
before(async () => {
  testEnv = await initializeTestEnvironment({
    projectId: "demo-spider-shop",
    firestore: { rules: readFileSync(RULES, "utf8") },
  });
});

// 4. 테스트마다 가게를 비우고 문서 두 장을 넣어 둔다 - 규칙을 끈 채로
beforeEach(async () => {
  await testEnv.clearFirestore();
  await testEnv.withSecurityRulesDisabled(async (context) => {
    const db = context.firestore();
    await setDoc(doc(db, "products/s1"), { name: "거미줄 키링", price: 9000, stock: 5 });
    await setDoc(doc(db, "orders/o1"), { userId: "b", totalPrice: 9000, status: "placed" });
  });
});

// 5. 다 끝나면 테스트 환경 정리
after(async () => {
  await testEnv.cleanup();
});

// 6. 통과 테스트 셋 (Q3)
test("1. 로그인 안 한 사람이 상품 s1 을 읽는다", async () => {
  const guest = testEnv.unauthenticatedContext();
  await assertSucceeds(getDoc(doc(guest.firestore(), "products/s1")));
});

test("2. a 가 자기 이름으로 주문을 만든다", async () => {
  const a = testEnv.authenticatedContext("a");
  await assertSucceeds(setDoc(doc(a.firestore(), "orders/o2"), { userId: "a", totalPrice: 9000, status: "placed" }));
});

test("3. 점원 k 가 o1 의 상태를 packing 으로 바꾼다", async () => {
  const k = testEnv.authenticatedContext("k", { role: "clerk" });
  await assertSucceeds(updateDoc(doc(k.firestore(), "orders/o1"), { status: "packing" }));
});

// 7. 차단 테스트 셋 (Q4) - 바로 아래 줄과 맨 아래 줄을 지우면 살아난다
test("4. a 가 b 의 주문 o1 을 읽는다", async () => {
  const a = testEnv.authenticatedContext("a");
  await assertFails(getDoc(doc(a.firestore(), "orders/o1")));
});

test("5. a 가 상품 s1 의 가격을 1원으로 바꾼다", async () => {
  const a = testEnv.authenticatedContext("a");
  await assertFails(updateDoc(doc(a.firestore(), "products/s1"), { price: 1 }));
});

test("6. b 가 자기 주문 o1 의 상태를 sent 로 바꾼다", async () => {
  const b = testEnv.authenticatedContext("b");
  await assertFails(updateDoc(doc(b.firestore(), "orders/o1"), { status: "sent" }));
});
