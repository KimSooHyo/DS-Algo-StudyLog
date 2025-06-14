"""
문자열을 정말 회전시키는 것이 아니라 인덱스를 활용
"""

def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        stack = []
        for j in range(n):
            # 괄호 문자열을 회전시키면서 참조
            c = s[(i+j) % n] #문자열 끝에 도달하면 다시 처음으로 이동
            if c == '(' or c=='{' or c == '[': #열린 괄호는 푸시
                stack.append(c)
            else:
                if not stack: #닫힌 괄호가 나왔는데 스택이 비어있다면 열린 괄호랑 짝이 맞지 않다는 것
                    break
                
                #stack의 top 위치의 괄호와 짝이 맞는지 비교 (stack[-1]은 stack의 top)
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c== '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    break
        else: #for문이 break에 의해 끝나지 않고 끝까지 수행된 경우
            if not stack:
                answer += 1
    return answer
            
                
            