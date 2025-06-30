def solution(record):
    answer = []
    uid = {}
    for line in record: #record의 각 줄을 하나씩 처리
        cmd = line.split(" ")
        if cmd[0] != "Leave": #enter 또는 change인 경우
            uid[cmd[1]] = cmd[2]
    
    for line in record: # record의 각 줄을 하나씩 처리
        cmd = line.split(" ")
        
        #각 상태에 맞는 메세지 answer에 저장
        if cmd[0] == "Enter":
            answer.append("%s님이 들어왔습니다." %uid[cmd[1]])
        elif cmd[0] == "Change":
            pass
        else:
            answer.append("%s님이 나갔습니다." % uid[cmd[1]])
            
    return answer