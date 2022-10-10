> 🤯 문제를 똑바로 읽자!

## 단어장 만들기 문제
- 알고리즘 : 정렬, 구현, 문자열
- 단어들을 정렬하고 번에 위치한 단어를 출력해야 한다. ➡️ 길이가 짧을수록 앞에 있고 길이가 같다면, 사전 순으로 정렬한다.
- `sorted 함수`는 정렬된 새로운 리스트를 리턴시켜주는 반면, `sort 메소드`는 아무것도 리턴시켜주지 않는다. (None을 리턴시켜줌).
- list를 변경하려면 list.sort()를 사용하고, 새로운 정렬된 객체를 원하면 sorted()를 사용하면 된다.
---
- `lambda x:x` 를 통해 안에 있는 엘리먼트를 내가 지정한 상태를 기준으로 정렬
- 단어의 길이로 정렬하기 위해 `list_.sort(key = lambda x : len(x))` 

```
test = [(1, 8), (2, 3), (7, 9), (6, 1), (4, 5)]
print(sorted(test, key = lambda x:x[1]))
# [(6, 1), (2, 3), (4, 5), (1, 8), (7, 9)]
```

🔎 [참고](https://edu.goorm.io/learn/lecture/33428/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%A8%BC%EB%8D%B0%EC%9D%B4-%EC%B1%8C%EB%A6%B0%EC%A7%80-%ED%95%B4%EC%84%A4/lesson/1664564/%EC%98%88%EC%8B%9C-%EB%AC%B8%EC%A0%9C%ED%95%B4%EC%84%A4-1-%EB%8B%A8%EC%96%B4%EC%9E%A5-%EB%A7%8C%EB%93%A4%EA%B8%B0)

