def preorder(nodes, idx):
    #idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        #루트 노드 출력, 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출하여 출령 순서대로 이어 붙임
        ret = str(nodes[idx]) + " "
        ret += preorder(nodes, idx * 2 + 1)
        ret += preorder(nodes, idx * 2 + 2)
        return ret
    
    #idx >= len(nodes)일 때는 빈 문자열 반환
    else:
        return ""
    
def inorder(nodes, idx):
    #idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        #왼쪽 서브 트리를 먼저 재귀 호출하여 출력 순서대로 이어붙임
        ret = inorder(nodes, idx * 2 + 1)
        #루트 노드를 출력한 다음, 오른쪽 서브 트리를 재귀 호출하여 출력 순서대로 이어붙임
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    #idx >= len(nodes)일 때는 빈 문자열 반환
    else:
        return ""
    
def postorder(nodes, idx):
    #idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        #왼쪽 서브 트리와 오른쪽 서브 트리를 재귀호출 하여 출력 순서대로 이어붙임
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        #루트 노드 출력
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""
    
def solution(nodes):
    #전위, 중위, 후위 계산 결과 계산
    #노드 리스트와 루트 노드의 인덱스를 매개변수로 각각 호출
    return [
        preorder(nodes, 0)[:-1], #마지막 공백 제거
        inorder(nodes, 0)[:-1], #마지막 공백 제거
        postorder(nodes, 0)[:-1], #마지막 공백 제거
    ]