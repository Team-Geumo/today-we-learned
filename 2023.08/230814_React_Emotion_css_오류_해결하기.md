# React Emotion css 오류 해결하기

## 1. 컴포넌트에 jsxImportSource 주석 추가하기

`/** @jsxImportSource @emotion/react */`

위 코드를 컴포넌트 최상단에 추가하면 해결됨

## 2. craco를 이용해 CRA 커스터마이징 하기

커스터마이징을 마치면 매번 컴포넌트에 주석을 추가하지 않아도 됨

### 1. craco 설치

- npm : `npm i @craco/craco`
- yarn : `yarn add @craco/craco`

### 2. package.json의 script 수정

package.json의 scripts를 다음과 같이 수정함

```json
"scripts": {
    "start": "craco start",
    "build": "craco build",
    "test": "craco test",
    // ...
},
```

### 3. Emotion 관련 라이브러리 설치

- npm : `npm i @emotion/react @emotion/babel-preset-css-prop`
- yarn : `yarn add @emotion/react @emotion/babel-preset-css-prop`

### 4. tsconfig.json 수정

tsconfig.json에 다음 코드를 추가함

```json
"jsxImportSource": "@emotion/react"
```

### 5. craco.config.js 파일 생성

craco.config.js 파일을 루트 디렉토리에 생성한 후 다음 코드를 추가함

```js
module.exports = {
  babel: {
    presets: ['@emotion/babel-preset-css-prop'],
  },
};
```

## 회고

- 두 가지 방법을 모두 사용해보았음
- 주석을 사용하는 방법은 컴포넌트의 수가 많은 경우 작성할 때마다 주석을 추가해야 하므로 2번 방법을 추천함!
