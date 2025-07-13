"""
요구사항
1. 모든 섬을 연결 (직접 연결되지 않아도 됨)
2. 연결한 다리 비용의 합이 최소

문제 푸는 방법
1. 각 섬 사이의 다리를 건설하는 비용을 오름차순으로 정렬
2. 비용이 작은 다리부터 선택해 섬을 연결
3. n개의 섬을 연결하려면 n-1개의 다리 필요, n-1개의 다리가 선택될 때까지 위 두 과정을 반복
4. 비용을 최소화하기 위해 다리를 추가할 때 사이클을 형성하지 않도록 함
    - 다리를 추가할 때마다 사이틀 형성 여부 체크해야함
    - 다리에 연결된 섬의 루트 노드를 보고 이것이 같은지 확인
        - 이때 집합 알고리즘 활용
        
- 이 문제는 최소 신장 트리를 구현하는 것. 상호배타적 집합의 모든 연산을 활용해야하므로 집합 파트에 나옴. 이후에 다시 풀어볼 것
"""

def find(parent, i):
    #i가 속한 집합의 루트 노드 찾기
    if parent[i] == i:
        return i
    #경로 압축: 'i'의 부모를 직접 루트로 설정
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    #랭크를 기준으로 두 집합 합치기
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        #작은 랭크의 트리를 큰 랭크의 트리 아래에 연결
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        #랭크가 같은 경우, 한 트리를 다른 트리에 붙이고 랭크 증가
        parent[yroot] = xroot
        rank[xroot] += 1
        
def solution(n, costs):
    #비용을 기준으로 간선을 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    
    #각 노드의 부모를 추적하는 parent 배열 생성
    parent = [i for i in range(n)]
    
    #각 노드의 트리의 랭크를 추적하는 rank 배열 생성
    rank = [0] * n
    
    min_cost = 0 #최소 신장 트리의 총 비용
    edges = 0
    
    for edge in costs:
        if edges == n-1:
            #n-1개의 간선이 포함된 경우 중단
            break
        
        #현재 간선의 두 노드가 속한 집합의 루트 찾기
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x != y:
            #두 노드가 다른 집합인 경우, 집합 합치기
            union(parent, rank, x, y)
            #현재 간선의 비용을 최소 비용에 추가
            min_cost += edge[2]
            #포함된 간선의 개수 증가
            edges += 1
    
    return min_cost