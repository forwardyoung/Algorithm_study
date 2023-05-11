from collections import deque

S = int(input())
q = deque()
q.append((1, 0)) # 현재 이모티콘 개수, 클립보드 이모티콘 개수
visited = dict()
visited[(1, 0)] = 0 # 방문 표시 딕셔너리로

while q:
    now, clip = q.popleft()
    if now == S: # 현재 이모티콘 수가 S라면
        print(visited[(now, clip)]) # 걸린 시간 출력
        break  
    if (now, now) not in visited.keys():
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
        visited[(now, now)] = visited[(now, clip)] + 1 # 1초 더하기
        q.append((now, now))
    if (now+clip, clip) not in visited.keys():
        # 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
        visited[(now+clip, clip)] = visited[(now, clip)] + 1 # 1초 더하기
        q.append((now+clip, clip))
    if(now-1, clip) not in visited.keys():
        # 화면에 있는 이모티콘 중 하나를 삭제
        visited[(now-1, clip)] = visited[(now, clip)] + 1 # 1초 더하기
        q.append((now-1, clip))