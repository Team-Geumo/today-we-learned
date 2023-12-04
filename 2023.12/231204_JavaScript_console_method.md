# JavaScript console method

## console method 목록 확인하기

```js
console.log(console);
```

## console 함수 목록

### 1. clear

콘솔 창에 입력된 모든 것들을 초기화 함

특정 시점부터의 디버깅이 필요한 경우 해당 시점의 맨 앞에서 실행시켜주면 콘솔 확인이 편리함

```js
console.log(document.body);

console.clear();

const data = { a: 1, b: 5 };
console.log(data);
```

### 2. 로그 레벨 - debug / info / warn / error

```js
console.debug('debug test');
console.info('info test');
console.warn('warn test');
console.error('error test');
```

### 3. 카운트 체크 - count / countReset

`console.count()` 를 사용해서 이벤트, 함수 등의 실행 횟수를 체크할 수 있음

param 로는 라벨을 입력받을 수 있는데 받지 않더라도 `default` 로 카운트가 체크됨

라벨을 입력할 경우 해당 라벨에 대한 카운트가 올라가며, 입력하지 않을 때에도 동일하게 `default` 에 대한 카운트가 올라감

초기화는 `console.countReset(label)`

```js
console.count('myLabel'); // myLabel: 1
console.count(); // default: 1
console.count('myLabel'); // myLabel: 2
console.count('myLabel2'); // myLabel2: 1
console.count('default'); // default: 2
console.countReset('myLabel');
console.countReset('myLabel2');
console.countReset();
```

### 4. 시간 체크 - time / timeLog / timeEnd

count 와 마찬가지로 라벨을 받을 수 있고 받지 않으면 `default` 로 표시됨

시간 체크를 시작할 떄 `console.time()` 을 사용

중간 시간을 체크할 때 `console.timeLog()`를 사용

타이머 종료를 원할 때 `console.timeEnd()`를 사용

```js
console.time('myTimer');
console.timeLog('myTimer');
console.timeEnd('myTimer');
```

### 5. 콘솔 출력의 그룹핑 - group / groupCollapsed / groupEnd

console.group()은 console 의 method 들을 그룹화 함
console.groupCollapsed()은 사용하면 처음부터 그룹이 닫혀진 상태로 출력함

```js
console.group('myGroup');
console.groupEnd('myGroup');

console.groupCollapsed('myCollapsedGroup');
console.groupEnd('myCollapsedGroup');
```

그룹 내에서 호출된 함수가 console 을 사용하는 경우 해당 내용도 그룹에 포함됨

```js
function taskA() {
    console.log('execute taskA');
}

function taskB() {
    console.log('execute taskB');
}

console.group('myTask');
taskA();
taskB();
console.groupEnd('myTask');
```
