import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split())) # 상근이가 가지고 있는 숫자 카드
M = int(input())
cnt_card = list(map(int, input().split())) # 상근이가 몇 개 가지고 있는지 비교할 숫자 카드

dic = dict() 

# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드

for i in card: #
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in cnt_card:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")
