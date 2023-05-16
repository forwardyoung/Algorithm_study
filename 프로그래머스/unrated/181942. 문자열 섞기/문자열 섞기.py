def solution(str1, str2):
    answer = ''
    max_length = max(len(str1), len(str2)) # 두 문자열의 최대 길이를 결정한다.
    
    # str1과 str2를 번갈아가며 문자를 answer 문자열에 추가한다.
    for i in range(max_length):
        if i < len(str1):
            answer += str1[i]
        if i < len(str2):
            answer += str2[i]
            
    return answer