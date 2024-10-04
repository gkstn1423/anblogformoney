// 필요한 함수 가져오기
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// 웹 앱의 Firebase 구성
const firebaseConfig = {
  apiKey: "AIzaSyBY8RcFFWF4xtIyunlxAITZ3g1ugL_GPIs",
  authDomain: "blog-3927c.firebaseapp.com",
  projectId: "blog-3927c",
  storageBucket: "blog-3927c.appspot.com",
  messagingSenderId: "759887722779",
  appId: "1:759887722779:web:455e08e25bfbbc0476bbbe",
  measurementId: "G-XZ491HTJBV"
};

// Firebase 초기화
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
