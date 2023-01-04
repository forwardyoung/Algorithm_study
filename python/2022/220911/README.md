## 🔎 SWEA 1983 조교의 성적 매기기

- 모의고사 때 풀다가 출력 부분에서 막혔던 문제인데 오랜만에 다시 풀어보니 아직 인덱싱을 완벽하게 구현하지 못하는 것 같다.
- `x = score_list[b-1]` (b번째는 b-1인덱스에 존재), `score_list.index(x)`로 등수 출력하기!
- **sorted**는 정렬된 새로운 리스트를 리턴 시켜주지만, **sort** 메서드는 아무것도 리턴시켜주지 않음 (None)
- ⚠️ 총점 리스트 score를 생성할 때 test case 반복문 안에서 생성하지 않으면
  TypeError: 'builtin_function_or_method' object is not subscriptable 혹은 IndexError: list index out of range 에러가 자꾸 발생한다.

## 🔎 SWEA 1961 숫자배열회전

- 두려워했던 이차원 리스트 문제를 더 많이 풀어보자!
- 회전할 때 인덱스가 어떻게 변하는지 알면 풀기 쉬운 문제였다.
