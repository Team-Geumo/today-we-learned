# Chater 1 Next.js 알아보기

## 1. Next.js 시작하기

### Next.js 앱 생성하기

**Next.js 앱 생성하기** : `npx create-next-app <app-name>`

- `--use-npm` : npm을 기본 패키지 관리자로 설정 (yarn이 설치되어 있는 경우 기본값은 yarn)
- `--example` : Next.js GitHub 저장소에서 예제 코드를 다운로드 해 실행
- ex) `npx create-next-app <app-name> --use-npm --example with-docker`
- 앱 생성 시 설정에 따라 설치되는 패키지와 디렉토리 구조가 달라짐

**Next.js 앱 생성 옵션**

- `√ Would you like to use TypeScript?` : TypeScript 사용 여부
- `√ Would you like to use ESLint?` : ESLint 사용 여부
- `√ Would you like to use Tailwind CSS?` : Tailwind CSS 사용 여부
- `√ Would you like to use src/ directory?` : scr 폴더 사용 여부
- `√ Would you like to use App Router? (recommended)` : App Router 사용 여부, No 선택 시 Pages Router 방식 사용
- `√ Would you like to customize the default import alias?` : import alias (import 경로 단축 식별자) 사용 여부
- `√ What import alias would you like configured?` : import alias 설정

> App Router은 Next.js 13.4 버전부터 공식화 된 Router 방식으로, 현재 참고중인 책은 기존 방식인 Pages Router 방식을 따르고 있습니다. 라우팅 방식과 디렉토리 구조, 컨벤션 등에 차이가 있기 때문에 한 파트가 끝날 때마다 App Router에 대한 정보를 추가하겠습니다.

**Next.js 서버 실행하기** : `npm run dev`

### 프로젝트 기본 구조

`pages/` : 페이지를 구성하는 디렉토리

- 디렉토리 안의 모든 JavaScript 파일은 퍼블릭 페이지가 됨
- ex) `pages/about.js` : http://localhost:3000/about 주소로 접근 시 나타나느 페이지

`public/` : 웹 사이트의 모든 퍼블릭 페이지와 정적 콘텐츠가 있는 디렉토리 (이미지, 폰트, 컴파일된 파일 등)

`styles/` : 스타일 시트가 있는 디렉토리 (옵션)

- `pages/`, `public/` 디렉토리를 제외한 모든 디렉토리는 Next.js의 빌드, 개발에 영향을 주지 않으므로 자율적으로 설정

### TypeScript 지원

- 최상위 디렉토리에 `tsconfig.json`를 생성한 후 `npm run dev` 실행, 이후 메시지로 알려주는 필수 패키지 설치
- 컴파일러 옵션 등 Next.js와 TypeScript의 차이는 공식 바벨 문서 참고
- 현재는 `npx next-create-app` 실행 시 TypeScript 옵션을 기본적으로 제공함

### 바벨과 웹팩 설정 커스터마이징

**바벨 커스터마이징**

- JavaScript의 하위 호환을 위해 커스터마이징
- ex) ECMAScript의 파이프라인 연산자를 사용할 수 있도록 설정하기
- 바벨 플러그인 설치 : `npm install --save-dev @babel/plugin-proposal-pipeline-operator @babel/core`
- 최상위 디렉토리에 `.babelrc`를 생성한 후 코드 작성

  ```json
  // .babelrc
  {
    "presets": ["next/babel"],
    "plugins": [
      ["@babel/plubin-proposal-pipeline-operator", { "proposal": "fsharp" }]
    ]
  }
  ```

- 혹은 `package.json`에 babel 설정을 추가할 수 있음

  ```json
  {
    // ...
    "devDependencies": {
      "next": "13.4.19"
      // ...
    },
    "babel": {
      "presets": ["next/babel"],
      "plugins": [
        ["@babel/plugin-proposal-pipeline-operator", { "proposal": "fsharp" }]
      ]
    }
  }
  ```

**웹팩 커스터마이징**

- 웹팩 설정을 수정해 SASS 등의 CSS 전처리기를 사용할 수 있음
- 대부분의 경우 `next.config.js` 파일의 기본값을 변경해 해결할 수 있음
