## Vue 3.

> view에 대해 거의 다 까먹어서 다시 처음부터 짚어볼까 합니다.

---

### Vue 란?

- 사용자 인터페이스 구축을 위한 **javascript 프레임워크**입니다.

- HTML, CSS, JavaScript를 바탕으로 하는, 컴포넌트 베이스의 선언적인 프로그래밍 모델을 제공해줍니다.

- count sample

  ```javascript
  import { createApp } from "vue";

  createApp({
    data() {
      return {
        count: 0,
      };
    },
  }).mount("#app");
  ```

  ```js-templates
  <div id="app">
    <button @click="count++">
      Count is: {{ count }}
    </button>
  </div>
  ```

- HTML을 보여줄 때 JavaScript 기반의 **선언적**으로 작성된 것을 보여줍니다.

- 자바스크립트 상태의 변화를 자동으로 추적하고 변경이 발생하면 DOM을 **재활성화** 하여 효율적으로 업데이트 합니다.

---

### 프로그레시브 프레임워크

- 이러한 사례들로 활용되고 있음!

  - 빌드 단계 없지 정적 HTML 확장

  - 모든 페이지에 웹 구성 요소로 포함

  - 단일 페이지 애플리케이션 (SPA)

  - 풀 스택 / 서버 측 랜더링 (SSR)

  - Jamstack / 정적 사이트 생성 (SSG)

  - 데스크톱, 모바일, WebGL, 터미널을 타겟팅하는 개발

---

### 단일 파일 구성요소

- Vue는 Javascript와 HTML, CSS 요소를 한 파일 안에 저장합니다. 이를 **SFC(Single File Component)**라고 합니다.

  ```javascript
  <script>
  export default {
    data() {
      return {
        count: 0
      }
    }
  }
  </script>

  <template>
    <button @click="count++">Count is: {{ count }}</button>
  </template>

  <style scoped>
  button {
    font-weight: bold;
  }
  </style>
  ```

- 위의 Count Sample을 vue에서 실제 사용하듯 적으면 이렇게 된다.

---

### 두 가지 API 스타일

#### Options API

- data, methods와 mounted 같은 여러 옵션으로 구성된 단일 객체를 사용하여 구성 요소의 논리를 정의합니다.

  ```javascript
  <script>
  export default {
    // data()에서 반환하는 프로퍼티 반응하는 상태가 된다.
    // 'this' 로 엑세스 하는 것이 가능하다.
    data() {
      return {
        count: 0
      }
    },

    // 메소드의 핵심은 상태를 변화시키는 것에 있다.
    // 각 메소드는 템플릿 안의 이벤트 핸들러에 바인드 하는 것이 가능.
    methods: {
      increment() {
        this.count++
      }
    },

    // DOM 연결이 되었을 때 실행될 부분.
    mounted() {
      console.log(`The initial count is ${this.count}.`)
    }
  }
  </script>

  <template>
    <button @click="increment">Count is: {{ count }}</button>
  </template>
  ```

#### Composition API

- SFC에서 composition API는 일반적으로 `<script setup>`과 함께 사용됩니다. `setup`이라고 하는 속성을 붙이는 것으로, Vue 컴파일 시 해당 부분을 조작할 수 있습니다.

  ```javascript
  <script setup>
  import { ref, onMounted } from 'vue'

  // 동적인 상태
  const count = ref(0)

  // 상태 변화 가능한 함수.
  function increment() {
    count.value++
  }

  // 라이프 사이클
  onMounted(() => {
    console.log(`The initial count is ${count.value}.`)
  })
  </script>

  <template>
    <button @click="increment" >Count is: {{ count }}</button>
  </template>
  ```

  #### Options API VS Composition API

  - 두 스타일 모두 같은 기능을 구현하고 있습니다. 생김새는 다르지만 기반 시스템은 완전히 동일합니다.

  - Options API는 OOP 언어 경험이 있는 사용자에게 좋습니다. 재활용의 세부 사항을 추상화하고 각 옵션 그룹에 따라 코드 구성을 구성하므로 초보자가 쓰기도 좋은 방식입니다.

  - Composition API는 함수 범위 내에서 동적 상태 변수를 직접 선언하고 여러 함수를 조합하여 처리하는 것이 중심입니다.

  - Composition API가 Options API에 비해 자유도가 높은 대신 Vue의 reactivity가 어떠한 구조로 움직이는지 이해해야합니다. 러닝 커브가 조금 있는 대신 다양한 패턴을 따라 로직의 정리와 재사용을 강력하게 진행할 수 있습니다.
