from collections import deque

def solution(cards1, cards2, goal):
    #cards와 goal을 deque로 변환
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    #goal의 문자열을 순회
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break
        
    return "Yes" if not goal else "No"