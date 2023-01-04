N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
mid = int((N+1)/2) # 중간값은 numbers 리스트에서 몇 번째 숫자?
print(numbers[mid-1]) # 인덱스는 1을 빼줘야 함.