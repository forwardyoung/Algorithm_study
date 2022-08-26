import sys
input = sys.stdin.readline

censor = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = input()
for i in range(len(word)):
    if word[i] not in censor: # censor 리스트에 없는 철자만
        print(word[i], end= '') # end= '' : 띄어쓰기 없이 출력
