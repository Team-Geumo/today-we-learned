# [Java] 컬렉션(Collection)

## 2. List Interface

- 정렬될 모든 객체 컬렉션을 저장할 수 있는 목록 데이터 전용
- 인터페이스에는 ArrayList, Vector, Stack 등이 대표적

<br>

### 2.1. ArrayList

- 동적 배열을 제공
- 표준 배열보다 느릴 수 있지만 배열에서 많은 움직임이 필요한 프로그램에서 유용
- 컬렉션에서 개체를 추가, 삭제하면 ArrayList의 크기가 자동으로 조정됨

```java
import java.io.*;
import java.util.*;
  
class GFG {
    public static void main(String[] args)
    {
  
        // ArrayList 선언
        ArrayList<Integer> al
            = new ArrayList<Integer>();
  
        // ArrayList에 데이터 입력
        for (int i = 1; i <= 5; i++)
            al.add(i);
  
        // 결과 출력
        System.out.println(al);
  
        // 3번 데이터 제거
        al.remove(3);
  
        // 결과 출력
        System.out.println(al);
  
        // 하나씩 가져와서 결과 출력
        for (int i = 0; i < al.size(); i++)
            System.out.print(al.get(i) + " ");
    }
}
```

```bash
[1, 2, 3, 4, 5]
[1, 2, 3, 5]
1 2 3 5
```

<br>

### 2.2. LinkedList

- 요소가 연속 된 위치에 저장되지 않고 모든 요소가 데이터 부분과 주소 부분이 있는 별도의 객체에 저장됨
- 포인터와 주소를 사용해서 데이터를 가져옴
- 각 요소를 노드라고 부름

```java
import java.io.*;
import java.util.*;
  
class GFG {
    public static void main(String[] args)
    {
  
        // LinkedList 선언
        LinkedList<Integer> ll
            = new LinkedList<Integer>();
  
        // 값 입력
        for (int i = 1; i <= 5; i++)
            ll.add(i);
  
        // 결과 출력
        System.out.println(ll);
  
        // 3번 데이터 삭제
        ll.remove(3);
  
        // 결과 출력
        System.out.println(ll);
  
        // 결과를 하나씩 출력
        for (int i = 0; i < ll.size(); i++)
            System.out.print(ll.get(i) + " ");
    }
}
```

```bash
[1, 2, 3, 4, 5]
[1, 2, 3, 5]
1 2 3 5
```

<br>

### 2.3. Vector

- 동적 배열을 제공하고, 표준 배열보다 느리지만 많은 움직임이 필요한 프로그램에서 유용
- ArrayList와 유사
- Vector는 동기화가 되고, ArrayList는 동기화가 되지 않는다는 것이 차이점

```java
import java.io.*;
import java.util.*;
  
class GFG {
    public static void main(String[] args)
    {
  
        // Vector 선언
        Vector<Integer> v
            = new Vector<Integer>();
  
        // 데이터 입력
        for (int i = 1; i <= 5; i++)
            v.add(i);
  
        // 결과 출력
        System.out.println(v);
  
        // 3번 데이터 삭제
        v.remove(3);
  
        // 결과 출력
        System.out.println(v);
  
        // 하나씩 결과 출력
        for (int i = 0; i < v.size(); i++)
            System.out.print(v.get(i) + " ");
    }
}
```

```bash
[1, 2, 3, 4, 5]
[1, 2, 3, 5]
1 2 3 5
```

<br>

### 2.4. Stack

- 스택 클래스 모델 및 스택 데이터 구조를 구현할 때 주로 사용
- 후입선출을 기본 원칙으로 함

```java
import java.util.*;
public class GFG {
    public static void main(String args[])
    {
        Stack<String> stack = new Stack<String>();
        stack.push("Hello");
        stack.push("World!");
        stack.push("Hello");
        stack.push("Hello");
  
        // Stack Iterator 선언
        Iterator<String> itr
            = stack.iterator();
  
        // 결과 출력
        while (itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
  
  		// Enter입력
        System.out.println();
  
  		// 후입선출
        stack.pop();
  
        // 재정의
        itr
            = stack.iterator();
  
        // 결과 출력
        while (itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
    }
}
```

```bash
Hello World! Hello Hello
Hello World! Hello
```

<br>

---

<br>

## 3. Queue Interface

- 대기열 인터페이스라는 이름에서 알 수 있듯이 선입선출을 기본적으로 사용
- 순서가 중요한 업무에서 주로 사용
- ex) 선착순 티켓 판매
- PriorityQueue, Deque, ArrayDeque 등과 같은 클래스가 있음

<br>

### 3.1. PriorityQueue

- 우선 순위에 따라 객체를 처리해야 할 때 사용
- 선입선출 기본으로 하지만 우선 순위에 따라 먼저 처리해야할 것이 있다면 우선 순위 힙을 기반으로 처리

```java
import java.util.*;
  
class GfG {
    public static void main(String args[])
    {
        // 우선순위 큐 선언
        PriorityQueue<Integer> pQueue
            = new PriorityQueue<Integer>();
  
        // 데이터 입력
        pQueue.add(10);
        pQueue.add(20);
        pQueue.add(15);
  
        // 첫 번째 데이터 결과 출력
        System.out.println(pQueue.peek());
  
        // 오름차순하여 데이터 출력 -> 출력한 데이터는 제거된다
        System.out.println(pQueue.poll());
  
        // 두 번째 데이터 15 출력
        System.out.println(pQueue.peek());
    }
}
```

```bash
10 
10 
15
```

<br>

---

<br>

## 4. Deque Interface

- 큐 데이터 구조의 변형
- 양방향 큐라고도 불리고 양쪽 끝에서 요소를 추가하고 제거할 수 있는 구조

<br>

### 4.1. ArrayDeque

- 크기가 조정되는 배열이고 양쪽 끝에서 요소를 추가하고 제거하는 구조

```java
import java.util.*;
public class ArrayDequeDemo {
    public static void main(String[] args)
    {
        // Deque 선언
        ArrayDeque<Integer> de_que
            = new ArrayDeque<Integer>(10);
  
        // 값 입력
        de_que.add(10);
        de_que.add(20);
        de_que.add(30);
        de_que.add(40);
        de_que.add(50);
  
  		// 결과 출력
        System.out.println(de_que);
  
        // deque초기화
        de_que.clear();
  
        // 첫 번째에 데이터 입력
        de_que.addFirst(564);
        de_que.addFirst(291);
  
        // 마지막에 데이터 입력
        de_que.addLast(24);
        de_que.addLast(14);
  
  		// 결과 출력
        System.out.println(de_que);
    }
}
```

```bash
[10, 20, 30, 40, 50] 
[291, 564, 24, 14]
```

<br>

---

<br>

## 5. Set Interface

- 중복 값을 저장할 수 없는 정렬되지 않은 데이터 모음
- 중복을 방지하고 고유한 데이터만 저장해야하는 경우 사용
- HashSet, TreeSet, LinkedHashSet 등에서 사용

<br>

### 5.1. HashSet

- HashSet에 입력되는 데이터는 동일한 순서로 삽입되는 것을 보장하지 않음
- 이 클래스는 NULL 요소 삽입을 허용

```java
import java.util.*;
public class HashSetDemo {
    public static void main(String args[])
    {
        // HashSet 선언 및 데이터 입력
        HashSet<String> hs = new HashSet<String>();
  
        hs.add("Hello");
        hs.add("World");
        hs.add("Hello");
        hs.add("Blog");
        hs.add("CrazyKim");
  
        // Traversing elements
        Iterator<String> itr = hs.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
    }
}
```

```bash
Hello
CrazyKim
World
Blog
```

<br>

### 5.2. LinkedHashSet

-  HashSet과 유사하지만 차이점은 데이터를 저장하는 순서를 유지

```java
import java.util.*;
public class LinkedHashSetDemo {
    public static void main(String args[])
    {
        // LinkedHashSet 선언 및 데이터 입력
        LinkedHashSet<String> lhs
            = new LinkedHashSet<String>();
  
        lhs.add("Hello");
        lhs.add("World");
        lhs.add("Hello");
        lhs.add("blog");
        lhs.add("CrazyKim");
  
        // 결과 출력
        Iterator<String> itr = lhs.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
    }
}
```

```bash
Hello
World
blog
CrazyKim
```

<br>

---

<br>

## 6. Sorted Set Interface

- 위의 Set Interface와 유사하지만 순서를 정렬하는 메서드를 제공

<br>

### 6.1. TreeSet

- Tree를 사용하여 저장
- 데이터의 순서는 자연적인 순서(오름차순)대로 유지됨

```java
import java.util.*;
public class TreeSetDemo {
    public static void main(String args[])
    {
        // TreeSet 변수 선언 및 데이터 입력
        TreeSet<String> ts
            = new TreeSet<String>();
  
        ts.add("Hello");
        ts.add("World");
        ts.add("Hello");
        ts.add("Blog");
        ts.add("CrazyKim");
  
        // Traversing elements
        Iterator<String> itr = ts.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
    }
}
```

```bash
Blog
CrazyKim
Hello
World
```

<br>

---

<br>

## 7. Map Interface

- Map은 데이터를 키 - 값으로 매핑을 지원하는 데이터 구조
- 동일한 키가 여러 개가 있을 수 없어 중복 키는 지원하지 않음
- 키를 기반으로 프로그래밍을 하는 경우 유용
- Map Interface는 HashMap, TreeMap 등의 클래스가 있음

<br>

### 7.1. HashMap

- 자바의 Map Interface의 기본적인 방법
- 데이터를 키 - 값 형태로 저장
- HashMap의 데이터에 접근하려면 키를 알고 있어야 접근이 가능
- Hashing이라는 기술을 사용하는데 해싱은 인덱싱 및 검색 작업이 더 빨라지도록 키에 산술적인 연산을 적용하여 항목이 저장되어 있는 테이블의 주소를 계산하여 항목에 접근하는 방식

```java
import java.util.*;
public class HashMapDemo {
    public static void main(String args[])
    {
        // HashMap 선언 및 데이터 입력
        HashMap<Integer, String> hm
            = new HashMap<Integer, String>();
  
        hm.put(1, "Hello");
        hm.put(2, "World");
        hm.put(3, "CrazyKim");
  
        // 첫 번째 결과 출력
        System.out.println("Value for 1 is " + hm.get(1));
  
        // 전체 결과 출력
        for (Map.Entry<Integer, String> e : hm.entrySet())
            System.out.println(e.getKey() + " " + e.getValue());
    }
}
```

```bash
Value for 1 is Hello
1 Hello
2 World
3 CrazyKim
```
