# Dart Variables
## Intro (Hello World)
- dart는 자동으로 main 함수를 찾음
- main method가 반드시 존재해야 함
- 실제로 동작하는 코드는 main 안에 작성해야 함
```dart
void main() {
    print('hello world');
}
```
- 세미콜론을 자동으로 추가해주지 않으므로 직접 작성해줘야 함
    - 이유 : 일부러 세미콜론을 달아주지 않는 경우가 있기 때문

## The Var Keyword
- 변수를 선언하는 방법
1. var : 메서드 내 지역 변수는 var 사용을 권장
2. type 선언: class에서 변수나 프로퍼티를 선언할 때 사용
```dart
void main() {
    // 1. var
    var nameA = '니꼬';
    nameA = 'nico'; 
    // nameA를 자동으로 String type으로 컴파일 하기때문에 다른 type을 할당하면 에러 발생 (type은 유지해야 함)

    // 2. type 선언
    String nameB = '호롱';
    nameB = 'horong';
}
```

## Dynamic Type
- 여러 종류의 타입을 가지는 변수를 만들 수 있음
1. var
2. dynamic : 타입에 따른 처리를 할 수 있음
```dart
void main() {
    // 1. var
    var nameA;
    nameA = 'nico';
    nameA = 12;

    /// 2. dynamic
    dynamic nameB;
    if(nameB is String) {
        print(name.isEmpty)
        // name.까지 찍는 순간 String에서 사용할 수 있는 메서드가 자동완성됨
    }
    if(nameB is int) {
        print(nameB.isEven)
    }
} 
```

## Nullable Variables
### null safety란?
- 컴파일 전에 null을 찾아내 참고할 수 없도록 함
- null safety가 없을 때
    ```dart
    bool isEmpty(String string) => string.length == 0;

    main() {
        isEmpty(null); // 컴파일 에러 : null은 length가 없가 때문에 
    }
    ```
- null safety가 있을 때
    ```dart
        void main() {
            String? horong = 'horong' // horong이 null이 될 수도 있음을 선언
            nico = null;
            // nico.length 라는 코드를 치면 컴파일 전에 에러를 띄워줌 => null type을 고려해 처리해주어야 함
            // 1. if문 사용하기
            if(horong != null) {
                print(horong.length)
            }
            // 2. ?로 null을 제외하기
            print(horong?.length)
        }
    ```

- Dart의 변수는 기본적으로 non-nullable이기 때문에, 물음표를 넣지 않는 이상 null에 대해 신경쓰지 않아도 됨

## Final Variables
- final : 수정할 수 없는 변수
    - **JavaScript의 const와 같은 역할**
```dart
void main() {
    final name = 'hy'
    name = 'horong' // error
}
```

## Late Variables
- late : 변수를 먼저 만들고 데이터를 나중에 할당할 때 사용
```dart
void main() {
    late final String name;
    print(name) // error : 할당하기 전에는 사용할 수 없음
    name = 'nico'
    print(name)
}
```
- Flutter에서 data fetching을 할 때 사용
    - 변수를 먼저 만든 이후 API에서 받은 data를 fetching함

## Constant Variables
- **JavaScript의 const와 다르다**
- compile-time constant를 생성함
- const는 compilte-time에 알고있어야 함
- ex) API data는 const로 지정하면 안 됨
    - API는 컴파일이 되어야만 그 값을 알 수 있음
    - 따라서, final이나 late로 지정
    - 앱을 컴파일 하기 전에 알 수 있는 값만 const로 자정






