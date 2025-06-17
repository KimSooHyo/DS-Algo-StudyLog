"""
P. 177
실제 배열을 선언하고 연산하는 것이 아니라 인덱스만으로 연산해보자

- 인접한 행의 정보를 활용
EX) 위는 -1, 아래는 1 
"""

def solution(n, k, cmd):
    deleted = [] #삭제된 행의 인덱스 저장할 리스트
    
    #연결리스트에서 각 행의 위아래 행의 인덱스를 저장하는 리스트
    up = [i -1 for i in range(n+2)]
    down = [i + 1 for i in range(n+1)]
    
    #현재 위치
    k += 1
    
    #주어진 명령어 리스트 처리
    for cmd_i in cmd:
        #현재 위치 삭제, 그 다음 위치 이동
        if cmd_i.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        #가장 최근에 삭제된 행을 복원    
        elif cmd_i.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
            
        #현재 위치 위아래 이동
        else:
            action, num = cmd_i.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
                    
        #삭제된 행 위치에 X, 그렇지 않은 행은 O
    answer = ["O"] * n
    for i in deleted:
        answer[i-1] = 'X'
    return "".join(answer)