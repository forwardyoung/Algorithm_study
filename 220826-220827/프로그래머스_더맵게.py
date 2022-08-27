import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 최소 힙 생성, 초기화
    
    while scoville:
        first = heapq.heappop(scoville)
        
        if first >= K: # 힙의 첫 원소가 K보다 작아야한다.
            break
        
        if len(scoville) <= 0: # 모든 음식의 스코빌 지수가 K 이상이 아니면
            return -1  # -1을 return
            
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1
    
    return answer