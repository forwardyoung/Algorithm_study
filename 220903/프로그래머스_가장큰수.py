def solution(numbers):
    numbers = list(map(str, numbers))
    # print(numbers) ['3', '30', '34', '5', '9']
    # numbers.sort(reverse = True) # 기댓값 9534330과 실행 결과가 다름.
    # [999, 555, 343434, 303030, 333]
    numbers.sort(key=lambda x : x*3, reverse = True) # sort 함수는 key값을 기준으로 정렬, lambda 인자 : 표현식 
    # print(numbers) ['9', '5', '34', '3', '30']
    return str(int(''.join(numbers))) # 모든 값이 0일 때 '000'의 경우, int로 변환한 뒤 다시 str으로 변환한다.