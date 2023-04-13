from collections import deque

def solution(begin, target, words):
    if target not in words: # target이 words 안에 없으면 변환 불가능하므로 0 반환
        return 0
    q = deque ()
    q.append([begin, 0]) # 시작하는 단어, 깊이
    
    while q:
        word, cnt = q.popleft() # q에서 한 개를 뺀다
        
        if word == target: # word가 원하는 target이 된다면 끝낸다
            return cnt # 단계 수 
            
        for i in range(len(words)):
            temp_cnt = 0 
            for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
            if temp_cnt == 1:   # 만약 다른 글자 개수가 1개라면
                    q.append([words[i], cnt+1])
    return 0 # target값이 있으나 변환될 수 없다면
            
