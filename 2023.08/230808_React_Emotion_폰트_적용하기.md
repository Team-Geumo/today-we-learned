# React Emotion으로 폰트 적용하기

## 요약

1. **폰트 파일 다운로드 후 디렉토리에 추가**
2. **폰트 선언 CSS 파일 작성 후 `index.tsx`에 적용**
3. **`App.tsx`에서 `<Global/>`을 사용해 전체 컴포넌트에 폰트 적용**

## 1. 폰트 파일 다운로드 후 디렉토리에 추가

### 폰트 예시 : SUIT ([**다운로드 링크**](https://sunn.us/suit/))

### 원하는 폰트 파일 찾기

- [**눈누**](https://noonnu.cc/) : 저작권 없는 무료 한글 폰트 지원 (폰트 별 라이선스 확인 필수)
- [**DaFont**]() : 저작권 없는 무료 영문 폰트 지원 (Public domain / GPL / OFL, 100% Free)
- OTF, TFF, WOFF, WOFF2 중 **WOFF2** 권장

### Static, Variable

- Static, Variable로 구분되어 있는 폰트가 있음
- **Static** : font-style과 font-weight 별로 폰트 파일이 분리되어 있는 버전
- **Variable** : 여러가지 font-style과 font-weight가 한 개의 폰트 파일로 통합되어 있는 버전
- 지금은 Static 버전을 사용해 볼 예정

### WOFF(Web Open Font Format)란?

- OTF와 TTF의 무단배포 등의 문제 등을 해결하기 위해 모질라 재단과 오페라 소프트웨어, 마이크로소프트에서 제안한 웹 폰트 파일 형식
- 기본적으로 OTF, TTF를 이용한 구조를 하고 있으며, 압축된 버전이라 웹에서 사용하기에 최적화 되어있음
- 글꼴 파일내에서 라이센스 및 메타데이터 등을 따로 포함할 수 있어 저작권 문제에 도움을 줌
- W3C의 웹 폰트 작업 그룹에서 권장하는 파일 형식이며 모든 브라우저에서 사용 가능하도록 표준화 되고 있는 추세
- 이후 WOFF2가 추가로 개발되었는데, **기존 WOFF에 비해 30% ~ 50% 정도 더 압축되어 훨씬 가벼움** (IE를 제외한 거의 모든 브라우저에서 지원)

## 2. 폰트 선언 CSS 파일 작성 후 `index.tsx`에 적용

### 폰트 선언 CSS 파일(`fonts.css`) 작성하기

- 대부분의 경우 WOFF2 다운로드 시 **css 파일을 함께 제공함**
- 만약 CSS 파일이 없다면 직접 작성
- `url`에 들어가는 주소는 1.에서 폰트 파일을 넣은 경로로 수정

```css
/* fonts.css */

@font-face {
  font-family: 'SUIT';
  font-weight: 100;
  src: url('./SUIT-Thin.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 200;
  src: url('./SUIT-ExtraLight.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 300;
  src: url('./SUIT-Light.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 400;
  src: url('./SUIT-Regular.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 500;
  src: url('./SUIT-Medium.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 600;
  src: url('./SUIT-SemiBold.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 700;
  src: url('./SUIT-Bold.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 800;
  src: url('./SUIT-ExtraBold.woff2') format('woff2');
}
@font-face {
  font-family: 'SUIT';
  font-weight: 900;
  src: url('./SUIT-Heavy.woff2') format('woff2');
}
```

### `index.tsx`에 `fonts.css` 적용하기

- 위에서 작성한 `fonts.css`를 최상위 컴포넌트인 `index.tsx`에 적용
- 이제 하위 컴포넌트의 CSS에서 `font-family : 'SUIT'`와 같은 형태로 사용할 수 있게 됨

```jsx
// index.tsx
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import 'styles/fonts.css'; // font.css 적용

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

## 3. `App.tsx`에서 `<Global/>`을 사용해 전체 컴포넌트에 폰트 적용

### Emotion css 파일(`globalStyle.ts`) 작성하기

- 모든 요소에 대해 SUIT 폰트를 가장 우선적으로 적용하기 위해서는 `*`와 `!important`를 함께 사용해야 함
- **`*` (전체 선택자)** : HTML의 모든 요소를 선택하는 선택자
- **!important** : 속성 뒤에 붙일 시 해당 속성을 가장 우선적으로 적용

```ts
// globalStyle.ts
import { css } from '@emotion/react';

function globalStyle() {
  return css`
    * {
      font-family: 'SUIT' !important;
    }
  `;
}

export default globalStyle;
```

### `App.tsx`에 `<Global/>`로 적용하기

- **Global** : 앱 전체에 적용할 스타일을 지정할 때 사용하는 emotion 컴포넌트
- `styles`에 적용할 **Emotion CSS 파일**을 지정하거나 <code>css``</code>의 형태로 직접 작성
- 여러 개의 Emotion CSS 파일을 적용할 경우 리스트로 작성(`[reset, globalStyle]`)

```tsx
// App.tsx
import { Global } from '@emotion/react';
import reset from 'styles/reset';
import globalStyle from 'styles/globalStyle';
import Routes from 'routes/RoutesApp';
import NavBar from 'features/common/NavBar';

function App() {
  return (
    <div>
      <NavBar />
      <Global styles={[reset, globalStyle]} />
      <Routes />
    </div>
  );
}

export default App;
```

## 주의 사항

### 저장 형식 지키기

- `index.tsx`에 적용할 폰트 선언 파일은 `.css` 형식으로 저장
- `App.tsx`에 적용할 `globalStyles.ts` 파일은 `.js` 혹은 `.ts` 형식으로 저장
