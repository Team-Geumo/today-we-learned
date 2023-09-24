# Dynamic Import

웹사이트의 속도를 올리기 위해서는 큰 JS 파일의 용량을 줄여야 함

1. 코드의 크기를 줄이는 방법 : Tree Shaking 등
2. 코드를 분할하는 방법 : Split Chunks Plugin, Dynamic Import 등

- 사용되지 않는 코드를 최대한 줄이고 코드를 재사용 하더라도 전체 페이지의 코드가 한파일에 작성되어 있다면 줄이는데 한계가 있음
- 사용자가 보는 첫 렌더링 화면에 필요 없는 코드를 분할하여 이후 필요할때 마다 불러오는 방식을 사용하면 코드 더 줄일 수 있음

## 동적 코드 분할 Dynamic Imports

- 첫 페이지 진입시에 필요한 최소한의 코드만 다운 받고, 사용자가 특정 페이지나 위치에 도달할 때마다 코드를 로드 한다면, 첫 페이지의 초기 성능을 올릴 수 있음
- 이런 방식을 lazy-load이라고 함
- Dynamic Import를 사용하면 런타임시에 필요한 module을 import 할 수 있음
- Promise를 반환

```js
import(모듈)
  .then((모듈) => {
    // 모듈 가지고 할 것
  })
  .catch((e) => {
    // 모듈을 불러올 때 에러가 났을 때 할 것
  });
```

- Promise를 반환하기 때문에 async/await와 함께 사용하면 더 효과적임

```js
(async function () {
  const sumModule = await import('모듈');
})();
```

- Dynamic Import 는 일반적인 정적인 Module Import 를 필요한 시점에 로드 할 수 있도록 도와줌
- 또한 일반적인 Import 에서는 불가능한 방법도 가능함

```js
if (true) {
  import('a.js');
}
import(`${id}.js`);
Promise.all([import('b.js'), import('c.js')]);
```

## React Dynamic Import: Lazy 와 Suspense

- React 를 사용한다면, Lazy 를 이용해, Component 가 사용 되는 시점에 가져오도록 구현할 수 있음
- 하지만 이 경우 아무것도 없는 페이지가 노출 되었다가 페이지가 전환됨

```js
const Component = React.lazy(() => import('./Component'));
const Wrapper = () => {
  return (
    <div>
      <Component />
    </div>
  );
};
```

- Suspense 를 이용하여 로딩중 같은 전환 화면을 구현 할 수 있음. 이때 React.lazy는 여러 개여도 무관함

```js
const A = React.lazy(() => import('./A'));
const B = React.lazy(() => import('./B'));
const Wrapper = () => {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <A />
        <B />
      </Suspense>
    </div>
  );
};
```
