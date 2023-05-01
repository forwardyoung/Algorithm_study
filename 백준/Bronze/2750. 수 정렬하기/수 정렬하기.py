# 버블 정렬 알고리즘 O(n^2) 이용하여 풀이 
N = int(input())
numbers = [0]*N # N개의 수 저장 리스트 선언 

for i in range(N):
    numbers[i] = int(input()) # 수 입력 받기
    
for i in range(N-1):
    for j in range(N-1): # j를 0부터 N-1-i만큼 반복
        if numbers[j] > numbers[j+1]: # 현재 숫자 리스트 값보다 1칸 옆(오른쪽) 값이 더 작으면
            # 두 수 바꾸기
            temp = numbers[j] # 현재 값을 임시로 temp에 저장
            numbers[j] = numbers[j+1] # 현위치 값을 오른쪽 (더 작은) 값으로 바꾼다
            numbers[j+1] = temp # 오른쪽 값은 임시로 저장했던 temp로

for num in numbers:
    print(num) # 정렬된 숫자 리스트 출력

# 버블 정렬 두번째 풀이
# N = int(input())
# numbers = [] # 숫자 리스트 생성

# for _ in range(N) : 
#    numbers.append(int(input())) # N개의 수 리스트에 저장

# 버블 정렬
# for i in range(len(numbers)) : 
#    for j in range(len(numbers)) : 
#        if numbers[i] < numbers[j] : # 왼쪽 값이 오른쪽보다 크다면
#            numbers[i], numbers[j] = numbers[j], numbers[i] # 두 수를 바꾼다.
            
#for n in numbers : 
#    print(n) # 정렬된 숫자 출력

# sort 이용한 풀이
# N = int(input())
# number = [] # 리스트 생성
# for i in range(N):
#    number.append(int(input()))

# number.sort()
# for i in range(len(number)):
#    print(number[i])
