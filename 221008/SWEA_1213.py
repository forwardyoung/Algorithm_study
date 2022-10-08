for _ in range(10): # 총 10개의 테스트 케이스
    T = int(input()) # 테스트 케이스의 번호 입력 받고
    word = input() # 찾을 문자열 
    sentence = input() # 검색할 문장
    
    cnt = sentence.count(word) # 문장에서 문자열 word의 개수를 세는 count() 메서드 사용
    print("#{} {}".format(T, cnt))
        