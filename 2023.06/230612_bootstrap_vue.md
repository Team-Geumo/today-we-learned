### Bootstrap Vue

- Vue.js를 사용하여 웹 애플리케이션으 개발할 때 사용할 수 있는 오픈 소스 UI 컴포넌트 라이브러리.

- 이름에서 알 수 있듯 Bootstrap 프레임워크의 기능과 Vue가 결합되어있다.



### 특징

- Bootstrap 요소를 Vue에 맞게 쉽게 가져올 수 있다.
  
  - 버튼, 폼 입력, 모달, 탭, 드롭다운 등 다양한 UI 요소들을 쉽게 가지고 올 수 있다.
  
  - 옵션과 이벤트는 입맛대로 설정할 수 있지만 css 적인 부분은 쉽게 건드리기 쉽지 않다.

- 컴포넌트 간의 데이터 통신을 위한 props와 events를 사용할 수 있으며, Vuex를 사용할 수 있음. Vue Router와 함께 사용하여 다른 경로로의 내비게이션을 지원할 수도 있다.

- 여백이 있는 정적인 웹페이지를 깔쌈하게 디자인해서 보여주고 싶을 때 가장 빠르게 할 수 있는 방법이 Bootstrap을 사용하는 것이다.



### 사용예시

- 우선 vue-cli를 사용하여 프로젝트 생성 및 이동.
  
  ```bash
  vue create bootstrap-vue-app
  cd bootstrap-vue-app
  npm install bootstrap-vue bootstrap vue
  ```

- App.vue
  
  ```html
  <template>
    <div>
      <b-alert variant="success" show dismissible>
        This is a Bootstrap Vue alert!
      </b-alert>
  
      <b-button @click="toggleModal">Open Modal</b-button>
  
      <b-modal v-model="showModal" title="Bootstrap Vue Modal">
        This is a Bootstrap Vue modal!
      </b-modal>
    </div>
  </template>
  
  <script>
  import { BAlert, BButton, BModal } from 'bootstrap-vue'
  
  export default {
    components: {
      BAlert,
      BButton,
      BModal
    },
    data() {
      return {
        showModal: false
      }
    },
    methods: {
      toggleModal() {
        this.showModal = !this.showModal
      }
    }
  }
  </script>
  
  ```

- b- 이런 식으로 태그를 작성한다.

- main.js에서 Bootstrap Vue를 전역으로 등록한다.
  
  ```javascript
  import Vue from 'vue'
  import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
  
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  
  Vue.use(BootstrapVue)
  Vue.use(IconsPlugin)
  
  new Vue({
    render: h => h(App)
  }).$mount('#app')
  
  ```


