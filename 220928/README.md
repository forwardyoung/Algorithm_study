# 🔎 백준 12738번 가장 긴 증가하는 부분 수열 3
## 최장 증가 부분 수열(LIS)
> LIS : Longest Increasing Subsequence
어떤 임의의 수열이 주어질 때, 이 수열에서 몇 개의 수들을 제거해서 부분수열을 만들 수 있다.

이때 만들어진 부분수열 중 *오름차순으로 정렬된 가장 긴 수열*을 **최장 증가 부분 수열**이라 한다.

- 한 수열에서 여러 개의 LIS가 나올 수도 있다.
- ex) 수열 `5 1 6 2 7 3 8`에서 부분수열 `1 2 3 8`, `5 6 7 8`은 모두 길이가 4인 LIS
- **Dynamic programming**에서 유명한 문제 ➡️ 재귀 함수로도 풀 수 있음 ➡️ 시간복잡도(2^n) 😥
- for문으로 N을 한 번 돌린 이진탐색으로 풀면 시간복잡도는 NlogN
- 라이브러리 **bisect** 사용

## bisect 라이브러리
> bisect : 이진 탐색 알고리즘을 구현한 모듈로, 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 반환한다.
-  bisect_left(list, data): 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지)
- bisect_right(list, data): 리스트에 데이터를 삽입할 가장 오른쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지)
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 5, 10]
x = 3
# bisect_left: 2, bisect_right: 4
```
- bisect_left(a, x) : a에 x를 삽입할 위치 (기존 항목 앞)
- bisect_right(a, x) : a에 있는 x의 기존 항목 뒤에 오는 삽입 위치
---

🌍 [출처1](https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4)
🌍 [출처2](https://heytech.tistory.com/79)

