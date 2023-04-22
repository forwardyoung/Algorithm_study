def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량 진출 지점 기준으로 정렬한다.
    camera = -30001 # 차량 진입, 진출 지점 -30000이상이므로 -30001부터 카메라 위치 찾는다.
    for route in routes:
        if route[0] > camera: # 카메라 위치가 진입 지점보다 뒤에 있으면(차량과 카메라가 만나지 않으면)
            answer += 1 # 카메라 개수에 1을 더한다.
            camera = route[1] # 카메라 위치를 진출 지점으로 갱신
    return answer 