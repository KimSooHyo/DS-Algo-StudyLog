from collections import defaultdict, deque

#전역 변수 선언 및 초기화
adj_list = defaultdict(list)
visited = set()
result = []

def bfs(start):
    #탐색 시 맨 처음 방문할 노드를 큐에 추가하고 방문 처리
    queue = deque([start])
    visited.add(start)
    result.append(start)
    #큐가 비어있지 않은 동안 반복
    while queue:
        #큐에 있는 원소 중 가장 먼저 푸시된 원소 팝
        node = queue.popleft()
        
        #인접한 이웃 노드들에 대해서 방문하지 않은 노드 푸시
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                result.append(neighbor)
                
def solution(graph, start):
    #그래프를 인접 리스트로 표현
    for u, v in graph:
        adj_list[u].append(v)
    bfs(start)
    return result