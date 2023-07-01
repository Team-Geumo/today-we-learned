# Flutter Header
- Flutter의 위젯을 사용해서 Header 만들기
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(App());
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        // 컬러 입력 형식
        // 1. Colors.black.withOpacity(1)
        // 2. Color(0xFF000000)
        // 3. Color.fromARGB(1, 0, 0, 0)
        backgroundColor: Color(
          0xFF181818,
        ),
        body: Padding(
          padding: EdgeInsets.symmetric(
            horizontal: 40,
          ),
          child: Column(
            children: [
              SizedBox(
                height: 80,
              ),
              Row(
                // Row의 mainAxisAlignment는 Row 방향, crossAxisAlignment는 Column 방향
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Column(
                    // Column의 mainAxisAlignment는 Column 방향, crossAxisAlignment는 Row 방향
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text(
                        "Hey, Horongee",
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.w700,
                          fontSize: 28,
                        ),
                      ),
                      Text(
                        "Welcome back!",
                        style: TextStyle(
                          // 색상 미리보기 : Colors. 자동완성된 후 Ctrl + SpaceBar
                          color: Colors.white.withOpacity(0.8),
                          fontSize: 18,
                        ),
                      ),
                    ],
                  )
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```