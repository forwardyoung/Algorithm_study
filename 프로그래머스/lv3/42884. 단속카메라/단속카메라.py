def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량 진출 지점 기준으로 정렬한다.
    # 이중 리스트 key에 lambda 인자 : 표현식 형태로 정렬
    camera = -30001 # 차량 진입, 진출 지점은 -30000보다는 커야 하므로 -30001부터 카메라 위치 찾는다.
    for route in routes:
        if route[0] > camera: # 카메라 위치가 진입 지점보다 뒤에 있으면(차량과 카메라가 만나지 않으면)
            answer += 1 # 카메라를 새로 설치하고 개수에 1을 더한다.
            camera = route[1] # 카메라 위치를 최근 카메라 진출 지점으로 갱신
    return answer 
