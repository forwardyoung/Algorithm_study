import sys
sys.stdin = open("1983_조교의성적매기기.txt")

T = int(input())


for tc in range(1, T+1):
    a, b = map(int, input().split())  # a : 학생 수, b : 학점을 알고 싶은 학생의 번호

    score = []
    for i in range(a):
        mid, final, homework = map(int, input().split())
        score.append((mid*0.35 + final*0.45 + homework*0.2))  # 총점 계산 후 점수 리스트에 추가
    sort_score = sorted(score, reverse=True)  # 내림차순 성적 총점 리스트

    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade = ''  # 학생이 받을 평점

    for j in sort_score:
        if j == score[b-1]: # 내림차순 정렬된 총점이 점수 리스트의 [b-1] 인덱스에 해당한다면
            grade = grades[sort_score.index(j)//(a//10)]  # 등수(성적 순 인덱스)와 배율에 따라 평점 구한다.
    print(f"#{tc} {grade}")
    
