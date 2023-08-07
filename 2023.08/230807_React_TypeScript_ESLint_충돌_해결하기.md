# React TypeScript 문법과 ESLint 설정 충돌 해결하기

## 문제 상황

```tsx
interface InputObjectType {
  value: string;
  isValid: boolean;
  hasChanged: boolean;
  handleChange: (event: ChangeEvent<HTMLInputElement>) => void;
}
```

- `handleChange`의 `interface`에서 `event`가 함수 내부에서 사용되지 않아서 ESLint상 error로 인식됨

## 원인

- ESLint의 `no-unused-vars` 설정과 중돌한 것이 원인
- **`no-unused-vars`** : 쓰지않는 변수가 나오면 error을 발생시키는 ESLint의 설정 중 하나

## 해결 방법

- 기존의 `no-unused-vars` 설정을 `off`하고 `@typescript-eslint/no-unused-vars` (타입스크립트의 type, interface 문법을 제외하고 적용)의 설정을 이용하는 것으로 해결

```json
// .eslintrc.json

{
    "extends": [
        "next",
        "plugin:react/recommended",
        "plugin:prettier/recommended",
        "plugin:@typescript-eslint/recommended"
    ],
    "plugins": ["@typescript-eslint/eslint-plugin"],
    "rules": {
        "no-unused-vars": "off",
        "@typescript-eslint/no-unused-vars": "error",
        ...
    }
}
```
