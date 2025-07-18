"""
벨만포드는 모든 간선에 대해 가중치를 계산. 비교 연산을 매번함.
- num_vertices : 정점의 개수
- edges : 간선 정보
- source : 시작 정점
최단 거리를 담은 distance 배열을 반환하면 됨
"""

INF = 99999999
def solution(num_vertices, edges, source):
    #간선 정보를 활용해서 인접 리스트 생성
    graph = [[] for _ in range(num_vertices)]
    for edge in edges:
        from_vertex, to_vertex, weight = edge
        graph[from_vertex].append((to_vertex, weight))
        
    #현재까지 구한 최소 비용을 INF로 설정(시작 노드는 제외)
    distance = [INF] * num_vertices
    distance[source] = 0
    
    #정점의 개수 -1 만큼 최소 비용을 갱신
    for _ in range(num_vertices -1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    #음의 순환이 있는지 확인
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return [-1]
            
    return distance