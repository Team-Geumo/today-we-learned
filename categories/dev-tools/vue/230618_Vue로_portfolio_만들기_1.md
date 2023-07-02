### vue create my-portfolio

### vue 파일 내에서 양식 만드는 명령어는

- vue 입력 후 자동 완성!
  
  ![](C:\Users\MakersMark\AppData\Roaming\marktext\images\2023-06-18-23-39-33-image.png)
  
  

- Template는 div의 역할이 아니라 html 입력하라고 만들어 둔 곳이므로

- div나 section article과 같은 태그로 한 번 크게 감싸주어야 함!
  
  ![](C:\Users\MakersMark\AppData\Roaming\marktext\images\2023-06-18-23-40-16-image.png)

---

### 코드

---

![](C:\Users\MakersMark\AppData\Roaming\marktext\images\2023-06-18-23-34-35-image.png)

- App.vue
  
  ```html
  <template>
    <section>
      <NavHeader />
      <p>Portfolio</p>
      <NavFooter />
    </section>
  </template>
  
  <script>
  import NavHeader from "@/components/NavHeader.vue";
  import NavFooter from "./components/NavFooter.vue";
  export default {
    name: "App",
    components: {
      NavHeader,
      NavFooter,
    },
  };
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 10px;
  }
  </style>
  
  ```

- NavHeader.vue
  
  ```html
  <template>
    <div id="Nav-Header">
      <h2 id="portfolio-logo">Jin's Portfolio</h2>
      <div id="Nav-side">
        <p>자기소개</p>
        <p>기술스택</p>
        <section>
          <p @click="toggleMenu">▽ 프로젝트 ▽</p>
          <div id="menu-container" v-show="showMenu">
            <p>프로젝트 1</p>
            <p>프로젝트 2</p>
            <p>프로젝트 3</p>
            <!-- Add more menu items as needed -->
          </div>
        </section>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "NavHeader",
    data() {
      return {
        showMenu: false,
      };
    },
    methods: {
      toggleMenu() {
        this.showMenu = !this.showMenu;
      },
    },
  };
  </script>
  
  <style>
  /* Styles remain the same */
  #Nav-Header {
    display: flex;
    justify-content: space-between;
    margin: 0px 20px;
  }
  #portfolio-logo {
    padding: 8px;
    font: bold;
  }
  #Nav-side {
    display: flex;
  }
  #Nav-side p {
    margin: 20px;
    border: black solid 1px;
    padding: 8px;
    border-radius: 8px;
  }
  #menu-container {
    position: absolute;
    background-color: white;
    padding: 2px;
    border: black solid 1px;
    border-radius: 8px;
  }
  </style>
  
  ```

- 여기 오랜만에 기본적인 css 할라니까 용어 생각이 안 나서 재활치료의 필요성을 느낌.
  
  
  
  - NavFooter.vue
  
  ```html
  <template>
    <div></div>
  </template>
  
  <script>
  export default {};
  </script>
  
  <style></style>
  
  ```
  
  - 여기는 폼만 만들어뒀음.
