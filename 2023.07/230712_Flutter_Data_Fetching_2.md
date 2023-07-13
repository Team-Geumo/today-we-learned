# Flutter Data Fetching 2
## API Data Fetching
### 목표
- 받은 데이터를 Flutter Widget에서 사용할 수 있는 형태로 바꿔야 함 (== **class의 instance**)
### 순서
1. `http.get`으로 `response(Response)`를 받음
2. `response.body`가 `String`이라면 `JSON`으로 변환
3. `response.body`가 리스트의 형태를 띄고 있다면 `List<dynamic>`의 타입을 가지는 빈 리스트 작성
4. `JSON(List<dynamic>)`으로 변환한 리스트 안의 각 데이터를 `class`의 `instance`로 만듦
5. 각 `instance`를 3.에서 만든 리스트에 추가 후 반환

## Model
### Model
- 데이터를 해당 class의 instance로 만들어 형식을 지정해주는 역할
### 코드 예시
```dart
class WebtoonModel {
  final String title, thumb, id;
  // named constructor 사용
  // Map<K, V> : Key, Value 타입 지정된 Object
  // dynamic이나 Map으로 작성해도 오류는 없지만, 타입을 명확하게 하기 위해 Map<String, dynamic>으로 작성
  WebtoonModel.fromJson(Map<String, dynamic> json)
      : title = json["title"],
        thumb = json["thumb"],
        id = json["id"];
}
```
## 변환한 데이터 반환
### 코드 예시
```dart
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:toonflix/models/webtoon_model.dart';

class ApiService {
  final String baseUrl = "https://webtoon-crawler.nomadcoders.workers.dev";
  final String today = "today";

  Future<List<WebtoonModel>> getTodaysToons() async {
    // WebtoonModel로 변환한 데이터를 담을 리스트
    List<WebtoonModel> webtoonInstances = [];
    final url = Uri.parse("$baseUrl/$today");

    // 사용하고자 하는 모든 데이터는 최종적으로 class의 instance가 되어야 함
    final response = await http.get(url);
    if (response.statusCode == 200) {
      // response.body가 String으로 들어오기 때문에 JSON으로 변환
      // ex) "[{"id":"796152","title":"마루는 강쥐","thumb":"Maru.jpg"}]"
      // response.body를 출력했을 때 리스트의 형태를 띄고 있으므로 List<dynamic>으로 타입 지정
      final List<dynamic> webtoons = jsonDecode(response.body);

      // JSON(List<dynamic>)으로 변환한 webtoons의 각 데이터를 WebtoonModel class의 instance로 만든 후 webtoonInstances에 추가
      for (var webtoon in webtoons) {
        final webtoonInstance = WebtoonModel.fromJson(webtoon);
        webtoonInstances.add(webtoonInstance);
      }
      // 최종적으로 getTodaysToons()는 webtoonInstances를 반환
      return webtoonInstances;
    }
    throw Error();
  }
```

