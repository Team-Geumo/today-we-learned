# [PRO] JadenCase 문자열 만들기

## 1. 문제 출처

[pro_JadenCase_문자열_만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12951)


<br>

## 2. solution.js

```javascript
function solution(s) {
  return s
    .toLowerCase()
    .split(" ")
    .map((e) => e.substr(0, 1).toUpperCase() + e.substr(1))
    .join(" ");
}
```

### 2.1. 틀린 풀이

```javascript
function solution(s) {
  return s
    .toLowerCase()
    .split(" ")
    .map((e) => e.replace(e[0], e[0].toUpperCase()))  // e[0]이 없는 경우 -> undefined라서 런타임에서 발생
    .join(" ");
}
```