"""
큐와 덱을 활용하여 너비 우선 탐색 구현
"""

from collections import deque

#그래프를 인접 리스트로 표현
graph = {
    1:[4,5],
    2:[3],
    3:[],
    4:[2,3],
    5:[4]
}

def bfs(start_node):
    visited = [False] * (len(graph) + 1)
    
    #시작 노드 방문 처리
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        #가장 먼저 푸시된 노드 방문
        node = queue.popleft()
        print(node)
        
        #인접한 노드 순회
        for adj_node in graph[node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True
                
#BFS 알고리즘 실행
bfs(1) #출력값 : 1 4 5 2 3