def solution(decimal):
    stack = []
    
    while (decimal > 0):
        remain = decimal%2
        decimal //= 2
        stack.append(str(remain))
        
    print(''.join(reversed(stack)))