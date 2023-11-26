## 1. SPA란?

-   하나의 html 파일에서 구동 되는 웹 앱 형태의 페이지
-   SPA는 브라우저에 최초 한번만 요청하여 페이지 전체를 로드한 이후, 유저 요청에 의한 변화는 데이터를 업데이트하여 필요한 부분만 로드함

## 2. SEO에서 SPA의 단점

-   요약 : **여러 페이지가 한 개의 Meta Data를 가짐**

### SEO 과정

-   검색엔진의 크롤러는 링크를 타고 페이지를 돌아다니며 웹 문서(html) 파일을 읽음
-   이러한 작업을 통해 단일한 url의 페이지마다 색인을 만들고 검색 결과로 색인된 페이지를 보여줌

### SPA의 단점

-   SPA는 한 개의 url을 가지고 있음
-   따라서 SPA에서 변화하며 보여지는 수십가지의 기능을 가진 뷰가 단 한개의 페이지로 색인됨
-   페이지의 뷰는 변화해도 페이지의 타이틀과 디스크립션을 바꿀 수 없기 때문에 사용자 경험 개선 및 검색엔진의 최적화가 어려움
-   다양한 페이지 뷰가 단일한 Meta Data로 보임 : SEO에 치명적

## 3. SPA에서 SEO를 개선하는 방법.

### 1. history API 활용 (`putState()`)

-   **사이트 내에서 유저가 이동한 기록을 남겨주는 기능을 하는 API**
-   현대의 브라우저들은 `window` 객체의 하위 객체인 `history` 객체를 가지고 있음
-   history API의 메소드 중 하나인 `pushState()`를 활용하면 SPA SEO의 문제를 해결할 수 있음
    -   `pushState()` 메소드는 각각 (데이터 상태 객체, 빈 문자열, 표시할 URL)을 인자로 받음
    -   이 메소드가 호출되면 전달된 url이 브라우저의 url 창에 표시됨
-   `pushState()` 활용 예시
    ```jsx
    var stateObject = { 데이터_종류: '중요한 데이터' };
    history.pushState(stateObject, '', '새페이지.html');
    ```
    !https://seo.tbwakorea.com/wp-content/uploads/2023/11/SPA-SEO-4-1024x542.png
    -   `pushState()` 를 입력하면 url이 “seo.tbwakorea.com/새페이지.html” 로 바뀜
    -   SPA에서 구분이 필요한 뷰로 진입할 때마다 `pushState()` 메서드로 주소를 바꿔준다면 해당 뷰를 새 콘텐츠가 있는 새 페이지로 인식한 검색엔진 봇이 해당 페이지를 크롤링하고 색인을 생성함
    -   이 방법을 통해 **SPA는 여러가지 페이지를 가진 것처럼 검색 엔진에 표시될 수 있음**

### 2. 서버 사이드 랜더링(SSR) 활용

-   pushState는 페이지만 바꿀 뿐 아니라 페이지 간의 데이터도 전송합니다. 그러나 pushState로 전달할 수 있는 데이터는 직렬화된 데이터만 포함되기 때문에 데이터의 양에 제한이 있습니다.
-   이러한 문제의 대안으로 활용할 수 있는 것이 SSR
    -   CSR : 서버 측으로부터 필요한 리소스를 다운받고 스크립트를 실행시켜 서버에 필요한 데이터를 요청하여 콘텐츠를 렌더링하는 것
    -   SSR : 서버 쪽에서 화면을 전부 랜더링해서 보내는 것
-   일반적으로 SPA는 CSR을 활용하지만 **Next.js나 Remix같은 SSR 프레임워크를 활용한다면 SSR을 활용한 SPA를 만들 수 있음**

### 3. 웹 라이브러리 활용

-   SPA의 작동 방식은 html문서의 `<body>`를 업데이트하는 이므로 이과정에서 `<head>`에 대한 업데이트는 잘 이뤄지지 않음
-   `<head>`는 검색 결과에 영향을 미칠 수 있는 `<meta>` 등 중요한 SEO 요소가 있기 때문에 페이지마다 달라지도록 관리해야 함
-   따라서 `<**head>`를 업데이트한다면 SEO를 향상시킬 수 있음\*\*

### React Helmet

-   React에서 유저가 앱을 조작할 때마다 그에 맞는 `<head>` 태그를 업데이트하는 기능을 가진 라이브러리
-   앱 내에서 기능별로 나누어진 컴포넌트에 `<Helmet>`컴포넌트를 추가하여 사용

```jsx
import React from 'react';
import { Helmet } from 'react-helmet';

class Application extends React.Component {
    render() {
        return (
            <div className="application">
                <Helmet>
                    <meta charSet="utf-8" />
                    <title>My Title</title>
                    <link rel="canonical" href="http://mysite.com/example" />
                </Helmet>
                ...
            </div>
        );
    }
}
```

-   하지만 이렇게 동적으로 `<head>` 태그에 내용을 추가해도 바뀐 내용을 크롤링하지 못할 수 있음
    -   모든 검색 엔진이 자바스크립트 파일을 수집하는 것은 아닐 뿐더러, 자바스크립트를 수집하고 해석하는 것은 html 페이지의 해석보다 몇 배 이상의 리소스가 필요한 작업이기 때문
-   따라서 **주요영역은 검색 엔진 봇이 html만으로 콘텐츠를 읽을 수 있게 구성하는 것이 좋음**

### React Snap

-   변화하는 html 파일을 스냅 사진 찍듯이 고유한 html 파일로 변환하여 앱을 빌드하는 라이브러리
-   **SSR 방식을 사용하지 않고 고유한 html를 만들어낼 수 있음**
-   주의 ) 현재는 유지보수를 하지 않는 라이브러리
