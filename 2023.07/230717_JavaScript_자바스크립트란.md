# 자바스크립트란?
## 2.1 자바스크립트의 탄생
1995년 넷스케이프 커뮤니케이션즈가 도입한 브라우저에서 동작하는 경량 프로그래밍 언어<br>
현재 모든 브라우저의 표준 프로그래밍 언어로 자리 잡음

**이름 변천사** : 모카(Mocha) > 라이브스크립트(LiveScript) > 자바스크립트(JavaScript)

## 2.2 자바스크립트의 표준화
**배경 및 필요성**
- 마이크로소프트에서 자바스크립트의 파생 버전인 JScript를 만들어 인터넷 익스플로러에 탑재함
- 자바스크립트와 JScript는 서로 표준화 되지 못하고 자사 브라우저에서만 동작하는 기능을 경쟁적으로 추가
- **크로스 브라우징 이슈**가 발생해 모든 브라우저에서 정상적으로 동작하는 웹페이지를 개발하기 어려워짐
- 자바스크립트의 파편화를 방지하고 모든 브라우저에서 정상적으로 동작하는 표준화된 자바스크립트의 필요성이 대두됨

**표준화**
- 넷스케이프 커뮤니케이션즈에서 컴퓨터 시스템의 표준을 관리하는 비영리 표준화 기구인 **ECMA 인터내셔널**에 자바스크립트의 표준화를 요청
- 1997년 7월, **ECMA-262**라고 불리는 표준화된 자바스크립이 완성됨
- 상표권 문제로 **ECMAScript**로 명명

**ECMAScript의 버전별 특징**

|버전|출시 연도|특징|
|--|--|--|
|ES1|1997|초판|
|ES2|1998|ISO/IEC 16262 국제 표준과 동일한 규격을 적용|
|ES3|1999|정규 표현식, try ... catch|
|ES4|Abandoned|class(static, final, private, protected, public, prototype, generic function), interface, strict typing, E4X|
|ES5|2009|HTML5와 함께 출현한 표준안<br>JSON, strict mode, 접근자 프로퍼티, 프로퍼티 어트리뷰트 제어, 향상된 배열 조작 기능(forEach, map, filter, reduce, some, every)|
|ES6|2015|let/const, 클래스, 화살표 함수, 템플릿 리터럴, 디스트럭처링 할당, 스프레드 문법, rest 파라미터, 심벌, 프로미스, Map/Set, 이터러블, for ... of, 제너레이터, Proxy, 모듈 import/export|
|ES7|2016|지수 연산자(**), Array.prototype.includes,<br> String.prototype.includes|
|ES8|2017|async/await, Object 정적 메서드(values, entries, getOwnPropertyDescriptors)|
|ES9|2018|Object rest/spread 프로퍼티, Promise.prototype.finally, async generator, for awiat ... of|
|ES10|2019|Object.fromEntries, Array.prototype.flat, Array.prototype.flatMap, optional catch binding|
|ES11|2020|String.prototype.matchAll, BigInt, globalThis, Promise.allSettled, null 병합 연산자, 옵셔널 체이닝 연산자, for ... in enumeration order|
