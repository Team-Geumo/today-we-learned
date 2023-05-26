## vue_3_start

- node 16버전 이상의 최신 노드 버전이 깔려있어야 함.

- **npm init** vue@latest

- **npm create** vue@3
  
  - create-vue를 하게되면 테스트 지원 및 몇 가지 옵션 기능이 프롬프트에 표시합니다.
    
    ![loading-ag-266](C:\Users\gkwls\OneDrive\바탕%20화면\Study\today-we-learned\2023.05\image\create-vue-option.png)

- 필요 없다면 No로 두고 Enter 필요하다면 Yes를 선택하면 된다.

- **cd** <your-project-name>

- **npm install**

- **npm run** dev

- **Composition API**로 `<script setup>`작성
  
  - IDE 권장 구성은 visual studio code + volar extension.
  
  - 기본 빌드 도구로 Vite를 쓴다.

- **npm run** build

---

### CDN Vue 사용

```oscript
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

- 언패킹 사용중.

- jsdelivr나 cdnjs 등 npm 패키지 사용중인 모든 CDN은 무엇이든 사용할 수 있습니다.

---

### Global build 사용

- 글로벌 빌드로 Hello world 찍는 예시
  
  ```javascript
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  
  <div id="app">{{ message }}</div>
  
  <script>
    const { createApp } = Vue
  
    createApp({
      data() {
        return {
          message: 'Hello Vue!'
        }
      }
    }).mount('#app')
  </script>
  
  ```

---

### ES 모듈 빌드 사용

- ES 모듈 빌드로 Hello World 찍는 예시
  
  ```javascript
  <div id="app">{{ message }}</div>
  
  <script type="module">
    import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
  
    createApp({
      data() {
        return {
          message: 'Hello Vue!'
        }
      }
    }).mount('#app')
  </script>
  
  ```

---

### Maps import 사용

- Enabling import maps로 hello world 찍는 예시
  
  ```javascript
  import { createApp } from 'vue'
  
  
  <script type="importmap">
    {
      "imports": {
        "vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
      }
    }
  </script>
  
  <div id="app">{{ message }}</div>
  
  <script type="module">
    import { createApp } from 'vue'
  
    createApp({
      data() {
        return {
          message: 'Hello Vue!'
        }
      }
    }).mount('#app')
  </script>
  ```

----

### Splitting Up 모듈

- 으로 hello world
  
  ```html
  <!-- index.html -->
  <div id="app"></div>
  
  <script type="module">
    import { createApp } from 'vue'
    import MyComponent from './my-component.js'
  
    createApp(MyComponent).mount('#app')
  </script>
  ```
  
  ```javascript
  // my-component.js
  export default {
    data() {
      return { count: 0 }
    },
    template: `<div>count is {{ count }}</div>`
  }
  ```
