# vue3 _ 바인딩

여러분도 다 아시는 v-bind에 관한 얘기입니다.

---

- 지시어로 `v-`로 시작하는 속성들 중 하나!

- Vue 템플릿 구문 중 일부.

```js-templates
<div v-bind:id="dynamicId"></div>
```

- v-bind로 쓸 수 있지만 다르게 쓸 수 도 있음.
  
  ```js-templates
  <div :id="dynamicId"></div>
  ```

- v-bind의 축약형 `:id`

- **Options example**
  
  ```javascript
  <script>
  export default {
    data() {
      return {
        titleClass: 'title'
      }
    }
  }
  </script>
  
  <template>
    <h1 :class="titleClass">Make me red</h1> 
    <!-- add dynamic class binding -->
  </template>
  
  <style>
  .title {
    color: red;
  }
  </style>
  ```

---

- **Composition example**
  
  ```javascript
  <script setup>
  import { ref } from 'vue'
  
  const titleClass = ref('title')
  </script>
  
  <template>
    <h1 :class="titleClass">Make me red</h1> 
    <!-- add dynamic class binding -->
  </template>
  
  <style>
  .title {
    color: red;
  }
  </style>
  ```
