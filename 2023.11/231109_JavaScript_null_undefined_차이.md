# null undefined 차이

<aside>
✅ null 은 비어 있는 존재하지 않는 값을 의미합니다. undefined는 변수가 정의 되어 있지만 아무런 값도 할당 받지 않은 상태를 의미합니다.

또한 null의 typeof는 object를 반환하고, undefined의 typeof는 undefined를 반환합니다. 변수에 값이 없다는 것을 명시하고 싶다면, undefined는 개발자가 의도적으로 할당하는 것이 권장되지 않기 때문에 null을 할당한다.

</aside>

## **1. null**

- JavaScript에서 null은 메모리에 값이 비어있음을 명시적으로 표현하기 위하여 빈 값에 null을 할당되어있는 상태이다.
- 또한 typeof로 null의 타입을 알아보면 object를 출력한다.
- 이는 자바스크립트 개발자들이 null의 예외처리를 고려하지 못하여 object로 출력되는 버그이다. (아래 페이지 참조) 초기 구현의 결함을 수정하지 않도록 권장하기 때문에 수정하지 않고 있다.
- 자바스크립트에서는 대소문자를 구별 함으로 `null`이라고 작성해야 주어야 한다.
- 이전에 참조하던 값을 사용하지 않기 위해 null을 할당하여 더 이상 참조하지 않겠다고 명시해줄 때 쓰인다.
- 함수가 유효한 값을 반환할 수 없을 경우 명시적으로 null을 반환하기도 한다.

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>document</title>
  </head>
  <body>
    <script>
      var element = document.querySelector('.test');
      console.log(element);
    </script>
  </body>
</html>
```

- 위 예시에서는 test를 가진 class가 존재하지 않으므로 console로 출력되는 값은 null이다.

## **2. undefined**

- undefined는 변수를 선언하고 값을 할당하지 않은 상태이다. 말 그대로 "정의되지 않았음"을 뜻한다.
- typeof를 사용하여 undefined의 타입을 알아봤을 때 undefined를 반환한다.
- undefined타입은 undefined가 유일하다.
- 자바스크립트 엔진이 초기화되지 않은 변수에 자동으로 넣어주어 초기화해주는 값이다. 따라서 변수를 참조하였을 때 undefined가 반환된다면 값이 할당되지 않았음을 알 수 있다.
- 즉, 자바스크립트 엔진이 변수를 초기화하는 데 사용되는 역할이기 때문에 개발자가 의도적으로 변수에 할당한다면 본래의 취지와 어긋나고 혼란을 유발하기 때문에 직접 할당하는 방식은 권장되지 않는다.
