def solution(n, computers):
    def DFS(i):
        visited[i] = 1 # 방문 처리
        for j in range(n):
            if computers[i][j] and not visited[j]:
                DFS(j)
    answer = 0
    visited = [0 for i in range(len(computers))] # 컴퓨터의 개수와 동일한 크기의 방문 리스트 생성
    for i in range(n):
        if not visited[i]: # 방문하지 않은 컴퓨터라면
            DFS(i)
            answer += 1 # 네트워크 개수에 1을 더한다.
        
    return answer
