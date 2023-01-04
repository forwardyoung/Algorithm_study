import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split())) # 상근이가 가지고 있는 숫자 카드
M = int(input())
cnt_card = list(map(int, input().split())) # 상근이가 몇 개 가지고 있는지 비교할 숫자 카드

dic = {} # 딕셔너리 생성 (key : 카드 번호 value : 각 카드 번호가 몇 개 있는지)
# dic = dict()로 생성해도 됨

for i in card: 
    if i in dic: # i가 딕셔너리에 존재하는 key라면
        dic[i] += 1 # value에 1을 더한다.
    else:
        dic[i] = 1 # 존재하지 않는다면 value는 그냥 1이다.

for i in cnt_card:
    if i in dic: # i가 딕셔너리에 존재하는 key라면
        print(dic[i] , end = " ") # dic 딕셔너리의 i라는 key에 해당하는 value(상근이가 cnt_card를 몇 개 가지고 있는지) 출력
    else:
        print(0, end=" ") # 존재하지 않는다면 0 출력

# 위의 2번의 for문에서 if, else 문 대신 try, except로 작성해도 됨

# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드

# for i in card: 
#     try:
#         dic[i] += 1
#     except:
#         dic[i] = 1