## React에서 svg 활용하기

## SVG란?

- SVG란 'Scalable Vector Graphics' 의 약어로 각 위치 값을 표시하는 벡터와 같은 방식의 2차원 그래픽용 XML 기반의 형식

## XML이란?

- XML(Extensible Markup Language)은 W3C에서 개발된, 다른 특수한 목적을 갖는 마크업 언어를 만드는데 사용하도록 권장하는 다목적 마크업 언어
- HTML이 브라우저가 분석할 수 있는 태그로 기술되어있는 문서라면, XML은 웹페이지에서 데이터를 주고받기(통신하기) 위한 태그들로 기술된 문서임
- <>를 이용한 태그로 감싸진 구조이며 이미지가 코드로 구성된 개념

## png, jpg 와 svg

1. png와 jpg

   - 비트맵 기반의 이미지로 각 항목에 하나 이상의 정보 비트를 가지고 있는 표현
   - 비트맵으로 이뤄져 있기 때문에 원래의 크기보다 크게 보여지게 할 경우 이미지가 깨져서 보인다는 문제점이 있습니다.

2. svg

- xml 이라는 마크업 언어의 종류이므로 css와 javascript로 수정할 수 있음
- 벡터 기반으로 각 좌표에 점을 이어서 만들어지기 때문에 벡터 기반의 아이콘은 확대나 축소를 해도 깨지지 않고 선명하게 볼 수 있음
- 코드를 수정함으로써 크기와 색깔 등을 쉽게 변경할 수 있음
- png나 jpg보다 용량이 작음

## React에서 사용하기

- 참고 : 1, 2번은 Create-React-App으로 생성한 프로젝트가 아닌 경우 webpack의 file-loader에 대한 설정이 필요함

1. img src에 이용하는 경우 (기존의 png나 jpg 이미지를 가져오는 방식)

   ```JSX
   import Cookie from 'assets/cookie_icon.svg';

   <img src={Cookie} />
   ```

- png, jpg 이미지를 불러오는 방식과 동일
- 크기, 색깔을 코드로 조정할 수 없기 때문에 svg의 특성을 활용할 수 없음

2. svg를 React 컴포넌트로 사용하기

   ```JSX
   import { ReactComponent as Cookie } from 'assets/cookie_icon.svg';

   <svg
   xmlns="http://www.w3.org/2000/svg"
   width="current"
   height="current"
   viewBox="0 0 24 24"
   >   <path fill="current" fill-rule="evenodd" d="...." />
   </svg>
   ```

- SVG 코드에서 바꾸고자 하는 요소를 "current" 로 바꿔줌
- current로 값을 바꿔준 property는 사용하는 컴포넌트에서 다음과 같이 색상과 크기를 조정할 수 있음

```JSX
import { ReactComponent as Cookie } from 'assets/cookie_icon.svg';

<Cookie width="10" height="10" fill="orange"/>
```

3. svgr을 통해 React Component로 사용하기

`$ yarn add @svgr/webpack -D`

- 먼저 svgr을 devDependency로 설치해 준 다음, webpack.config.js에 다음과 같이 작성

```JS
webpack.config.js

const webpack = require('webpack');

module.exports = {
entry: './src/index.js',
module: {
rules: [
//...
{
test: /\.svg$/,
use: ['@svgr/webpack'],
},
],
},
//...
};
```

다음과 같이 세팅을 완료하면 컴포넌트처럼 사용할 수 있음

```JSX
import React from 'react';
import Cookie from 'assets/cookie_icon.svg';

const App = () =>{
return(

<div className='App'>
<Cookie />
</div>
);
}

export default App;
```
