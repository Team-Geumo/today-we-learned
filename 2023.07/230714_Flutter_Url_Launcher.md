# Flutter url_launcher
## url_launcher
- https://pub.dev/packages/url_launcher
- 웹 브라우저를 실행하거나 메알, 전화 등을 실행할 수 있는 패키지

## 설치 및 설정
### 설치
- `flutter pub add url_launcher`
### 설정
1. **iOS**
- ios/Runner/Info.plist 파일을 열고 다음과 같이 수정
```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  ...
  <key>LSApplicationQueriesSchemes</key>
  <array>
    <string>https</string>
    <string>http</string>
  </array>
</dict>
</plist>
```
2. **Android**
- android/app/src/main/AndroidManifest.xml 파일을 열고 다음과 같이 수정
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.url_launcher_example">
    <queries>
        <!-- If your app opens https URLs -->
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <data android:scheme="https" />
        </intent>
        <!-- If your app makes calls -->
        <intent>
            <action android:name="android.intent.action.DIAL" />
            <data android:scheme="tel" />
        </intent>
        <!-- If your sends SMS messages -->
        <intent>
            <action android:name="android.intent.action.SENDTO" />
            <data android:scheme="smsto" />
        </intent>
        <!-- If your app sends emails -->
        <intent>
            <action android:name="android.intent.action.SEND" />
            <data android:mimeType="*/*" />
        </intent>
    </queries>

   <application>
        ...
    </application>
</manifest>
```

## 사용법
1. launchUrl 함수를 통해 브라우저를 실행할 수 있음
```dart
import 'package:url_launcher/url_launcher.dart';
...
// Uri 문자열로 생성
launchUrl(
  Uri.parse('https://google.com/'),

// Uri 생성자로 생성
Uri(
  scheme: 'https',
  host: 'play.google.com',
  path: 'store/apps/details',
  queryParameters: {"id": 'com.google.android.tts'},
),
);
```

2. canLaunchUrl 함수를 사용하여 해당 URL이 실행 가능한지 확인할 수 있음
```dart
const url = Uri.parse('https://google.com/');
if (await canLaunchUrl(url)) {
  launchUrl(url);
}
```
3. 이 외에 메일, 전화, 문자 등을 실행할 수 있음
```dart
Email: launchUrl(Uri.parse('mailto:dev-yakuza@gmail.com?subject=Hello&body=Test'));
Tel: launchUrl(Uri.parse('tel:+1 555 010 999'));
SMS: launchUrl(Uri.parse('sms:5550101234'));
Google Play store App page: launchUrl(Uri.parse('http://play.google.com/store/apps/details?id=com.google.android.tts'));
```
## 예시
- 해당 웹툰의 id와 에피소드 id를 사용해 해당 에피소드 열람하기
```dart
import 'package:flutter/material.dart';
import 'package:toonflix/models/webtoon_episode_model.dart';
import 'package:url_launcher/url_launcher_string.dart';

class Episode extends StatelessWidget {
  final WebtoonEpisodeModel episode;
  final String webtoonId;

  const Episode({
    super.key,
    required this.episode,
    required this.webtoonId,
  });

  // 버튼 클릭 시 Url로 이동하는 함수
  onButtonTap() async {
    await launchUrlString(
      "https://comic.naver.com/webtoon/detail?titleId=$webtoonId&no=${episode.id}",
      mode: LaunchMode.externalApplication,
    );
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onButtonTap,
      child: Container(
        margin: const EdgeInsets.only(
          bottom: 10,
        ),
        decoration: BoxDecoration(
          color: Colors.green.shade400,
          borderRadius: BorderRadius.circular(20),
        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(
            vertical: 10,
            horizontal: 20,
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                episode.title,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 16,
                ),
              ),
              const Icon(
                Icons.chevron_right_rounded,
                color: Colors.white,
              ),
            ],
          ),
        ),
      ),
    );
  }
}

```
