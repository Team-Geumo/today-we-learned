## 프로그래밍 패러다임 (Programming Paradigm)

- 명령형 프로그래밍
  
  - 무엇을 할 것인지 < `어떻게 할 것인지`
  
  - 절차지향 프로그래밍
  
  - 객체지향 프로그래밍

- 선언형 프로그래밍
  
  - `무엇을 할 것인지` > 어떻게 할 것인지
  
  - 함수형 프로그래밍

### 함수형 프로그래밍 (Functional Programming)

- 개념
  
  - `순수 함수`를 블록처럼 쌓아 로직을 구현하고 `고차 함수`를 통해 재사용성을 높인 프로그래밍 패러다임
    
    - 순수함수 (Pure Functions)
      
      - 동일한 인자를 넣었을 때 항상 동일한 결과값을 반환하고 언제 선언이 되었는지 외부에 전혀 영향을 작성해야 함
        
        ```js
        // 순수함수
        function add(a, b) {
            return a + b;
        }
        
        // 순수함수가 아닌 경우
        let b = 3;
        function add(a) {
            return a + b;
        }
        ```
    
    - 고차함수 (Higher-order Functions)
      
      - 함수가 함수를 값처럼 매개변수로 받아 로직을 생성할 수 있는 것
        
        ```js
        const addSauce = (rice) => (sauce) => sauce + rice;
        const rice = addSauce("밥");
        
        console.log(rice("간장계란"))
        ```
      
      - 해당 언어가 일급 객체의 특징을 가져야 함
        
        - 일급 객체 (First-class)
          
          - 변수나 메서드에 함수를 할당할 수 있음
          
          - 함수 안에 함수를 매개변수로 담을 수 있음
          
          - 함수가 함수를 반환할 수 있음
            
            ```js
            const addOne = (num) => num + 1;
            const multiplyThree = (num) => num * 3;
            const addOneMultiplyThree = (numbers) => numbers.map(addOne).map(multiplyThree);
            
            console.log(addOneMultiplyThree([2, 5, 7, 8]))
            ```

- 특징
  
  - 비상태 (Stateless), 불변성 (Immutability)
    
    - 전달된 데이터를 변경하는 것이 아니라 새로운 버전의 새로운 오브젝트를 만들어서 결과값으로 전달해야 함
    
    - 부작용 (side effect)을 만들지 않으므로 불변성을 유지하기 때문에 **여러가지 동시다발적인 멀티쓰레딩 환경에서도 안정적으로 동작**할 수 있음
  
  - expression만 사용
    
    - if, switch, for과 같은 명령문 사용 X
    
    - map, filter, reduce와 같은 함수 이용

- 장점
  
  - 높은 수준의 추상화
  
  - 함수 단위의 코드 재사용 수워
  
  - 불변성을 지향하기 때문에 프로그램의 동작 예측 용이

- 단점
  
  - 코드의 가독성이 좋지 않을 수 있음
  
  - 조합하기 쉽지 않음