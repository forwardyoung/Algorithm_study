n = int(input()) # 팀 수 입력 받는다.
w = list(map(int, input().split())) # 코딩 역량을 나타내는 2n개의 정수


asc = sorted(w) # 코딩 역량 w 오름차순 정렬
desc = sorted(w, reverse=True) # 내림차순 정렬

arr = []
for i in range(len(w)): 
    sum_ = asc[i] + desc[i] # 역량 w가 가장 높은 학생과 가장 낮은 학생이 한 팀이 된다.
    arr.append(sum_) # 각 팀당 역량의 합들을 arr에 추가

# w가 {1, 7, 3, 5, 9, 2}라면 (9, 1), (7, 2), (5, 3)의 3개 조를 짤 수 있고
# w의 합 10, 9, 8 중 8을 출력해야 한다.

print(min(arr)) # arr 중 가장 작은 것을 출력한다.
