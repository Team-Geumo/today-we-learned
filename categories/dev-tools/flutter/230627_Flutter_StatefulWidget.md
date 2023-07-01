# Flutter StatefulWidget
## setState
### setState란
- State class에게 데이터가 변경되었다고 알리는 함수
- setState를 실행하면 build를 다시 실행하면서 변화한 State를 반영
### 코드 예시
- 클릭할 때마다 counter이 1씩 증가하는 Widget의 State
```dart
class _AppState extends State<App> {
  int counter = 0;

  void onClicked() {
    // setState와 함수를 각각 작성해도 되지만, 가독성을 위해 내부에 작성함
    setState(() {
      counter += 1;
    });
  }
}
```
<br>

## Stateful Widget
### Stateful Widget이란
- 상태를 가지고 있는 Widget
- 상태에 따라 변하는 데이터를 실시간으로 반영함
### Stateful Wiget 만들기
- 방법 1 : `st` 입력 후 Flutter Stateful Widget 선택 (단축키)
- 방법 2 : 기존의 StatelessWidget을 StatefulWidget으로 변경 (Ctrl + .)
### 구성
- Stateful Widget은 두 가지 부분으로 나뉨
1. State가 존재하지 않는 Widget 부분
    ```dart
    class App extends StatefulWidget {
        const App({super.key});

        @override
        State<App> createState() => _AppState();
    }
    ```
2. Widget의 State : Widget에 들어갈 데이터와 UI가 들어감, 데이터가 들어가면 해당 Widget의 UI도 변경
    ```dart
    class _AppState extends State<App> {
        int counter = 0;

        void onClicked() {
            counter += 1;
        }

        @override
        Widget build(BuildContext context) {
            return ...(
                counter, ...
            );
        }
    }
    ```
<br>