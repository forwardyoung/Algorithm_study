## 스택과 활성화 레코드

('[파이썬 자료구조와 알고리즘](https://product.kyobobook.co.kr/detail/S000001810161)' 서적을 읽으며 정리한 내용)

#### 활성화 레코드(Activation Records)란?

> 활성화 레코드는 프로시저 한 번 실행하는 데 필요한 정보를 관리하는 연속된 스토리지 블록

함수가 호출될 때마다 활성화 레코드가 생성되는데, 활성화 레코드에는 다음 그림과 같은 함수의 정보가 기록되며 이를 스택에 저장한다.

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210625101557/Activationrecord.png)

### 활성화 레코드 처리 순서

1) 함수의 실제 매개변수를 스택에 저장(push)한다.
2) 반환 주소를 스택에 저장
3) 스택의 최상위 인덱스를 함수의 [지역 변수](https://wikidocs.net/62)에 필요한 총량만큼 늘린다.
4) 함수로 건너뛴다(jump).

### 활성화 레코드를 풀어내는(unwinding) 절차

1. 스택의 최상위 인덱스는 함수에 소비된 총 메모리양(지역 변수)만큼 감소한다.
2. 반환 주소를 스택에서 빼낸다(pop).
3. 스택의 최상위 인덱스는 함수의 실제 매개변수만큼 감소한다.



**참고**

- [Activation Records](https://www.geeksforgeeks.org/access-links-and-control-links/)