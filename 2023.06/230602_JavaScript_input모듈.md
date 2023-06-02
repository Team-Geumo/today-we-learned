# ES6방식이 아닌 CommonJS 방식으로!

## readline

### 1. 모듈 불러오기

```javascript
const readline = require('readline')
```

### 2. interface 객체 만들기

```javascript
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
```

### 3. 입출력 코드 작성하기

```javascript
rl.on('line', (line) => {
    // 여기에 입력 받은 값 처리하는 코드
        
}
```

---

## fs

### 1. 모듈 불러오기

```javascript
const fs = require("fs");
```

### 2. 한 줄로 입력 받을 경우

```javascript
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

const num = Number(input);

for (let i = 1; i <= num; i++) {
  console.log(i);
}
```

### 3. 여러 줄로 입력 받을 경우

```javascript
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const count = input[0];
const numbers = [];

for (let i = 1; i < input.length; i++) {
  if (input[i] !== '') {
    numbers.push(input[i].split(' '));
  }
}

for (let i = 0; i < numbers.length; i++){
  let num1 = Number(numbers[i][0]);
  let num2 = Number(numbers[i][1]);

  console.log(num1 + num2);
}
```

### 쉽게 한 줄로 사용하기.

```javascript
// 한 줄인 경우
const input1 = require('fs').readFileSync('예제.txt').toString().split(' ');

// 두 줄인 경우
const input2 = require('fs').readFileSync('예제.txt').toString().split('\n');
```


# 중요 !

- readline 보다 fs 모듈 쪽이 성능적으로 우수하다. 그냥 fs 쓰자...