# 코딩 테스트에 끝말잇기 문제가 나왔었음

def solution(n, words):
    answer = [0,0]

    cnt = 0  # cnt를 계산하여 answer 리스트에 활용할 것임
    list_ = []  # 나온 단어 확인할 리스트
    list_.append(words[0])
    
    for i in range(1, len(words)): 
        cnt += 1
        # 등장하지 않은 단어이고 이전 단어의 마지막 알파벳과 일치하면 단어 리스트에 넣음 
        if words[i] not in list_ and list(words[i-1])[-1] == list(words[i])[0]:
            list_.append(words[i])
        else: # 탈락
            answer[0] = cnt%n +1  # 가장 먼저 탈락하는 사람의 번호
            answer[1] = cnt//n +1  # 몇 번째로 탈락하는지
            break

    return answer