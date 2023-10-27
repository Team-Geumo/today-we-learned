# ECMA 2023

## 1. Array find from last

### find의 문제점

마지막부터 검색할때 array.reverse().find() 를 사용할 경우 문제점은 reverse 함수는 원본 배열을 변경한다.
원본 배열의 변경을 피하기 위해서는 […array].reverse().find() 를 사용할 수 있는데 이는 불필요한 복사본이 생긴다는 것이다.

### findIndex의 문제점

마지막부터 검색할때 […array].reverse().findIndex(0) 를 사용하게 되면 실제 index를 계산하는 과정이 추가로 필요해 계산이 복잡해진다.

```js
const arr = [1, 2, 3, 10, 5];

//8이 넘는 array 계산하기

const index = [...arr].reverse().findIndex((n) => n > 8); //1
const resultIndex = arr.length - 1 - index; //3, 원본 배열 기준 index를 구해야하기 때문에
```

### 결론

`Array.prototype.findLast` , `Array.prototype.findLastIndex` 은 `find`와 `findIndex`와 사용법은 똑같고 배열의 마지막부터 검색한다는 점만 다르다

## 2. HashBang grammer

### HashBang (Shebang)

script 시작 부분에 있는 `#!` 로 시작하는 문자 시퀀스.
`#!` 뒤의 내용은 인터프리터 지시문으로 분석된다.
유닉스 계열 운영체제에서 쓰이는 문법이다.

### 제안

Hashbang을 사용하는 CLI js host에서의 사용을 일치시키기 위한 제안임.
Hashbang을 허용하는 호스트는 javascript 엔진으로 지시문을 전달하기 위해 Hashbang을 제거한다.
이러한 절차를 통일화하고 표준화하기 위한 제안이다.

### 결론

Hashbang을 처리하는 절차를 통일화하고 표준화한다.

## 3. Symbols as WeakMap keys

### Symbol

object key로 사용되어 유일한 식별자를 만들수 있음.
ES6에서 도입된 7번째 데이터 타입으로 원시타입이다.

### 제안

WeakMap은 key가 반드시 객체여야함.
문제는 그 객체가 GC(Garbage Collection)의 대상이 되어 사라질 수도 있다는 것이다.

### 결론

Symbol을 WeakMap의 key로 사용할 수 있도록 WekMap API를 확장함

## 4. Change Array by Copy

### 제안

원본 배열을 수정하던 함수와 똑같은 기능을 하지만 새로운 배열을 반환하는 함수들을 추가함

### 결론

`Array.prototype.toReversed()` -> Array : 배열 뒤집기
`Array.prototype.toSorted(compareFn)` -> Array : 배열 정렬
`Array.prototype.toSpliced(start, deleteCount, ...items)` -> Array : 배열의 요소 삭제, 요소 추가
`Array.prototype.with(index, value)` -> Array : 배열의 index의 값 변경
`arr[index]` = value 대체
