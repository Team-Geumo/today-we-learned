### python에서 replace

- 문자열 치환 함수
  
  - 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    
    - 내 풀이
      
      ```python
      cnt = 0
      for i in range(len(temp)):
          if temp[i] == '.':
              cnt += 1
          else:
              if not cnt:
                  answer += temp[i]
              else:
                  answer = answer + '.' + temp[i]
                  cnt = 0
      ```
    
    - replace 사용
      
      ```python
      while '..' in answer:
          answer = answer.replace('..', '.')
      ```