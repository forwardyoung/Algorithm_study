N = int(input())
number = [] # 리스트 생성
for i in range(N):
    number.append(int(input()))

number.sort()
for i in range(len(number)):
    print(number[i])