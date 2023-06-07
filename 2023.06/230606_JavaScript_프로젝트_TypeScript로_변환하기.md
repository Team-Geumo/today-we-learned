# JavaScript 프로젝트 TypeScript로 변환하기

## TypeScript를 적용할 때 주의해야 될 점

    - 기능적인 변경 하지 않기
    - 테스트 커버리지가 낮을 때는 함부로 타입스크립트 적용하지 않기
    - 처음부터 타입을 엄격하게 적용하지 않기. (점진적으로 strict 하게)

## TypeScript를 적용하는 절차

### 1. 타입스크립트 프로젝트 환경 구성

- 프로젝트 생성 후 npm init -y (npm 초기화 명령어)로 package.json 파일 생성하기
- 프로젝트 폴더에서 npm i typescript -D 로 타입스크립트 라이브러리 설치하기
- 타입스크립트 설정 파일 tsconfig.json 을 생성하고 기본값 추가하기

```js
{
"compilerOptions": {
"allowJs": true,
"target": "ES5",
"outDir": "./dist",
"moduleResolution": "Node",
"lib": ["ES2015", "DOM", "DOM.Iterable"]
},
"include": ["./src/**/*"],
"exclude": ["node_modules", "dist"]
}
```

- 서비스 코드가 포함된 자바스크립트 파일을 타입스크립트 파일로 변환하기
- 타입스크립트 컴파일 명령어 tsc 로 타입스크립트 파일을 자바스크립트 파일로 변환하기

### 2. 엄격하지 않은 타입 환경(loose type)에서 프로젝트 돌려보기

- 프로젝트에 테스트 코드가 있다면, 테스트 코드가 통과하는지 먼저 확인
- js 확장자를 전부 ts로 변경 (jsx는 tsx로)
- 타입스크립트 컴파일 에러가 나는 것 위주로만 먼저 에러가 나지 않게 수정
- 여기서, 기능 변경을 절대 하지 말아야 함
- 테스트 코드가 성공하는지 확인

### 3. 명시적인 any 선언하기

- 프로젝트 테스트 코드가 통과하는지 확인
- 타입스크립트 설정 파일(tsconfig.json)에 noImplicitAny: true 를 추가
- 가능한 타입을 적용할 수 있는 모든 곳에 타입을 적용
- 라이브러리를 쓰는 경우 DefinitelyTyped에서 @types 관련 라이브러리를 찾아 설치
- 만약 타입을 정하기 어려운 곳이 있으면 명시적으로라도 any를 선언
- 테스트 코드가 통과하는지 확인

### 4. strict 모드 설정하기

- 타입스크립트 설정 파일에 아래 설정을 추가

```js
{
"strict": true,
"strictNullChecks": true,
"strictFunctionTypes": true,
"strictBindCallApply": true,
"strictPropertyInitialization": true,
"noImplicitThis": true,
"alwaysStrict": true,
}
```

- any로 되어있는 타입을 최대한 더 적절한 타입으로 변환
- as와 같은 키워드를 최대한 사용하지 않도록 고민해서 변경
