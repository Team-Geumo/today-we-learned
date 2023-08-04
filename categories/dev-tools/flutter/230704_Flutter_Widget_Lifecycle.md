# Flutter Widget Lifecycle
## Lifecycle의 종류 (대표적)
### 1. build
- 앱이 화면에 렌더링 될 때 호출되는 함수
### 2. initState
- initState : 부모 요소에 의존하는 데이터를 초기화하는 함수
- 일반적인 경우 initState를 사용하지 않고 바로 작성해도 초기화 가능함
- 부모 요소 (context)에 의존하는 경우에는 initState를 사용해야 함 ex) API의 업데이트를 반영할 때
- 항상 build 메서드보다 먼저 호출되어야 함, 오직 단 한번만 호출됨
### 3. dispose
- dispose : Widget이 스크린에서 제거될 때 호출되는 함수
- Widget이 Widget Tree에서 제거되기 전에 취소하고 싶을 때 사용함
- ex) API 업데이트, 이벤트 리스터 등을 더이상 반영하지 않으려고 할 때

## Widget Lifecycle 코드 예시
- ex) LargeTitle을 toggle하는 함수 구현
- Debug Console에 출력되는 순서
  1. 앱 첫 build 시 : initState! build!
  2. toggle 버튼으로 LargeTitle을 숨겼을 시 : dispose!
  3. toggle 버튼으로 LargeTitle을 다시 나타나게 할 시 : initState! build!
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
  // LargeTitle을 toggle하는 함수 구현
  bool showTitle = true;

  void toggleTitle() {
    setState(() {
      showTitle = !showTitle;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        textTheme: const TextTheme(
          titleLarge: TextStyle(
            color: Colors.red,
          ),
        ),
      ),
      home: Scaffold(
        backgroundColor: const Color(0xFFF4EDDB),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              showTitle ? const MyLargeTitle() : const Text("nothing"),
              IconButton(
                onPressed: toggleTitle,
                icon: const Icon(Icons.remove_red_eye),
              )
            ],
          ),
        ),
      ),
    );
  }
}

class MyLargeTitle extends StatefulWidget {
  const MyLargeTitle({
    super.key,
  });

  @override
  State<MyLargeTitle> createState() => _MyLargeTitleState();
}

class _MyLargeTitleState extends State<MyLargeTitle> {
  // initState
  @override
  void initState() {
    super.initState();
    print("initState!");
  }

  // dispose
  @override
  void dispose() {
    super.dispose();
    print("dispose!");
  }

  // build
  @override
  Widget build(BuildContext context) {
    print("build!");
    return Text(
      "My Large Title",
      style: TextStyle(
        fontSize: 30,
        color: Theme.of(context).textTheme.titleLarge?.color,
      ),
    );
  }
}

```