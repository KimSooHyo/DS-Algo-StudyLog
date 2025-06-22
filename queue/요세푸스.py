"""
1. 첫 번째 데이터부터 마지막 데이터까지 큐에 푸시
2. 큐에서 k-1번째까지의 데이터를 각각 front에서 팝, rear에 푸시
3. k번째 데이터를 팝
4. 과정 2~3을 큐에 데이터가 없을때까지 반복
"""

from collections import deque

def solution(N, K):
    #1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1, N+1))
    
    while len(queue) > 1:
        for _ in range(K-1):
            queue.append(queue.popleft())
            
        queue.popleft()
    return queue[0]