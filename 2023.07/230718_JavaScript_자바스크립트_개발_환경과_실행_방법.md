# 03 자바스크립트 개발 환경과 실행 방법
## 3.1 자바스크립트 실행 환경
자바스크립트는 웹 브라우저, Node.js 환경에서 모두 동작하지만 두 환경에 차이가 있음

**웹 브라우저**
- HTML, CSS, JavaScript를 실행해 웹페이지를 **브라우저 화면에 렌더링** 하는 것이 목적
- **ECMAScript** + **클라이언트 사이드 Web API** 지원
- ex) HTML 요소를 선택, 조작하는 DOM API(Web API)을 지원하지만, 보안상의 이유로 파일 시스템을 지원하지 않음<br>
    - FileReader(Web API)를 사용해 사용자가 지정한 파일을 읽는 것은 가능

**Node.js**
- **브라우저 외부**에서 자바스크립트 실행 환경을 제공하는 것이 목적
- **ECMAScript** + **Node.js 빌트인 API** 지원
- ex) 파일을 생성하고 수정할 수 있는 파일 시스템(Node.js 빌트인 API)을 지원하지만, HTML 요소를 다루는 DOM API는 기본 제공하지 않음
    - 웹 크롤링 시 cheerio와 같은 DOM 라이브러리를 사용해 HTML 가공
    - **웹 크롤링**(web crolling) : 서버에서 웹사이트의 콘텐츠를 수집하기 위해 HTML 문서를 가져온 후 이를 가공해 필요한 데이터만 추출하는 것

## 3.2 웹 브라우저
### 3.2.1 개발자 도구
**단축키** : `F12` 또는 `Ctrl`+`Shift`+`I`

|패널|기능|
|---|---|
|Elements|로딩된 웹페이지의 DOM과 CSS를 편집해서 렌더링 된 뷰 확인|
|Console|로딩된 웹페이지의 에러 또는 `console.log` 메서드의 실행 결과 확인|
|Sources|로딩된 웹페이지의 자바스크립트 코드 디버깅|
|Network|로딩된 웹페이지에 관련된 네트워크 요청 정보와 성능 확인|
|Application|웹 스토리지, 세션, 쿠키 확인 및 관리|

### 3.2.2 콘솔(Console)
- 구현 단계에서 에러 발생 관찰 및 코드의 실행 결과 확인
- 프롬프트에 자바스크립트 코드를 입력해 **REPL** 환경으로 사용할 수 있음
- **REPL(Read Eval Print Roop)** : 코드를 입력하면 바로 결과를 반환하고 다시 입력할 수 있는 도구

### 3.2.3 브라우저에서 자바스크립트 실행
- HTML 파일을 로드하면 script 태그에 포함된 자바스크립트를 실행함

### 3.2.4 디버깅
1. 콘솔에 출력된 에러 정보의 발생 위치(링크)를 클릭 해 Source 패널로 이동
2. 해당 에러 확인 후 코드 왼쪽 라인 번호를 클릭해 중단점(break point) 설정
3. 코드를 재실행하면 디버깅 모드로 진입

## 3.3 Node.js
### 3.3.1 Node.js와 npm 소개
**Node.js**
- 크롬 V8 자바스크립트 엔진으로 빌드된 자바스크립트 런타임 환경
- 자바스크립트를 브라우저 외의 환경에서 동작시킬 수 있는 자바스크립트 실행 환경

**npm(node package manager)**
- 자바스크립트 패키지 매니저
- Node.js에서 사용할 수 있는 모듈들을 패키지로 만들어서 모아둔 저장소 역할과 패키지 설치 및 관리를 위한 CLI(Command Line Interface)를 제공

### 3.3.2 Node.js 설치
**설치 링크** : [**Install Node.js**](https://nodejs.org/ko/download)

**LTS와 Current**
- **LTS(Long Term Support)** : 장기적으로 안정된 지원이 보장되는 버전
- **Current** : 업데이트가 발생하는 버전, 최신 기능을 제공하지만 불안정할 수 있음

**버전 확인하기**
```powershell
$ node -v
$ npm -v
```

### 3.3.3 Node.js REPL
**Node.js REPL 실행하기**
```powershell
$ node
```

**자바스크립트 파일 실행하기**
: `.js` 생략 가능
```powershell
$ node index.js
```

## 3.4 비주얼 스튜디오 코드
### 3.4.1 비주얼 스튜디오 코드 설치
**설치 링크** : [**Install Visual Studio Code**](https://code.visualstudio.com/Download)

### 3.4.2 내장 터미널
**단축키**
- 터미널 열기 : `Ctrl`+<code>`</code>
- 터미널 추가하기 : `Ctrl`+`Shift`+<code>`</code>

### 3.4.3 Code Runner 확장 플러그인
내장 터미널에서 단축키를 사용해 현재 표시 중인 파일을 간단히 실행<br>
자바스크립트 파일 실행 시 node.js 환경에서 실행되므로, `alert` 등의 Web API는 실행되지 않고 에러 발생

**단축키**
- 파일 실행하기 : `Ctrl`+`Alt`+`N`
- 실행 중단하기 : `Ctrl`+`Alt`+`M`


### 3.4.4 Live Server 확장 플러그인
`Go Live` 버튼을 클릭해 가상 서버를 기동하면 수정 사항이 가상 서버에 자동으로 반영