import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    
    #각 작업의 배포 가능일 계산
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(n)]
    
    count = 0 #배포할 작업의 수 카운트
    max_day = days[0] #기준 배포일
    
    for i in range(n):
        if max_day >= days[i]: #배포 가능일이 기준일 보다 빠르면
            count += 1
        else: #배포 예정일이 기준일보다 느리면
            answer.append(count) #큐에 푸시
            count = 1 #카운트 초기화
            max_day = days[i] #기준일 초기화
            
    answer.append(count)
    return answer