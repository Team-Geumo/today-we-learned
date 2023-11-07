# Async Storage란?

# async/await란?

```
✅ AsyncStorage는 React Native에서 데이터를 로컬에 비동기적으로 저장하고 관리하기 위한 모듈입니다. 주로 텍스트, JSON 형식의 데이터를 저장하며, 로그인 정보 또는 앱 설정, 캐시 데이터와 같은 정보를 보관하는 데 사용됩니다. AsyncStorage는 간단한 키-값 쌍으로 데이터를 저장하고 검색할 수 있으며, 비동기적인 작업을 통해 데이터를 읽고 쓸 수 있습니다. 이를 통해 앱이 오프라인 상황에서도 데이터를 유지하고 필요한 정보를 로드할 수 있게 됩니다.
```

<br>

## 1. AsyncStorage란?

- React Native에서 사용할 수 있는 key-value 형식의 저장소
- iOS에서는 네이티브 코드로 구현되어 있으며, 안드로이드에서는 네이티브 코드와 SQLite를 기반으로 구현되어 있음
- 브라우저에서 사용하는 localStorage와 유사함
  - 값을 저장할 때 문자열 타입으로 저장해야 하며, `getItem`, `setItem`, `removeItem`, `clear` 등 localStorage에서 사용하는 메서드와 같은 이름을 가진 메서드들이 존재함
- localStorage와 차이점 → **AsyncStorage는 비동기적으로 작동함**
  - 값을 조회하거나 설정할 때 Promise를 반환함

<br><br>

## 2. AsyncStorage 기본 사용법

### 2.1. 설치하기

- With npm
  ```bash
  npm install @react-native-async-storage/async-storage
  ```
- With Yarn
  ```bash
  yarn add @react-native-async-storage/async-storage
  ```
- 참고
  [Installation | Async Storage](https://react-native-async-storage.github.io/async-storage/docs/install/)
