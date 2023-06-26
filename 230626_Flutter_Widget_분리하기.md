# Flutter Widget 분리하기
## Container
### Container란?
- HTML의 div와 유사한 Widget
- decoration 등 다양한 property 제공

### decoration 사용하기 (코드)
- ex) Container에 모서리 라운드 처리하기
```dart
Row(
  children: [
    Container(
      decoration: BoxDecoration(
        color: Colors.amber,
        // 1. 모서리 중 일부만 적용하고 싶을 때
        // borderRadius: BorderRadius.vertical(
        //   top: Radius.circular(20),
        //   bottom: Radius.circular(40),
        // ),
        // 2. 모서리 전체 적용할 때 : all 생략 가능
        borderRadius: BorderRadius.circular(55),
      ),
    ),
  ],
),
```

## Widget 분리하기
- 내가 작성한 Widget을 분리해서 사용할 수 있음

  **방법 1 : Code Actions (Ctrl + .) > Extract Widget**

  **방법 2 : 직접 작성하기**

### 작성 방법
  1. 사용할 변수를 선언
  2. 선언한 변수를 contsuctor에서 사용
  - Code Actions의 Create constructor for final fields 선택하면 자동으로 생성됨
  - 자동완성되는 super.key는 필수 요소
  3. build 함수의 return에 반환할 Widget을 작성
  - 위에서 선언한 변수를 Widget에 사용
  - 변수를 사용하면서 기존 Widget이 const가 아니게 변경될 수 있으므로 오류 발생 시 const 삭제
  - cf) const로 작성된 부모 Widget의 자식 Widget은 모두 const임. 따라서 자식 Widget중 일부가 const가 아니게 될 시 부모 Widget의 const는 사라지고, const인 자식 Widget에만 const가 새롭게 작성됨

### 코드 예시
- ex) Text와 Color들을 커스터마이징 할 수 있는 Widget
```dart
import 'package:flutter/material.dart';

class Button extends StatelessWidget {
  final String text;
  final Color bgColor;
  final Color textColor;

  const Button({
    super.key,
    required this.text,
    required this.bgColor,
    required this.textColor,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: BorderRadius.circular(55),
      ),
      child: Padding(
        padding: const EdgeInsets.symmetric(
          vertical: 20,
          horizontal: 40,
        ),
        child: Text(
          text,
          style: TextStyle(
            fontSize: 20,
            color: textColor,
          ),
        ),
      ),
    );
  }
}

```
