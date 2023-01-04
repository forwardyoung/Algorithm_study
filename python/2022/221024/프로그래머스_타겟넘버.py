def solution(numbers, target):
    answer = 0 # 타겟 넘버를 만드는 방법의 수
    arr = [0]  # 타겟과 비교할 수를 넣을 배열 -> 처음 계산을 해야하니 초기값 필요
    
    for i in numbers:
        tmp = []  # 한 사이클 결과값 임시 저장 배열
        for j in arr:
            tmp.append(j + i)
            tmp.append(j - i)
        arr = tmp #임시 저장 배열 arr에 넣어주기
    
    for i in arr:
        if i == target: # 타겟과 arr[i]값 비교
            answer += 1
    
    return answer