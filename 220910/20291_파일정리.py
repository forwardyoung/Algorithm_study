N = int(input())

e = []  # 파일의 확장자를 담을 리스트 생성
dict = {}

for _ in range(N):
    file = input().split('.')  # 알바펫 소문자와 .으로 구성된 파일명 입력 받는다.
    # print(file[1]) ==> txt ; 파일명의 [1] 인덱스는 확장자 의미
    e.append(file[1])  # file[1]를 확장자 리스트 e에 추가

for i in e:
    if dict.get(i):  # 딕셔너리의 key를 (e를 순회하는) i로 불러올 수 있으면
        dict[i] += 1  # 확장자 파일의 개수에 1을 더한다.
    else:
        dict[i] = 1  # 확장자 파일의 개수는 1이다.

    # print(dict[i]) ==> 1

dict = sorted(dict.items())  # 키 값(확장자 이름) 기준으로 정렬

# print(dict) [('txt', 1)]

for i, j in dict:
    print(i, j)  # 확장자 이름과 확장자 파일의 개수 출력
