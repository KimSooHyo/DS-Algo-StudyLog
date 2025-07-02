def solution(id_list, report, k):
    reported_user = {} #신고 당한 유저
    count = {} #처리 결과 메일 받은 횟수
    
    #신고 기록 순회
    for r in report:
        user_id, reported_id, = r.split()
        if reported_id not in reported_user: #신고당한 기록 없는 경우
            reported_user[reported_id] = set()
        reported_user[reported_id].add(user_id) #신고한 사람 아이디를 집합에 저장
        
    for reported_id, user_id_lst in reported_user.items():
        if len(user_id_lst) >= k: #정지 기준에 맞는지 확인
            for uid in user_id_lst:
                if uid not in count:
                    count[uid] = 1
                else:
                    count[uid] += 1
                    
    answer = []
    for i in range(len(id_list)): #각 아이디별 메일 받은 횟수 정리 
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    
    return answer