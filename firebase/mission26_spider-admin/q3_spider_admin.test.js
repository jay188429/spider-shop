import { readFileSync } from "node:fs";
import { test, before, beforeEach, after } from "node:test";
import {
  initializeTestEnvironment,
  assertSucceeds,
  assertFails,
} from "@firebase/rules-unit-testing";
import { doc, getDoc, setDoc, updateDoc, deleteDoc } from "firebase/firestore";

const RULES = new URL("./q3_spider_admin.rules", import.meta.url);

let testEnv;

before(async () => {
  testEnv = await initializeTestEnvironment({
    projectId: "demo-spider-shop",
    firestore: { rules: readFileSync(RULES, "utf8") },
  });
});

beforeEach(async () => {
  await testEnv.clearFirestore();
  await testEnv.withSecurityRulesDisabled(async (context) => {
    const db = context.firestore();
    await setDoc(doc(db, "products/s1"), {
      name: "거미줄 키링",
      price: 9000,
      stock: 5,
      isVisible: true,
    });
  });
});

after(async () => {
  await testEnv.cleanup();
});

test("1. 로그인 안 한 사람이 상품 s1 을 읽는다", async () => {
  const guest = testEnv.unauthenticatedContext();
  await assertSucceeds(getDoc(doc(guest.firestore(), "products/s1")));
});

test("2. 점원 k 가 s1 의 가격을 9500 으로 바꾼다", async () => {
  const k = testEnv.authenticatedContext("k", { role: "clerk" });
  await assertSucceeds(updateDoc(doc(k.firestore(), "products/s1"), { price: 9500 }));
});

test("3. 손님 a 가 주문하며 s1 의 재고를 4 로 줄인다", async () => {
  const a = testEnv.authenticatedContext("a");
  await assertSucceeds(updateDoc(doc(a.firestore(), "products/s1"), { stock: 4 }));
});

test("4. 손님 a 가 s1 의 가격을 1원으로 바꾼다", async () => {
  const a = testEnv.authenticatedContext("a");
  await assertFails(updateDoc(doc(a.firestore(), "products/s1"), { price: 1 }));
});

test("5. 손님 a 가 재고를 4 로 줄이면서 가격도 1원으로 바꾼다", async () => {
  const a = testEnv.authenticatedContext("a");
  await assertFails(updateDoc(doc(a.firestore(), "products/s1"), { stock: 4, price: 1 }));
});

test("6. 점장 m 이 상품 s1 을 지운다", async () => {
  const m = testEnv.authenticatedContext("m", { role: "manager" });
  await assertFails(deleteDoc(doc(m.firestore(), "products/s1")));
});
