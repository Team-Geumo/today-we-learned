# 람다(lambda)

## 람다란?

## lambda 매개변수 : 표현식

- 예시 : 두 수를 더하는 함수

```python
>>> def hap(x, y):
...   return x + y
...
>>> hap(10, 20)
```

- 위 함수를 람다 형식으로 표현하기

```python
>>> (lambda x,y: x + y)(10, 20)
```

## map()과 함께 사용하기

- 0부터 4까지 제곱수 배열 생성하기

```python
>>> list(map(lambda x: x ** 2, range(5)))
>>> [0, 1, 4, 9, 16]
```

## reduce()와 함께 사용하기

- 배열의 숫자 더하기

```python
>>> from functools import reduce
>>> reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
>>> 10
```

- 문자열 거꾸로 배치하기

```python
>>> reduce(lambda x, y: y + x, 'abcde')
>>> 'edcba'
```

## filter()와 함께 사용하기

- 0부터 9까지 숫자 중 5보다 작은 것만 리스트로 돌려주기

```python
>>> list(filter(lambda x: x < 5, range(10)))
>>> [0, 1, 2, 3, 4]
```

- 홀수만 리스트로 돌려주기

```python
>>> list(filter(lambda x: x % 2, range(10)))
>>> [1, 3, 5, 7, 9]
```

## sorted()와 함께 사용하기

- 학생 정보의 0번째 원소 (이름) 기준으로 정렬하기

```python
>>> sorted([['김현영', 29], ['김휘영', 35], ['김지영', 37]], key=lambda person: person[0])
>>> [['김지영', 37], ['김현영', 29], ['김휘영', 35]]
```
