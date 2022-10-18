def solution(arr):
    answer = [] # answer 리스트 생성
    answer.append(arr[0]) # 배열 arr의 첫번째 인덱스 값 answer에 추가
    for i in range(1, len(arr)) # i는 1부터 arr의 길이만큼 순회
        if arr[i] != arr[i-1]: # 만약 배열의 i 인덱스 값이 그 전 인덱스(i-1)과 같지 않다면 [1, 3] 같이
            answer.append(arr[i]) # 배열의 i 인덱스 값을 answer에 추가
    return answer # 제거된 후 남은 수들을 반환한다.