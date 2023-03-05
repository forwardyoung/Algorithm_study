# 모듈

파이썬에서 모듈(module)은 `def`를 사용하여 정의한다.

`def`가 실행되면, 함수의 객체와 참조가 같이 생성된다.

반환값(`return value`)을 정의하지 않으면, 파이썬은 자동으로 `None`을 반환한다.

아무런 값을 반환하지 않는 함수는 **프로시저(procedure)**라고 부른다.

### 모듈의 기본값

- 모듈을 생성할 때, 함수 또는 메서드에서 가변 객체(매개 변수)를 기본값으로 사용하면 안 된다.

나쁜 예)

```python
def append(number, number_list=[]):
    number_list.append(number)
    return number_list

append(5) # [5]

append(7) # [5, 7]

append(2) # [5, 7, 2]
```

좋은 예)

```python
def append(number, number_list=None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    return number_list

append(5) # [5]

append(7) # [7]

append(2) # [2]
```

