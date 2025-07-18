"""
가중치가 모두 양수일 때, 최소 비용을 구하는 알고리즘 -> 다익스트라
BFS, DFS는 탐색을 하는 것이지 최소 비용을 구하진 않음
"""
import heapq

def solution(N, road, K):
    #각 노드에 연결된 간선들을 저장할 리스트
    graph = [[] for _ in range(N + 1)]
    #출발점에서 각 노드까지의 최단 거리를 저장할 리스트
    distances = [float("inf")] * (N + 1)
    distances[1] = 0 #출발점은 0으로 초기화
    
    #그래프 구성
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    #다익스트라 알고리즘 시작
    heap = []
    heapq.heappush(heap, (0,1)) #출발점을 heap에 추가
    while heap:
        dist, node = heapq.heappop(heap)
        
        #인접한 노드들의 최단 거리를 갱신하고 heap에 추가
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
                
    #distances 리스트에서 k이하인 값의 개수를 구하여 반환
    return sum(1 for dist in distances if dist <= K)        