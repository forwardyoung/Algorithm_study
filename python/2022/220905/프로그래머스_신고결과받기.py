def solution(id_list, report, k):
    report = set(report)
    mail = {x:0 for x in id_list} # 메일 받을 횟수
    
    warning = {x:0 for x in id_list} # 신고 당한 횟수
    
    for x in report:
        warning[x.split()[1]] += 1
        
    for x in report:
        if warning[x.split()[1]] >= k: # 신고 당한 횟수가 k보다 크면 메일 받을 횟수 +1
            mail[x.split()[0]] += 1
            
    return list(mail.values())