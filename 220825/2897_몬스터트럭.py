R, C = map(int, input().split())        # 행, 열

parking = []                            # 주차장 상태
for i in range(R):
    parking.append(list(input()))       # 리스트로 저장

destroy = [0] * 5                       # 부수고 주차할 수 있는 공간 개수

for r in range(R-1):                    # 행 범위 지정
    for c in range(C-1):                # 열 범위 지정
        # 범위를 벗어나지 않고 탐색하기 위해 -1
        space = []                      # 4칸(몬스터 트럭 크기) 상태 저장
        space.append(parking[r][c])     # 첫번째 칸 상태
        space.append(parking[r][c+1])   # 두번째 칸 상태
        space.append(parking[r+1][c])   # 세번째 칸 상태
        space.append(parking[r+1][c+1]) # 네번째 칸 상태

        if '#' not in space:            # 4칸에 빌딩이 없으면
            car = space.count('X')      # 주차된 차 수를 세서
            if car == 0:
                destroy[0] += 1         # 부수지 않으면 해당 공간 개수 +1
            elif car == 1:
                destroy[1] += 1         # 1대 부수면 해당 공간 개수 +1
            elif car == 2:
                destroy[2] += 1         # 2대 부수면 해당 공간 개수 +1
            elif car == 3:
                destroy[3] += 1         # 3대 부수면 해당 공간 개수 +1
            elif car == 4:
                destroy[4] += 1         # 4대 부수면 해당 공간 개수 +1

for i in range(5):
    print(destroy[i])                   # destroy 공간 개수 순서대로 출력