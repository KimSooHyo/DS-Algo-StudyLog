"""
스택과 재귀로 구현하는 방법이 각각 있으나, 실제 문제 풀이에서는 재귀를 많이 사용하므로 재귀로 구현해보자
"""
#그래프를 인접 리스트로 표현
graph = {
    1:[4,5],
    2:[3],
    3:[],
    4:[2,3],
    5:[4]
}

#방문 여부를 표시하는 배열
visited = [False] * (len(graph)+1)

def dfs(current_node):
    #현재 노드 방문
    visited[current_node] = True
    print(current_node)
    
    #현재 노드와 인접한 노드 순회
    for adj_node in graph[current_node]:
        if not visited[adj_node]:
            dfs(adj_node)
            
#DFS 알고리즘 실행
dfs(1) #출력값 : 1 4 2 3 5