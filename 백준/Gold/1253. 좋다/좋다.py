import sys
input = sys.stdin.readline

N = int(input())
cnt = 0 # 좋은 수 개수 
numbers = list(map(int, input().split())) # N개의 수 입력 받고
numbers.sort() # 정렬

for k in range(N):
    find = numbers[k] # 찾고자 하는 값
    # 투 포인터 i, j 리스트의 양쪽 끝에 위치시킨다
    i = 0 
    j = N - 1
    while i < j: # 투 포인터 알고리즘
        if numbers[i] + numbers[j] == find: # 서로 다른 두 수의 합이 find라면
            if i != k and j != k: # i와 j가 k가 아닐 때
                cnt += 1 # 좋은 수 개수 1 증가
                break # while 문 종료
            elif i == k:
                i += 1 # 포인터 변경
            elif j == k:
                j -= 1                
        elif numbers[i] + numbers[j] < find: # find가 더 크다면
            i += 1 # 포인터 i 증가(오른쪽으로)
        else: # find가 더 작다면
            j -= 1 # 포인터 j 감소(왼쪽으로)
 
print(cnt) # 좋은 수 개수 출력