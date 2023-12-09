# MVC 패턴

## MVC 패턴이란?

사용자 인터페이스, 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴

소프트웨어의 비즈니스 로직과 화면을 구분하는데 중점을 두고 있으며, 이러한 관심사 분리 는 더나은 업무의 분리와 향상된 관리를 제공

소프트웨어를 Model, View, Controller라는 3가지 구성 요소로 구분한 개발 방법론

## Model, View, Controller의 관계

사용자가 Controller를 사용하게되면 Controller는 Model에게서 데이터를 받아오고 받아온 데이터를 통해 View에서 시각적인 부분을 제어하여 사용자에게 전달함

1. 사용자의 Request(요청)를 Controller가 받음
2. Controller는 Service에서 비즈니스 로직을 처리한 후 결과를 Model에 담음
3. Model에 저장된 결과를 바탕으로 시각적 요소 출력을 담당하는 View를 제어하여 사용자에게 전달

## Model, View, Controller의 역할

## Model(모델)

Model은 소프트웨어나 애플리케이션에서 정보 및 데이터 부분을 의미

이는 Controller에게 받은 데이터를 조작(가공)하는 역할을 수행한다고 볼 수 있음

즉, 데이터와 관련된 부분을 담당하며 값과 기능을 가지는 객체

## View(뷰)

입력값이나 체크박스 등과 같은 사용자 인터페이스 요소를 나타냄

Controller에게 받은 Model의 데이터를 사용자에게 시각적으로 보여주기 위한 역할을 수행

사용자에게 보여지는 화면.

## Controller(컨트롤러)

Model과 View 사이에서 데이터 흐름을 제어 사용자가 접근한 URL에 따라 요청을 파악하고 URL에 적절한 Method를 호출하여 Service에서 비즈니스 로직을 처리 이 후 결과를 Model에 저장하여 View에게 전달하는 역할을 수행

Controller는 Model과 View의 역할을 분리하는 중요한 요소
