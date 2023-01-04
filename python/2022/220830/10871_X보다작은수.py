N, X = map(int, input().split()) # N : 정수의 개수, X : 정수
list_ = list(map(int, input().split())) # N개의 정수를 list_ 리스트에 담는다.
for i in list_: # i가 list_의 요소일 때
    if i < X: # i가 정수 X보다 작다면
        print(i, end=" ") # i를 출력한다. (입력받은 순서대로 공백으로 구분해 출력한다) -- 굳이 1, 2, 3, 4 순으로 정렬하지 않아도 됨!