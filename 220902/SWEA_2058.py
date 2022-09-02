n = list(input()) # list를 통해 각 자릿수 쪼개기
# print(n) ['6', '7', '8', '9']
numbers = list(map(int, n)) # n을 int로 형변환 
# print(numbers) [6, 7, 8, 9]
print(sum(numbers))