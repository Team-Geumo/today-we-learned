# 08장 제어문
**제어문(control flow statement)** 은 조건에 따라 코드 블록을 실행(**조건문**)하거나 반복 실행(**반복문**)할 때 사용

## 8.1 블록문(block statement/compound statement)
0개 이상의 문을 중괄호로 묶은 것으로 **코드 블록** 또는 **블록**이라고 함<br>
단독으로 사용할 수도 있으나 일반적으로 **제어문이나 함수를 정의할 때 사용**<br>
- 블록문은 언제나 문의 종료를 의미하는 자체 종결성을 갖기 때문에 세미콜론을 붙이지 않음

	```js
	{
		var foo = 10;
	}
	```

## 8.2 조건문(conditional stsatement)
주어진 조건식의 평가 결과에 따라 코드 블록의 실행을 결정<br>
**조건식(conditional expression)** : 불리언 값으로 평가될 수 있는 표현식<br>

### 8.2.1 if ... else 문
주어진 조건식의 평가 결과에 따라 실행할 코드 블록을 결정함
```js
if (조건식1) {
	// 조건식1이 참이면 이 코드 블록을 실행
} else if (조건식2) {
	// 조건식1이 참이면 이 코드 블록을 실행
} else {
	// 조건식 1과 조건식 2가 모두 거짓이면 이 코드 블록을 실행
}
```
- 만약 코드 블록 내의 문이 하나 뿐이라면 중괄호를 생략할 수 있음

	```js
	var num = 2;
	var kind;

	if (num > 0) 		  kind = 'plus';
	else if (num < 0) kind = 'minus';
	else 						  kind = 'zero';

	console.log(kind); // plus
	```

- 대부분의 `if ... else` 문은 삼항 조건 연산자로 바꿔 쓸 수 있음

	```js
	var kind = num > 0 ? 'plus' : num < 0 ? 'minus' : 'zero';
	```

### 8.2.2 switch 문
주어진 표현식을 평가하여 그 값과 일치하는 표현식을 갖는 `case` 문으로 실행 흐름을 옮김<br>
표현식과 일치하는 `case` 문이 없다면 `default` 문으로 이동 (선택 사항)
```js
switch (표현식) {
	case 표현식1:
		표현식과 표현식1이 일치하면 실행되는 문;
		break;
	case 표현식2:
		표현식과 표현식2가 일치하면 실행되는 문;
		break;
	default:
		표현식1, 표현식2 모두 표현식과 일치하지 않을 때 실행되는 문;
}
```
- **폴스루(fall through)** : 평가 결과가 일치하는 `case` 문으로 흐름이 이동한 이후에도 `switch` 문을 탈출하지 않고 이후 모든 `case` 문과 `default` 문을 실행하는 것으로, `break` 문을 사용해 방지할 수 있음

	```js
	var index = 1;
	var indexName;
	
	switch (index) {
		case 1: indexName = 'First';
		case 2: indexName = 'Second';
		case 3: indexName = 'Third';
		default indexName = 'Invalid index';
	}

	console.log(indexName); // Invalid index : defalt 문까지 실행한 결과
	```

- 폴스루를 활용해 여러 개의 `case` 문을 하나의 조건으로 사용할 수도 있음

	```js
	var number = 3;

	switch (month) {
		case 1: case 3: case 5: case 7: case :
			days = 31;
			break;
		case 4: case 6: case 9: case 11:
			days = 30;
			break;
		case 2:
			days = ((year % ))
	}
	```

## 8.3 반복문(loop statement)
조건식의 평가 결과가 참인 경우 코드 블록을 실행한 후 **조건식이 거짓이 되기 전까지 반복함**<br>
자바스크립트는 세 가지 반복문 `for` 문, `while` 문, `do ... while` 문을 제공함<br>

### 8.3.1 for 문
**for 문의 형식**
```js
for (변수 선언 문 또는 할당문; 조건식; 증감식;) {
	조건식이 참인 경우 반복 실행될 문;
}
```

**for 문의 동작 순서**
```js
for (var i = 0; i < 2; i++) {
	console.log(i);
}
```
1. `for` 문을 실행하면 먼저 변수 선언문 `var i = 0`이 실행됨. 변수 선언문은 단 한번만 실행됨
2. 변수 선언문의 실행이 종료되면 조건식이 실행됨. 현재 `i`의 값은 `0`이므로 조건식의 평가 결과는 `true`임
3. 조건식의 평가 결과가 `true`이므로 코드 블록이 실앻됨. 증감문으로 실행 흐름이 이동하는 것이 아니라 코드 블록으로 실행 흐름이 이동됨
4. 코드 블록의 실행이 종료되면 증감식 `i++`가 실행되어 `i`의 값은 1이 됨
5. 증감식 실행이 종료되면 다시 조건식이 실행됨. 변수 선언문이 실행되는 것이 아니라 조건식이 실행됨. 현재 `i`의 값은 `1`이므로 조건식의 평가 결과는 `true`임
6. 조건식의 평가 결과가 `true`이므로 코드 블록이 다시 실행함
7. 코드 블록의 실행이 종료되면 증감식 `i++`가 실행되어 `i`의 값은 `2`가 됨
8. 증감식 실행이 종료되면 다시 조건식이 실행됨. 현재 `i`의 값은 `2`이므로 조건식의 평가 결과는 `false`임. 조건식의 평가 결과가 `false`이므로 `for` 문의 실행이 종료됨

- `for` 문의 변수 선언문, 조건식, 증감식은 모두 옵션이지만 어떤 식도 선언하지 않으면 무한 루프가 됨

	```js
	for (;;) { ... }
	```

- `for` 문 내에 `for` 문을 중첩해서 사용할 수 있음

	```js
	// 두 개의 주사위를 던졌을 때 합이 6이 되는 모든 경우의 수 출력
	for (var i = 1; i <= 6; i++>) {
		for (var j = 1; j <= 6; j++>) {
			if (i + j === 6) console.log(`${i}, ${j}`);
		}
	}
	```

### 8.3.2 while 문
`for` 문은 반복 회수가 명확할 때 주로 사용하고 `while` 문은 반복 횟수가 불명확 할 때 주로 사용함<br>

**while 문의 형식**
```js
while (조건식) {
	조건식이 참인 경우 반복 실행될 문;
}
```
- 조건식의 평가 결과가 언제나 참이면 무한루프가 됨

	```js
	while (true) { ... }
	```
- 무한 루프에서 탈출하기 위해서 코드 블록 내에 `if` 문으로 탈출 조건을 만들어 `break` 문으로 코드 블록을 탈출함

	```js
	var count = 0;

	while (true) {
		console.log(count);
		count++;
		if (count === 3) break;
	} // 0 1 2
	```

### 8.3.3 do ... while 문
**코드 블록을 먼저 실행한 후 조건식을 평가**하므로 코드 블록은 무조건 한 번 이상 실행됨
```js
var count = 0;

do {
	console.log(count);
	count++;
} while (count < 3); // 0 1 2
```

## 8.4 break 문
레이블 문, 반복 문(`for`, `for ... in`, `for ... of`, `while`, `do ... while`) 또는 `switch` 문의 코드 블록을 탈출함<br>
이 외의 코드 블록에서 `break` 문을 사용하면 `SyntaxError`가 발생함<br>
```js
if (true) {
	break; // Uncaught SyntaxError : Illegal break statement
}
```
**레이블 문(label statement)**

식별자가 붙은 문으로 프로그램의 실행 순서를 제어하는 데 사용함 (`switch` 문의 `case` 문과 `default` 문 등)
```js
// foo라는 레이블 식별자가 붙은 레이블 문
foo: console.log('foo');

chop: {
	console.log(1);
	break chop; // chop 레이블 블록문을 탈출함
	console.log(2);
} // 1
```
- 중첩된 `for` 문의 내부 `for` 문에서 외부 `for` 문까지 한번에 탈출할 때 레이블 문과 `break`를 사용함

	```js
	outer: for (var i = 0; i < 3; i++) {
		for (var j = 0; j < 3; j++>) {
			if (i + j === 2) break outer;
			console.log(`${i}, ${j}`)
		}
	}
	// 0, 0
	// 0, 1
	```

## 8.5 continue 문
반복문의 코드 블록 실행을 현 지점에서 중단하고 반복문의 증감식으로 실행 흐름을 이동시킴<br>
- `if` 문의 실행 코드가 한 줄일 때를 제외하면 `continue` 문을 사용했을 때 가독성이 좋아짐 (들여쓰기 탈출)

	```js
	// continue 문을 사용하지 않으면 if 문 내에 코드를 작성해야 함
	for (var i = 0; i < string.length; i++) {
		if (string[i] === search) {
			count++;
			console.log('실행 코드');
			console.log('실행 코드');
		}
	}

	// continue 문을 사용하면 if 문 밖에 코드를 작성할 수 있음
	for (var i = 0; i < string.length; i++) {
		if (string[i] === search) continue;

		count++;
		console.log('실행 코드');
		console.log('실행 코드');
	}

	```