def solution(s):
    stack = [] #스택 초기화
    for c in s:
        if stack and stack[-1] == c: #스택이 비어있지 않고, 현재 문자와 스택 맨 위 문자가 같으면
            stack.pop #스택의 맨 위 문자 제거
        else:
            stack.append(c) #스택에 문자 추가
    
    return int(not stack) #스택이 비어있으면 1, 그렇지 않으면 0