def solution(s):
    answer = 0
    stack = []
    for c in s.split():
        if c == 'Z':
            stack.pop()
        else:
            stack.append(int(c))
    answer = sum(stack)
    
    return answer