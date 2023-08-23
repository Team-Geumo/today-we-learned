# [React/TypeScript] CRA에서 Path Alias 설정하기

## 1. Path Alias란

- 경로에 별칭을 붙인다는 뜻
- `"../../../recoil/SuryveyState"`과 같은 경로를 `"@recoil/SuryveyState"` 형식으로 변경할 수 있음

<br><br>

## 2. tsconfig 설정

- 컴파일 시 path alias를 인식할 수 있도록 typescript 컴파일러에게 설정할 path alias를 알려줘야 함
- `tsconfig.paths.json`이라는 파일을 `tsconfig.json`과 같은 위치에 생성하고, 그 안에 path를 정의

```json
// tsconfig.paths.json

{
  "compilerOptions": {
    "baseUrl": "src",
    "paths": {
      "@api/*": ["api/*"],
      "@assets/*": ["assets/*"],
      "@components/*": ["components/*"],
      "@fonts/*": ["fonts/*"],
      "@hooks/*": ["hooks/*"],
      "@pages/*": ["pages/*"],
      "@recoil/*": ["recoil/*"],
      "@styles/*": ["styles/*"],
      "@types/*": ["types/*"]
    }
  }
}
```

- 사용할 폴더에 따라 커스텀해서 사용하면 됨

<br>

- 다음으로 `tsconfig.json`에 확장 경로 파일을 추가함

```json
// tsconfig.json

{
  ...
  "extends": "./tsconfig.paths.json",
}
```

<br><br>

## 3. craco 설치

- 프로젝트 빌드 시에도 path alias를 보고 올바른 경로를 찾을 수 있도록 웹팩에도 path alias를 알려줘야 함
- 웹팩에서 path alias 설정은 `webpach.config.js` 파일을 변경해줘야 하는데 CRA로 만든 프로젝트라면 `eject`를 해야 해당 파일이 나타남
- `eject`를 하지 않고 webpack 설정을 확장하기 위해 `craco` 라이브러리를 사용
- **`craco`**
  - Create React App Configuration Override의 약자
  - `eject` 없이 cra의 편리함과 자유로운 커스터마이징을 누리자!라는 취지로 만들어진 라이브러리
  - [craco 라이브러리 NPM 링크](https://www.npmjs.com/package/@craco/craco)

```bash
npm install @craco/craco
```

- `craco` 설치

<br>

- 웹팩 플러그인인 `tsconfig-paths-webpack-plugin`을 사용하면 간편하게 path alias를 설정 가능
- `tsconfig-paths-webpack-plugin`
  - `tsconfig.json`에서 설정한 path를 웹팩에 그대로 설정해주는 플러그인
  - [tsconfig-paths-webpack-plugin NPM 링크](https://www.npmjs.com/package/tsconfig-paths-webpack-plugin)

```bash
npm install -D tsconfig-paths-webpack-plugin
```

<br><br>

## 4. craco.config.js 파일 생성

- `package.json`과 동일한 위치에 `craco.config.js` 파일 생성

<br><br>

## 5. package.json 수정

```json
// package.json

"scripts": {
    "start": "craco start",
    "build": "craco build",
  },
```

- `package.json` 파일의 `scripts`에서 `react-script`를 호출하는 부분을 `craco`로 변경

<br><br>

## 6. craco 설정 파일 수정

```javascript
// craco.config.js

const TsconfigPathsPlugin = require("tsconfig-paths-webpack-plugin");

module.exports = {
  plugins: [
    {
      plugin: {
        overrideWebpackConfig: ({ webpackConfig }) => {
          webpackConfig.resolve.plugins.push(new TsconfigPathsPlugin({}));
          return webpackConfig;
        },
      },
    },
  ],
};
```

- `craco.config.js`에서 웹팩 설정을 재정의

<br><br>

- 설정이 끝나면 아래와 같이 깔끔한 코드 사용 가능

   <img src="https://velog.velcdn.com/images/yeguu037/post/ae50719c-9d86-4e57-874f-c7503b81ffe7/image.png" width="70%" height="70%"/>
