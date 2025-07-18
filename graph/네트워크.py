"""
최적의 해를 구하는 것이 아니라, 모든 요소를 탐색하는 것이 목적
-> 깊이 우선 탐색이 좋음
모든 노드를 방문했을 때, 깊이 우선 탐색을 몇 번 했는지 반환하면 됨
"""

def dfs(computers, visited, node):
    visited[node] = True #현재 노드 방문 처리
    for idx, connected in enumerate(computers[node]):
        if connected and not visited[idx]: #연결되어 있지만 방문하지 않은 노드면
            dfs(computers, visited, idx) #해당 노드 방문하러 이동

def solution(n, computers):
    answer = 0
    visited = [False] * n #방문 여부 저장할 리스트
    for i in range(n):
        if not visited[i]: #아직 방문하지 않은 노드라면 해당 노드를 시작으로 깊이 우선 탐색 진행
            dfs(computers, visited, i)
            answer += 1
    return answer