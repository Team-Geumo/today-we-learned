# Flutter BuildContext, Theme

## BuildContext
### BuildContext란
- 상위 요소에 접근할 수 있게 하는 매개체로서, 상위 요소들의 모든 정보를 담고있음
- Widget Tree에서 Widget의 위치를 제공해서 상위 요소 데이터에 접근할 수 있음
- 바로 상위 요소 뿐만 아니라 최상위까지 탐색 가능

## Theme
### theme이란
- 모든 스타일을 한 곳에서 지정할 수 있는 기능을 제공
- theme을 사용하면 동일한 스타일을 모든 곳에 복사, 붙여넣기 하는 불편함을 줄일 수 있음
- MaterialApp의 property로서 ThemeData라는 타입을 가짐

### 사용 방법
- theme: ThemeData()의 형식으로 사용
- ThemeData의 property로 다양한 스타일 테마 설정
- 하위 Widget에서 사용할 때 `BuildContext`를 통해 접근 가능

### 코드 예시
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const App());
}

class App extends StatefulWidget {
  const App({super.key});

  @override
  State<App> createState() => _AppState();
}

class _AppState extends State<App> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(

      // theme 설정
      theme: ThemeData(
        textTheme: const TextTheme(
          titleLarge: TextStyle(
            color: Colors.red,
          ),
        ),
      ),
      home: const Scaffold(
        backgroundColor: Color(0xFFF4EDDB),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              MyLargeTitle(),
            ],
          ),
        ),
      ),
    );
  }
}

// StatelessWidget인 MyLargeTitle에서 theme의 값에 접근해야 함
// context는 MyLargeTitle Text의 상위 요소들의 모든 정보를 담고있음

class MyLargeTitle extends StatelessWidget {
  const MyLargeTitle({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Text(
      "My Large Title",
      style: TextStyle(
        fontSize: 30,
        
        // 에러 발생 : color property에 null이 들어갈 수 없음
        // - 방법 1 : titleLarge.color이 반드시 null이 아니라고 알려주기
        // color: Theme.of(context).textTheme.titleLarge.color,
        // - 방법 2 : titleLarge.color이 null이 아닐 때만 사용하기
        color: Theme.of(context).textTheme.titleLarge?.color,
      ),
    );
  }
}

```