import sys
input = sys.stdin.readline # readline : 한 줄 씩 읽는다. readlines : 한 줄 한 줄이 각각 리스트의 원소로 들어간다.   

num = list(map(int, input().split())) # 4개의 정수를 입력받는다.
num.sort()
# print(num) [-10, -3, -1, 5]

x = abs(num[0] - num[2])
y = abs(num[1] - num[3])
# print(x, y) 9 8
print(x+y)

# print(num[3] +  num[2] - num[1] - num[0]) sort() 정렬 후 num에서 다음과 같이 계산해도 된다. 4-(-13) = 17