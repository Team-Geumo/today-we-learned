# Dawn JavaAPI

오늘 javaAPI 나가?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 동일성과 동등성

```java
두 객체가 할당된 메모리 주소가 같으면 동일하고, 두 객체의 내용이 같으면 동등하다고 말한다. 
동일성은 == 연산자를 통해 판별할 수 있고, 
동등성은 equals 연산자를 통해 판별할 수 있다.
equals 연산자는 재정의하지 않으면 내부적으로 == 연산자와 같은 로직을 수행하므로 차이가 없다. 
따라서 equals 연산자는 각 객체의 특성에 맞게 재정의를 해야 동등성의 기능을 수행한다.
```

# hashing

https://mattlee.tistory.com/62

- **해싱은 키 값에 직접 산술적인 연산을 적용**하여 항목이 저장되어 있는 **테이블의 주소를 계산하여 항목에 접근**한다. 이렇게 키 값의 연산에 의해 직접 접근이 가능한 구조를 **해시 테이블(hash table)**이라 부르고, 해시 테이블을 이용한 탐색을 **해싱(hashing)**이라 한다.

# hash 함수

- **해시 함수(hash function)**란 탐색 키를 입력으로 받아 **해시 주소(hash address)**를 생성하고 이 해시 주소가 배열로 구현된 **해시 테이블(hash table)의 인덱스**가 된다. 이 배열의 인덱스 위치에 자료를 저장할 수도 있고 저장된 자료를 꺼낼 수도 있다. 예를 들어 영어 사전을 **배열 hashTable[ ]**에 저장한다고 하면 단어를 **해싱 함수를 이용**하여 적절한 **정수 i로 변환**한 다음, 배열 요소 **hashTable[ i ]에 단어의 정의를 저장**하는 것이다.

### String s = “hello” && String s = new String(”hello”)

### String s = “hello”의 경우

### 1. hashing → constant pool 에서 탐색

### 2. 없으면 new (hash값, reference 저장)

### 3. String s2=”hello”가 들어오면

### 4. 같은 hash에 저장

### String method

```java
package chapter04;

public class StringTest04 {

	public static void main(String[] args) {
		// String s1 = "Hello" + "World" + "Java" + 17;
		StringBuffer sb = new StringBuffer("Hello");
		sb.append("World");
		sb.append("Java");
		sb.append(17);
		String s1 = sb.toString();
		System.out.println(s1);
		String s2 = new StringBuffer("Hello").append("World").append("Java").append(17).toString();

		String s3 = "";
		for (int i = 0; i < 1000000; i++) {
			// s2 += i;
			// new StringBuffer(s2).append(i).toString();
		}
		StringBuffer sb2 = new StringBuffer("");
		for (int i = 0; i < 100000; i++) {
			sb2.append(i);
		}
		String s4 = sb2.toString();

		// String method
		String s5 = "aBcABCabcAbc";
		System.out.println(s5.length());
		System.out.println(s5.charAt(0));
		System.out.println(s5.indexOf("abc")); // 없으면 -1
		System.out.println(s5.substring(0, 3)); // 0 ~ 2까지

		String s6 = "   ab   cd   ";
		String s7 = "efg,hij,klm,nop,qrs";
		String s8 = s6.concat(s7);
		System.out.println(s8.trim()); // 양쪽 공백 없애기
		System.out.println(s8.replaceAll(" ", "")); // A를 B로 대체

		String[] tokenStrings = s7.split(",");
		for (String s : tokenStrings) {
			System.out.println(s);
		}

		String[] tokens2 = s7.split(" ");
		for (String s : tokens2) {
			System.out.println(s); // 원본 결과
		}
	}

}
```

# java.lang

# java.util

- `Collection Framework`
    - map, set, stack …

# java.io

# java.net

- socket

## Singleton Pattern

- 팩토리 메소드
- **객체의 인스턴스가 오직 1개만 생성**되는 패턴