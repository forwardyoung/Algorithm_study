from collections import deque

def solution(begin, target, words):
    if target not in words: # target이 words 안에 없으면 변환 불가능하므로 0 반환
        return 0
    q = deque ()
    q.append([begin, 0]) # 시작하는 단어, 변환(이동)횟수
    V = [ 0 ] * (len(words))    # 방문 노드 여부 확인 리스트
    
    while q:
        word, cnt = q.popleft() # q에서 한 개를 뺀다
        
        if word == target: # q에서 pop한 단어가 target과 일치하면 cnt 출력
            return cnt # 단계 수 
            
        for i in range(len(words)):
            temp_cnt = 0 
            if not V[i]:    # 만약 확인 안 한 단어라면
                # 그 단어가 words 속 단어와 다를 때 한 자씩 비교해서 더하기
                for j in range(len(word)):
                        if word[j] != words[i][j]:
                            temp_cnt += 1
                if temp_cnt == 1:   # 만약 다른 글자 개수가 1개라면
                        q.append([words[i], cnt+1])
                        V[i] = 1
    return 0 # target값이 있으나 변환될 수 없다면
            
