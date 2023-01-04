S = input() # 알파벳 소문자로만 이루어진 문자열 S 입력 받음
word = set() # 
for i in range(len(S)):
    for j in range(i,len(S)):
        word.add(S[i:j+1]) # 0~4까지 인덱스 부분문자열 

print(len(word)) 
