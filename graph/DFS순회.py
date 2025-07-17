from collections import defaultdict

#깊이 우선 탐색에 필요한 전역 변수 선언
adj_list = defaultdict(list)
visited = set()
result = []

def dfs(node):
    #현재 노드 방문 여부를 표시
    visited.add(node)
    result.append(node)
    #현재 노드와 인접한 노드를 순회하며 인접하지 않은 노드 탐색
    for neighbor in adj_list.get(node, []): #node라는 키가 존재하지 않는다면 KeyError가 발생하지 않고, 대신 빈 리스트 []를 기본값으로 반환
        if neighbor not in visited:
            dfs(neighbor)
            
def solution(graph, start):
    #그래프를 인접리스트로 변환
    for u, v in graph:
        adj_list[u].append(v)
        
    dfs(start)
    return result