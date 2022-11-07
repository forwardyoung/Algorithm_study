def solution(nums):
    choose = int(len(nums)/2) #  N/2마리를 선택
    nums = set(nums) # 
    
    answer = min(len(nums), choose)
    
    return answer