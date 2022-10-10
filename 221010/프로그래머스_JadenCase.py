# 파이썬 문자열 capitalize()
# 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

def solution(s):
    answer = ''
    list_ = s.split(' ') # 입력받은 문자열 s를 공백 기준으로 split

    for i in range(len(list_)):
        list_[i] = list_[i].capitalize()
        
    answer = ' '.join(list_) # 리스트를 문자열로 합치기
    
    return answer