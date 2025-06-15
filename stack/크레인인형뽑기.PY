def solution(board, moves):
    #각 열에 대한 스택
    lanes = [[] for _ in range(len(board[0]))]
    
    #board를 역순으로 탐색, 각 열의 인형을 lanes에 추가
    for i in range(len(board) -1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])
                
    #인형을 담을 스택
    bucket = []
    
    #사라진 인형의 개수 저장할 변수
    cnt = 0
    
    #moves를 순회하면서 각 열에서 인행 뽑아서 bucket에 추가
    for m in moves:
        if lanes[m-1]: #해당 열에 인형이 있는 경우
            doll = lanes[m-1].pop()
            
            if bucket and bucket[-1] == doll: #바구니에 인형 있고, 같은 인형이 연속되는 경우
                cnt += 2
                bucket.pop()
            else: # 바구니에 인형이 없거나 다른 인형인 경우
                bucket.append(doll)
                
    return cnt