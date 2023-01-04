> collections.defaultdict
: 값(value)에 초기값을 지정하여 딕셔너리를 생성하는 모듈

```python
from collections import defaultdict

text = "Life is too short, You need python."

d = defaultdict(int)
for c in text:
    d[c] += 1

print(dict(d))
```

- defaultdict()의 인수로 int를 전달하여 딕셔너리 d를 생성
- int를 기준으로 생성한 딕셔너리 d의 값은 항상 0으로 자동 초기화되므로 초기화를 위한 별도의 코드가 필요 없다.

📍 defaultdict()의 인수로는 int 외에도 list 등 여러 자료형을 사용할 수 있다.