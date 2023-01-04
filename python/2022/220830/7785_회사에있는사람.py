dic = {}
n = int(input())
for i in range(n):
    s, l = list(input().split()) # s : 직원 이름, l : 출입 기록
    dic[s] = l

dic = sorted(dic.items(), reverse=True) # 딕셔너리 역순으로 정렬
# print(dic) [('Baha', 'leave'), ('Askar', 'enter'), ('Artem', 'enter')]

for i in dic:
    if i[1] == 'enter':
        print(i[0])